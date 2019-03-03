with open('referat.txt', 'r', encoding='utf-8') as myfile:    
    text = myfile.read()
    print('Длина файла - ', len(text))
    print('Количество слов - ', len(text.split()))
    with open('referat2.txt', 'w', encoding='utf-8') as myfile2:    
        myfile2.write(text.replace('.', '!'))







# with open('myfile.txt', 'a', encoding='utf-8') as myfile:
#     myfile.write("\nПойдем гулять!")
    
    
# with open('myfile.txt', 'r', encoding='utf-8') as myfile2:
#     for line in myfile2:
#         line = line.upper()
#         line = line.replace("\n", "")
#         print(line)

# with open('myfile.txt', 'w', encoding='utf-8') as myfile:
# myfile.write("Всем привет!")