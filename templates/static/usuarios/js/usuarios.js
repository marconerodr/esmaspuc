// Abaixo, inserimos o formulário de evoluções de usuário, conforme a necessidade do profissional técnico.

function add_evol(){
    container = document.getElementById("form-evol")

    html = "<br><div class='row'> <div class='col-md'> <p>Data:</p> <input type='date' class='form-control' name='dia'></div> <div class='col-md'><p>Demanda:</p> <input type='text' placeholder='Demanda' class='form-control' name='demanda'> </div></div><br><p>Descrição:</p> <textarea class='form-control' placeholder='Digite uma descrição...' name='descricao'></textarea><hr style='border-color: gray;'>";

    container.innerHTML += html


}

// Abaixo, mudamos a tela da página Usuários, de acordo com a opção selecionada, para adicionar um usuário ou atualizar um já existente.

function exibir_form(tipo){
    add_usuario = document.getElementById('add_usuario')
    att_usuario = document.getElementById('att_usuario')

    if(tipo=="1"){
        att_usuario.style.display = 'none'
        add_usuario.style.display = 'block'
    }else if(tipo=="2"){
        att_usuario.style.display = 'block'
        add_usuario.style.display = 'none'        
    }
}

// Abaixo, usamos um CSRF Token para identificar o usuário selecionado na tela de Atualizar usuário e puxar os dados dele pra exibição.
function dados_usuario(){
    usuario = document.getElementById('usuario-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    id_usuario = usuario.value

    data = new FormData()
    data.append('id_usuario', id_usuario)

    fetch("/usuarios/atualiza_usuario/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: data,
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('form-att-usuario').style.display = 'block'

        id = document.getElementById('usuario_id')
        id.value = data['usuario_id']

        nome = document.getElementById('nome')
        nome.value = data['usuario']['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['usuario']['sobrenome']

        cpf = document.getElementById('cpf')
        cpf.value = data['usuario']['cpf']

        email = document.getElementById('email')
        email.value = data['usuario']['email']

        div_evolucoes = document.getElementById('evolucoes');
        div_evolucoes.innerHTML = ""
        for (i = 0; i < data['evolucoes'].length; i++) {
            div_evolucoes.innerHTML += "<form action='/usuarios/update_evolucao/" + data['evolucoes'][i]['id'] + "' method='POST'>" +
                "<div class='row'>" +
                "<div class='col-md'>" +
                "<input class='form-control' type='text' name='demanda' value='" + data['evolucoes'][i]['fields']['demanda'] + "'>" +
                "</div>" +
                "<div class='col-md'>" +
                "<input class='form-control' type='text' name='descricao' value='" + data['evolucoes'][i]['fields']['descricao'] + "'>" +
                "</div>" +
                "<div class='col-md'>" +
                "<input class='btn btn-success' type='submit' value='Salvar evolução'>" +
                "</div>" +
                "<div>" +
                "<a class='btn btn-danger' href='/usuarios/excluir_evolucao/" + data['evolucoes'][i]['id'] + "'>Excluir evolução</a>" +
                "</div>" +
                "</div>" +
                "</form>" ;
        }
    })
}

function update_usuario(){
    nome = document.getElementById('nome').value
    sobrenome = document.getElementById('sobrenome').value
    email = document.getElementById('email').value
    cpf = document.getElementById('cpf').value
    id = document.getElementById('usuario_id').value

    fetch('/usuarios/update_usuario/' + id + '/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrf_token,
        },
        body: JSON.stringify({
            nome: nome,
            sobrenome: sobrenome,
            email: email,
            cpf: cpf
        })
    }).then(function(result){
        return result.json()
    }).then(function(data){
        var homeSection = document.querySelector('.home-section');

        if(data['status'] == '200'){
        nome = data['nome']
        sobrenome = data['sobrenome']
        email = data['email']
        cpf = data['cpf']
       
        var successAlert = document.createElement('div');
            successAlert.classList.add('alert', 'alert-success');
            successAlert.textContent = 'Alterado com sucesso';
            // Adicionando o alerta ao topo de homeSection
            homeSection.insertBefore(successAlert, homeSection.firstChild);
            // Adicionando o alerta ao topo de homeSection
            homeSection.insertBefore(successAlert, homeSection.firstChild);
            // Removendo o alerta após 3 segundos
            setTimeout(function() {
                successAlert.remove();
            }, 3000);
        }else{
            var errorAlert = document.createElement('div');
            errorAlert.classList.add('alert', 'alert-danger');
            errorAlert.textContent = 'Ocorreu algum erro';
            // Adicionando o alerta ao topo de homeSection
            homeSection.insertBefore(errorAlert, homeSection.firstChild);
            // Adicionando o alerta ao topo de homeSection
            homeSection.insertBefore(errorAlert, homeSection.firstChild);
            // Removendo o alerta após 3 segundos
            setTimeout(function() {
                errorAlert.remove();
            }, 3000);
        }
    })
}