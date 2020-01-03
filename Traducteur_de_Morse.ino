#include <LiquidCrystal.h> // On importe la bibliothèque nécessaire  à l'utilisation de l'écran LCD

/* La durée d'un point est la référence en terme de temps 
 * le tiret " DASH" vaut trois fois la durée d'un point 
 * le temps entre un pojnt et un tiret et l'affichage d'une lettre est la durée d'un point
 * le temps entre l'affiche de 2 caractuères est de trois fois la duré ed'un point
 * le temps entre deux mots doit être sept fois la durée d'un point  
 */

const char CLEAR = 0; //On assigne les valeur en fonction du type d'information reçu , ici l'espace "ESPACE" vaut 0 
const char DOT = 1;   //Le point "DOT" vaut 1 en valeur de temps 
const char DASH = 2;  // Le tiret "DASH" vaut la valeur 2 
const char alphabet[26][6] { // On créer une matrice nommée "alphabet" qui correspond à une suite de valeur 02111 pour A par exemple  
  { 'A', DOT, DASH, CLEAR, CLEAR, CLEAR},
  { 'B', DASH, DOT, DOT, DOT, CLEAR},
  { 'C', DASH, DOT, DASH, DOT, CLEAR},
  { 'D', DASH, DOT, DOT, CLEAR, CLEAR},
  { 'E', DOT, CLEAR, CLEAR, CLEAR, CLEAR},
  { 'F', DOT, DOT, DASH, DOT, CLEAR},
  { 'G', DASH, DASH, DOT, CLEAR, CLEAR},
  { 'H', DOT, DOT, DOT, DOT, CLEAR},
  { 'I', DOT, DOT, CLEAR, CLEAR, CLEAR},
  { 'J', DOT, DASH, DASH, DASH, CLEAR},
  { 'K', DASH, DOT, DASH, CLEAR, CLEAR},
  { 'L', DOT, DASH, DOT, DOT, CLEAR},
  { 'M', DASH, DASH, CLEAR, CLEAR, CLEAR},
  { 'N', DASH, DOT, CLEAR, CLEAR, CLEAR},
  { 'O', DASH, DASH, DASH, CLEAR, CLEAR},
  { 'P', DOT, DASH, DASH, DOT, CLEAR},
  { 'Q', DASH, DASH, DOT, DASH, CLEAR},
  { 'R', DOT, DASH, DOT, CLEAR, CLEAR},
  { 'S', DOT, DOT, DOT, CLEAR, CLEAR},
  { 'T', DASH, CLEAR, CLEAR, CLEAR, CLEAR},
  { 'U', DOT, DOT, DASH, CLEAR, CLEAR},
  { 'V', DOT, DOT, DOT, DASH, CLEAR},
  { 'W', DOT, DASH, DASH, CLEAR, CLEAR},
  { 'X', DASH, DOT, DOT, DASH, CLEAR},
  { 'Y', DASH, DOT, DASH, DASH, CLEAR},
  { 'Z', DASH, DASH, DOT, DOT, CLEAR}
};

const unsigned long dotDuration = 1000; // On indique la durée en ms d'un point la référence de temps ici 1000ms 
const unsigned long tolerance = 500; // Le temps de tolérence de reconnaissance d'un tirer ou d'in point ou d'un espace. LA tolérance est d'ici une demi seconde 500ms
const unsigned long dashDuration = 3 * dotDuration; // On indique à quelles valeur de temps vaut un point , un espace ou un tiret
const unsigned long shortGap = dotDuration;
const unsigned long mediumGap = 3 * dotDuration;  
const unsigned long longGap = 7 * dotDuration;// longGap correspond à l'espace entre le changement de mot

// Etat actuel du boutton
enum State { 
  UP = 0, 
  DOWN = 1 } state;

// Le temps entre deux changement d'état du boutton
unsigned long lastChange;

// temps séparant de la dernière action sur le boutton
unsigned long downDuration;

// La  séquence du caracère en cours d'inscrption
char character[5];

// La variable stockant la valeur du caractère dans la matrice
int characterIndex;

