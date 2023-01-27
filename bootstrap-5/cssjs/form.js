const form1 = document.getElementById('signin');
const form2 = document.getElementById('signup')
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const firstname = document.getElementById('firstname');
const lastname = document.getElementById('lastname');
const Username = document.getElementById('Username');
const Email = document.getElementById('Email');
const Password = document.getElementById('Password');
const confirm = document.getElementById('confirm');
const create = document.getElementById('btn');
const or = document.getElementById('or')
const login = document.getElementById('btn1');
const or1 = document.getElementById('or1')
function showError(input, message) {
    const formcontrol = input.parentElement;
    formcontrol.className = ' error';
    const small = formcontrol.querySelector('small');
    small.innerText = message;
}
function showSuccess(input){
    const formcontrol = input.parentElement;
    formcontrol.className = ' success';
}
function checkEmail(input) {
    const regex = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    if (regex.test(input.value.trim())) {
      showSuccess(input);
    } else {
      showError(input, 'Email is not valid');
    }
  }
function checkRequired(inputArr) {
    inputArr.forEach(function (input) {
      if (input.value.trim() === '') {
        showError(input, `${getFieldName(input)} is required`);
      } else {
        showSuccess(input);
      }
    });
}
function checkLength(input, min, max) {
    if (input.value.length < min) {
      showError(input, `${getFieldName(input)} must be at least ${min} characters`);
    } else if (input.value.length > max) {
      showError(input, `${getFieldName(input)} must be less than ${max} characters`);
    } else {
      showSuccess(input);
    }
} 
function checkPasswordsMatch(input1, input2) {
    if (input1.value !== input2.value) {
      showError(input2, 'Passwords do not match');
    }
}
function getFieldName(input) {
    return input.id.charAt(0).toUpperCase() + input.id.slice(1);
} 
form1.addEventListener('submit', function(e){
    e.preventDefault()
    checkRequired([username, email, password]);
    checkEmail(email);
});
form2.addEventListener('submit', function(e){
    e.preventDefault()
    checkRequired([firstname, lastname, Username, Email, Password, confirm]);
    checkLength(Username, 5, 15);
    checkLength(Password, 8, 20);
    checkEmail(Email);
    checkPasswordsMatch(Password, confirm);
});
create.addEventListener('click',() => {
    form1.classList.add = 'd-none';
    or.classList.add = 'd-none';
    create.classList.add = 'd-none';
    form2.classList.remove = 'd-none';
    login.classList.remove = 'd-none';
    or1.classList.remove = 'd-none';
})
login.addEventListener('click',() => {
    form1.classList.remove = 'd-none';
    or.classList.remove = 'd-none';
    create.classList.remove = 'd-none';
    form2.classList.add = 'd-none';
    login.classList.add = 'd-none';
    or1.classList.add = 'd-none';
})
