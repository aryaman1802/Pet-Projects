class Car{
    constructor(x, y, width, height){
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;

        this.speed = 0;
        this.acceleration = 0.2;
        this.maxSpeed = 5;
        this.friction = 0.05;
        this.angle = 0;

        this.sensor = new Sensor(this);
        this.controls = new Controls();
    }

    update(){
        this.#move();
        this.sensor.update();
    }

    #move(){
        // increase the speed of the car if the forward key is pressed
        // decrease the speed of the car if the reverse key is pressed
        // negative speed means that the car is moving backwards
        if(this.controls.forward){
            this.speed += this.acceleration;
        }
        if(this.controls.reverse){
            this.speed -= this.acceleration;
        }

        // do not allow the car to turn if it is stationary
        if(this.speed != 0){
            // when going backwards, the controls for left and right are reversed
            // like it happens in real life
            const flip = this.speed > 0 ? 1: -1;
            // check this video for understanding the coordinate system
            // https://youtu.be/Rs_rAxEsAvI?si=nLcuyqzkMMheZk_a&t=1570
            // timestamp is 26:10
            if(this.controls.left){
                this.angle += 0.03*flip;
            }
            if(this.controls.right){
                this.angle -= 0.03*flip;
            }
        }
        
        // check that the car does not exceed the maximum speed
        if(this.speed > this.maxSpeed){
            this.speed = this.maxSpeed;
        }
        if(this.speed < -this.maxSpeed){
            // if the car is moving backwards, then the maximum speed is halved
            this.speed = -this.maxSpeed/2;
        }

        // apply friction to the car
        if(this.speed > 0){
            this.speed -= this.friction;
        }
        if(this.speed < 0){
            this.speed += this.friction;
        }

        // if the absolute value of speed is less than the friction, then set the speed to 0
        // otherwise the car will always keep moving forward, albeit very slowly
        if(Math.abs(this.speed) < this.friction){
            this.speed = 0;
        }

        // check this video for understanding why we use the below formula
        // https://youtu.be/Rs_rAxEsAvI?si=5Jja5VPMTnNQkx3T&t=1731
        // time stamp is 28:51
        this.x -= Math.sin(this.angle)*this.speed;
        // remember that the y-axis is inverted, ie, y increases as we go down
        this.y -= Math.cos(this.angle)*this.speed;
    }

    draw(ctx){
        // check this video for understanding why we use negative angle
        // https://youtu.be/Rs_rAxEsAvI?si=GswpnaWGuzOkkLbP&t=1625
        // timestamp is 27:06
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(-this.angle);   // check the above video

        ctx.beginPath();
        ctx.rect(
            -this.width/2,
            -this.height/2,
            this.width,
            this.height
        );
        ctx.fill();

        // without restore, the canvas will apply translation and 
        // keep rotating infinitely
        ctx.restore();

        this.sensor.draw(ctx);
    }
}