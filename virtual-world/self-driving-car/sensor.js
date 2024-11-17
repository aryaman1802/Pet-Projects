class Sensor{
    constructor(car){
        this.car = car;
        this.rayCount = 2;    // number of rays
        this.rayLength = 150; // the distance within which the sensor can detect objects
        this.raySpread = Math.PI/2;  // angle of spread of the rays 
        this.rays = [];
    }

    update(){
        this.#castRays();
    }

    #castRays(){
        // the rays array stores each individual ray after we create them
        this.rays = [];
        // check this video for understanding the code behind how rays are spread out
        // https://youtu.be/Rs_rAxEsAvI?si=bsBxvDkvqYigWphH&t=3216
        // timestamp = 53:26
        for(let i=0; i<this.rayCount; i++){
            const rayAngle = lerp(
                this.raySpread/2,
                -this.raySpread/2,
                this.rayCount == 1 ? 0.5 : i/(this.rayCount-1)
            ) + this.car.angle;

            const start = {
                x: this.car.x, 
                y: this.car.y
            };
            
            const end = {
                x: this.car.x - Math.sin(rayAngle)*this.rayLength,
                y: this.car.y - Math.cos(rayAngle)*this.rayLength
            };
            this.rays.push([start, end]);
        }
    }

    draw(ctx){
        for(let i=0; i<this.rayCount; i++){
            ctx.beginPath();
            ctx.lineWidth = 2;
            ctx.strokeStyle = "yellow";
            ctx.moveTo(  // move to the x and y start locations of the rays
                this.rays[i][0].x,
                this.rays[i][0].y
            )
            ctx.lineTo(  // draw a line from x and y start to the end locations of the rays 
                this.rays[i][1].x,
                this.rays[i][1].y
            )
            ctx.stroke();
        }
    }
}