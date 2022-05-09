class Timer {
	// TODO: remove
	startedBefore;
	buttonId;
	timeLeft;

	constructor(elem) {
		// DOM stuff
		this.elem = elem;
		this.row = elem.parentElement.parentElement.parentElement;
		this.button = elem.children[0].children[0];
		this.time_span = elem.parentElement.children[1];

		this.seconds = this.row.dataset.timerSeconds;
		this.interval = null;
		this.paused = true;
		this.finished = false;
	}

	toggle() {
		if (this.finished) {
			return;
		} else if (this.paused) {
			this.play();
		} else {
			this.pause();
		}
	}

	play() {
		console.log("Playing...");
		this.paused = false;

		// Run this code every 1 second
		this.interval = setInterval(() => {
			// Update time
			this.seconds--;
			this.time_span.innerHTML = `${parseInt(this.seconds / 60)}:${this.seconds % 60}`;

			// Check for finish
			if (this.seconds <= 0) {
				this.finish();
			}
		}, 1000);

		// Update button
		this.button.classList.remove('fa-play');
		this.button.classList.add('fa-pause');
	}

	pause() {
		console.log("Pausing...");
		this.paused = true;

		// Stop interval
		clearInterval(this.interval);

		// Update button
		this.button.classList.remove('fa-pause');
		this.button.classList.add('fa-play');
	}

	finish() {
		console.log("Finished...")
		this.finished = true;

		// Stop interval
		clearInterval(this.interval);
	}
}

// Get an arrayt of all inputs
allInputs = Array.from(document.getElementsByClassName('input')).filter(e => e.type == 'number');

// Register onsubmit handler for form (NOTE: unfortunatly not a better way to do this)
document.getElementById("form").addEventListener('submit', (el) => {
	Array.from(event.target.getElementsByTagName('input')).forEach(i => i.disabled = false);
});

// Attach a timer to all 

function setReset(row, index, values=true) {
	if (row.dataset.isTimer) {
		let timerButton = row.children[1].children[0].children[0];
		timerButton.disabled = false;
		timerButton.classList.remove('is-success');
		timerButton.classList.remove('is-danger');
		row.children[2].children[0].classList.remove('is-success');

	} else if (row.dataset.isReps) {
		let lbsInput = row.children[1].children[0];
		let repsInput = row.children[2].children[0];

		// Enable inputs
		lbsInput.disabled = false;
		repsInput.disabled = false;

		// Remove classes
		lbsInput.classList.remove('is-success');
		lbsInput.classList.remove('is-danger');
		repsInput.classList.remove('is-success');
		repsInput.classList.remove('is-danger');

		// update id/classes to new row index
		current = lbsInput.id;
		updated = current.substring(0, current.length - 5);
		lbs = updated + index + '-lbs';
		lbsInput.id = lbs;
		lbsInput.name = lbs;
		reps = updated + index + '-reps'
		repsInput.id = reps;
		repsInput.name = reps;

		row.children[3].children[0].classList.remove('is-success');

		if (values) {
			lbsInput.value = '';
			repsInput.value = '';
		}

	}
}

function setSetid(row, id) {
	let setNumber = row.children[0];
	//let lbsInput = row.children[1].children[0];
	//let repsInput = row.children[2].children[0];
	//let doneButton = row.children[3].children[0];

	setNumber.textContent = id + 1;
}

function setCheck(row) {
	if (row.dataset.isTimer) {
		timerButton = row.children[1].children[0].children[0];
		timerButton.disabled = true;
		timerButton.classList.add('is-success');
		if (timerButton.children[0].children[0].classList.contains('fa-pause')) {
			timerButton.children[0].children[0].classList.remove('fa-pause');
			timerButton.children[0].children[0].classList.add('fa-play');
			timers.get(timerButton.id).finished = true;
		} else if (timerButton.children[0].children[0].classList.contains('fa-play')) {
			timerButton.children[0].children[0].classList.remove('fa-play');
			timerButton.children[0].children[0].classList.add('fa-pause');
			timers.get(timerButton.id).finished = false;
		}
	} else {
		// Disable input editing
		row.children[1].firstChild.disabled = true;
		row.children[2].firstChild.disabled = true;

		// Add is-success to inputs
		row.children[1].firstChild.classList.add('is-success')
		row.children[2].firstChild.classList.add('is-success')
	}
	doneButton = row.children[2].children[0];
		doneButton.classList.add('is-success');
}

// ----- ----- CALLBACKS ----- ----- //
function onClickPausePlayTimer(elem) {
	// Create new timer object if one does not exist
	if (!elem.timer) {
		elem.timer = new Timer(elem);
	}

	// Toggle timer
	elem.timer.toggle();
}

function onKeyDown(event) {
	if (event.key === "Enter" || event.key === "Tab") {
		event.preventDefault();

		//Isolate the node that we're after
		const currentNode = event.target;
		//Find the current tab index.
		currentIndex = [...allInputs].findIndex(el => currentNode.isEqualNode(el));

		//focus the following element
		const targetIndex = (currentIndex + 1) % allInputs.length;
		const targetNode = allInputs[targetIndex];

		if (!targetNode.parentElement.parentElement.isEqualNode(currentNode.parentElement.parentElement)) {
			// going to new row
			if (currentNode.value != "" && allInputs[currentIndex-1].value != "") {
				onClickSetCheck(currentNode.parentElement.parentElement.children[3].children[0]);
			}
		}

		targetNode.focus();
	}
}

function onClickAddSet(elem) {
	// Create the new row
	const tableBody = elem.parentElement.parentElement.children[0].children[1];
	const row = tableBody.children[0].cloneNode(true);

	// Add new row to table
	setReset(row, tableBody.children.length, false);
	setSetid(row, tableBody.children.length)
	row.addEventListener('keydown', handleEnterKey)
	tableBody.appendChild(row)
}

function onClickSetCheck(elem) {
	const row = elem.parentElement.parentElement;

	if (elem.classList.contains('is-success')) {
		setReset(row, row.parentElement.children.length - 1, false);
	} else {
		elem.classList.add('is-success');
		setCheck(elem.parentElement.parentElement);
	}
}

