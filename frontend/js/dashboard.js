const token = localStorage.getItem("token");

document.getElementById("nombre").innerText =
    localStorage.getItem("nombre");

// 🔒 Si no hay token → login
if (!token) {
    window.location.href = "index.html";
}

// 🚪 Logout
function logout() {
    localStorage.clear();
    window.location.href = "index.html";
}

// 📊 PRODUCCIÓN
async function cargarProduccion() {

    const res = await fetch(`${API_URL}/reportes/`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const data = await res.json();

    renderTablaProduccion(data);
}

// 👤 USUARIOS
async function cargarUsuarios() {

    const res = await fetch(`${API_URL}/usuarios/`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const data = await res.json();

    renderTablaUsuarios(data);
}

// 🎨 TABLA PRODUCCIÓN
function renderTablaProduccion(data) {

    let html = `
        <h2>Producción</h2>
        <table>
            <tr>
                <th>Fecha</th>
                <th>Proceso</th>
                <th>Usuario</th>
                <th>Transformador</th>
            </tr>
    `;

    data.forEach(item => {
        html += `
            <tr>
                <td>${item.fecha || ""}</td>
                <td>${item.proceso || ""}</td>
                <td>${item.nombre || ""}</td>
                <td>${item.transformador_serial || ""}</td>
            </tr>
        `;
    });

    html += "</table>";

    document.getElementById("tabla-container").innerHTML = html;
}

// 🎨 TABLA USUARIOS
function renderTablaUsuarios(data) {

    let html = `
        <h2>Usuarios</h2>
        <table>
            <tr>
                <th>Nombre</th>
                <th>Usuario</th>
                <th>Rol</th>
            </tr>
    `;

    data.forEach(item => {
        html += `
            <tr>
                <td>${item.nombre}</td>
                <td>${item.usuario}</td>
                <td>${item.rol}</td>
            </tr>
        `;
    });

    html += "</table>";

    document.getElementById("tabla-container").innerHTML = html;
}