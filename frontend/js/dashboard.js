document.getElementById("nombre").innerText = localStorage.getItem("nombre");

async function verProduccion() {
    
    const token = localStorage.getItem("token");

    const res = await fetch(`${API_URL}/reportes/`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const data = await res.json();

    document.getElementById("resultado").innerText = 
        JSON.stringify(data, null, 2);
}