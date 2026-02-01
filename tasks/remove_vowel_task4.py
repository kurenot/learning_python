def remove_vowels(input_str: str) -> str:
    res_str = ""
    vowels_set = set([ "a" , "e" , "i" , "o" , "u" , "y"])
    for char in input_str:
        if char.lower() in vowels_set:
            continue
        else:
            res_str += char
    return res_str


print(remove_vowels("Hello, World!"))
print(remove_vowels("HELLO, WORLD !"))
print(remove_vowels("G, PRMCN"))
print(remove_vowels("O, OIO"))