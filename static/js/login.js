function switchForm(formToShow) {
    if (formToShow === 'signup') {
        document.getElementById('signup-card').style.display = 'block';
        document.getElementById('login-card').style.display = 'none';
    } else if (formToShow === 'login') {
        document.getElementById('signup-card').style.display = 'none';
        document.getElementById('login-card').style.display = 'block';
    }
}