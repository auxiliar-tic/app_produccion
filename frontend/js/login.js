async function login(){
    
    const usuario = document.getElementById("usuario").value
    const password = document.getElementById("password").value

    try{
        const res = await fetch(`${API_URL}/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({username:parseInt(usuario), password: password})
        });

        const data = await res.json();

        if(data.token){
            localStorage.setItem("token", data.token)
            localStorage.setItem("name", data.name)

            window.location.href = "dashboard.html";

        }else{
            document.getElementById("error").innerHTML = data.error;
        }

    }catch(error){
        console.error(error);
    }
}