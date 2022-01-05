function addressStreetValidation() {
    let inputID = 'street'
    let validationID = 'validation_street'
    let btnID = 'adsProfileBtn'
    let regex = /^[a-zA-Z0-9-_\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 2, 12, validateAddressForm);
}

function addressStreet2Validation() {
    let inputID = 'street2'
    let validationID = 'validation_street2'
    let btnID = 'adsProfileBtn'
    let regex = /^[a-zA-Z0-9-_\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 2, 12, validateAddressForm);
}

function addressCityValidation() {
    let inputID = 'city'
    let validationID = 'validation_city'
    let btnID = 'adsProfileBtn'
    let regex = /^[a-zA-Z\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 20, validateAddressForm);
}

function addressZipValidation() {
    let inputID = 'code'
    let validationID = 'validation_zip'
    let btnID = 'adsProfileBtn'
    let regex = /^[a-zA-Z0-9-_\s]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 12, validateAddressForm);
}

function addressPhoneValidation() {
    let inputID = 'phone'
    let validationID = 'validation_tp1'
    let btnID = 'adsProfileBtn'
    let regex = /[0-9+]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 12, validateAddressForm);
}

function addressMobileValidation() {
    let inputID = 'mobile'
    let validationID = 'validation_tp2'
    let btnID = 'adsProfileBtn'
    let regex = /[0-9+]+$/;
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 12, validateAddressForm);
}

function addressEmailValidation() {
    let inputID = 'email'
    let validationID = 'validation_email'
    let btnID = 'adsProfileBtn'
    let regex = /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/
    checkRegexMinMaxValidations(inputID, validationID, btnID, regex, 3, 50);
}


function validateAddressForm() {
    if (
        (document.getElementById("validation_tp1").innerHTML == "") &&
        (document.getElementById("validation_tp2").innerHTML == "") &&
        (document.getElementById("validation_email").innerHTML == "") &&
        (document.getElementById("validation_no").innerHTML == "") &&
        (document.getElementById("validation_address1").innerHTML == "") &&
        (document.getElementById("validation_address2").innerHTML == "") &&
        (document.getElementById("validation_zip").innerHTML == "")
    ) {
        document.getElementById("adsProfileBtn").disabled = false;
        console.log("form is valid");
    } else {
        console.log("forms is in-valid");
        document.getElementById("adsProfileBtn").setAttribute('disabled', true);
    }
}