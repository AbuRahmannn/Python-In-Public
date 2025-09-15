#python writing files

txt_data = "i like pizza"

file_path = "C:/Users/imara/OneDrive/Desktop/output.txt"

with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")
