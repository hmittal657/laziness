# laziness
Utilities for speeding up things, and things which are not available straight forward

insta_text_dms_extraction.py:
for Extracting text dms from insta chats, safe and legal way, no data is exposed.
1. Firstly request download your data from Instagram, from Privacy and Security in Account Settings.
2. Now, You will receive an email from Instagram to download the said data.
3. It is a zip file with everything you have shared on Instagram. Download that file and Extract
4. There's a file called messages.json in that zip which basically contains all your conversations in json format.
5. Place the insta_text_dms_extraction.py file in the directory
6. run insta_text_dms_extraction.py 
7. You will see index list with participants of a chat and date range
8. Select the desired index and you will see the output in your screen
