window.onload = function(){
  //var todoList =[];
  document.getElementById("add").onclick=function(){
    var li = document.createElement("li");
    var input = document.getElementById("myInput").value;
    if(input===""){
      alert("You must write something!");
    }else{
      var text = document.createTextNode(input);
      li.appendChild(text);
      
      document.getElementById("myTasks").appendChild(li);
      document.getElementById("myInput").value = "";
    }
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    li.appendChild(span);

    for (i = 0; i < close.length; i++) {
      close[i].onclick = function() {
        var div = this.parentElement;
        div.style.display = "none";
      }
    }
  }
 
  var list = document.querySelector('ul');
  list.addEventListener('click', function(ev) {
    if (ev.target.tagName == 'LI') {
      ev.target.classList.toggle('checked');
    }
  }, false);

  var close = document.getElementsByClassName("close");
  for (var i = 0; i < close.length; i++) {
    close[i].onclick = function() {
      close[i].parentElement.style.display="none";
    }
  }

}