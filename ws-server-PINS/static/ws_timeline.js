var ws = null;

window.onload = function() {

  var WEBSOCKET_ROUTE = "/ws";
  if(window.location.protocol == "http:"){
    //localhost
    ws = new WebSocket("ws://" + window.location.host + WEBSOCKET_ROUTE);

    ws.onopen = function(evt) {
      console.log("open");
    };

    ws.onmessage = function(evt) {
      console.log("msg",evt.data);
    };

    ws.onclose = function(evt) {
      console.log("close");
    };
  }
}
