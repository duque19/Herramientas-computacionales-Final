def char_to_ascii(char):
    return ord(char)

def ascii_to_binary(ascii_value):
    return bin(ascii_value)[2:].zfill(8)

def generate_byte_representation(character):
    ascii_value = char_to_ascii(character)
    binary_representation = ascii_to_binary(ascii_value)
    return binary_representation

def generate_word_representation(word):
    byte_representations = [generate_byte_representation(char) for char in word]
    return ' '.join(byte_representations)

def main():
    while True:
        print("Menú:")
        print("1. Generar la representación en byte de un carácter")
        print("2. Generar la representación en byte de una palabra")
        print("3. Salir")

        try:
            option = int(input("Ingrese la opción (1, 2, o 3): "))

            if option == 1:
                char = input("Ingrese un carácter: ")
                byte_representation = generate_byte_representation(char)
                print("Representación en byte:", byte_representation)

            elif option == 2:
                word = input("Ingrese una palabra: ")
                word_representation = generate_word_representation(word)
                print("Representación en byte de la palabra:")
                print(word_representation)

            elif option == 3:
                print("Saliendo del programa. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Por favor, ingrese 1, 2, o 3.")

        except ValueError:
            print("Error: Ingrese un número válido.")

if __name__ == "__main__":
    main()


