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

        // Preencher os campos de DadosPessoal
        nome_social = document.getElementById('nome_social')
        nome_social.value = data['dadospessoais']['nome_social']
        
        nis = document.getElementById('nis');
        nis.value = data['dadospessoais']['nis'];

        data_nascimento = document.getElementById('data_nascimento');
        data_nascimento.value = data['dadospessoais']['data_nascimento'];

        identidade_genero = document.getElementById('identidade_genero');
        identidade_genero.value = data['dadospessoais']['identidade_genero'];

        cor_raca = document.getElementById('cor_raca');
        cor_raca.value = data['dadospessoais']['cor_raca'];

        estado_civil = document.getElementById('estado_civil');
        estado_civil.value = data['dadospessoais']['estado_civil'];

        endereco = document.getElementById('endereco');
        endereco.value = data['dadospessoais']['endereco'];

        telefone = document.getElementById('telefone');
        telefone.value = data['dadospessoais']['telefone'];

        naturalidade = document.getElementById('naturalidade');
        naturalidade.value = data['dadospessoais']['naturalidade'];

        tempo_residencia_municipio = document.getElementById('tempo_residencia_municipio');
        tempo_residencia_municipio.value = data['dadospessoais']['tempo_residencia_municipio'];

        rg = document.getElementById('rg');
        rg.value = data['dadospessoais']['rg'];

        certidao_nascimento_casamento = document.getElementById('certidao_nascimento_casamento');
        certidao_nascimento_casamento.value = data['dadospessoais']['certidao_nascimento_casamento'];

        titulo_eleitor = document.getElementById('titulo_eleitor');
        titulo_eleitor.value = data['dadospessoais']['titulo_eleitor'];

        nivel_escolaridade = document.getElementById('nivel_escolaridade');
        nivel_escolaridade.value = data['dadospessoais']['nivel_escolaridade'];

        ocupacao = document.getElementById('ocupacao');
        ocupacao.value = data['dadospessoais']['ocupacao'];

        renda = document.getElementById('renda');
        renda.value = data['dadospessoais']['renda'];

        extrema_pobreza = document.getElementById('extrema_pobreza');
        extrema_pobreza.value = data['dadospessoais']['extrema_pobreza'];

        pessoa_com_deficiencia = document.getElementById('pessoa_com_deficiencia');
        pessoa_com_deficiencia.value = data['dadospessoais']['pessoa_com_deficiencia'];

        // Preencher os campos de Residencia
        tipo_imovel = document.getElementById('tipo_imovel');
        tipo_imovel.value = data['residencia_campos']['tipo_imovel'];

        valor_aluguel = document.getElementById('valor_aluguel');
        valor_aluguel.value = data['residencia_campos']['valor_aluguel'];

        numero_comodos = document.getElementById('numero_comodos');
        numero_comodos.value = data['residencia_campos']['numero_comodos'];

        material_paredes = document.getElementById('material_paredes');
        material_paredes.value = data['residencia_campos']['material_paredes'];

        material_piso = document.getElementById('material_piso');
        material_piso.value = data['residencia_campos']['material_piso'];

        material_telhado = document.getElementById('material_telhado');
        material_telhado.value = data['residencia_campos']['material_telhado'];

        estado_conservacao = document.getElementById('estado_conservacao');
        estado_conservacao.value = data['residencia_campos']['estado_conservacao'];

        fornecimento_agua = document.getElementById('fornecimento_agua');
        fornecimento_agua.value = data['residencia_campos']['fornecimento_agua'];

        fornecimento_energia = document.getElementById('fornecimento_energia');
        fornecimento_energia.value = data['residencia_campos']['fornecimento_energia'];

        coleta_esgoto = document.getElementById('coleta_esgoto');
        coleta_esgoto.value = data['residencia_campos']['coleta_esgoto'];

        coleta_lixo = document.getElementById('coleta_lixo');
        coleta_lixo.value = data['residencia_campos']['coleta_lixo'];

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