function myFunction() {
    const copyText = document.getElementById("myCopy");
    let range = document.createRange();
    range.selectNode(copyText);
    window.getSelection().removeAllRanges(); // clear current selection
    window.getSelection().addRange(range); // to select text
    document.execCommand("copy");
    window.getSelection().removeAllRanges();// to deselect
    alert("Скопирована ссылка: " + copyText.innerHTML);
}