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

    const rol = localStorage.getItem("rol");

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
                   ${rol === "admin" ? `<button class="button-eliminar" onclick="eliminar('${item._id}')">Eliminar</button>` : ""}
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

        <button class="button__crear" onclick="abrirModalUsuario()">Crear Nuevo Usuario ➕</button>

        <table>
            <tr>
                <th>Nombre</th>
                <th>Usuario</th>
                <th>Rol</th>
                <th>Acciones</th>
            </tr>
    `;

    data.forEach(item => {
        html += `
            <tr>
                <td>${item.nombre}</td>
                <td>${item.usuario}</td>
                <td>${item.rol}</td>
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


//CREAR USUARIOS
async function guardarUsuario() {

    const nombre = document.getElementById("user_nombre").value;
    const usuario = document.getElementById("user_usuario").value;
    const password = document.getElementById("user_password").value;
    const rol = document.getElementById("user_rol").value;

    try {
        const res = await fetch(`${API_URL}/usuarios/`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${token}`
            },
            body: JSON.stringify({
                nombre,
                usuario,
                password,
                rol
            })
        });

        const data = await res.json();

        alert("Usuario creado correctamente");

        cerrarModalUsuario();
        cargarUsuarios();

    } catch (error) {
        console.error(error);
        alert("Error al crear usuario");
    }
}


//MODAL USUARIOS

function abrirModalUsuario(){
    document.getElementById("modalUsuario").style.display = "block";
}

function cerrarModalUsuario(){
    document.getElementById("modalUsuario").style.display = "none";
}

//EDITAR Y ELIMINAR USUARIOS

function editarUsuario(usuario) {

    document.getElementById("edit_user_usuario").value = usuario;

    document.getElementById("modalEditarUsuario").style.display = "block";
}

function cerrarModalEditarUsuario() {
    document.getElementById("modalEditarUsuario").style.display = "none";
}

async function guardarEdicionUsuario() {

    const usuario = document.getElementById("edit_user_usuario").value;
    const password = document.getElementById("edit_user_password").value;
    const rol = document.getElementById("edit_user_rol").value;

    const res = await fetch(`${API_URL}/usuarios/${usuario}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            password,
            rol
        })
    });

    alert("Usuario Actualizado");

    cerrarModalEditarUsuario();
    cargarUsuarios();
}

async function eliminarUsuario(usuario) {
    if (!confirm("¿Desea eliminar el registro?")) return;

    await fetch(`${API_URL}/usuarios/${usuario}`, {
        method: "DELETE",
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    cargarUsuarios();
}   

// CARGAR TRANSFORMADORES

async function cargarTransformadores() {

    const res = await fetch(`${API_URL}/transformadores/`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const data = await res.json();

    renderTablaTransformadores(data);
}   

function renderTablaTransformadores(data) { 

    let html = `
    <h2>Transformadores</h2>

    <button class="button__crear" onclick="abrirModalTransformador()">Crear Nuevo Transformador ➕</button>

    <table>
        <thead>
            <tr>
                <th>item</th>
                <th>Lote</th>
                <th>Serial</th>
                <th>Potencia</th>
                <th>Voltaje</th>
                <th>Marca</th>
                <th>Fase</th>
                <th>Cliente</th>
                <th>Servicio</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
    `;

    data.forEach(item =>{
        html += `
            <tr>
                <td>${item.item}</td>
                <td>${item.lote}</td>
                <td>${item.serial}</td>
                <td>${item.potencia}</td>
                <td>${item.voltaje}</td>
                <td>${item.marca}</td>
                <td>${item.fase}</td>
                <td>${item.cliente}</td>
                <td>${item.servicio}</td>
                <td>
                    <button class="button-editar" onclick="editarTransformador('${item._id}')">Editar</button>
                    <button class="button-eliminar" onclick="eliminarTransformador('${item._id}')">Eliminar</button>
                </td>
            </tr>
        `;
    });

    html += "</table>";

    document.getElementById("tabla-container").innerHTML = html;
}