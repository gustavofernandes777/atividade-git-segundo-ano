let itens = {};
let tvendas = {};
let contas = {};
let tganho = 0;
let tcontas = 0;

let senha_mestre = "147";
let senha_chefe = "";
let senha_cont = "";
let senha_func = "";
let senha_rep = "";

function login() {
    let role = document.getElementById("role").value;
    let password = document.getElementById("password").value;
    let msg = document.getElementById("login-msg");

    msg.textContent = "";

    if (role == "0") {
        msg.textContent = "Selecione um acesso!";
        return;
    }

    // CADASTRO DE SENHAS
    if (role == "1") {
        if (password === senha_mestre) {
            let newRole = prompt("Escolha usuário para criar senha: (2-Repositor, 3-Funcionário, 4-Contador, 5-Chefe)");
            let newPassword = prompt("Digite a nova senha:");
            if (newRole == "2") senha_rep = newPassword;
            else if (newRole == "3") senha_func = newPassword;
            else if (newRole == "4") senha_cont = newPassword;
            else if (newRole == "5") senha_chefe = newPassword;
            else alert("Opção inválida!");
            alert("Senha criada com sucesso!");
        } else {
            msg.textContent = "Acesso negado";
        }
        return;
    }

    // VERIFICAÇÃO DE SENHA
    if ((role == "2" && password === senha_rep) ||
        (role == "3" && password === senha_func) ||
        (role == "4" && password === senha_cont) ||
        (role == "5" && password === senha_chefe)) {
        showMenu(role);
    } else {
        msg.textContent = "Acesso negado";
    }
}

function showMenu(role) {
    document.getElementById("login-section").style.display = "none";
    let menu = document.getElementById("menu-section");
    menu.style.display = "block";
    menu.innerHTML = "";

    if (role == "2") {
        // Menu Repositor
        menu.innerHTML = `<h2>Menu Repositor</h2>
        <button onclick="addItem()">Adicionar item</button>
        <button onclick="alterQuantity()">Alterar quantidade</button>
        <button onclick="back()">Sair</button>
        <div id="estoque"></div>`;
        showEstoque();
    }
    else if (role == "3") {
        // Menu Funcionário
        menu.innerHTML = `<h2>Menu Funcionário</h2>
        <button onclick="registrarVenda()">Registrar venda</button>
        <button onclick="back()">Sair</button>
        <div id="estoque"></div>`;
        showEstoque();
    }
    else if (role == "4") {
        // Menu Contador
        menu.innerHTML = `<h2>Menu Contador</h2>
        <button onclick="verVendas()">Ver vendas</button>
        <button onclick="addConta()">Adicionar contas</button>
        <button onclick="verContas()">Ver contas</button>
        <button onclick="verLucro()">Ver lucro</button>
        <button onclick="back()">Sair</button>
        <div id="info"></div>`;
    }
    else if (role == "5") {
        // Menu Chefe
        menu.innerHTML = `<h2>Menu Chefe</h2>
        <button onclick="verEstoque()">Ver estoque completo</button>
        <button onclick="verVendas()">Ver relatório de vendas</button>
        <button onclick="verContas()">Ver contas</button>
        <button onclick="verLucro()">Ver lucro geral</button>
        <button onclick="back()">Sair</button>
        <div id="info"></div>`;
    }
}

// Funções de Repositor
function addItem() {
    let nomep = prompt("Produto:");
    let quantp = parseInt(prompt("Quantidade:"));
    let valorp = parseFloat(prompt("Preço:"));
    itens[nomep] = { quantidade: quantp, valor: valorp };
    showEstoque();
}

function alterQuantity() {
    let nomep = prompt("Qual item deseja alterar?");
    if (itens[nomep]) {
        let novaquant = parseInt(prompt("Nova quantidade:"));
        itens[nomep].quantidade = novaquant;
        showEstoque();
    } else {
        alert("Item não encontrado");
    }
}

function showEstoque() {
    let div = document.getElementById("estoque");
    let html = "<h3>Estoque:</h3><table><tr><th>Produto</th><th>Quantidade</th><th>Preço</th></tr>";
    for (let nome in itens) {
        html += `<tr><td>${nome}</td><td>${itens[nome].quantidade}</td><td>R$${itens[nome].valor}</td></tr>`;
    }
    html += "</table>";
    div.innerHTML = html;
}

// Outras funções (Funcionário, Contador, Chefe)
function registrarVenda() {
    let nomep = prompt("Produto vendido:");
    if (itens[nomep]) {
        let quantr = parseInt(prompt("Quantidade vendida:"));
        if (itens[nomep].quantidade >= quantr) {
            itens[nomep].quantidade -= quantr;
            let venda = itens[nomep].valor * quantr;
            tganho += venda;
            if (!tvendas[nomep]) tvendas[nomep] = { vendidos: 0, total: 0 };
            tvendas[nomep].vendidos += quantr;
            tvendas[nomep].total += venda;
            alert(`Venda realizada! Valor: R$${venda}`);
        } else alert("Estoque insuficiente!");
    } else alert("Produto não existe");
    showEstoque();
}

function verVendas() {
    let div = document.getElementById("info");
    let html = "<h3>Relatório de Vendas:</h3><table><tr><th>Produto</th><th>Vendidos</th><th>Total R$</th></tr>";
    for (let nome in tvendas) {
        html += `<tr><td>${nome}</td><td>${tvendas[nome].vendidos}</td><td>${tvendas[nome].total}</td></tr>`;
    }
    html += "</table>";
    div.innerHTML = html;
}

function addConta() {
    let tipo = prompt("Tipo da conta:");
    let valor = parseFloat(prompt("Valor:"));
    contas[tipo] = valor;
    tcontas += valor;
}

function verContas() {
    let div = document.getElementById("info");
    let html = "<h3>Contas:</h3><table><tr><th>Tipo</th><th>Valor R$</th></tr>";
    for (let tipo in contas) {
        html += `<tr><td>${tipo}</td><td>${contas[tipo]}</td></tr>`;
    }
    html += `</table><p>Total de contas: R$${tcontas}</p>`;
    div.innerHTML = html;
}

function verLucro() {
    let lucro = tganho - tcontas;
    let div = document.getElementById("info");
    div.innerHTML = `<h3>Lucro atual: R$${lucro}</h3>`;
}

// Menu Chefe
function verEstoque() {
    let div = document.getElementById("info");
    let html = "<h3>Estoque Completo:</h3><table><tr><th>Produto</th><th>Quantidade</th><th>Preço R$</th></tr>";
    for (let nome in itens) {
        html += `<tr><td>${nome}</td><td>${itens[nome].quantidade}</td><td>${itens[nome].valor}</td></tr>`;
    }
    html += "</table>";
    div.innerHTML = html;
}

// Botão voltar
function back() {
    document.getElementById("menu-section").style.display = "none";
    document.getElementById("login-section").style.display = "block";
    document.getElementById("password").value = "";
    document.getElementById("login-msg").textContent = "";
    document.getElementById("role").value = "0";
    document.getElementById("menu-section").innerHTML = "";
}