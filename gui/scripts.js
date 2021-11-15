function updatePassword(e) {
  const passModal = new bootstrap.Modal(document.getElementById("passwordModal"), {});
  passModal.show()

  row = e.currentTarget.closest("tr")
  modal = document.getElementById("passwordModal")
  passwordModalLabel = modal.querySelector("#passwordModalLabel")
  passwordModalLabel.innerText = "Update password"

  return getPasswords(row.dataset.uuid).then((pw_data) => {
    nameField = modal.querySelector("#name")
    loginField = modal.querySelector("#login")
    passField = modal.querySelector("#password")

    nameField.value = pw_data["name"]
    loginField.value = pw_data["login"]
    passField.value = pw_data["password"]

    // Update the form action function
    form = modal.querySelector("#passwordForm")
    form.onsubmit = () => updateEntry(pw_data["uuid"], form)
  })
}

function updateEntry(pw_id, form) {
  const passForm = new FormData(form);
  let api = `http://127.0.0.1:5000/api/passwords/${String(pw_id)}/`

  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");
  let pw_data = JSON.stringify({
    "name": passForm.get("name"),
    "login": passForm.get("login"),
    "password": passForm.get("password")
  })

  const requestOptions = {
    method: 'PUT',
    redirect: 'follow',
    headers: myHeaders,
    body: pw_data
  };

  return fetch(api, requestOptions)
    .then(response => response.json())
    .then(result =>
      {
        buildStuff()
        return result.data
      })
    .catch(error => console.log('error', error));
}

function createEntry(e) {
  e.preventDefault();
  const form = new FormData(e.target);
  let api = "http://127.0.0.1:5000/api/passwords/"

  const myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");
  let pw_data = JSON.stringify({
    "name": form.get("name"),
    "login": form.get("login"),
    "password": form.get("password")
  })

  const requestOptions = {
    method: 'POST',
    redirect: 'follow',
    headers: myHeaders,
    body: pw_data
  };

  return fetch(api, requestOptions)
    .then(response => response.json())
    .then(result =>
      {
        buildStuff()
        return result.data
      })
    .catch(error => console.log('error', error));
}

function getPasswords(id="") {
  let api = "http://127.0.0.1:5000/api/passwords/"

  if(id) {
    api = api + String(id) + "/"
  }

  const requestOptions = {
    method: 'GET',
    redirect: 'follow'
  };

  return fetch(api, requestOptions)
    .then(response => response.json())
    .then(result =>
      {
        return result.data
      })
    .catch(error => console.log('error', error));

}

function deletePassword(id) {
  const api = `http://127.0.0.1:5000/api/passwords/${id}/`
  const requestOptions = {
    method: 'DELETE',
    redirect: 'follow'
  };

  return fetch(api, requestOptions)
    .then(response => response.json())
    .then(result =>
      {
        return result.data
      })
    .catch(error => console.log('error', error));
}

function showPassword(e) {
  row = e.currentTarget.closest("tr")
  passwordCell = row.querySelector("[data-type='password']")
  return getPasswords(row.dataset.uuid).then((pw_data) => {
    passwordCell.innerText = pw_data["password"]
  })
}

function hidePassword(e) {
  row = e.currentTarget.closest("tr")
  passwordCell = row.querySelector("[data-type='password']")
  passwordCell.innerText = "********"
}


function createRows(pw_data) {
  tbody = document.querySelector("#pw_table tbody")
  // Remove existing child elements
  tbody.innerHTML = ""
  for (i=0; i < pw_data.length; i++) {
    const pw = pw_data[i]
    const tableRow = document.createElement("tr")
    const serialNumber = document.createElement("td")
    const nameTableData = document.createElement("td")
    const loginTableData = document.createElement("td")
    const passTableData = document.createElement("td")
    const lastTableData = document.createElement("td")

    tableRow.dataset.uuid = pw.uuid
    serialNumber.innerText = String(i+1)
    nameTableData.innerText = pw.name
    loginTableData.innerText = pw.login
    passTableData.innerText = "********"
    passTableData.dataset.type = "password"
    lastTableData.dataset.type = "action_buttons"
    lastTableData.innerHTML = `
       <span class="badge rounded-pill bg-success text-dark pw_viewer" data-uuid=${pw.uuid}>view</span>
       <span class="badge rounded-pill bg-info text-dark pw_conceal" data-uuid=${pw.uuid}>hide</span>
       <span class="badge rounded-pill bg-warning text-dark pw_edit" data-uuid=${pw.uuid}>edit</span>
       <span class="badge rounded-pill bg-danger text-dark pw_delete" data-uuid=${pw.uuid}>delete</span>
    `

    tableRow.appendChild(serialNumber)
    tableRow.appendChild(nameTableData)
    tableRow.appendChild(loginTableData)
    tableRow.append(passTableData)
    tableRow.append(lastTableData)
    tbody.append(tableRow)
  }
}

function addEvents() {

  action_columns = document.querySelectorAll("[data-type='action_buttons']")
  for (col of action_columns) {
    viewer_button = col.querySelector(".pw_viewer")
    viewer_button.addEventListener("click", showPassword)

    conceal_button = col.querySelector(".pw_conceal")
    conceal_button.addEventListener("click", hidePassword)

    edit_button = col.querySelector(".pw_edit")
    edit_button.addEventListener("click", updatePassword)


    delete_button = col.querySelector(".pw_delete")
    delete_button.addEventListener("click", (e) => {
      deletePassword(e.currentTarget.dataset.uuid).then(() => {
        buildStuff()
      })
    })
  }

  // for (button of viewer_buttons) {
  //   button.addEventListener("mouseenter", hidePassword)
  //   button.addEventListener("mouseleave", hidePassword)
  // }
}


// Action block
// Resolve the getpasswords call and build rows
function buildStuff() {
  getPasswords().then((pw_data) => {
    createRows(pw_data)
    addEvents()
  })
}

buildStuff()
