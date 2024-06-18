def main():
    file_path = 'books/frankenstein.txt'
    with open(file_path) as f:
        book_text = f.read()
        word_count_total = word_count(book_text)
        character_count_list = character_count(book_text)

        print(f"--- Begin report of {file_path} ---")
        print(f"{word_count_total} words found in the document")
        print(" ")
        for char in character_count_list:
            print(f"The '{char['char']}' character was found {char['num']} times")
        print("--- End report ---")

def sort_on(d):
    return d["num"]

def word_count(text):
    words_list = text.split()
    return len(words_list)

def character_count(text):
    character_dict = {}
    character_list_sorted = []
    lowered_text = text.lower()

    for char in lowered_text:
        if char in character_dict:
            character_dict[char] += 1
        elif char.isalpha():
            character_dict[char] = 1

    for key,value in character_dict.items():
        character_list_sorted.append({"char":key, "num":value})
    
    character_list_sorted.sort(reverse=True, key=sort_on)
    return character_list_sorted
        
main()