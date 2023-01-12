const { error } = require('console');
const { json } = require('express');
const express = require('express');
const jwt = require('jsonwebtoken')
const fs = require('fs');
const path = require('path');


const app = express();
app.use(express.json());
app.use('/static', express.static(__dirname + "/public"));

const api_url = "http://127.0.0.1:8080/api/v1/models"

app.set('view engine', 'ejs');
app.set('views', 'templates');

const port = process.env.PORT || 3000;


let string = {
    password: "admin",
    provider: "db",
    refresh: true,
    username: "admin"
}


async function getToken(){
    const response = await fetch('http://127.0.0.1:8080/api/v1/security/login', {
        method: "POST",
        mode: "cors",
        body: JSON.stringify( string ),
        headers: { 
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json' 
        }
    });
    const d = await response.json()
    const { access_token } = d;
    return access_token;
}

async function getApi(url, token){
    try{console.log('\nfetching from: '+ api_url + '\n');
    const response = await fetch(url, {
        method: "GET",
        mode: "cors",
        headers: {
            'Access-Control-Allow-Origin': '*',
            'Authorization':'Bearer '+token,
            'Content-Type':'aplicaton/json'
        }
    })
    const data = await response.json();
    return data;
    }catch(err){
        console.log(err);
        res.sendStatus(500);
        return;
    }
}

/* getApi(api_url).then((val) => {
    return val.result
}).then((objectData) => {
    let dataA = "";
    objectData.map((values) => {
        dataA=`<a href="${values.model_category.name}"><model-viewer  src="${values.file}"  shadow-intensity="1" camera-controls touch-action="pan-y"></model-viewer></a>`
        return dataA;
    })
}) */


/* for (let res of [apiData]){
    for(let desc of res.result){
        console.log(desc.description);
    }
}; */

getToken().then(token => getApi(api_url, token)).then((apiData) => {
    console.log(apiData);
});

app.listen(port, () => {
    console.log('Listening on http://127.0.0.1:' + port);
}),


app.get('/', (req, res) => {
    res.render('index');
}),

app.get('/api/data', (req, res) => {
    res.send(apiData);
});

app.get('/admin', (req, res) => {
    res.redirect('http://127.0.0.1:8080/');
}),

app.use((req, res) => {
    res.status(404).render('404');
})

