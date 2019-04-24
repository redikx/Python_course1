meals = ["apple", "bread", "milk", "trash", "butter", "meal"]
for plate in meals:
    if plate == "trash":
        break
    print(plate)
else:
    print("shows when no break, so no trash in whole loop")

