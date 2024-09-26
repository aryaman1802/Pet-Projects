class Controls{
    constructor(){
        this.forward = false;
        this.reverse = false;
        this.left = false;
        this.right = false;
        
        // # indicates that addKeyboardListeners is a private method
        this.#addKeyboardListeners();
    }

    #addKeyboardListeners(){
        
        // if we use the arrow function =>, then 'this' refers to the that of the
        // Controls class
        // however, if we use the function keyword, then 'this' refers to the
        // to that of the function
        document.onkeydown = (event) => {
            switch(event.key){
                case "ArrowLeft":
                    this.left = true;
                    break;
                case "ArrowRight":
                    this.right = true;
                    break;
                case "ArrowUp":
                    this.forward = true;
                    break;
                case "ArrowDown":
                    this.reverse = true;
                    break;
            }
            // uncomment the below line for debugging
            // console.table(this);
        }
        document.onkeyup = (event) => {
            switch(event.key){
                case "ArrowLeft":
                    this.left = false;
                    break;
                case "ArrowRight":
                    this.right = false;
                    break;
                case "ArrowUp":
                    this.forward = false;
                    break;
                case "ArrowDown":
                    this.reverse = false;
                    break;
            }
            // uncomment the below line for debugging
            // console.table(this);
        }

    }

}