window.onload = () => {
  document.getElementById("year").innerHTML = `&copy; ${new Date().getFullYear()} - My Django Application</p>`
}

function removeAlert() {
  setTimeout(() => {
    document.getElementById('alert').remove()
  }, 500)
}