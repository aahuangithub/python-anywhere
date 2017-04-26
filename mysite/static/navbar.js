var scroll=0;
function toggleNav(){
	var nav = document.getElementsByClassName("nav")[0];
	var menu = document.getElementById("menu");
	if(nav.style.cssText=='display: inline;'){
		document.getElementById("main-content").style.cssText='display:inline';
		document.body.scrollTop=scroll;
		nav.style.cssText='@media screen and (max-width: 900px){display:none}';
		menu.innerHTML="&#9776;";
		menu.style.cssText='left:-3px';
	}
	else{
		scroll=document.body.scrollTop;
		document.getElementById("main-content").style.cssText='display:none';
		nav.style.cssText='display:inline;';
		menu.innerHTML="&#10005;";
		menu.style.cssText='left:5px';
	}
}
