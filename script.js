document.getElementById('formData').addEventListener('submit', retrieveName)

function retrieveName (e) {
    e.preventDefault()

    let name = document.getElementById('name').value

    fetch(`http://localhost:5000/${name}`)
    .then((res)=> res.json())
    .then((data)=> {
        document.getElementById('output').innerHTML = `<li class="list-group-item">Name : ${data.name} Gender : ${data.gender} Age : ${data.age}</li>`
    })
}

document.getElementById('postData').addEventListener('submit', postData)

function postData (e) {
    e.preventDefault()

    let name = document.getElementById('postName').value
    let gender = document.getElementById('postGender').value
    var age = document.getElementById('postAge').value

    fetch('http://localhost:5000/postData', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({
            'name' : name,
            'gender' : gender,
            'age' : age
        })
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
}