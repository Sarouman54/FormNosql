function addQuestion() {
    const question_list = document.getElementById('questions_list').getElementsByTagName('li');
    var i = 1;
    while (i <= question_list.length) {
        i++;
    }
    const node = document.createElement('li');
    const br1 = document.createElement('br');
    const br2 = document.createElement('br');
    const br3 = document.createElement('br');

    const input = document.createElement('input');
    input.type = 'text';
    input.setAttribute('name', 'question'+i);
    input.setAttribute('id', 'question'+i);
    input.setAttribute('required','required');
    input.setAttribute("class","form-control");

    const label = document.createElement('label');
    label.setAttribute("class", "form-label");
    label.innerHTML = "Sélectionner le type de la question (par défaut \"ouverte\")";

    const select = document.createElement('select');
    select.setAttribute('name', 'type'+i);
    select.setAttribute('id', 'type'+i);
    select.setAttribute("class", "form-select");
    select.setAttribute('aria-label', "Default select example");

    const option1 = document.createElement('option');
    option1.setAttribute('value', 'ouverte');
    option1.innerHTML = "ouverte";

    const option2 = document.createElement('option');
    option2.setAttribute('value', 'fermée');
    option2.innerHTML = "fermée";

    select.appendChild(option1);
    select.appendChild(option2);
    
    node.appendChild(input);
    document.getElementById("questions_list").appendChild(node);
    document.getElementById("questions_list").appendChild(br1);
    document.getElementById("questions_list").appendChild(label);
    document.getElementById("questions_list").appendChild(select);
    document.getElementById("questions_list").appendChild(br2);
    document.getElementById("questions_list").appendChild(br3);
}