#include <LiquidCrystal.h> // On indique à Arduino quelle bibliothèques sont nécessaires pour utiliser les composants
#include <Servo.h> // On à importé les bibliothèques nécessaires à l'utilisation de l'écran LCD et du servo moteur


Servo name_servo;  // On assigne le nom "Servo" au servo moteur
LiquidCrystal lcd(1, 2, 4, 5, 6, 7); // (rs, enable, d4, d5, d6, d7) //On indique à quelle sorties digitales est relié l'écran.

int position_servo = 0; // On indique la position initiale du servo moteur. 0 est un entier "int" correspond à 0 degré par rapport à l'angle initiale.
const int trigPin = 9; // capteur de proximité : On indique que la pin "trig" déclancheur de l'impulsion ultrasonore est reliée à la borne 9 de la carte.
const int echoPin = 10; // capteur de proximité : On indique que la pin "echo" récepteur de l'onde ultrasonore est reliée à la borne 10 de la carte.
const int buzzer = 11;  // Buzzer : On indique que le buzzer d'alerte de profondeur trop faible est relié à la borne 11 de la carte.
const int ledPin = 13; // Capteur de proximité : On indique que la LED s'allumant en cas de profondeur trop faible est reliée à la borne 13 de la carte.
const int pinLight = A0; // Capteur de luminosité : On indique que le capteur de luminosité translet ses information à la borne analogique A0 de la carte.
const int pinLed   = 8; // LEDs Blanches : On indique que les LEDS "phares " sont reliées à la borne 8 de la carte.
long duration;                  //On intriduit les variables dans le programme
int distanceCm, distanceInch;
int safetyDistance;
int thresholdvalue=200;         // On applique une valeur de référence de 200 Lux au capteur de luminosité

void setup() {

lcd.begin(16,2); // On initialise l'écran LCD en indiquant ses dimensions ( 16 caractères de largeur , 2 de hauteur)
pinMode(trigPin, OUTPUT); // On indique quelles connexions sont des entrées ou sorties 
pinMode(echoPin, INPUT);
pinMode(buzzer, OUTPUT);
pinMode(ledPin, OUTPUT);
pinMode(pinLed, OUTPUT); 
name_servo.attach(3);
}

void loop() {  // Le relevé d'information commence et s'effectue en boucle 


digitalWrite(trigPin, LOW);            
delayMicroseconds(2);
digitalWrite(trigPin, HIGH); // On envoi une impulsion ultrasonore
delayMicroseconds(10);
digitalWrite(trigPin, LOW);  // On stoppe l'envoi de l'impulsion

duration = pulseIn(echoPin, HIGH);  // On assigne à la variable "duration" le temps d'arrivée de l'impulsion "pulseIn" au récepteur 
distanceCm= duration*0.034/2;      // On calcul la distance en Cm de l'objet avec la définition de la vitesse d=v*t
distanceInch = duration*0.0133/2;  // On calcul la distance en Pouce de l'objet avec la définition de la vitesse d=v*t
safetyDistance = distanceCm;      // On assigne à la valeur de profoncdeuer la valeur calculé précédemment en Cm
if (safetyDistance <= 5){        // On compare la valeur mesurée avec l'entier 5 , il elle est inférieur ou non
  digitalWrite(buzzer, HIGH);    // Si elle est inférieur on ferme le circuit du buzzer , le courant passe et le buzer sonne
  digitalWrite(ledPin, HIGH);    // Le courant passe et la LED rouge s'allume
}
else{                           
  digitalWrite(buzzer, LOW);     // Sinon on laisse le circuit du buzzer ouvert , le buzzer ne sonne pas
  digitalWrite(ledPin, LOW);     // La LED rouge ne s'allume pas
}
{
    int sensorValue = analogRead(pinLight);      //On relève la valeur du capteur de luminosité 
    if(sensorValue<thresholdvalue)              // On la compare avec la valeur de 200Lux assigné à thresholdvalue , si elle est inférieur:
    {
        digitalWrite(pinLed, HIGH);               //On ferme le circuit des led et les phares s'allument
    }
    else
    {
        digitalWrite(pinLed, LOW);               //Sinon on laisse le circuit des led ouvert et les phares restent éteints 
    }
}
{
lcd.setCursor(0,0); // On indique à quel caractère de l'acran on souhaite que le texte commence
lcd.print("Distance: "); // On affiche distance: sur l'écran
lcd.print(distanceCm); // Puis on affiche à la suite la valeur de la distance calculée précedemment en cm
lcd.print("  cm");    // On marque cm à la suite de la valeur
delay(1);
lcd.setCursor(0,1);   // On indique à quel caractère de l'acran on souhaite que la suite du texte commence
lcd.print("Distance: "); // On affiche distance: sur l'écran
lcd.print(distanceInch); // Puis on affiche à la suite la valeur de la distance calculée précedemment en pouce
lcd.print("inch"); // On rajoute inch soit pouce après la veur
position_servo=0;  // On indique le degrès d'inclinaison de la barre , ici le degrè d'inclination de la roue du servo moteur
  if (50 <=position_servo ; position_servo +=1){   // On compare la position du servo moteur avec celle rentrée à l'origine 0 degrè et si elle est différente on rajoute +1 degrè
        name_servo.write(position_servo);                      // On assigne la nouvelle position du servo moteur à celle de référence
        delay(6);          // On applique un raffaichissement des données toutes les 6ms pour que les informations soient relevées rapidement et pour qu'elles restent lisibles sur l'écran et qie le servo moteur n'aille pas trop vite
      }  
      
      if (50 >= position_servo; position_servo -=1){ // On compare la position du servo moteur avec celle rentrée à l'origine 0 degrè et si elle est différente on rajoute -1 degrè
      name_servo.write(position_servo);    // On assigne la nouvelle position du servo moteur à celle de référence
      delay(6); }         // On applique un raffaichissement des données toutes les 6ms pour que les informations soient relevées rapidement et pour qu'elles restent lisibles sur l'écran et qie le servo moteur n'aille pas trop vite
}
}
    
      
 
    
