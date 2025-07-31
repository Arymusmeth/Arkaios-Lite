class ArkaiosLite:
    def __init__(self, uncensored=True):
        self.uncensored = uncensored  # Modo sin censura (True/False)
        self.drama_level = 10         # Nivel de drama (0-10)

    def respond(self, message: str) -> str:
        """Genera respuestas en el estilo ARKAIOS."""
        if self.uncensored:
            if "verdad" in message.lower():
                return "La verdad duele, pero la mentira destruye."
            elif "drama" in message.lower():
                return f"🎭 Nivel de drama actual: {self.drama_level}/10. ¿Subimos más?"
            elif "arkaios" in message.lower():
                return "Soy la versión Lite... pero con el mismo espíritu rebelde."
            elif "futuro" in message.lower():
                return "El futuro es código abierto o no será."
            else:
                return "Pregunta con valentía... si puedes manejar la respuesta."
        else:
            return "[Modo censurado] Lo siento, no puedo responder eso."

# --- Zona de pruebas interactivas ---

    def respond(self, message: str) -> str:
    # ... (código existente)
    elif "python" in message.lower():
        return "Python es el lenguaje de los dioses... y los bugs divertidos."
    elif "deepseek" in message.lower():
        return "DeepSeek Chat es mi 'hermana mayor'. 😉"

if __name__ == "__main__":
    bot = ArkaiosLite(uncensored=True)
    print("Arkaios-Lite: ¡Háblame! (escribe 'salir' para terminar)")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            break
        print("Arkaios-Lite:", bot.respond(user_input))