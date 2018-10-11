/*

Noise generator

*/

float yoff = 0.0;

void setup() {

  size(640, 360);
}

void draw() {
  background(51);
  
  fill(255);
  beginShape();
  
  float xoff = 0;
  
  for (float x = 0; x <= width; x += 10) {
    
    float y = map(noise(xoff, yoff), 0, 1, 200, 300);
    
    vertex (x, y);
    
    xoff += 0.05;
  }
  
  yoff += 0.01;
  vertex (width, height);
  vertex(0, height);
  endShape(CLOSE);
}
