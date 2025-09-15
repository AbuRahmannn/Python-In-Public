txt_data = "i like pizza"

file_path = "C:\Users\imara\OneDrive\Desktop\output.txt"

try:
    with open(file_path, "a") as file:
        file.write("\n" + txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")  