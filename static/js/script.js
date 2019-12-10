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
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.setRequestHeader('X-CSRFToken', getFromCookie('csrftoken'));


    xhr.onreadystatechange = function(){
        if(this.readyState==4 && this.status==200){
            response = JSON.parse(this.responseText);
            fun(response);
            }
    };

    xhr.send(dic);//JSON.stringify(dic));
};

//To initialize the sidenav in mobile view
document.addEventListener("DOMContentLoaded", ()=>{
    let SideNav = document.getElementsByClassName("sidenav")[0];
    M.Sidenav.init(SideNav, {edge: 'right'});
});


//To insert products
//document.addEventListener("DOMContentLoaded", ()=>{
//
//});