window.onload = function () {

    const rol = localStorage.getItem("rol");
    const nombre = localStorage.getItem("name");

    document.getElementById("nombre").innerText = nombre;

    if (rol !== "admin") {

        ocultarElemento("btnUsuarios");
        ocultarElemento("btnTransformadores");

        cargarProduccion();

    } else {

        cargarProduccion();
    }
};

function ocultarElemento(id){
    const el = document.getElementById(id);
    if (el) el.style.display = "none";
}   

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
function renderTablaProduccion(data = null) {

    const rol = localStorage.getItem("rol");

    let html = `
        <h2>Producción</h2>

        <input type="number" id="buscar_serial" placeholder="Buscar por serial">
        <button class="button-buscar" onclick="buscarPorSerial()">Buscar</button>
    `;
    
    if (data && data.length > 0) {
        html += `
                <table>
            <tr>
                <th>Item</th>
                <th>Lote</th>
                <th>Serie</th>
                <th>Potencia</th>
                <th>Voltaje</th>
                <th>Marca</th>
                <th>Fase</th>
                <th>Proceso</th>
                <th>Fecha</th>
                <th>Nombre</th>
                <th>Acciones</th>
            </tr>     
        `;
    }
    
    if(data && data.length > 0) {
        data.forEach(item => {
            
        html += `
            <tr>
                <td>${item.numero || ""}</td>
                <td>${item.lote || ""}</td>
                <td>${item.serial || ""}</td>
                <td>${item.potencia || ""}</td>
                <td>${item.voltaje || ""}</td>
                <td>${item.marca || ""}</td>
                <td>${item.fase || ""}</td>
                <td>${item.proceso || ""}</td>
                <td>${item.fecha || ""}</td>
                <td>${item.nombre || ""}</td>
                <td>
                   ${rol === "admin" ? `<button class="button-eliminar" onclick="eliminar('${item._id}')">Eliminar</button>` : ""}
                    <button class="button-editar" onclick="editar('${item._id}')">Editar</button>
                </td>
            </tr>
        `;
    });
    }

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
                <td>${item.nombre || ""}</td>
                <td>${item.usuario || ""}</td>
                <td>${item.rol || ""}</td>
                <td>
                    <button class="button-eliminar" onclick="eliminarUsuario('${item.usuario}')">Eliminar</button>
                    <button class="button-editar" onclick="editarUsuario(
                    '${item.usuario}',
                    '${item.nombre}',
                    '${item.rol}'
                    )">Editar</button>
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

    document.getElementById("modalEditarProduccion").style.display = "block";
}

function cerrarModal() {
    document.getElementById("modalEditarProduccion").style.display = "none";
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
    const usuarioInput = document.getElementById("user_usuario").value;
    const usuario = usuarioInput ? Number(usuarioInput) : null;
    const password = document.getElementById("user_password").value;
    const rol = document.getElementById("user_rol").value;

    console.log(nombre, usuario, password, rol); // 🔥 DEBUG

    if (!nombre || !usuario || !password) {
        alert("Campos obligatorios");
        return;
    }

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

        console.log("RESPUESTA:", data); // 🔥 CLAVE

        alert("Usuario creado correctamente");

        cerrarModalUsuario();
        cargarUsuarios();

    } catch (error) {
        console.error("ERROR:", error);
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

function editarUsuario(usuario,nombre,rol) {

    document.getElementById("edit_user_id").value = usuario;
    document.getElementById("edit_user_nombre").value = nombre;
    document.getElementById("edit_usuario").value = usuario;
    document.getElementById("edit_user_role").value = rol;
    document.getElementById("edit_user_password").value = "";

    document.getElementById("modalEditarUsuario").style.display = "block";
}

function cerrarModalEditarUsuario() {
    document.getElementById("modalEditarUsuario").style.display = "none";
}

async function guardarEdicionUsuario() {

    const usuario = document.getElementById("edit_user_id").value;
    const nombre = document.getElementById("edit_user_nombre").value;
    const nuevo_usuario = document.getElementById("edit_usuario").value;
    const password = document.getElementById("edit_user_password").value;
    const rol = document.getElementById("edit_user_role").value;

    const body = {
        nombre,
        rol,
        usuario: Number(nuevo_usuario)
    };

    // 🔥 solo si escribe contraseña
    if (password) {
        body.password = password;
    }

    await fetch(`${API_URL}/usuarios/${usuario}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify(body)
    });

    alert("Usuario actualizado");

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
                    <button class="button-editar" onclick="editarTransformador(
                    '${item._id}',
                    '${item.item}',
                    '${item.lote}',
                    '${item.serial}',
                    '${item.potencia}',
                    '${item.voltaje}',
                    '${item.marca}',
                    '${item.fase}',
                    '${item.cliente}',
                    '${item.servicio}'
                    )">Editar</button>
                    <button class="button-eliminar" onclick="eliminarTransformador('${item._id}')">Eliminar</button>
                </td>
            </tr>
        `;
    });

    html += "</table>";

    document.getElementById("tabla-container").innerHTML = html;
}

