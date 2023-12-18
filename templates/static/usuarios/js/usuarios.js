function add_evol(){
    container = document.getElementById("form-evol")

    html = "<br><div class='row'> <div class='col-md'> <p>Data:</p> <input type='date' class='form-control' name='dia'></div> <div class='col-md'><p>Demanda:</p> <input type='text' placeholder='Demanda' class='form-control' name='demanda'> </div></div><br><p>Descrição:</p> <textarea class='form-control' placeholder='Digite uma descrição...' name='descricao'></textarea><hr style='border-color: gray;'>";

    container.innerHTML += html


}