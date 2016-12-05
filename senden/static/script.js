

function masterOnload() {
    TextCounter();
}

function refreshName(namefield) {
    var textbox = document.getElementById("messageID");
    //textbox.value += "\nGrüße, "+ namefield.value;
    TextCounter();
}


function handleSend(datestring){
    var FormDatefield = document.getElementById("datetimefieldID");
    FormDatefield.value = datestring;
    document.getElementById("form1").submit();
}

function resetAction() {
//Reset-Button wurde gedrückt
    window.location.href='.'
    //var form1 = document.getElementById("form1");
    //form1.reset();
    //TextCounter();
}
