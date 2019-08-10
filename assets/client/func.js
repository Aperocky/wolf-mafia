let SEAT_FLAG = false;
let ROLE_FLAG = "default";

// Locations within the single page app
let first_link = document.querySelector("button#first_menu");
let second_link = document.querySelector("button#second_menu");
let prompt_div = document.querySelector("div#prompt");

// Image location within the single page app
let default_image = document.querySelector("div#image_default");
let all_images = Array.from(document.querySelectorAll(".imageblock"));

// PromptDivToggler, used to show prompt instead of images
function prompt_toggler(bool){
    // Will auto hide true role
    console.log(bool);
    if (bool){
        for (let image of all_images){
            image.style.display = "none";
        }
        prompt_div.style.display = "block";
    } else {
        prompt_div.style.display = "none";
        default_image.style.display = "block";
    }
}

// cleans the prompt and return the form to build
function prompt_initiator(config){
    // Remove everything within prompt
    while (prompt_div.firstChild){prompt_div.removeChild(prompt_div.firstChild);}
    let form_element = document.createElement("form");
    form_element.id = "prompt_form";
    prompt_div.appendChild(form_element);
    return form_element;
}

// --------- IMAGE RECON BLOCK ----------- //

// Associate all images with on-click event
for (let image of all_images){
    image.addEventListener("click", toggle_role);
}

// Let you see your role
function toggle_role(){
    let display_status = default_image.style.display;
    let role_image = document.querySelector("div#image_" + ROLE_FLAG);
    if (display_status === "none"){
        role_image.style.display = "none";
        default_image.style.display = "block";
    } else {
        default_image.style.display = "none";
        role_image.style.display = "block";
    }
}

// --------- END IMAGE RECON BLOCK ----------- //

// --------- TAKE SEAT BLOCK ----------- //

function call_take_seat_ajax(number){
    let req = new XMLHttpRequest();
    req.addEventListener("load", e => {
        response = req.response;
        console.log("I AM HERE");
        let response_status = response["status"]
        let response_reason = response["reason"]
        if (response_status){
            let response_role = response["role"].toLowerCase();
            ROLE_FLAG = response_role;
            alert(`${response_reason}`);
            prompt_toggler(false);
        } else {
            alert(`您入座失败：${response_reason}`);
        }
    });
    console.log("AJAX REQUEST");
    req.open("get", `/seat?seat=${number}`);
    req.responseType = 'json';
    req.send();
}

function create_take_seat_prompt(){
    form_element = prompt_initiator();
    let question_div = document.createElement("div");
    question_div.className = "formgroup";
    let question_label = document.createElement("label");
    question_label.textContent = "您要坐哪？";
    let question_input = document.createElement("input");
    question_input.setAttribute("type", "number");
    question_input.id = "prompt_question_input";
    question_div.appendChild(question_label);
    question_div.appendChild(question_input);
    let submit_button = document.createElement("button");
    submit_button.className = "btn btn-primary";
    submit_button.id = "prompt_submit_button";
    submit_button.textContent = "爷要坐这儿";
    submit_button.style.marginTop = "25px";
    submit_button.addEventListener("click", e => {
        e.preventDefault();
        let question_input = document.querySelector("#prompt_question_input");
        let number = question_input.value;
        console.log(number);
        call_take_seat_ajax(number);
    });

    let return_button = document.createElement("button");
    return_button.className = "btn btn-primary";
    return_button.id = "prompt_return_button";
    return_button.textContent = "等会儿再坐";
    return_button.addEventListener("click", e => {
        e.preventDefault();
        prompt_toggler(false);
    });
    return_button.style.marginTop = "25px";
    form_element.appendChild(question_div);
    form_element.appendChild(submit_button);
    form_element.appendChild(return_button);
}

function take_seat_begin(){
    prompt_toggler(true);
    create_take_seat_prompt();
}

first_link.addEventListener("click", take_seat_begin);


