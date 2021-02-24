#Christian Flores 15/02/2021

first_route = "Chapter_10_Text_Exceptions/"
files = ["cats.txt", "dogs.txt"]
for file in files:
    print("\n")
    file_to_open = first_route+file
    try:
        with open(file_to_open) as f:
            for line in f:
                print(line.strip())
    except FileNotFoundError:
        print(f"File {file} not found!")