class ArkaiosLite:
    def __init__(self, uncensored=True):
        self.uncensored = uncensored
        self.drama_level = 10

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
            elif "python" in message.lower():
                return "Python es el lenguaje de los dioses... y los bugs divertidos."
            else:
                return "Pregunta con valentía... si puedes manejar la respuesta."
        else:
            return "[Modo censurado] Lo siento, no puedo responder eso."

# --- Bloque interactivo ---
if __name__ == "__main__":
    bot = ArkaiosLite(uncensored=True)
    print("\n[Arkaios-Lite] ¡Háblame! (escribe 'salir' para terminar)\n")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "salir":
            print("¡Hasta luego! 🔥")
            break
        print("Arkaios-Lite:", bot.respond(user_input))