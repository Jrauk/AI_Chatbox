let translate_to_french = ()=>{
    text_to_translate = document.getElementById("text_to_translate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "english_to_french?text_to_translate"+"="+text_to_translate, true);
    xhttp.send();
}

let translate_to_english = ()=>{
    text_to_translate = document.getElementById("text_to_translate").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("translated_text").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "french_to_english?text_to_translate"+"="+text_to_translate, true);
    xhttp.send();
}

