async function login(){
    
    const usuario = document.getElementById("usuario").value
    const password = document.getElementById("password").value

    if (!usuario || !password) {
    document.getElementById("error").innerText = "Campos obligatorios";
    return;
}

    try{
        const res = await fetch(`${API_URL}/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({usuario:Number(usuario), password: password})
        });

        const data = await res.json();

        console.log("RESPUESTA: ", data);

        if(data.token){
            localStorage.setItem("token", data.token)
            localStorage.setItem("name", data.name)
            localStorage.setItem("rol", data.rol)

            console.log("login exitoso");

            window.location.href = "dashboard.html";

        }else{
            document.getElementById("error").innerHTML = data.error;
        }

    }catch(error){
        console.error(error);
    }
}