def mood_response(mood: str) -> str:
    if mood is None:
        return "I didn't catch that — how are you feeling?"
    m = mood.strip().lower()
    responses = {
        "happy": "Awesome — keep that smile going! 😊",
        "sad": "I'm sorry you're feeling sad. It's okay to take a break and be kind to yourself.",
        "excited": "Love the energy — enjoy the moment and ride that wave! 🎉",
        "tired": "Rest is important — consider a short break or a nap.",
        "anxious": "Try a few slow breaths. You got this.",
        "angry": "Take a moment to breathe. It's okay to step back and cool off.",
    }
    return responses.get(m, f"Thanks for sharing — you said: \"{mood.strip()}\".")
