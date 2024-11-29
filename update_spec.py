# update_spec.py
file_name = "buildozer.spec"

try:
    with open(file_name, 'r') as f:
        lines = f.readlines()

    with open(file_name, 'w') as f:
        for line in lines:
            if line.startswith("title = "):
                f.write("title = DeepSpace\n")
            else:
                f.write(line)
    print(f"Файл {file_name} успешно обновлён.")
except FileNotFoundError:
    print(f"Файл {file_name} не найден.")
