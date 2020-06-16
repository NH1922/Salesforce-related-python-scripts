editCheckboxes = document.querySelectorAll('[type="checkbox"][title="Edit Access"]')
editCheckboxes.forEach(box =>{box.checked = false})

readCheckboxes = document.querySelectorAll('[type="checkbox"][title="Read Access"]')
readCheckboxes.forEach(box =>{box.checked = true})


