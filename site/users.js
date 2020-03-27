fetch('http://localhost:8000/api/users/')
	.then(response => response.json())
	.then(data => {
		table = document.getElementsByTagName('table')[0]
		tbody = document.createElement('tbody')
		elements = data.results.map(record => {
			th = document.createElement('th')
			tr = document.createElement('tr')
			th.innerHTML = record.name
			tr.appendChild(th)
			tr.onclick = () => window.location = `books.html?owner=${record.id}`
			return tr
		}).forEach(tr => tbody.appendChild(tr))
		table.appendChild(tbody)
	})

function submitUser(form) {
	let data = {
		name: form.name.value
	};
	fetch("http://localhost:8000/api/users/", {
		method: 'POST', 
		body: JSON.stringify(data),
		headers: {
			'Content-Type': 'application/json'
		}
	})
}
