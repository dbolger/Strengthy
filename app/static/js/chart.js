
function fillChart(id) {
	const ctx = document.getElementById(id)
	new Chart(document.getElementById('exercise_chart'), {
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
}
