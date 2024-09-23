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

// Obtem as Cateogrias em Json e adiciona uma açao no campo de Categorias
function display_category_options(){

    // const icon_arrow = document.querySelector(".bi-caret-down")
    // icon_arrow.classList.remove('bi-caret-down')
    // icon_arrow.classList.add('bi-caret-up')


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


// Exibe o modal de acordo com a opcão escolhida
function add_expenses_or_revenues(evt){
    const modal = document.querySelector('.container-modal')
    modal.style.display = 'flex'
    const evt_action = evt.target  
    const title_modal = document.querySelector('#title-modal-id')

    document.body.classList.add('modal-open')
    document.querySelector('.wrapping').style.display = 'block'

    if (evt_action.classList.contains('option-expenses')){
        title_modal.textContent = 'Despesas'
        title_modal.style.color = '#ff6347'
        document.getElementById("value-input").style.color = '#ff6347'

    }
    else if (evt_action.classList.contains('option-revenues')){
        title_modal.textContent = 'Receitas'
        title_modal.style.color = '#008000'
        document.getElementById("value-input").style.color = '#008000'
    }   
}

const add_expenses = document.querySelector('#option-expenses-id').addEventListener('click', add_expenses_or_revenues)
const add_revenues = document.querySelector('#option-revenues-id').addEventListener('click', add_expenses_or_revenues)

// Adiciona um event de click no icone 'x' para fechar o modal
document.querySelector('.bi-x-lg').addEventListener('click', function(){
    document.querySelector('.wrapping').style.display = 'none'
    document.body.classList.remove('modal-open')
    const modal = document.querySelector('.container-modal')
    modal.style.display = 'none'

})

// O botão do modal muda de estilo ao digitar no input de valor
const value_input = document.getElementById("value-input").addEventListener('input', function(){
    const title_modal = document.querySelector('#title-modal-id')
    const color_title = window.getComputedStyle(title_modal)
    const btn_modal = document.querySelector('.btn-modal')
    if (this.value){
        const color = color_title.color
        btn_modal.style.background = color
        btn_modal.style.pointerEvents = 'auto'
    }

    if (this.value == 'R$ 0.00'){
        btn_modal.style.background = '#aa9b9b'
        btn_modal.style.pointerEvents = 'none'  
    }
    
})  
