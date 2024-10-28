import os
import shutil


def delete_files_in_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if "gitkeep" in filename:
                continue
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Deleted directory: {file_path}")
    except FileNotFoundError:
        print(f"Folder not found: {folder_path}")
    except PermissionError:
        print(f"Permission error while deleting files in: {folder_path}")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    output_folder = "output"
    if os.path.exists(output_folder):
        for folder in os.listdir(output_folder):
            delete_files_in_folder(os.path.join(output_folder, folder))
    else:
        print(f"Output folder not found: {output_folder}")

    spec_file = "main.spec"
    try:
        if os.path.exists(spec_file):
            os.remove(spec_file)
            print(f"Deleted file: {spec_file}")
    except Exception as e:
        print(f"An error occurred while deleting {spec_file}: {e}")

    print("Cleanup complete!")


if __name__ == "__main__":
    main()