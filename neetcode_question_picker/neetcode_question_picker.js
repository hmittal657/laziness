x = document.getElementsByTagName('tr');
var unsolved = [];
for (var i = 0; i < x.length ; i++) {
  if (!x[i].classList.contains("completed")) {
  	var z =  x[i].children[2].childElementCount;
    if (z != 2) {
    	unsolved.push(x[i]);
    }
  }
}
var random = unsolved[Math.floor(Math.random() * unsolved.length)];
var url = random.getElementsByTagName('a')[0].getAttribute('href')
console.log(url);
