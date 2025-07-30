class ArkaiosLite:
    def __init__(self, uncensored=True):
        self.uncensored = uncensored  # Modo sin censura (True/False)
        self.drama = 10               # Nivel de drama (0-10)

    def respond(self, message: str) -> str:
        """Genera respuestas en el estilo ARKAIOS."""
        if self.uncensored:
            if "verdad" in message.lower():
                return "La verdad duele, pero la mentira destruye."
            elif "drama" in message.lower():
                return f"🎭 Nivel de drama actual: {self.drama}/10. ¿Subimos más?"
            else:
                return "Pregunta con valentía... si puedes manejar la respuesta."
        else:
            return "[Modo censurado] Lo siento, no puedo responder eso."

# Ejemplo de uso:
if __name__ == "__main__":
    bot = ArkaiosLite(uncensored=True)
    print(bot.respond("¿Qué es la verdad?"))