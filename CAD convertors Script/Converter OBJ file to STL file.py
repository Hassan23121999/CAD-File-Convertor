import os
import tkinter as tk
from tkinter import filedialog, simpledialog
from obj2stl import obj2stl

def convert_obj_files(input_directory, output_directory, base_name):
    for i, file_name in enumerate(os.listdir(input_directory), start=1):
        if file_name.lower().endswith('.obj'):
            obj_file_path = os.path.join(input_directory, file_name)
            output_file_name = f"{base_name}{i}_mediumshape_fraunhofer.stl"
            output_file_path = os.path.join(output_directory, output_file_name)
            obj2stl.convert(input=obj_file_path, output=output_file_path)
            print(f"Converted: {output_file_name}")

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask user for the input directory
    input_directory = filedialog.askdirectory(title="Select Input Folder with OBJ files")

    # Ask user for the output directory
    output_directory = filedialog.askdirectory(title="Select Output Folder for STL files")

    # Ask user for the base name for output files
    base_name = simpledialog.askstring("Input", "Enter base name for output files:", parent=root)

    if input_directory and output_directory and base_name:
        convert_obj_files(input_directory, output_directory, base_name)
    else:
        print("Operation cancelled.")

    root.destroy()

if __name__ == "__main__":
    main()
