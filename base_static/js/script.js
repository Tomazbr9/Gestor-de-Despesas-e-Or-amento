/* Logica que faz com que a janela de opçoes de inserir valores apareça ou 
desapareça de acordo com o click do usuario*/
document.querySelector('#input-add').addEventListener('click', function(event){

    event.preventDefault()

    var window = document.getElementById('container-options-id')
    window.style.display = window.style.display === 'flex' ? 'none' : 'flex'
})


window.addEventListener('click', function(evt){
    var add = document.querySelector('#input-add')
    var window_options = document.querySelector('#container-options-id')
    var category_options = document.querySelector('.select-items')
    var display_category_options = document.querySelector('.bi-caret-down')
    var input_revenues_expenses = document.querySelector('#input-revenues-expenses-id')

    if (window_options.style.display === 'flex' 
        && !add.contains(evt.target)
        && !window_options.contains(evt.target)){
            window_options.style.display = 'none'
        }
    if (category_options.style.display === 'flex' 
        && !display_category_options.contains(evt.target)
        && !display_category_options.contains(evt.target)
        && !input_revenues_expenses.contains(evt.target)){
            category_options.style.display = 'none'
        }
})

/* Função que formata o valor do input do modal*/
function format_currency(input){
    let value = input.value.replace(/\D/g, "")
    value = (value / 100).toFixed(2)
    value.replace('.', ',')
    input.value = 'R$ ' + value
}

/* Padroniza o valor do input de valor*/
document.getElementById("value-input").value = "R$ 0,00"

function display_category_options(){
    fetch('/category/').then(response => response.json()).then(data => {

        const select_items = document.querySelector('.select-items')
        select_items.style.display = select_items.style.display === 'flex' ? 'none' : 'flex'
        const input_revenues_expenses = document.querySelector('#input-revenues-expenses-id')
        const get_id_category = document.querySelector('#get-id-category')

        select_items.innerHTML = ''

        data.forEach(category => {
            var item = document.createElement('div')
            item.classList.add('category-options')
            item.setAttribute('data-value', category.id)
            item.innerHTML = `
            <i class="${category.icone} icon-category"></i>
            <span>${category.name}</span>
            `
            select_items.appendChild(item)

            item.addEventListener('click', function(){
                input_revenues_expenses.value = category.name
                get_id_category.value = category.id
            })
        })
    })
}

const icon_arrow = document.querySelector(".bi-caret-down").addEventListener('click', display_category_options)

