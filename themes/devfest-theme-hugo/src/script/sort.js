// Sort
function surnameSorter(a, b) {
	if (a[0] < b[0]) return -1;
    if (a[0] > b[0]) return 1;
    return 0;
}

document.querySelectorAll('ul.sort')
    .forEach(listElt => {
    	var surnames = [];
    	len = listElt.children.length;
        for (let i = 0; i < len; i++) {
        	var surnames_temp = listElt.children[i].innerText.split(/\s+/).slice(2,4);
        	if(surnames_temp[0]=="de" || surnames_temp[0]=="van"){
        		var surname = surnames_temp[1];
        	}
        	else{
        		var surname = surnames_temp[0];
        	}
        	surnames.push([surname,i]);
        }
        surnames.sort(surnameSorter);

        var items = listElt.childNodes;
		var itemsArr = [];
		for (var i in items) {
		    if (items[i].nodeType == 1) { // get rid of the whitespace text nodes
		        itemsArr.push(items[i]);
		    }
		}

		for (i = 0; i < itemsArr.length; ++i) {
  			listElt.appendChild(itemsArr[surnames[i][1]]);
		}
    });
