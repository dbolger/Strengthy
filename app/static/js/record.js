
// Register 'Enter' listeners on all inputs
Array.from(document.getElementsByClassName('input'))
	.filter(e => e.type == 'number')
	.forEach(e => e.addEventListener('keyup', function(event) {
		if (event.key == 'Enter') {
			console.log("ENTER");
		}
	}))

function checkSet(row) {
	// Disable input editing
	row.children[1].firstChild.disabled = true;
	row.children[2].firstChild.disabled = true;

	// Add is-success to inputs
	row.children[1].firstChild.classList.add('is-success')
	row.children[2].firstChild.classList.add('is-success')
}

function uncheckSet(row) {
	// Re-enable input editing
	row.children[1].firstChild.disabled = false;
	row.children[2].firstChild.disabled = false;

	// Remove is-success from inputs
	row.children[1].firstChild.classList.remove('is-success')
	row.children[2].firstChild.classList.remove('is-success')
}

// Called when the check at the end of a set line is clicked
function onClickSetCheck(elem) {
	if (elem.classList.contains('is-success')) {
		elem.classList.remove('is-success');

		uncheckSet(elem.parentElement.parentElement);
	} else {
		elem.classList.add('is-success');

		checkSet(elem.parentElement.parentElement);
	}
}
