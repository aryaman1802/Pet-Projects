const canvas = document.getElementById("myCanvas");
canvas.width = 200;

const ctx = canvas.getContext("2d");
const road = new Road(canvas.width/2, canvas.width*0.9);
const car = new Car(road.getLaneCenter(1), 100, 30, 50);

animate();

function animate(){
    car.update();

    canvas.height = window.innerHeight;

    ctx.save();
    ctx.translate(0, -car.y + canvas.height*0.5);

    road.draw(ctx);
    car.draw(ctx);

    ctx.restore();
    // requestAnimationFrame repeatedly calls the animate function
    // this gives the illusion of movement, ie, as if the car is moving
    requestAnimationFrame(animate);
    // the reason we put canvas.height here is because everytime 
    // requestAnimationFrame is called, the canvas is redrawn, and
    // the canvas now shows the car at a new position with the old one 
    // removed
}