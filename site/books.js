function getUrlParameter(name) {
	    name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
	    var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
	    var results = regex.exec(location.search);
	    return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
};
document.getElementById("btn-sbmt").onclick = function(event){
	submitBook(this.form)
	event.preventDefault()
};

let currentUser = getUrlParameter('owner')
fetch(`http://localhost:8000/api/books/?owner=${currentUser}`)
	.then(response => {
		return response.json()
	})
	.then(data => {
		table = document.getElementsByTagName('table')[0]
		tbody = document.createElement('tbody')
		data.results.map(record => {
			tr = document.createElement('tr');
			['title', 'author', 'description'].map(prop => {
				th = document.createElement('th')
				th.innerHTML = record[prop]
				return th
			}).forEach(th => tr.appendChild(th))
			tr.onclick = () => window.location = 'google.com'
			return tr
		}).forEach(tr => tbody.appendChild(tr))
		table.appendChild(tbody)
	})

function submitBook(form) { 
	let href = document.location
	let data = { 
		title: form.title.value,
		author: form.title.value,
		description: form.description.value,
		owner: currentUser,
	};
	fetch("http://localhost:8000/api/books/", {
		method: 'POST', 
		body: JSON.stringify(data),
		headers: {
			'Content-Type': 'application/json'
		}
	}).then(() => {document.location = href})
}
