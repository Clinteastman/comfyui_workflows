#---------------------------------------------------------------------------------------------------------------------#
# Comfyroll Nodes by RockOfFire and Akatsuzi      https://github.com/RockOfFire/CR-Animation-Nodes
# for ComfyUI                                     https://github.com/comfyanonymous/ComfyUI
#---------------------------------------------------------------------------------------------------------------------#

import os
import folder_paths
from PIL import Image, ImageFont
import torch
import numpy as np
import re
from pathlib import Path
import typing as t
from dataclasses import dataclass
from ..nodes.xygrid_functions import create_images_grid_by_columns, Annotation
from ..categories import icons
    
def tensor_to_pillow(image: t.Any) -> Image.Image:
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

def pillow_to_tensor(image: Image.Image) -> t.Any:
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)

def find_highest_numeric_value(directory, filename_prefix):
    highest_value = -1  # Initialize with a value lower than possible numeric values
    
    # Iterate through all files in the directory
    for filename in os.listdir(directory):
        if filename.startswith(filename_prefix):
            try:
                # Extract numeric part of the filename
                numeric_part = filename[len(filename_prefix):]
                numeric_str = re.search(r'\d+', numeric_part).group()
                numeric_value = int(numeric_str)
                # Check if the current numeric value is higher than the highest found so far
                if numeric_value > highest_value:
                    highest_value = int(numeric_value)
            except ValueError:
                # If the numeric part is not a valid integer, ignore the file
                continue
    
    return highest_value
    
