if __name__ == '__main__':
    s = input()

    first_out=False
    second_out=False
    third_out=False
    fourth_out=False
    fifth_out=False
    
    s = list(s)

    for i in range(0, len(s)):
        if s[i].isalnum():
            first_out = True

        if s[i].isalpha():
            second_out = True

        if s[i].isnumeric():
            third_out = True

        if s[i].islower():
            fourth_out = True

        if s[i].isupper():
            fifth_out = True

print(first_out)
print(second_out)
print(third_out)
print(fourth_out)
print(fifth_out)
