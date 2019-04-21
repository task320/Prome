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

function postContent(){
    let result = confirm('投稿します。よろしいですか？')
    if(result){
        document.formContent.submit()
    }
}