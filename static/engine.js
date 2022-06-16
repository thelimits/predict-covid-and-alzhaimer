const realfilebutton = document.getElementById("file")
const realfilebuttons = document.querySelector(".Alzhaimer_body #file")
const customebutton = document.querySelector("#button_file #txt")
const customebutton1 = document.querySelector(".Alzhaimer_body #button_file #txt")
const text = document.getElementById("value")
const text_alz = document.querySelector(".Alzhaimer_body #value")

customebutton.addEventListener('click' , ()=>{
    realfilebutton.click();
});

customebutton1.addEventListener('click' , ()=>{
    realfilebuttons.click();
});

realfilebutton.addEventListener('change', ()=>{
    if(realfilebutton.value){
        text.innerText = realfilebutton.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
    }
    else{
        text.innerText = "No File input";
    }
})

realfilebuttons.addEventListener('change', ()=>{
    if(realfilebuttons.value){
        text_alz.innerText = realfilebuttons.value.match(/[\/\\]([\w\d\s\.\-\(\)]+)$/)[1];
    }
    else{
        text_alz.innerText = "No File input";
    }
})

// -----------------------------------------------------------------------------------------------------
$(function(){
    $('.cvd').click((e)=>{   
        $('.Alzhaimer_body').css('display', 'none')
        $('.covid_body').css('display', '')
        $('.cvd').css('color', 'red')
        $('.alz').css('color', '')
    });

    $('.alz').click(()=>{
        $('.covid_body').css('display', 'none')
        $('.Alzhaimer_body').css('display', '')
        $('.alz').css('color', 'red')
        $('.cvd').css('color', '')
    });
});

