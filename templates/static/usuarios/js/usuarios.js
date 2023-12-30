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

        nome = document.getElementById('nome')
        nome.value = data['nome']

        sobrenome = document.getElementById('sobrenome')
        sobrenome.value = data['sobrenome']

        cpf = document.getElementById('cpf')
        cpf.value = data['cpf']

        email = document.getElementById('email')
        email.value = data['email']
    })
}