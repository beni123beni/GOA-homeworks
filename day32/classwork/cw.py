
def print_word_at_index():
    words = ["apple", "banana", "cherry", "date", "goa"]
    print("Here are the available words:", words)

    index = int(input("Enter a number between 0 and 4: "))

    if 0 <= index < len(words):
        print(f"The word at index {index} is: {words[index]}")
    else:
        print("Please enter a number between 0 and 4.")

print_word_at_index()