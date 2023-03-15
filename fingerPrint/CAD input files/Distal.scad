
faceNumber = 560;
hole = 3;

// Base sshape

module indexDistalBone(){
union(){
    translate([diameter/6, 0, 0])
    cylinder(h = height/2, d = diameter, center=false, $fn=faceNumber);
    translate([-diameter/6, 0, 0])
    cylinder(h = height/2, d = diameter, center=false, $fn=faceNumber);
    translate([-diameter/6,-diameter/2,0])
    cube([diameter/3, diameter, height/2], center=false);}

// make tip

module halfSphere(){    
    rotate([0,0,90])
    translate([0, -diameter/6,height/2])
    rotate_extrude(angle=180, $fn=100)
    difference(){
        scale([1,1.5,1])
        circle(d=diameter, $fn=faceNumber);
        square([diameter,diameter]);
        translate([-diameter,-diameter,0])
        square([2*diameter,diameter]);
    }
}
halfSphere();
mirror([1, 0, 0]) halfSphere();
    
    
module quarterSphere(){    
    rotate([90,0,90])
    translate([0,height/2,-diameter/6])
    linear_extrude(diameter/3)
    difference(){
        scale([1,1.5,1])
        circle(d=diameter, $fn=faceNumber);
        square([15,15]);
        translate([-15,-15,0])
        square([30,15]);
    }}
quarterSphere();
mirror([0,1,0]) quarterSphere();
    

//Second half of geometry
    
rotate([180,0,0])
difference(){

// Base sshape

    union(){
    translate([diameter/6, 0, 0])
    cylinder(h = height/2, d = diameter, center=false, $fn=faceNumber);
    translate([-diameter/6, 0, 0])
    cylinder(h = height/2, d = diameter, center=false, $fn=faceNumber);
    translate([-diameter/6,-diameter/2,0])
    cube([diameter/3, diameter, height/2], center=false);}

// remove side material
    
    translate([diameter/3, -diameter, height/4])
    cube([diameter, 2*diameter, height/2], center=false);
    translate([-4/3*diameter, -diameter, height/4])
    cube([diameter, 2*diameter, height/2], center=false);
    
// make a hole through the base shape

    translate([0, diameter/8, 0])
    cylinder(h = 2*height, r = diameter/6,$fn=faceNumber, center=true);
    translate([0, -diameter/8, 0])
    cylinder(h = 2*height, r = diameter/6,$fn=faceNumber, center=true);
    cube([diameter/3, diameter/4, 2*height], center=true);
    
// make pin hole

    translate([0, 0, height/2-hole])
    rotate([0,90,0])
    cylinder(h=height, d = hole, center=true, $fn=faceNumber);
    
// fillet edges

    translate([0, 0, -diameter/3])
    difference(){        
            translate([-diameter, 0, height/2])
            cube([2*diameter, diameter, diameter], center=false);
            translate([0, 0, height/2])
            rotate([0, 90, 0])
            cylinder(h = 40, d = diameter/1.5, $fn=faceNumber, center=true);}
            translate([-diameter/2, diameter/3, height/4])
            cube([diameter, diameter, diameter]);
            translate([-diameter/6, 0, height/4])
            cube([diameter/3,diameter,diameter]);
        }}
        indexDistalBone();