/* MODAL CREAR TRANSFORMADOR */

function abrirModalTransformador() {
    document.getElementById("modalTransformador").style.display = "block";
}

function cerrarModalTransformador() {
    document.getElementById("modalTransformador").style.display = "none";
}

async function guardarTransformador() {
    const item = document.getElementById("item").value;
    const lote = document.getElementById("lote").value;
    const serial = document.getElementById("serial").value;
    const potencia = document.getElementById("potencia").value;
    const voltaje = document.getElementById("voltaje").value;
    const marca = document.getElementById("marca").value;
    const fase = document.getElementById("fase").value;
    const cliente = document.getElementById("cliente").value;
    const servicio = document.getElementById("servicio").value;

    if (!item || !serial){
        alert("Item y Serial son obligatorios");
        return;
    }
    
    await fetch(`${API_URL}/transformadores/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            item,
            lote,
            serial,
            potencia,
            voltaje,
            marca,
            fase,
            cliente,
            servicio
        })
    });

    alert("Transformador creado correctamente");
    cerrarModalTransformador();
    cargarTransformadores();
}

/* MODAL EDITAR TRANSFORMADOR */

function editarTransformador(id, item, lote, serial, potencia, voltaje, marca, fase, cliente, servicio) {

    console.log("ID Recibido:", id);

    document.getElementById("edit_transformador_id").value = id;
    document.getElementById("edit_item").value = item;
    document.getElementById("edit_lote").value = lote;
    document.getElementById("edit_serial").value = serial;
    document.getElementById("edit_potencia").value = potencia;
    document.getElementById("edit_voltaje").value = voltaje;
    document.getElementById("edit_marca").value = marca;
    document.getElementById("edit_fase").value = fase;
    document.getElementById("edit_cliente").value = cliente;
    document.getElementById("edit_servicio").value = servicio;

    document.getElementById("modalEditarTransformador").style.display = "block";
}

function cerrarModalEditarTransformador() {
    document.getElementById("modalEditarTransformador").style.display = "none";
}

async function guardarEdicionTransformador() {

    const id = document.getElementById("edit_transformador_id").value;

    const item = document.getElementById("edit_item").value;
    const lote = document.getElementById("edit_lote").value;
    const serial = document.getElementById("edit_serial").value;
    const potencia = document.getElementById("edit_potencia").value;
    const voltaje = document.getElementById("edit_voltaje").value;
    const marca = document.getElementById("edit_marca").value;
    const fase = document.getElementById("edit_fase").value;
    const cliente = document.getElementById("edit_cliente").value;
    const servicio = document.getElementById("edit_servicio").value;

    await fetch(`${API_URL}/transformadores/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            item,
            lote,
            serial,
            potencia,
            voltaje,
            marca,
            fase,
            cliente,
            servicio
        })
    });

    alert("Transformador editado correctamente");

    cerrarModalEditarTransformador();
    cargarTransformadores();
}

/* ELIMINAR TRANSFORMADOR */

async function eliminarTransformador(id) {
    if (!confirm("¿Desea eliminar el transformador?")){
         return;
    }

    try {
        await fetch(`${API_URL}/transformadores/${id}`, {
            method: "DELETE",
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        alert("Transformador eliminado correctamente");

        cargarTransformadores();

    } catch (error) {
        console.error(error);
        alert("Error al eliminar el transformador");
    }
}

/*BUSCAR POR SERIAL*/

async function buscarPorSerial() {
    const serial = document.getElementById("buscar_serial").value;
    const token = localStorage.getItem("token");

    try {
        // 🔹 traer transformador
        const resTransformador = await fetch(`http://localhost:8000/transformadores/buscar/${serial}`, {
            headers: { "Authorization": `Bearer ${token}` }
        });

        const transformador = await resTransformador.json();

        console.log("TRANSFORMADOR:", transformador);

        // 🔹 crear objeto combinado
        const combinado = {
            ...transformador,
            proceso: "",
            fecha: "",
            nombre: ""
        };

        renderTablaProduccion([combinado]);

    } catch (error) {
        console.error("Error:", error);
    }
}
