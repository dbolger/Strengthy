timers = new Map([]);
class Timer {
	startedBefore;
	buttonId;
	timeLeft;
	finish;
}

// Get an arrayt of all inputs
allInputs = Array.from(document.getElementsByClassName('input')).filter(e => e.type == 'number');

// Register onsubmit handler for form (NOTE: unfortunatly not a better way to do this)
document.getElementById("form").addEventListener('submit', (el) => {
	Array.from(event.target.getElementsByTagName('input')).forEach(i => i.disabled = false);
});

function handleEnterKey(event) {
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

// Called when the check at the end of a set line is clicked
function onClickSetCheck(elem) {
	row = elem.parentElement.parentElement;
		if (elem.classList.contains('is-success')) {
			setReset(row, row.parentElement.children.length - 1, false);
		} else {
			elem.classList.add('is-success');
			setCheck(elem.parentElement.parentElement);
		}

}

function onClickAddSet(elem) {
	// Create the new row
	let tableBody = elem.parentElement.parentElement.children[0].children[1];
	let row = tableBody.children[0].cloneNode(true);

	// Add new row to table
	setReset(row, tableBody.children.length, false);
	setSetid(row, tableBody.children.length)
	row.addEventListener('keydown', handleEnterKey)
	tableBody.appendChild(row)
}

function getTimeRemaining(end) {
	var t = Date.parse(end) - Date.parse(new Date());
	var seconds = Math.floor((t/1000) % 60);
	var minutes = Math.floor((t/1000/60) % 60);
	return { 'total': t,
		'minutes': minutes,
		'seconds': seconds,
	};
}

function runClock(timer) {
	var timeInterval;
	function updateClock() {
		var t = getTimeRemaining(timer.finishDate);
		timer_time = document.getElementById(timer.elem.parentElement.children[1].id);
		timer_time.innerHTML = t.minutes.toString().padStart(2, "0") + ':' + t.seconds.toString().padStart(2, "0");
		if (t.total <= 0 || timer.finished) {
			clearInterval(timeInterval);
			updateTimerButton(timer.elem);
			onClickSetCheck(timer.elem.parentElement);
			timer.elem.dataset.isActive = false;
			timers.delete(timer.elem.id);
		}
	}
	if (!timer.startedBefore) {
		// if its never been started before say it now has
		timer.startedBefore = true;
	}
	// create a new timeInterval for this element
	timeInterval = setInterval(updateClock, 100);
	timer.intervalId = timeInterval;
	// add a new map record
	console.log(timer.elem.id);
	timers.set(timer.elem.id, timer);
}

function updateTimerButton(elem) {
	if (elem.children[0].children[0].classList.contains('fa-play')) {
		elem.children[0].children[0].classList.remove('fa-play');
		elem.children[0].children[0].classList.add('fa-pause');
	} else {
		elem.children[0].children[0].classList.add('fa-play');
		elem.children[0].children[0].classList.remove('fa-pause');
	}
}

function onClickPausePlayTimer(elem) {
	// on press, if the button is not currently active (in use)
	if (elem.dataset.isActive == false || typeof elem.dataset.isActive == 'undefined') {
		elem.dataset.isActive = true;
		// create a new Timer object that represents the timer for this row
		timer = new Timer();
		timer.elem = elem;
		timer.paused = true;
		seconds = elem.parentElement.parentElement.parentElement.dataset.timerSeconds;
		timer.finishDate = new Date(Date.parse(new Date()) + 1*seconds*1000);
		console.log(timer.finishDate);
	} else {
		timer = timers.get(elem.id);
	}
	updateTimerButton(elem);
	if (timer.paused) {
		console.log('paused, starting...');
		timer.paused = false;
		// start/resume timer
		resumeTimer(timer);
	} else {
		console.log('started, pausing...');
		timer.paused = true;
		// pause timer
		pauseTimer(timer);
	}
}

function resumeTimer(timer) {
	var finish;
	if (typeof timer.timeLeft !== 'undefined') {
		// if we have set the time left before, then use that time
		finish = new Date(Date.parse(new Date()) + timer.timeLeft);
		timer.finishDate = finish;
	} else {
		// otherwise, this is first run, so use finishDate
		finish = new Date(Date.parse(timer.finishDate));
	}
	runClock(timer, finish);
}

function pauseTimer(timer) {
	console.log(timer);
	intervalId = timers.get(timer.elem.id).intervalId;
	clearInterval(intervalId);
	timer.timeLeft = getTimeRemaining(timer.finishDate).total;
}
