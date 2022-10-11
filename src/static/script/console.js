function editContent(id){
    window.location.href = '/console/edit?contentId=' + id
}

function deleteContent(id){
    let result = confirm('削除します。よろしいですか？')
    if(result){
        document.getElementById('contentId').value = id
        document.formContent.submit()
    }
}

function postMdContent(){
    let titleElement = document.getElementById("title");
    if(!titleElement.value){
        alert("記事のタイトルが設定されていません。");
        return;
    }

    let uploadFileElement = document.getElementById("uploadFile");
    if(!uploadFileElement.value){
        alert("Markdownファイルが指定されていません。");
        return;
    }


    let result = confirm('投稿します。よろしいですか？');
    if(result){
        let tagsElement = document.getElementById("tag-list"); 
        let arrayTags = [];
        for(let i = 0; i < tagsElement.children.length; i++){
            arrayTags.push(tagsElement.children[i].children[0].innerText);
        }
        let jsonTags = JSON.stringify(arrayTags);
        let tagsHidden = document.postContent.tags;
        tagsHidden.value = jsonTags;
        
        document.postContent.submit()
    }
}