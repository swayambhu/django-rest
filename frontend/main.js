const loginBtn = document.getElementById('login-btn')
const logoutBtn = document.getElementById("logout-btn");

const token = localStorage.getItem("token");

if (token) {
    loginBtn.remove()
} else {
    logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location.replace('login.html')
})
const projectsUrl = `http://127.0.0.1:8000/api/projects`

const getProjects = async() => {
    const data = await fetch(projectsUrl).then(res => res.json()).then(res => res)

    buildProjects(data);
}

getProjects()

const buildProjects = (projects) => {
    const projectsWrapper = document.getElementById("projects--wrapper")
    let projectCards = ""
    projects.map(({id, featured_image, vote_ratio, title, description }) => {
		projectCards += `
        <div class='project--card'>
            <img src="http://127.0.0.1:8000${featured_image}"/>
            <div>
                <div class="card--header">
                    <h3>
                        ${title}
                    </h3>
                    <strong class="vote--option" data-vote='up' data-project='${id}'>
                        &#43;
                    </strong>
                    <strong class="vote--option" data-vote='down' data-project='${id}'>
                        &#8722;
                    </strong>
                </div>
                <em>${vote_ratio}% Positive Feedback</em>
                <p>${description.substring(0, 150)}</p>
            </div>


        </div>
        `;
	});

    Promise.all(projects).then(() => {
        projectsWrapper.innerHTML = projectCards;
        addVoteEvents()
    })

}

// ADD AN EVENT LISTENER

const addVoteEvents = () => {
    const voteBtns = document.getElementsByClassName("vote--option");

    
    for (let i = 0; i < voteBtns.length; i++){
        voteBtns[i].addEventListener('click', (e) => {
            const { vote, project } = e.target.dataset
            
            fetch(`${projectsUrl}/${project}/vote/`, {
				method: "POST",
				headers: {
					"Content-type": "application/json",
					Authorization: `Bearer ${token}`,
                },
                body: JSON.stringify({
                    value: vote,
                })
            }).then(res => res.json()).then(data => {
                getProjects();
            });
        })
    }
}

