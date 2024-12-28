async function fetchEmails() {
  try {
    // Fetch sorted emails from the backend
    const response = await fetch("http://127.0.0.1:8000/emails/gmail");
    const data = await response.json();

    const sortedEmails = data.sorted_emails;
    const emailResultsDiv = document.getElementById("email-results");

    emailResultsDiv.innerHTML = ""; // Clear previous results

    // Display sorted emails
    for (let category in sortedEmails) {
      const categoryDiv = document.createElement("div");
      categoryDiv.classList.add("email-category");
      categoryDiv.innerHTML = `<h3>${category
        .replace("_", " ")
        .toUpperCase()}</h3>`;

      const emails = sortedEmails[category];
      if (emails.length > 0) {
        const list = document.createElement("ul");
        emails.forEach((email) => {
          const listItem = document.createElement("li");
          listItem.classList.add("email-item");
          listItem.innerHTML = `<strong>From:</strong> ${email.sender} <br> <strong>Subject:</strong> ${email.subject}`;
          list.appendChild(listItem);
        });
        categoryDiv.appendChild(list);
      } else {
        categoryDiv.innerHTML += `<p>No emails in this category.</p>`;
      }

      emailResultsDiv.appendChild(categoryDiv);
    }
  } catch (error) {
    console.error("Error fetching emails:", error);
  }
}
