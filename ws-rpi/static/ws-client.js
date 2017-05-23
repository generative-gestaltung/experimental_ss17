function fill (c) {
  context.fillStyle = c;
  conect.fillRect(0,0,canvas.width, canvas.height);
}

window.onload = function() {

  var WEBSOCKET_ROUTE = "/ws";

  if(window.location.protocol == "http:"){
    //localhost
    var ws = new WebSocket("ws://" + window.location.host + WEBSOCKET_ROUTE);
  }

  ws.onopen = function(evt) {
    console.log("open");
    document.getElementById("ws-status").innerHTML = "WS connected";
  };

  ws.onmessage = function(evt) {
    console.log("msg",evt.data);
    if (evt.data[0]=='r') {
      fill("#f00");
    }
    if (evt.data[0]=='g') {
      fill("#0f0");
    }
  };

  ws.onclose = function(evt) {
    console.log("close");
  };

  document.getElementById("green_on").onclick = function() {
    ws.send("on_g");
  }

  document.getElementById("green_off").onclick = function() {
    ws.send("off_g");
  }


  
}
