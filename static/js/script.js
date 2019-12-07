//To get the cookie
let getFromCookie = key=>{
    let result = false;
    let cookies = document.cookie;
    let split = cookies.split(';');
    split.forEach( cookie=>{
        let res = cookie.split('=');
        result = res[0]==key ? res[0]: result;
    });
    return result;
};

//The host address
let HOST = 'http://127.0.0.1:8000/'

//To send POST request
let sendPOST = (url, dic, fun)=>{
    let xhr = new XMLHttpRequest();
    let response = false;
    xhr.open("POST", url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.setRequestHeader('X-CSRFToken', getFromCookie('csrftoken'));


    xhr.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            response = JSON.parse(this.responseText);
            fun(response);
            }
    };

    xhr.send(JSON.stringify(dic));
};

//To initialize the sidenav in mobile view
document.addEventListener("DOMContentLoaded", ()=>{
    let SideNav = document.getElementsByClassName("sidenav")[0];
    M.Sidenav.init(SideNav, {edge: 'right'})

//    To insert Products

    let createCards=res=>{
        res['pdts'].forEach( pdt=>{
            console.log(HOST+pdt['imgURL']);
            let pdtList = document.getElementById('product-list');
            let imgURL = HOST+pdt['imgURL'];
            let title = pdt['pdt-title'];
            let content = pdt['pdt-content'];
            pdtList.innerHTML += `
                <div class="col s12 m4">
                    <div class="card card-css">
                        <div class="card-image">
                            <img src="${imgURL}" alt="${title}">
                            <a href="" class="btn-floating  halfway-fab waves-effect green"><i class="material-icons">shopping_cart</i></a>
                        </div>
                        <div class="card-content">
                            <p>${content}</p>
                        </div>
                    </div>
                </div>
            `;

        });
//            console.log(res['pdts'][0]['imgURL']);

    };
    let response = sendPOST(`${HOST}Ecom/pdts/`, {'pdts':'?'}, createCards);
//    console.log(response);


});


//To insert products
//document.addEventListener("DOMContentLoaded", ()=>{
//
//});