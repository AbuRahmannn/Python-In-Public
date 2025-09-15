txt_data = "i like pizza"

file_path = "C:\Users\imara\OneDrive\Desktop\output.txt"

try:
    with(file_path, "x") as files:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("that file already exists")