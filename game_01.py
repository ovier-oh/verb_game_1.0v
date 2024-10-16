import random

class Round:
    """Representa una ronda del juego, donde se selecciona un verbo y se manejan los intentos"""
    def __init__(self, verb_info):
        self.infinitive, self.past_simple, self.meaning = verb_info
        self.attempts = 0
        self.max_attempts = 5

    def play(self):
        """Ejecuta una ronda completa, donde el jugador intenta adivinar el pasado simple"""
        print(f"\nVerbo en infinitivo: {self.infinitive}")
        
        while self.attempts < self.max_attempts:
            user_input = input("Escribe el pasado simple: ").strip().lower()
            self.attempts += 1
            
            if user_input == self.past_simple:
                score = self.calculate_score()
                print(f"¡Correcto! Obtuviste {score} puntos.")
                return score
            else:
                remaining_attempts = self.max_attempts - self.attempts
                print(f"Incorrecto. Te quedan {remaining_attempts} intentos.")
        
        # Si no adivina en los 5 intentos, mostrar la palabra correcta en español y restar vida
        print(f"Has agotado tus intentos. La respuesta correcta era: {self.past_simple} ({self.meaning} en español).")
        return 0

    def calculate_score(self):
        """Calcula los puntos obtenidos según el número de intentos"""
        if self.attempts == 1:
            return 6
        elif self.attempts == 2:
            return 4
        elif self.attempts == 3:
            return 2
        else:
            return 1


class VerbGame:
    """Clase principal que maneja el juego completo"""
    def __init__(self):
        self.verb_pairs = [
                ("run", "ran", "correr", "corrió"),
    ("go", "went", "ir", "fue"),
    ("be", "was/were", "ser/estar", "fue/estuvo"),
    ("eat", "ate", "comer", "comió"),
    ("have", "had", "tener", "tuvo"),
    ("do", "did", "hacer", "hizo"),
    ("see", "saw", "ver", "vio"),
    ("take", "took", "tomar", "tomó"),
    ("make", "made", "hacer", "hizo"),
    ("say", "said", "decir", "dijo"),
    ("get", "got", "obtener", "obtuvo"),
    ("know", "knew", "saber", "supó"),
    ("think", "thought", "pensar", "pensó"),
    ("come", "came", "venir", "vino"),
    ("give", "gave", "dar", "dio"),
    ("find", "found", "encontrar", "encontró"),
    ("tell", "told", "decir", "dijo"),
    ("leave", "left", "dejar", "dejó"),
    ("feel", "felt", "sentir", "sintió"),
    ("bring", "brought", "traer", "trajo"),
    ("begin", "began", "comenzar", "comenzó"),
    ("keep", "kept", "mantener", "mantuvo"),
    ("hold", "held", "sostener", "sostuvo"),
    ("write", "wrote", "escribir", "escribió"),
    ("stand", "stood", "pararse", "se paró"),
    ("hear", "heard", "oír", "oyó"),
    ("meet", "met", "conocer", "conoció"),
    ("pay", "paid", "pagar", "pagó"),
    ("sit", "sat", "sentarse", "se sentó"),
    ("speak", "spoke", "hablar", "habló"),
    ("lie", "lay", "mentir", "mintió"),
    ("drive", "drove", "conducir", "condujo"),
    ("break", "broke", "romper", "rompió"),
    ("buy", "bought", "comprar", "compró"),
    ("build", "built", "construir", "construyó"),
    ("grow", "grew", "crecer", "creció"),
    ("win", "won", "ganar", "ganó"),
    ("send", "sent", "enviar", "envió"),
    ("sell", "sold", "vender", "vendió"),
    ("read", "read", "leer", "leyó"),
    ("spend", "spent", "gastar", "gastó"),
    ("sleep", "slept", "dormir", "durmió"),
    ("wear", "wore", "llevar (puesto)", "llevó (puesto)"),
    ("cut", "cut", "cortar", "cortó"),
    ("rise", "rose", "elevar", "elevó"),
    ("swim", "swam", "nadar", "nadó"),
    ("teach", "taught", "enseñar", "enseñó"),
    ("understand", "understood", "entender", "entendió"),
    ("choose", "chose", "elegir", "eligió"),
    ("fly", "flew", "volar", "voló"),
    ("forget", "forgot", "olvidar", "olvidó"),
    ("hide", "hid", "esconder", "escondió"),
    ("lend", "lent", "prestar", "prestó"),
    ("lead", "led", "liderar", "lideró"),
    ("run", "ran", "correr", "corrió"),
    ("burn", "burnt/burned", "quemar", "quemó"),
    ("draw", "drew", "dibujar", "dibujó"),
    ("dream", "dreamt/dreamed", "soñar", "soñó"),
    ("fight", "fought", "pelear", "peleó"),
    ("freeze", "froze", "congelar", "congeló"),
    ("hang", "hung", "colgar", "colgó"),
    ("hit", "hit", "golpear", "golpeó"),
    ("hurt", "hurt", "herir", "hirió"),
    ("let", "let", "permitir", "permitió"),
    ("light", "lit/lighted", "encender", "encendió"),
    ("mean", "meant", "significar", "significó"),
    ("shake", "shook", "sacudir", "sacudió"),
    ("shine", "shone", "brillar", "brilló"),
    ("shoot", "shot", "disparar", "disparó"),
    ("sing", "sang", "cantar", "cantó"),
    ("sit", "sat", "sentarse", "se sentó"),
    ("stick", "stuck", "pegar", "pegó"),
    ("strike", "struck", "golpear", "golpeó"),
    ("swing", "swung", "balancearse", "se balanceó"),
    ("tear", "tore", "romper (desgarrar)", "desgarró"),
    ("throw", "threw", "lanzar", "lanzó"),
    ("wake", "woke", "despertar", "despertó"),
    ("withdraw", "withdrew", "retirar", "retiró"),
    ("feel", "felt", "sentir", "sintió"),
    ("shake", "shook", "sacudir", "sacudió"),
    ("sink", "sank", "hundir", "hundió"),
    ("shut", "shut", "cerrar", "cerró"),
    ("ring", "rang", "sonar", "sonó"),
    ("ride", "rode", "montar", "montó"),
    ("steal", "stole", "robar", "robó"),
    ("strike", "struck", "golpear", "golpeó"),
    ("wake", "woke", "despertar", "despertó"),
    ("win", "won", "ganar", "ganó"),
    ("write", "wrote", "escribir", "escribió")
        ]
        self.total_score = 0
        self.total_life = 10

    def start_game(self):
        """Inicia el juego y controla el flujo del mismo"""
        print("¡Bienvenido al juego de memoria de verbos!")

        while self.total_life > 0:
            self.play_round()

            # Mostrar estado actual
            print(f"Vida restante: {self.total_life}")
            print(f"Puntaje total: {self.total_score}")

            if self.total_life <= 0:
                print("Has perdido todas tus vidas. Fin del juego.")
                break

        print(f"Juego terminado. Puntaje final: {self.total_score}")

    def play_round(self):
        """Juega una ronda completa, seleccionando un verbo y evaluando los intentos"""
        # Seleccionar un verbo aleatorio
        verb_info = random.choice(self.verb_pairs)
        round_instance = Round(verb_info)

        # Jugar la ronda
        score = round_instance.play()

        if score > 0:
            self.total_score += score
        else:
            # Restar vida si se alcanzaron los 5 intentos sin éxito
            self.total_life -= 1


if __name__ == "__main__":
    game = VerbGame()
    game.start_game()
