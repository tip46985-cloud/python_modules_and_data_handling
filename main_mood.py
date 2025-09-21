import mood_responses

def main():
    try:
        mood = input("How are you feeling today? ").strip()
        if not mood:
            print("You didn't enter a mood. Please try again.")
            return
        print(mood_responses.mood_response(mood))
    except Exception as e:
        print("Error:", e)
    finally:
        print("Thanks for using Mood Checker!")

if __name__ == "__main__":
    main()
