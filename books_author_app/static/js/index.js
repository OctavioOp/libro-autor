// js code
$(document).ready(function(){
    console.log('funciona')


    $('.foto').hover(function(){
        $(this).addClass('blur')
    },function(){
        $(this).removeClass('blur')
    })
})