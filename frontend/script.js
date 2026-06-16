// display the user message on the UI 

const chatbox = document.querySelector("#chatbox");

const inputMessage = document.querySelector("#inputMessage");

const button = document.querySelector("#btn");


async function SendMessage(){
  
  // ishmai joh trim use hua hai voh extra space htaane ke liye hai 

 const message = inputMessage.value.trim(); 
 
 if(message == ""){
   return;
 }

//  user-message 
//  phle create karenge  user div 
// phir ushmai user-message class ko add karenge 
// phir ush user message ko 

const userDiv = document.createElement("div");

userDiv.classList.add("user-message");

userDiv.textContent = message;
chatbox.appendChild(userDiv);

// fetching
const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "content-Type":"application/json"
      },

      body: JSON.stringify({
        message:message
      })
    });

const data = await response.json();
console.log(data);



// bot messsage 

const botDiv = document.createElement("div");
botDiv.classList.add("bot-message");
botDiv.textContent = data.response;




// bot img ke saath message 
const botWrapper = document.createElement("div");
botWrapper.classList.add("bot-wrapper");

const botImg = document.createElement("img");
botImg.setAttribute("src","logo.jpeg");
botImg.classList.add("logo");

// now bot message and  botImg ko botWrapper mai daal denge 
botWrapper.appendChild(botImg);
botWrapper.appendChild(botDiv);

chatbox.appendChild(botWrapper);
chatbox.scrollTop = chatbox.scrollHeight;

inputMessage.value = "";
}

// all eventlistner 

//  click wala event listner  ushka logic SendMessage  wale function mai 
button.addEventListener("click",SendMessage);

// enter wala event lgaa rhaa huu mai idhar 

inputMessage.addEventListener("keydown", (event)=>{
      if (event.key === "Enter"){
        SendMessage();   
      }
});





