void setup() {
  pinMode(2, OUTPUT);
}

uint16_t cnt = 0;
uint16_t cmp = 20;
int max = 200;

void loop() {
 
  cnt = (cnt+1) % max;
  if (cnt==0) {
    digitalWrite(2, HIGH);
    cmp = (cmp+1)%(max*3);
  }
  if (cnt==(cmp/3))
    digitalWrite(2, LOW);
  
}
