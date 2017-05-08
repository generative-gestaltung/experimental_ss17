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


/*
  $("#green_on").click(function(){
            ws.send("on_g");
            });

        $("#green_off").click(function(){
            ws.send("off_g");
            });

        $("#red_on").click(function(){
            ws.send("on_r");
            });

        $("#red_off").click(function(){
            ws.send("off_r");
            });

      });
*/
}
