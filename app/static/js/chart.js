function exercise_chart(elem_id, exercise_id) {
	// Create initial chart
	let chart = new Chart(document.getElementById(elem_id), {
		type: 'line',
		data: {
			cubicInterpolationMode: 'monotone',
			tension: 0.4,
			pointStyle: 'circle',
			pointRadius: 5,
			pointHoverRadius: 10,
		},
		option: {
			scales: {
				y: {
					beginAtZero: true
				}
			}
		}
	});

	// Load chart data for exercise
}
