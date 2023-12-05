import html

with open('film_list.txt', 'r', encoding='utf-8') as file:
    original_text = file.read()

#Change HTML to Polish letters
decoded_text = html.unescape(original_text)


with open('film_list.txt', 'w', encoding='utf-8') as file:
    file.write(decoded_text)
    
