window.onload = function() {

  var WEBSOCKET_ROUTE = "/ws";

  if(window.location.protocol == "http:"){
    //localhost
    var ws = new WebSocket("ws://" + window.location.host + WEBSOCKET_ROUTE);

    ws.onopen = function(evt) {
      console.log("open");
      window.addEventListener("deviceorientation", function () {
        if (!event.alpha) {
          a = 0;
        }
        else {
          a = event.alpha;
        }
        ws.send("x"+Math.round(a));
        ws.send("y"+Math.round(event.beta));
        ws.send("z"+Math.round(event.gamma));

      });
    };

    ws.onmessage = function(evt) {
      console.log("msg",evt.data);
    };

    ws.onclose = function(evt) {
      console.log("close");
    };
  }
}
