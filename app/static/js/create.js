var rowsDiv = document.getElementById("rows");
var rowId = rowsDiv.children.length;


function handleAdd() {
	newRow = rowsDiv.children[0].cloneNode(true);

	exerciseNameInput = newRow.children[0].children[0].children[0].children[0];
	exerciseNameInput.value = '';
	exerciseNameInput.name = 'exercises-' + rowId + '-name';

	exerciseSetInput = newRow.children[0].children[1].children[0].children[0];
	exerciseSetInput.value = '';
	exerciseSetInput.name = 'exercises-' + rowId + '-sets';

	exerciseUnitInput = newRow.children[0].children[2].children[1];
	exerciseUnitInput.value = '';
	exerciseUnitInput.placeholder = 'Reps';
	exerciseUnitInput.name = 'exercises-' + rowId + '-units';

	exerciseUnitInput.parentNode.children[0].children[0].children[0].addEventListener("input", handleChange);

	rowId++;
	rowsDiv.append(newRow);
}

function handleDel(elem) {
	if (rowId > 1) {
		elem.parentNode.parentNode.remove();
		rowId--;
	}
}

document.getElementById("add").onclick = handleAdd;

function handleChange(elem) {
	if (elem.target.value == 'time') {
		elem.target.parentNode.parentNode.parentNode.children[1].placeholder = "Time";
		elem.target.parentNode.parentNode.parentNode.children[1].selected = true;
		elem.target.parentNode.parentNode.children[1].children[0].classList.remove('fa-calculator');
		elem.target.parentNode.parentNode.children[1].children[0].classList.add('fa-clock-o');
	} else if (elem.target.value == 'reps') {
		elem.target.parentNode.parentNode.children[1].children[0].classList.add('fa-calculator');
		elem.target.parentNode.parentNode.children[1].children[0].classList.remove('fa-clock-o');
		elem.target.parentNode.parentNode.parentNode.children[1].selected = true;
		elem.target.parentNode.parentNode.parentNode.children[1].placeholder = "Reps";
	}
}

for (row of rowsDiv.children) {
	row.children[0].children[2].children[0].children[0].children[0].addEventListener('input', handleChange);
}
