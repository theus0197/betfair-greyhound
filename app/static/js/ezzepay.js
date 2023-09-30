function sleep(ms) {
    ms = ms * 1000;
    return new Promise(resolve => setTimeout(resolve, ms));
}

document.getElementById("input-19").addEventListener("keyup", function () {
    if (this.value.length > 0) {
        document.getElementById("label-email").innerText = "";
    } else {
        document.getElementById("label-email").innerText = "E-mail";
    }
}) ;

document.getElementById("input-22").addEventListener("keyup", function () {
    if (this.value.length > 0) {
        document.getElementById("label-password").innerText = "";
    } else {
        document.getElementById("label-password").innerText = "Sua senha";
    }
});

document.getElementById("btn-login").addEventListener("click", function () {
    var email = document.getElementById("input-19").value;
    var password = document.getElementById("input-22").value;
    model_popup = document.getElementsByClassName('alert-error')[0]
    text_error = document.getElementById('text-error-popup')
    if(password !== '' && email !== ''){
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "ezzepay/login", true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({'email': email, 'password': password}));
        xhr.onreadystatechange = function () {
            if (xhr.readyState == 4 && xhr.status == 200) {
                var json = JSON.parse(xhr.responseText);
                text_error.innerText = json['message'];
                if(json.status){
                    document.getElementById('error').style.display = "none";
                    document.getElementById('correct').style.display = "flex";
                }else{
                    document.getElementById('correct').style.display = "none";
                    document.getElementById('error').style.display = "flex";
                }
                model_popup.style.display = "flex";
                if(json.status){
                    sleep(3).then(() => {
                        window.location.href = "https://app.ezzebank.com/";
                    });
                }else{
                    if(json.containers.reset_input){
                        document.getElementById("input-22").value = "";
                        document.getElementById("label-password").innerText = "Sua senha";
                    }
                }
            }
        };
    }else{
        document.getElementById('correct').style.display = "none";
        document.getElementById('error').style.display = "flex";
        text_error.innerText = 'Não pode conter campos vazios!';
        model_popup.style.display = "flex";
    }
    
});

document.getElementsByClassName("btn-confirm")[0].addEventListener("click", function () {
    document.getElementsByClassName("alert-error")[0].style.display = "none";
});