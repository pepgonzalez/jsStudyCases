/**/

(function(){

	function processString(str){
		var lines = [];
		var considered = [];
		var words = str.toUpperCase().split(" ");
		
		if (words.length == 1){
			lines.push(words[0]);
			return lines;
		
		}else{
			//obtener la palabra mas larga
			var maxLength = 0;
			var maxPosition = 0;
			
			for (var i = 0; i < words.length; i++){
				if (words[i].length > maxLength){
					maxLength = words[i].length;
					maxPosition = i;
				}
			}
			
			console.log("palabra mas larga: " + words[maxPosition]);
			console.log("posicion palabra maxima: " + maxPosition);
			console.log("largo: "  + maxLength);
			
			//procesamiento de palabras
			for(var i = 0; i < words.length; i++){
				
				console.log("**************************");
				console.log("iteracion principal de palabras: " + i);
				
				var alreadyConsidered = false;
				considered.forEach(function(e){
					if(i == e){
						alreadyConsidered = true;
					}
				});
				
				if(alreadyConsidered){
					console.log("elemento ya integrado: " + i);
					continue;
				}
				
				if (i == maxPosition){
					console.log("considerando palabra: " + i );
					lines.push(words[i]); 
					considered.push(i);
					continue;
				}
				
				//se es al menos la penultima palabra
				if (i < words.length - 1){
				
					var currentWord = words[i];
					var lineConsidered = [i];
				
					for(var j = i + 1; j < words.length; j++){
					
						console.log("---- iteacion secundaria: " + j);
						
						//si las siguiente palabra es la mas grande no tiene caso concatenar, se agregan ambas
						if(j == maxPosition){
							console.log("siguiente palabra es complementaria");
							lines.push(currentWord);
							lines.push(words[j]);
							for(var x = 0; x < lineConsidered.length; x++){
								considered.push(lineConsidered[x]);
							}
							considered.push(j);
							break;
						}
						
						if ( ( currentWord.length + words[j].length + 1 ) <= maxLength){
							console.log("concatenando palabras");
							currentWord = currentWord + " " + words[j];
							lineConsidered.push(j);
							continue;
						}else{
							console.log("no se puede concatenar:  agregando actual");
							lines.push(currentWord);
							for(var x = 0; x < lineConsidered.length; x++){
								considered.push(lineConsidered[x]);
							}
							
							break;
						}
					}
					
					//validar que no haya palabras que aun no se integran
				
				}else{
					lines.push(words[i]);
				}
			}
			return lines;
		}
	}

	function addEvent(e){
		e.preventDefault();
		var name = prompt("Nombre:");
		var lines = processString(name);
		console.log(lines);
	}
	
	var button = document.getElementById("add");
	button.addEventListener("click", addEvent);
	
})();