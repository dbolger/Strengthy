
// Register 'Enter' listeners on all inputs
Array.from(document.getElementsByClassName('input'))
	.filter(e => e.type == 'number')
	.forEach(e => e.addEventListener('keyup', function(event) {
		if (event.key == 'Enter') {
			// TODO implement
			console.log("ENTER")
		}
	}))

function setReset(row, values=true) {
	let lbsInput = row.children[1].children[0];
	let repsInput = row.children[2].children[0];
	let doneButton = row.children[3].children[0];

	// Enable inputs
	lbsInput.disabled = false;
	repsInput.disabled = false;

	// Remove classes
	lbsInput.classList.remove('is-success');
	lbsInput.classList.remove('is-danger');
	repsInput.classList.remove('is-success');
	repsInput.classList.remove('is-danger');

	doneButton.classList.remove('is-success');

	if (values) {
		lbsInput.value = '';
		repsInput.value = '';
	}
}

function setSetid(row, id) {
	let setNumber = row.children[0];
	let lbsInput = row.children[1].children[0];
	let repsInput = row.children[2].children[0];
	let doneButton = row.children[3].children[0];

	setNumber.textContent = id + 1;
}

function setCheck(row) {
	// Disable input editing
	row.children[1].firstChild.disabled = true;
	row.children[2].firstChild.disabled = true;

	// Add is-success to inputs
	row.children[1].firstChild.classList.add('is-success')
	row.children[2].firstChild.classList.add('is-success')
}

// Called when the check at the end of a set line is clicked
function onClickSetCheck(elem) {
	if (elem.classList.contains('is-success')) {
		setReset(elem.parentElement.parentElement, false);
	} else {
		elem.classList.add('is-success');

		setCheck(elem.parentElement.parentElement);
	}
}

function onClickAddSet(elem) {
	// Create the new row
	let tableBody = elem.parentElement.parentElement.children[1].children[1];
	let row = tableBody.children[0].cloneNode(true);

	// Add new row to table
	setReset(row);
	setSetid(row, tableBody.children.length)
	tableBody.appendChild(row)
}
