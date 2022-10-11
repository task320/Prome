function tagInputKeydwon(event){
    if (event.key === 'Enter') {
        appendTag(event);
    }
}
function appendTag(event){
    let element = document.getElementById("tag-list");
    let tagElement = createTagElement(event.target.value);
    element.appendChild(tagElement)

}
function createTagElement(tagName){
    let tagElement = document.createElement('il');
    tagElement.classList.add("tag-item");

    let spanElement = document.createElement('span');
    spanElement.innerText = tagName;
    tagElement.appendChild(spanElement);

    let tagXButton = document.createElement('button');
    tagXButton.type = "button";
    tagXButton.classList.add("tag-remove");
    tagXButton.addEventListener("click",() => removeTag(tagXButton));
    tagXButton.innerText = "X";

    tagElement.appendChild(tagXButton);

    return tagElement;

}
function removeTag(el){
    element = el.closest(".tag-item");
    element.remove();
}
function forcusInput(){
    let element = document.getElementById("tag-input");
    element.focus();
}