document.getElementById("checkBtn").addEventListener("click", function () {
  const emailText = document.getElementById("emailText").value;

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ email_text: emailText })
  })
    .then(response => response.json())
    .then(data => {
      document.getElementById("result").innerText =
        `Result: ${data.label}\nPhishing Score: ${data.phishing_score}%`;
    })
    .catch(err => {
      document.getElementById("result").innerText = "Error contacting server.";
      console.error(err);
    });
});