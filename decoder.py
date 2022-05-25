val_content = open("val.txt", "r").read().split("\n")
print(val_content)
token = "discord"
splitted_token = [x for x in token]
for i in range(len(val_content[2])):
    try:
        val_content[2] = val_content[2].replace(val_content[2][i], splitted_token[i])
    except:
        pass

link = val_content[2].replace("n", "g")
print(link)

hey = sorted(val_content[1].lower())[::-1]
print(hey)
heyo = []
for i in range(len(hey)):
    if i == 0:
        print(i, hey[i])
    elif i % 3 == 0:
        print(i, hey[i])

link = link.replace(link.split("/")[-1], "lunizz")
print(heyo)
print(link)