// La prochaine étape possible dans la séquence
enum Action {
  START = 0,
  READ_DASHDOT = 1,
  READ_CHARACTER = 2,
  READ_WORD = 3
} action;

// pin sur lequel le boutton est connecté
int buttonPin = 6;
// pin qur lequel le buzzer est connecté
int buzzerPin = 9;

LiquidCrystal lcd(12, 11, 5, 4, 3, 2); // On indique les dimensions de l'écran utilisé

void setup() {
  Serial.begin(9600); // La fréquence de raffraichissement de l'écran

  lcd.begin(16, 2);
  
  pinMode(buttonPin, INPUT_PULLUP);

  state = UP;
  characterIndex = 0;
  downDuration = 0;
  lastChange = 0;
  action = START;
}

// Reset la séquence de point , tiret à chaque séquence complète rentrée
void clearCharacter() {
  characterIndex = 0;
  for (int i = 0; i < 5; ++i) {
    character[i] = CLEAR;
  }
}

// Détermine la dernière durée d'appuie sur le bouton
void readDashDot() {
  Serial.print("Down duration was: ");
  Serial.println(downDuration);
  
  if (downDuration >= dashDuration - tolerance && downDuration < dashDuration + tolerance) { // Avec les tolérances on détermine la suite de la séquence , soit un tiret
    character[characterIndex] = DASH;
    Serial.println("DASH");
    characterIndex++;
  } else if (downDuration >= dotDuration - tolerance && downDuration < dotDuration + tolerance) {  // Soit un point
    character[characterIndex] = DOT;
    Serial.println("DOT");
    characterIndex++;
  } else {
    Serial.println("Erreur temps d'appuis non reconnu");   // Si une autre valeur est entrée , si le boutton est resté appuyé trop longtemps on afffiche une erreur
  }
}

// Interprète la séquence en une lettre dans la matrice alphabet
char readCharacter() {
  bool found;
  for (int i = 0; i < 26; ++i) {
    found = true;
    for (int j = 0; found && j < 5; ++j) {
      if (character[j] != alphabet[i][j + 1]) {
        found = false;
      }
    }
    if (found) {
      return alphabet[i][0];
    }
  }
  return 0;
}

void loop() { // On effectue le programme suivant en boucle 
  State newState = digitalRead(buttonPin) ? UP : DOWN;

  // Si on appuie sur le bouton on ferme le circuit du buzzer et on emet un son
  if (newState == DOWN) {
    tone(buzzerPin, 800); // On indique la fréquence du son qu'on souhaite on mets par exemple 800Hz
  } else {
    noTone(buzzerPin);
  }

  if (newState == state) {
    if (newState == UP) {
      // Calcule le temps pour lequel le bouton n'est pas appuyé en suivant notre valeur de référence
      unsigned long upDuration = (millis() - lastChange);
     
      if (action == READ_DASHDOT && upDuration >= shortGap - tolerance && upDuration < shortGap + tolerance) {
        readDashDot();
        action = READ_CHARACTER;
      } else if (action == READ_CHARACTER && upDuration >= mediumGap - tolerance && upDuration < mediumGap + tolerance) {
        char c = readCharacter();
        if (c != 0) {
          //Un lettre valide à été reconnue 
          Serial.print("Read character: ");  // On affiche sur l'écran la lettre reconnue
          Serial.println(c);
          lcd.print(c);
        } else {
          Serial.println("Lettre non reconnue"); // Sinon on affiche que la séquence ne correspond à aucune lettre
        }
        clearCharacter();
        action = READ_WORD;
      } else if (action == READ_WORD && upDuration >= longGap - tolerance && upDuration < longGap + tolerance) {
        Serial.println("Read next word");   // Si la longueur de l'espace est assez long on applique un caractère vide , un espace entre deux mots.
        lcd.print(' ');
        action = READ_DASHDOT;
      }
    } else {
      downDuration = (millis() - lastChange);
    }
  } else {
    if (state == UP && newState == DOWN) {      // On rajoute à la séquence la valeur 0 
      downDuration = 0;
    }
    lastChange = millis();
    state = newState;
    action = READ_DASHDOT;
  }
}
