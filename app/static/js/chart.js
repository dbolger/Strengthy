async function request(url) {
	const response = await fetch(url);

	return response.json();
}

async function exercise_chart(elem_id, exercise_id, exercise_name) {
	// Create initial chart
	let chart = new Chart(document.getElementById(elem_id), {
		type: 'line',
		data: {
			cubicInterpolationMode: 'monotone',
			tension: 0.4,
			pointStyle: 'circle',
			pointRadius: 5,
			pointHoverRadius: 10,
			datasets: [{
				label: exercise_name,
				data: [],
				fill: false,
				borderColor: 'rgb(75, 192, 192)',
				tension: 0.1
			}]
		},
		options: {
			scales: {
				y: {
					beginAtZero: true
				}
			},
			plugins: {
				legend: {
					labels: {
						font:  {
							size: 18
						}
					}
				}
			}
		}
	});

	// Load chart data for exercise
	const json = await request(`/api/progress/exercise/${exercise_id}`);

	json.forEach(row => {
		chart.data.datasets[0].data.push(row[1]);
		chart.data.labels.push(row[0]);
	});


	chart.update();
}
