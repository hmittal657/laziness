import json

with open('messages.json', encoding='utf8', errors='ignore') as f:
	content = f.readlines()


content = [x.strip() for x in content] 

d = json.loads(content[0])

def get_date(node):
	time_stamp = node['created_at'][0:10]
	return time_stamp

def get_index():
	for x in range(len(d)):
		z = d[x]['conversation']
		participants = set()
		dates = set()
		length = len(z)
		for t in range(length):
			node = z[length-t-1]
			dates.add(get_date(node))
			participants.add(node['sender'])

		print("Index: ",x)
		print("")
		print("Participants: ")
		print (sorted(participants))
		print("")
		print("Between Dates: ")
		if len(dates) > 0:
			print(sorted(dates)[0],"to",sorted(dates)[-1])
		print("------------------------------------------")


def get_result(i):
	z = d[i]['conversation']
	date_set = set()
	length = len(z)
	for x in range(length):
		node = z[length-x-1]
		if 'text' in node:
			prev_len = len(date_set)
			date_set.add(get_date(node))
			if len(date_set) > prev_len:
				print(get_date(node))
			print(node['sender']+" : "+node['text'])
		print("--")


get_index()

ind = input("Enter your index: ")

get_result(int(ind))
