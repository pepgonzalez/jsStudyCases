/**/

(function(){

	var Element = function(name, x, y, elementType){
		this.name = name;
		this.x = x;
		this.y = y;
		this.type = elementType;
	}

	var Canvas = function(canvasId){
		var canvas = document.getElementById(canvasId);
		canvas.onmousemove = this.mouseTracker;
		this.context = canvas.getContext("2d");
		this.elements = [];
	}

	Canvas.prototype.mouseTracker = function(e){
		e.preventDefault();
	}
	
	Canvas.prototype.addElement = function(name, type){
		var e = new Element(name, 450, 150, type);
		this.elements = [];
		this.elements.push(e);
		this.draw();
	}
	
	Canvas.prototype.draw = function(){
		
		for(var i = 0; i < this.elements.length; i++){
			var element = this.elements[i];
			this.drawElement(element);
		}
	}
	
	Canvas.prototype.drawElement = function(e){
		if (e.type == 1){
			this.drawStage(e);
		}
	}
	
	Canvas.prototype.drawStage = function(e){
		var textLength = e.name.length;
		var textPixelLength = this.context.measureText(e.name);
		
		var textHeigth = Math.floor(( textLength * 10 ) / 100) + 1;
		
		//se pinta el rectangulo
		this.context.fillStyle = "green";
		this.context.fillRect(e.x, e.y, 120, (16 * textHeigth) + 20);
		
		//se pinta el texto
		this.context.fillStyle = "white";
		this.context.font="16px Arial";
		this.context.textAlign = "left";
		this.context.textBaseline = "top";
		
		var lines = [];
		var words = e.name.split(" ");
		
		if (words.length > 1){
		
		
		}else{
			if( (words[0].length * 10) >= 100 ){
				var l = Math.floor(( words[0].length * 10 ) / 100) + 1;
				if ( (words[0].length * 10) % 100 == 0){
					l -= 1;
				}
				for (var  i = 0; i < l; i++){
					var position = 10 * i;
					lines.push( words[0].substring( position, position + 10) );
				}
			}else{
				lines.push( words[0] );
			}
		}
		
		for (var i = 0; i < lines.length; i ++){
			this.context.fillText(lines[i].toUpperCase(), e.x + 10, e.y + 10 + (16 * i), 100);
		}
	}

	var CanvasContainer = new Canvas("canvas");
	
	function addEvent(e){
		e.preventDefault();
		var name = prompt("Nombre:");
		CanvasContainer.addElement(name, 1);
	}
	
	var button = document.getElementById("add");
	button.addEventListener("click", addEvent);
	
})();


