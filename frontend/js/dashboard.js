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
                <th>Acciones</th>
            </tr>
    `;

    data.forEach(item => {
        html += `
            <tr>
                <td>${item.fecha || ""}</td>
                <td>${item.proceso || ""}</td>
                <td>${item.nombre || ""}</td>
                <td>${item.transformador_serial || ""}</td>
                <td>
                    <button class="button-eliminar" onclick="eliminar('${item._id}')">Eliminar</button>
                    <button class="button-editar" onclick="editar('${item._id}')">Editar</button>
                </td>
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

// 🎨 ELIMINAR PRODUCCION
async function eliminar(id) {
    if (!confirm("¿Desea eliminar el registro?")) return;

    const res = await fetch(`${API_URL}/produccion/${id}`, {
        method: "DELETE",
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const data = await res.json();

    alert(data.mensaje || data.error);

    cargarProduccion();
}

// 🎨 EDITAR PRODUCCION
async function editar(id) {

    console.log("EDITANDO ID:", id);

    document.getElementById("edit_id").value = id;

    const res = await fetch(`${API_URL}/procesos/`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const procesos = await res.json();

    console.log("PROCESOS:", procesos); // 🔥 DEBUG IMPORTANTE

    const select = document.getElementById("edit_proceso");

    if (!select) {
        console.error("No existe el select edit_proceso");
        return;
    }

    select.innerHTML = "";

    // 🔥 VALIDACIÓN CLAVE
    if (!Array.isArray(procesos)) {
        console.error("Procesos no es un array:", procesos);
        return;
    }

    procesos.forEach(p => {
        select.innerHTML += `<option value="${p.nombre}">${p.nombre}</option>`;
    });

    document.getElementById("modalEditar").style.display = "block";
}

function cerrarModal() {
    document.getElementById("modalEditar").style.display = "none";
}

async function guardarEdicion() {

    const id = document.getElementById("edit_id").value;
    const proceso = document.getElementById("edit_proceso").value;
    const fecha = document.getElementById("edit_fecha").value;

    const res = await fetch(`${API_URL}/produccion/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            proceso: proceso,
            fecha: fecha
        })
    });

    const data = await res.json();

    alert("Actualizado correctamente");

    cerrarModal();
    cargarProduccion(); // recargar tabla
}

//OBTENER LOS PROCESOS

async function obtenerProcesos() {

    const res = await fetch(`${API_URL}/procesos/`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    return await res.json();
}