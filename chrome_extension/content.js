// ...inside setTimeout
const body = getEmailBody();
if (body) {
  console.log("Extracted Email Body:", body);  // <== ADD THIS
  sendToServer(body);
} else {
  console.log("No email body found.");
}