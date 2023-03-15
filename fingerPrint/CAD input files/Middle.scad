
faceNumber = 560;
hole = 3;

module indexMiddleBone(){

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
        }
        
// second half of geometry
rotate([180, 0, 0]){        
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
}}}
indexMiddleBone();