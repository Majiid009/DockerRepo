'use strict'

const submitBtn = document.querySelector('button')

submitBtn.addEventListener('click', function(e){
    e.preventDefault()
    console.log(e.data)
})