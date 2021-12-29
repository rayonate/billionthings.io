let commonMsg = 'This field is required'
let serviceExists = 'This title is already taken'
let invalidCharacters = 'Invalid Characters'
let minimumField = "Minimum length of this field is "
let maximumField = "Maximum length of this field is "



let clearValidationError = (inputID, validationID, btnID) => {
    var elem = document.getElementById(inputID);
    elem.classList.add("valid-input-field");
    elem.classList.remove("invalid-input-field");
    document.getElementById(validationID).innerHTML = "";
    document.getElementById(btnID).removeAttribute('disabled');
    validateAdsProfileForm();
}


let raiseValidationError = (inputID, validationID, btnID, msg) => {
    var elem = document.getElementById(inputID);
    elem.classList.add("invalid-input-field");
    elem.classList.remove("valid-input-field");
    document.getElementById(validationID).innerHTML = msg;
    document.getElementById(btnID).setAttribute('disabled', true);
}

let checkRegexMinMaxValidations = (inputID, validationID, btnID, regex, min, max) => {
    let inputElement = document.getElementById(inputID);
    if (inputElement.value == "") {
        raiseValidationError(inputID, validationID, btnID, commonMsg);
    } else {
        if (regex.test(inputElement.value) === false) {
            raiseValidationError(inputID, validationID, btnID, invalidCharacters);
        } else if (inputElement.value.length < min) {
            raiseValidationError(inputID, validationID, btnID, minimumField + `${min}`);
        } else if (inputElement.value.length > max) {
            raiseValidationError(inputID, validationID, btnID, maximumField + `${max}`);
        } else {
            clearValidationError(inputID, validationID, btnID, )
        }
    }
}


function categoryValidation() {
    let inputID = 'bt_category'
    let validationID = 'validation_category'
    let btnID = 'adsProfileNextBtn'
    checkRegexMinMaxValidations(inputID, validationID, btnID)
}

function titleValidation() {
    let inputID = 'bt_title'
    let validationID = 'validation_title'
    let btnID = 'adsProfileNextBtn'
    let regex = /^[a-zA-Z-_\s]+$/;
    let inputElement = document.getElementById(inputID);
    let _data = {
        bt_title: inputElement.value,
    }
    let url = window.location.origin + '/check_title';
    fetch(url, {
            method: "POST",
            body: JSON.stringify(_data),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        })
        .then(response => response.json())
        .then(json => {
            console.log(json);
            console.log(json.result.data);
            if (json.result.data.exists) {
                raiseValidationError('bt_title', 'validation_title', 'adsProfileNextBtn', serviceExists);
            } else {
                checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 20);
            }
        })
        .catch(err => console.log(err));
}

function descriptionValidation() {
    let inputID = 'bt_description'
    let validationID = 'validation_description'
    let btnID = 'adsProfileNextBtn'
    let regex = /^[a-zA-Z\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 200)
}

function validateAdsProfileForm() {
    if (
        (document.getElementById("validation_category").innerHTML == "") &&
        (document.getElementById("validation_title").innerHTML == "") &&
        (document.getElementById("validation_description").innerHTML == "")
    ) {
        document.getElementById("adsProfileNextBtn").disabled = false;
        console.log("form is valid");
    } else {
        console.log("forms is in-valid");
        document.getElementById("adsProfileNextBtn").setAttribute('disabled', true);
    }
}