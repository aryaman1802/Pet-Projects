class Sensor{
    constructor(car){
        this.car = car;
        this.rayCount = 3;    // number of rays
        this.rayLength = 100; // the distance within which the sensor can detect objects
        this.raySpread = Math.PI/4;  // angle of spread of the rays 
        this.rays = [];
    }

    update(){
        this.rays = [];
        // check this video for understanding the code behind how rays are spread out
        // https://youtu.be/Rs_rAxEsAvI?si=bsBxvDkvqYigWphH&t=3216
        // timestamp = 53:26
        for(let i=0; i<this.rayCount; i++){
            const rayAngle = lerp(
                this.raySpread/2,
                -this.raySpread/2,
                i/(this.rayCount-1)
            );
        }
    }
}