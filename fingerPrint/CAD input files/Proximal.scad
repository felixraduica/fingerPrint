
faceNumber = 560;
hole = 3;


// Base sshape

module halfProximalBone(height, diameter, faceNumber, hole){
difference(){
difference(){
union(){
    translate([diameter/6, 0, 0])
    cylinder(h = height/2, d = diameter, center=false, $fn=faceNumber);
    translate([-diameter/6, 0, 0])
    cylinder(h = height/2, d = diameter, center=false, $fn=faceNumber);
    translate([-diameter/6,-diameter/2,0])
    cube([diameter/3, diameter, height/2], center=false);}

// remove middle material

    translate([0, 0, height/2])
    cube([diameter/1.5, diameter*2, height/2], center=true);

// remove side material

    translate([-diameter, diameter/3, height/4])
    cube([diameter*2, diameter, height/2], center=false);
    translate([-diameter, -diameter/3-diameter, height/4])
    cube([diameter*2, diameter, height/2], center=false);

// make a hole through the base shape

    translate([0, diameter/8, 0])
    cylinder(h = height, r = diameter/6,$fn=faceNumber, center=true);
    translate([0, -diameter/8, 0])
    cylinder(h = height, r = diameter/6,$fn=faceNumber, center=true);
    cube([diameter/3, diameter/4, height], center=true);

// make pin hole

    translate([0, 0, height/2-hole])
    rotate([0,90,0])
    cylinder(h=height, d = hole, center=true, $fn=faceNumber);
    
// fillet edges

    translate([0, 0, -diameter/3])
    difference(){
        union(){
            translate([0, 0, height/2])
            cube([diameter, diameter, diameter], center=false);
            translate([-diameter, 0, height/2])
            cube([diameter, diameter, diameter], center=false);}
            translate([0, 0, height/2])
            rotate([0, 90, 0])
            cylinder(h = 40, r = diameter/3, $fn=faceNumber, center=true);}
    }
}}
// generate proximalBone geometry
    
module indexProximalBone(){
union(){
    
// generate half of geometry

halfProximalBone(height, diameter,560, 3);
    
// generate other half
    
mirror([0,0, 1]) halfProximalBone(height, diameter,560, 3);}}
indexProximalBone();