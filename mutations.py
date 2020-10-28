def mutate_string(string, position, character):
    s = list(string)
    
    s[position] = character
    string1 = ''.join(s)
    return string1
