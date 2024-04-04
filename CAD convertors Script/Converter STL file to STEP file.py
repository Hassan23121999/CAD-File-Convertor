import tkinter as tk
from tkinter import filedialog
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.IFSelect import IFSelect_RetDone
from OCC.Core.StlAPI import StlAPI_Writer
from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
import os

def load_step_file(filename):
    step_reader = STEPControl_Reader()
    status = step_reader.ReadFile(filename)
    if status == IFSelect_RetDone:
        step_reader.TransferRoot()
        return step_reader.OneShape()
    else:
        print("Error: Unable to read the STEP file.")
        return None

def convert_to_stl(step_shape, output_filename):
    mesh = BRepMesh_IncrementalMesh(step_shape, 0.01)
    mesh.Perform()
    stl_writer = StlAPI_Writer()
    stl_writer.SetASCIIMode(True)  # Use False for binary mode
    stl_writer.Write(step_shape, output_filename)

def select_directory_and_convert():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory()

    for subdir, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".step"):
                step_path = os.path.join(subdir, file)
                stl_path = step_path.replace('.step', '.stl')
                step_shape = load_step_file(step_path)
                if step_shape:
                    convert_to_stl(step_shape, stl_path)
                    print(f"Converted: {stl_path}")

select_directory_and_convert()
