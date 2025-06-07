document.getElementById("toggle-sidebar").addEventListener("click", function () {
    let sidebar = document.getElementById("sidebar");

    if (sidebar.classList.contains("sidebar-hidden")) {
        sidebar.classList.remove("sidebar-hidden"); // Remove a classe para mostrar a sidebar
    } else {
        // Adiciona a classe 'sidebar-hidden' para esconder a sidebar
        sidebar.classList.add("sidebar-hidden");
        
        // Para garantir a transição de volta, forçamos a re-aplicação de transform
        sidebar.offsetHeight; // Lê uma propriedade para forçar o reflow (necessário para reiniciar a animação)
    }
});

// Referenciar os elementos
const searchBar = document.getElementById("search-bar");
const listItems = document.querySelectorAll("nav#sidebar li");

// Adicionar evento de input na barra de pesquisa
searchBar.addEventListener("input", () => {
    const query = searchBar.value.toLowerCase();

    // Filtrar os itens da lista
    listItems.forEach((item) => {
        const text = item.textContent.toLowerCase();
        if (text.includes(query)) {
            item.style.display = ""; // Mostrar o item
        } else {
            item.style.display = "none"; // Esconder o item
        }
    });
});