#---------------------------------------------------------------------------------------------------------------------#
# NODES
#---------------------------------------------------------------------------------------------------------------------#
# These nodes are based on https://github.com/LEv145/images-grid-comfy-plugin
#---------------------------------------------------------------------------------------------------------------------
class CR_XYZList:

    @classmethod
    def INPUT_TYPES(s):
        return {"required":{
                    "index": ("INT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                    "list1": ("STRING", {"multiline": True, "default": "x"}),
                    "x_prepend": ("STRING", {"multiline": False, "default": ""}),
                    "x_append": ("STRING", {"multiline": False, "default": ""}),
                    "x_annotation_prepend": ("STRING", {"multiline": False, "default": ""}),                    
                    "list2": ("STRING", {"multiline": True, "default": "y"}),
                    "y_prepend": ("STRING", {"multiline": False, "default": ""}),
                    "y_append": ("STRING", {"multiline": False, "default": ""}),
                    "y_annotation_prepend": ("STRING", {"multiline": False, "default": ""}),                    
                    "list3": ("STRING", {"multiline": True, "default": "z"}),
                    "z_prepend": ("STRING", {"multiline": False, "default": ""}),
                    "z_append": ("STRING", {"multiline": False, "default": ""}),
                    "z_annotation_prepend": ("STRING", {"multiline": False, "default": ""}),                      
                    }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING", "STRING", "BOOLEAN",)
    RETURN_NAMES = ("X", "Y", "Z", "x_annotation", "y_annotation", "z_annotation", "trigger",) 
    FUNCTION = "cross_join"
    CATEGORY = icons.get("Comfyroll/XY Grid")  
    
    def cross_join(self, list1, list2, list3,
        x_prepend, x_append, x_annotation_prepend,
        y_prepend, y_append, y_annotation_prepend,
        z_prepend, z_append, z_annotation_prepend, index):

        # Index values for all XY nodes start from 1
        index -=1  
        trigger = False

        listx = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', list1)
        listy = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', list2)
        listz = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', list3)
        
        listx = [item.strip() for item in listx]
        listy = [item.strip() for item in listy]
        listz = [item.strip() for item in listz]
        
        lenx = len(listx)
        leny = len(listy)
        lenz = len(listz)

        sheet_size = lenx * leny    
        grid_size = lenx * leny * lenz

        x = index % lenx
        y = int(index / lenx) % leny   
        z = int(index / sheet_size)         
        
        x_out = x_prepend + listx[x] + x_append
        y_out = y_prepend + listy[y] + y_append
        z_out = z_prepend + listz[z] + z_append

        x_ann_out = ""
        y_ann_out = ""
        z_ann_out = ""
        
        if index + 1 == grid_size:
            x_ann_out = [x_annotation_prepend + item + ";" for item in listx]
            y_ann_out = [y_annotation_prepend + item + ";" for item in listy]
            z_ann_out = [z_annotation_prepend + item + ";" for item in listz]
            x_ann_out = "".join([str(item) for item in x_ann_out])
            y_ann_out = "".join([str(item) for item in y_ann_out])
            z_ann_out = "".join([str(item) for item in z_ann_out])
            trigger = True
            
        return (x_out, y_out, z_out, x_ann_out, y_ann_out, z_ann_out, trigger, )

#---------------------------------------------------------------------------------------------------------------------
class CR_XYZInterpolate:

    @classmethod
    def INPUT_TYPES(s):
        gradient_profiles = ["Lerp"]    
    
        return {"required": {"x_columns":("INT", {"default": 5.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "x_start_value": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 0.01,}),
                             "x_step": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 0.01,}),
                             "x_annotation_prepend": ("STRING", {"multiline": False, "default": ""}), 
                             "y_rows":("INT", {"default": 5.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "y_start_value": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 0.01,}),
                             "y_step": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 0.01,}),
                             "y_annotation_prepend": ("STRING", {"multiline": False, "default": ""}),
                             "z_sheets":("INT", {"default": 5.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "z_start_value": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 0.01,}),
                             "z_step": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 9999.0, "step": 0.01,}),
                             "z_annotation_prepend": ("STRING", {"multiline": False, "default": ""}),                              
                             "index": ("INT", {"default": 0.0, "min": 0.0, "max": 9999.0, "step": 1.0,}),
                             "gradient_profile": (gradient_profiles,)                              
                            }              
                }
    
    RETURN_TYPES = ("FLOAT", "FLOAT", "FLOAT", "STRING", "STRING", "STRING", "BOOLEAN", )
    RETURN_NAMES = ("X", "Y", "Z", "x_annotation", "y_annotation", "z_annotation", "trigger", )    
    FUNCTION = "gradient"
    CATEGORY = icons.get("Comfyroll/XY Grid")  

    def gradient(self, x_columns, x_start_value, x_step, x_annotation_prepend,
    y_rows, y_start_value, y_step, y_annotation_prepend,
    z_rows, z_start_value, z_step, z_annotation_prepend,
    index, gradient_profile):

        # Index values for all XY nodes start from 1
        index -=1
        trigger = False
        sheet_size = x_columns * y_rows
        grid_size = x_columns * y_rows * z_sheets
        
        x = index % x_columns
        y = int(index / x_columns) % y_rows    
        z = int(index / sheet_size) 
        
        x_float_out = round(x_start_value + x * x_step, 3)
        y_float_out = round(y_start_value + y * y_step, 3)
        z_float_out = round(z_start_value + z * z_step, 3)
           
        x_ann_out = ""
        y_ann_out = ""
        z_ann_out = ""
        
        if index + 1 == grid_size:
            for i in range(0, x_columns):
                x = index % x_columns
                x_float_out = x_start_value + i * x_step
                x_float_out = round(x_float_out, 3)
                x_ann_out = x_ann_out + x_annotation_prepend + str(x_float_out) + "; "
            for j in range(0, y_rows):
                y = int(index / x_columns)
                y_float_out = y_start_value + j * y_step
                y_float_out = round(y_float_out, 3)
                y_ann_out = y_ann_out + y_annotation_prepend + str(y_float_out) + "; "
            for k in range(0, z_sheets):
                z = int(index / x_columns)
                z_float_out = z_start_value + k * z_step
                z_float_out = round(z_float_out, 3)
                z_ann_out = z_ann_out + z_annotation_prepend + str(z_float_out) + "; "                
                    
            x_ann_out = x_ann_out[:-1]
            y_ann_out = y_ann_out[:-1]
            z_ann_out = z_ann_out[:-1]
            print(x_ann_out,y_ann_out,z_ann_out)
            trigger = True
             
        return (x_float_out, y_float_out, z_float_out, x_ann_out, y_ann_out, z_ann_out, trigger)
               
#---------------------------------------------------------------------------------------------------------------------#
class CR_LoadXYAnnotationFromFile:
    
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
            "input_file_path": ("STRING", {"multiline": False, "default": ""}),
            "file_name": ("STRING", {"multiline": False, "default": ""}),
            "file_extension": (["txt", "csv"],),
            }
        }

    RETURN_TYPES = ("GRID_ANNOTATION", "STRING", )
    RETURN_NAMES = ("GRID_ANNOTATION", "show_text", )
    FUNCTION = "load"
    CATEGORY = icons.get("Comfyroll/XY Grid")      
    
    def load(self, input_file_path, file_name, file_extension):
        filepath = input_file_path + "\\" + file_name + "." + file_extension
        print(f"CR_Load Schedule From File: Loading {filepath}")
        
        lists = []
            
        if file_extension == "csv":
            with open(filepath, "r") as csv_file:
                reader = csv.reader(csv_file)
        
                for row in reader:
                    lists.append(row)
                    
        else:
            with open(filepath, "r") as txt_file:
                for row in txt_file:
                    parts = row.strip().split(",", 1)
                    
                    if len(parts) >= 2:
                        second_part = parts[1].strip('"')
                        lists.append([parts[0], second_part])

        print(lists)
        return(lists,str(lists),)

