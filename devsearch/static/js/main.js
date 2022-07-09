// get search form and page links
const searchForm = document.getElementById("searchForm");
const pageLinks = document.getElementsByClassName("page-link");

// Ensure search form exists
if (searchForm) {
	for (let i = 0; pageLinks.length > i; i++) {
		pageLinks[i].addEventListener("click", function (e) {
			e.preventDefault();
			console.log("button clicked");

			// Get the data attribute

			const page = this.dataset.page;

			// Add hidden search input to form

			searchForm.innerHTML += `
                    <input value=${page} name="page" hidden />
                `;

			// SUBMIT FORM
			searchForm.submit();
		});
	}
}
