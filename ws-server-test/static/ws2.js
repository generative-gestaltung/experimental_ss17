window.onload = function() {

  var WEBSOCKET_ROUTE = "/ws";

  if(window.location.protocol == "http:"){
    //localhost
    var ws = new WebSocket("ws://" + window.location.host + WEBSOCKET_ROUTE);
  }

  ws.onopen = function(evt) {
    context.fillStyle = "#00f";
    context.fillRect (0, 0, canvas.width, canvas.height);
  };

  ws.onmessage = function(evt) {
    console.log(evt);
    if (evt.data=="0")
      context.fillStyle = "#ff0";
      context.fillRect (0, 0, canvas.width, canvas.height);
    if (evt.data=="1")
      context.fillStyle = "#f0f";
      context.fillRect (0, 0, canvas.width, canvas.height);
  };

  ws.onclose = function(evt) {
    console.log("close");
  };
}
