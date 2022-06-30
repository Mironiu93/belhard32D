morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

message = input("Enter your message in English (enter message in upper case): ")

english_to_morse = {}
for key, value in morse_code.items():
    english_to_morse[value] = key



def english_to_morse(message):
    morse = []
    for char in message:
        if char in morse_code:
            morse.append(morse_code[char])
    return " ".join(morse)

print(english_to_morse(message))

