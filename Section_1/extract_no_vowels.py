inptext = input("Enter the text you want to analyze :")


inpletters = set(inptext)

inlist=list(inpletters)
print(inlist)

volwels = set("a" "e" "i" "o" "y" "u")

print(sorted(inpletters.difference(volwels)))

