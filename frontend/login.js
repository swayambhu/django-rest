const form = document.getElementById('login-form')

form.addEventListener('submit', (e) => {
    e.preventDefault();
    console.log('form submited')

    const formData = {
        username: form.username.value,
        password: form.password.value
    }

    fetch(`http://127.0.0.1:8000/api/users/token/`, {
        method: "POST",
        headers: {
            'Content-type': 'application/json',
        },
        body: JSON.stringify(formData)
    }).then(res => res.json()).then((data) => {
        const accessToken = data.access
        if (accessToken) {
            localStorage.setItem('token', accessToken)
            window.location.replace('project-list.html')
        } else {
            alert('Username or password incorrect')
        }
    });
})