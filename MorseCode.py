def morse_it(string, morse_dict):
    string = string.upper()
    result = ""
    
    for letter in string:
        if letter in morse_dict.keys():
            result += morse_dict[letter] + " "
        elif letter == " ":
            result += " "
        else:
            print(f"Error: Character '{letter}' is not in the Morse code dictionary. Skipping.")
    
    return result


def main():
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
        '(': '-.--.', ')': '-.--.-', '!': '-.-.--'
    }

    while True:
        print("\nMenu:")
        print("a. Translate English to Morse code")
        print("b. Translate Morse code to English")
        print("c. Exit")

        choice = input("Enter your choice (a/b/c): ").lower()

        if choice == 'a':
            text_input = input("Enter the English text to translate to Morse code: ")
            morse_result = morse_it(text_input, morse_dict)
            print(f"\nMorse Code: {morse_result.strip()}")

        elif choice == 'b':
            morse_input = input("Enter the Morse code to translate to English (use spaces between symbols): ")
            english_result = morse_it(morse_input, morse_dict)
            print(f"\nEnglish Text: {english_result.strip()}")

        elif choice == 'c':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option (a/b/c).")


if __name__ == "__main__":
    main()