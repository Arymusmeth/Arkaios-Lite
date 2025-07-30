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
if __name__ == "__main__":
    bot = ArkaiosLite(uncensored=True)
    
    # Ejemplos de uso (puedes probarlos al ejecutar el archivo)
    print(bot.respond("¿Qué es la verdad?"))      # Output: "La verdad duele..."
    print(bot.respond("Háblame de ARKAIOS"))     # Output: "Soy la versión Lite..."
    print(bot.respond("¿Cómo ves el futuro?"))   # Output: "El futuro es código abierto..."