function cpf(v){
    if(v != ''){
        v=v.replace(/\D/g,"");
        v=v.replace(/(\d{3})(\d)/,"$1.$2");
        v=v.replace(/(\d{3})(\d)/,"$1.$2");
        v=v.replace(/(\d{3})(\d)/,"$1-$2");
    }
    return v;
}

document.getElementsByClassName('btn-add')[0].addEventListener('click', function() {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/client/add');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            try{
                var response = JSON.parse(xhr.responseText);
            }catch(e){
                document.getElementsByClassName('main-window')[0].innerHTML = xhr.responseText;
                document.getElementsByClassName('main-window')[0].style.display = 'flex';
                add_test();
            }
        }
    }
    xhr.send();
});

function getClients(){
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/get/client');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            document.getElementsByClassName('manager-group-content')[0].innerHTML = xhr.responseText;
            var nameClients = document.getElementsByClassName('name-group');
            for(var i = 0; i < nameClients.length; i++){
                nameClients[i].addEventListener('click', function(){
                    var id = this.getAttribute('id');
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', '/view/client');
                    xhr.onreadystatechange = function() {
                        document.getElementsByClassName('main-window')[0].innerHTML = xhr.responseText;
                        document.getElementsByClassName('main-window')[0].style.display = 'flex';
                        update_test();
                    };
                    xhr.send(JSON.stringify({
                        'id': id
                    }));
                });
            }

            var trashs = document.getElementsByClassName('trash');
            for(var i = 0; i < trashs.length; i++){
                trashs[i].addEventListener('click', function(){
                    var id = this.getAttribute('id');
                    var xhr = new XMLHttpRequest();
                    xhr.open('POST', 'delete/client');
                    xhr.setRequestHeader('Content-Type', 'application/json');
                    xhr.onreadystatechange = function() {
                        if (xhr.readyState === 4 && xhr.status === 200) {
                            window.location.reload();
                        }
                    }
                    xhr.send(JSON.stringify({
                        'id': id
                    }));
                });
            };
        }
    }
    xhr.send(); 
}

function update_test(){    
    document.getElementsByName('cpf')[0].addEventListener('keypress', function(e) {
        if(e.target.value.length >= 14) {
        }else{
            e.target.value = cpf(e.target.value);
        };
    });

    for (var i = 0; i < document.getElementsByClassName('status').length; i++) {
        document.getElementsByClassName('status')[i].addEventListener('click', function() {
            if (this.classList.contains('true')) {
                this.classList.remove('true');
                this.classList.add('false');
                this.dataset.id = 'false';
            } else {
                this.classList.remove('false');
                this.classList.add('true');
                this.dataset.id = 'true'
            }
        });
    }
    
    
    document.getElementsByClassName('btn-update-button')[0].addEventListener('click', function() {
        var id_ = document.getElementById('title-text-form').dataset.id;
        var name = document.getElementsByName('name')[0].value;
        var cpf = document.getElementsByName('cpf')[0].value;
        var email = document.getElementsByName('email')[0].value;
        var roleta = document.getElementById('roleta').dataset.id;
        var dados = document.getElementById('dados').dataset.id;
        var football = document.getElementById('football').dataset.id;
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/update/client');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function() {
            var response = JSON.parse(xhr.responseText);
            if(response.status){
                alert('Alteração do cliente '+ name + ' foi realizado com sucesso!')
                window.location.reload();
            }
        }
        xhr.send(JSON.stringify({
            'id': id_,
            'name': name,
            'cpf': cpf,
            'email': email,
            'roleta': roleta,
            'dados': dados,
            'football': football
        }));
    
    });

    document.getElementsByClassName('close-notification')[0].addEventListener('click', function() {
        notShow();
    });
    
    function notShow(){
        document.getElementsByClassName('main-window')[0].style.display = 'none';
    }
}

function add_test(){
    document.getElementsByName('cpf')[0].addEventListener('keypress', function(e) {
        if(e.target.value.length >= 14) {
        }else{
            e.target.value = cpf(e.target.value);
        };
    });

    document.getElementsByClassName('close-notification')[0].addEventListener('click', function() {
        notShow();
    });
    
    for (var i = 0; i < document.getElementsByClassName('status').length; i++) {
        console.log(i);
        document.getElementsByClassName('status')[i].addEventListener('click', function() {
            if (this.classList.contains('true')) {
                this.classList.remove('true');
                this.classList.add('false');
                this.dataset.id = 'false';
            } else {
                this.classList.remove('false');
                this.classList.add('true');
                this.dataset.id = 'true'
            }
        });
    }
    
    document.getElementsByClassName('btn-add-button')[0].addEventListener('click', function() {
        var name = document.getElementsByName('name')[0].value;
        var cpf = document.getElementsByName('cpf')[0].value;
        var email = document.getElementsByName('email')[0].value;
        var roleta = document.getElementById('roleta').dataset.id;
        var dados = document.getElementById('dados').dataset.id;
        var football = document.getElementById('football').dataset.id;
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/add/newClient');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.onreadystatechange = function() {
            var response = JSON.parse(xhr.responseText);
            if(response.status){
                window.location.reload();
            }
        }
        xhr.send(JSON.stringify({
            'name': name,
            'cpf': cpf,
            'email': email,
            'roleta': roleta,
            'dados': dados,
            'football': football
        }));
    
    });
    
    function notShow(){
        document.getElementsByClassName('main-window')[0].style.display = 'none';
    }
}