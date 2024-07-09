console.log("loaded script");

//pcq c une array
const loginForm = document.getElementsByClassName("login_form")[0];

// const pongScene = document.getElementById("pongScene")[0];

function pongPageScripts () {
    console.log("launchPongScript")

    // connect to game
    connectToGame();

}

const page_scripts = {
    // 'gameSession' : loadGameSession,
    'menuPong/' : loadMenuPong,
    '/pong/' : pongPageScripts,
}

function loadContent(url, pushState = true) {
    console.log(url)
    if (url == '/')
        url = ""

    // if there is a trailing session id, remove it
    if (url.includes('pong/')) 
        page_url = '/pong/'
    else 
        page_url = url

    fetch('/partials/' + url)
        .then(response => response.text())
        .then(data => {
            console.log("fetched url : ", url);
            
            // Update page content
            const mainDiv = document.getElementById('content');
            mainDiv.innerHTML = data;

            // Change URL in browser address bar
            if (pushState) {
                history.pushState({url: url}, '', url);
            }

            // Load scripts for the page
            if (page_scripts[page_url])
              page_scripts[page_url]();
            else
                console.log("pas trouve chef");
        })
        .catch(error => console.error('Error loading content:', error));
}

