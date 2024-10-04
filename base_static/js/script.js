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
    var display_category_options_up = document.querySelector('.bi-caret-up')
    var input_revenues_expenses = document.querySelector('#input-revenues-expenses-id')

    if (window_options.style.display === 'flex' 
        && !add.contains(evt.target)
        && !window_options.contains(evt.target)){
            window_options.style.display = 'none'
        }
    if (category_options.style.display === 'flex' 
        && !display_category_options_up.contains(evt.target)
        && !input_revenues_expenses.contains(evt.target)){
            category_options.style.display = 'none'
            const icon_arrow = document.querySelector(".bi-caret-up")
            icon_arrow.classList.remove('bi-caret-up')
            icon_arrow.classList.add('bi-caret-down')
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

    const icon_arrow = document.querySelector(".bi-caret-down")
    icon_arrow.classList.remove('bi-caret-down')
    icon_arrow.classList.add('bi-caret-up')

    const title_modal = document.querySelector('#title-modal-id').innerText
    const address_json = title_modal === 'Despesas' ? '/expense_category/' : '/income_category/' 

    fetch(address_json).then(response => response.json()).then(data => {

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

// Da Close no modal
function close_modal(){
    document.querySelector('.wrapping').style.display = 'none'
    document.querySelector('#msg_error').innerText = ""
    document.body.classList.remove('modal-open')
    const modal = document.querySelector('.container-modal')
    modal.style.display = 'none'
    document.querySelector('.form-revenues-expenses').reset()
    document.getElementById("value-input").value = "R$ 0,00"
    document.querySelector('.btn-modal').style.pointerEvents = 'none'
    document.querySelector('.btn-modal').style.background = '#aa9b9b'
}

document.querySelector('.bi-x-lg').addEventListener('click', close_modal)

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

// Apresentar Mensagem de erro antes de enviar formulario
$(document).ready(function() {
    $('.form-revenues-expenses').on('submit', function(event) {
        event.preventDefault(); // Impede o envio padrão do formulário

        var form = $(this)[0]
        var formdata = new FormData(form)

        if (formdata.get('id') !== '') {
            // Se a condição for atendida, envia o formulário via AJAX
            $.ajax({
                type: 'POST',
                url: addTransactionUrl, 
                data: formdata,
                processData: false,
                contentType: false,
                success: function(response){
                    close_modal(),
                    $('#get-id-category').val('') 
                }      
            })
        } else {
            document.querySelector('#msg_error').innerText = "Por Favor, Selecione uma Categoria"
        }
    })
})

/* Faz a Soma das Despesas e Receitas para obter o valor do saldo total */
function total_balance(url, element_id){
    fetch(url).then(response => response.json()).then(data => {
        total = 0
        for (i of data){
            if (i['total_amount'] == null){
                continue
            }
            total += parseFloat(i['total_amount'])
        }
        console.log(total.toFixed(2))
        document.querySelector(element_id).innerText = `R$ ${total.toFixed(2)}`.replace('.', ',').replace('-', '')
    })
}

document.addEventListener('DOMContentLoaded', function(){
    total_balance('/total_balance/', '#balance-total')
    total_balance('/total_income/', '#income-total')
    total_balance('/total_expense/', '#expense-total')
})
