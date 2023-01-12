let string = {
    password: "admin",
    provider: "db",
    refresh: true,
    username: "admin"
};

const api_url = "http://127.0.0.1:8080/api/v1/models";

async function getToken(){
    const response = await fetch('http://127.0.0.1:8080/api/v1/security/login', {
        method: "POST",
        mode: "cors",
        body: JSON.stringify( string ),
        headers: { 
            'Access-Control-Allow-Origin': 'http://localhost:3000/',
            'Content-Type': 'application/json' 
        }
    });
    const d = await response.json()
    const { access_token } = d;
    return access_token;
}

async function getApi(){
    try{let token = await getToken();
    const response = await fetch('http://127.0.0.1:8080/api/v1/models', {
        method: "GET",
        mode: "cors",
        headers: {
            'Access-Control-Allow-Origin': 'http://localhost:3000/',
            'Authorization':'Bearer '+token,
            'Content-Type':'aplicaton/json'
        }
    });
    const data = await response.json();
    return data;}catch(err){
        console.error(err.message);
    }
}