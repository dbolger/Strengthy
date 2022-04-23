
// Called when the check at the end of a set line is clicked
function onClickSetCheck(elem) {
	if (elem.classList.contains('is-success')) {
		elem.classList.remove('is-success');
	} else {
		elem.classList.add('is-success');
	}
}
