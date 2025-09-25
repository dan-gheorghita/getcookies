#Get cookies

import ast

def import_cookies():
    cookies_file = open('cookies.txt')

    text = cookies_file.read()

    start_list = 0
    new_list = ''
    list_of_list = []
    for i in range(len(text)):
        if start_list == 0:
            if text[i] == '[':
                new_list += text[i]
                start_list = 1
        else:
            if text[i] == ']':
                new_list += text[i]
                list_of_list.append(ast.literal_eval(new_list))
                start_list = 0
                new_list = ''
            else:
                new_list += text[i]
                
    return list_of_list[1]
