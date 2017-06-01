

window.onload = function() {
  var WEBSOCKET_ROUTE = "/ws";
  var ws;

  if(window.location.protocol == "http:"){
    //localhost
    ws = new WebSocket("ws://" + window.location.host + WEBSOCKET_ROUTE);

    document.getElementById("div0").onclick = function() {
      ws.send("b01");
    }

    document.getElementById("div1").onclick = function() {
      ws.send("b11");
    }

    document.getElementById("div2").onclick = function() {
      ws.send("b21");
    }

    document.getElementById("div3").onclick = function() {
      ws.send("b00");
    }

    document.getElementById("div4").onclick = function() {
      ws.send("b10");
    }

    document.getElementById("div5").onclick = function() {
      ws.send("b20");
    }
  }

  ws.onopen = function(evt) {

  };

  ws.onmessage = function(evt) {

    if (evt.data=="0") {

    }
  };

  ws.onclose = function(evt) {
    console.log("close");
  };
}
