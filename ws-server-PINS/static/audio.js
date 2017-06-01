var Source0 = function (dt, sp) {
  this.ph = 0;
  this.dT = dt;
  this.initDT = dt;
  this.sp = sp;
}

Source0.prototype.getValue = function() {
  this.ph += this.dT;
  this.dT -= this.sp;
  if (this.dT<0) this.dT = 0;
  return Math.sin(this.ph);
}
Source0.prototype.trigger = function() {
  this.dT = this.initDT;
}



var phase = 0;
var ss = [
  new Source0(0.2, 0.001),
  new Source0(0.6, 0.002),
  new Source0(0.6, 0.0001),
  new Source0(0.3, 0.00003),
  new Source0(0.6, 0.002),
  new Source0(0.6, 0.0001),
  new Source0(0.3, 0.00003)
];

function audio_init() {

		var audioCtx = new (window.AudioContext || window.webkitAudioContext)();
		var button = document.querySelector('button');

		// Stereo
		var channels = 2;
		var frameCount = audioCtx.sampleRate;
		var myArrayBuffer = audioCtx.createBuffer(channels, frameCount, audioCtx.sampleRate);

		var bufferSize = 4096;
		var myPCMProcessingNode = audioCtx.createScriptProcessor(bufferSize, 1, 1);


		myPCMProcessingNode.onaudioprocess = function(e) {
  		var output = e.outputBuffer.getChannelData(0);
			for (var i = 0; i<bufferSize; i++) {
        output[i] = 0;
        for (var j=0; j<ss.length; j++)
     		 output[i] += ss[j].getValue();
  		}
		}

		myPCMProcessingNode.connect(audioCtx.destination);
}
