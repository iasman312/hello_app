function onError(error) {
    console.log('Лайк не был поставлен');
}

async function makeRequest(url, method='GET') {
    let response = await fetch(url, {method});
    console.log(response)
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function onClickArticle(event) {
    event.preventDefault();
    let button = event.target
    let form = button.parentElement
    let url = form.getAttribute('action')
    try {
        let data = await makeRequest(url);
        if (button.innerText == 'Unlike'){
            button.innerText = 'Like'
            button.classList.remove('btn-danger')
            button.classList.add('btn-primary')
        }
        else if (button.innerText == 'Like') {
            button.innerText = 'Unlike'
            button.classList.remove('btn-primary')
            button.classList.add('btn-danger')
        }
        let total_likes = form.getElementsByClassName('like_article_total')
        total_likes[0].innerText = data
    }
    catch (error) {
        onError(error);
    }
}

async function onClickComment(event){
    event.preventDefault();
    let button = event.target
    let form = button.parentElement
    let url = form.getAttribute('action')
    try {
        let data = await makeRequest(url);
        if (button.innerText == 'Unlike'){
            button.innerText = 'Like'
            button.classList.remove('btn-danger')
            button.classList.add('btn-primary')
        }
        else if (button.innerText == 'Like') {
            button.innerText = 'Unlike'
            button.classList.remove('btn-primary')
            button.classList.add('btn-danger')
        }
        let total_likes = form.getElementsByClassName('like_comment_total')
        total_likes[0].innerText = data
    }
    catch (error) {
        onError(error);
    }
}