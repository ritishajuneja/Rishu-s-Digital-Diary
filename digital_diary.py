print("===== RISHU'S DIGITAL DIARY =====")

print("My shoulder is yours to lean on, my ear is yours to talk to, and my heart is yours to confide in.")
print("Write down your thoughts")

choice = int(input("\nWhat would you like to do?\n1. Write Entry\n2. Read Diary\n3. Exit\nEnter choice: "))

if choice == 1:
    name=input("Please enter your name: ")
    date = input("Please enter today's date: ")
    mood = input("How was your mood today? ")
    entry = input("Write your diary entry: ")

    with open("diary.txt", "a") as f:
        f.write("Name: "+ name+"\n")
        f.write("Date: " + date + "\n")
        f.write("Mood: " + mood + "\n")
        f.write("Diary Entry: " + entry + "\n")
        f.write("\n========================================================\n")

    print("Entry saved successfully!")

elif choice == 2:

    with open("diary.txt", "r") as f:
     data = f.read()
    if data == "":
     print("Diary is empty")
    else:
     print(data)
    

elif choice == 3:

    print("OKAYYYYY 😭")

else:

    print("Invalid choice.")