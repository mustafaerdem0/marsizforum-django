let toggle = document.getElementById("toggle");
let container = document.getElementById("container");
let main = document.getElementById('main');
toggle.onclick = function(){
	container.classList.toggle('active');
	main.classList.toggle('mainactive');

}