#---------------------------------------------------------------------------------------------------------------------
class CR_XYGrid:

    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {
                    "images": ("IMAGE",),
                    "gap": ("INT", {"default": 0, "min": 0}),
                    "max_columns": ("INT", {"default": 1, "min": 1, "max": 10000}),
            },
                "optional": {
                    "annotation": ("GRID_ANNOTATION",),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "create_image"
    CATEGORY = icons.get("Comfyroll/XY Grid")    
    
    def create_image(self, images, gap, max_columns, annotation=None):

        pillow_images = [tensor_to_pillow(i) for i in images]
        pillow_grid = create_images_grid_by_columns(
            images=pillow_images,
            gap=gap,
            annotation=annotation,
            max_columns=max_columns,
        )
        tensor_grid = pillow_to_tensor(pillow_grid)

        return (tensor_grid,)

#---------------------------------------------------------------------------------------------------------------------
class CR_XYSaveGridImage:
# originally based on SaveImageSequence by mtb

    def __init__(self):
        self.type = "output"

    @classmethod
    def INPUT_TYPES(cls):
    
        output_dir = folder_paths.output_directory
        output_folders = [name for name in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir,name))]
    
        return {
            "required": {"mode": (["Save", "Preview"],),
                         "output_folder": (sorted(output_folders), ),
                         "image": ("IMAGE", ),
                         "filename_prefix": ("STRING", {"default": "CR"}),
                         "file_format": (["webp", "jpg", "png", "tif"],),
            },
            "optional": {"output_path": ("STRING", {"default": '', "multiline": False}),
                         "trigger": ("BOOLEAN", {"default": False},),                         
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "save_image"
    OUTPUT_NODE = True
    CATEGORY = icons.get("Comfyroll/XY Grid")  
            
    def save_image(self, mode, output_folder, image, file_format, output_path='', filename_prefix="CR", trigger=False):

        if trigger == False:
            return ()
        
        output_dir = folder_paths.get_output_directory()  
        out_folder = os.path.join(output_dir, output_folder)

        # Set the output path
        if output_path != '':
            if not os.path.exists(output_path):
                print(f"[Warning] CR Save XY Grid Image: The input_path `{output_path}` does not exist")
                return ("",)
            out_path = output_path
        else:
            out_path = os.path.join(output_dir, out_folder)
        
        if mode == "Preview":
            out_path = folder_paths.temp_directory

        print(f"[Info] CR Save XY Grid Image: Output path is `{out_path}`")
        
        # Set the counter
        counter = find_highest_numeric_value(out_path, filename_prefix) + 1
        #print(f"[Debug] counter {counter}")
        
        # Output image
        output_image = image[0].cpu().numpy()
        img = Image.fromarray(np.clip(output_image * 255.0, 0, 255).astype(np.uint8))
        
        output_filename = f"{filename_prefix}_{counter:05}"
        img_params = {'png': {'compress_level': 4}, 
                      'webp': {'method': 6, 'lossless': False, 'quality': 80},
                      'jpg': {'format': 'JPEG'},
                      'tif': {'format': 'TIFF'}
                     } 
        self.type = "output" if mode == "Save" else 'temp'

        resolved_image_path = os.path.join(out_path, f"{output_filename}.{file_format}")
        img.save(resolved_image_path, **img_params[file_format])
        print(f"[Info] CR Save XY Grid Image: Saved to {output_filename}.{file_format}")
        out_filename = f"{output_filename}.{file_format}"
        preview = {"ui": {"images": [{"filename": out_filename,"subfolder": out_path,"type": self.type,}]}}
       
        return preview

#---------------------------------------------------------------------------------------------------------------------
# MAPPINGS
#---------------------------------------------------------------------------------------------------------------------#
# For reference only, actual mappings are in __init__.py
# 0 nodes released
'''
NODE_CLASS_MAPPINGS = {
    # XY Grid
    "CR XYZ Index":CR_XYZIndex,    
    "CR XYZ Interpolate":CR_XYZInterpolate,
    "CR Load XY Annotation From File":CR_LoadXYAnnotationFromFile,
    "CR XY Grid":CR_XYGrid,
}
'''

    
     
