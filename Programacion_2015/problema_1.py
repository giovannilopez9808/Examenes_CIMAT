list_character = ["a",
                  "d",
                  "a",
                  "a",
                  "f",
                  "a",
                  "g",
                  "r",
                  "r",
                  "a",
                  "0"]
pos = 1
count = 0
while list_character[pos] != "0":
    if list_character[pos-1] != "a" and list_character[pos+1] != "a":
        count += 1
    pos += 1
print("Existen {} letras que cumplen la condicion".format(count))
