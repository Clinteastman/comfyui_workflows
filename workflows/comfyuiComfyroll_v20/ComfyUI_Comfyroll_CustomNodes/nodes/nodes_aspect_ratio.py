#---------------------------------------------------------------------------------------------------------------------#
# Comfyroll Studio custom nodes by RockOfFire and Akatsuzi    https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes                             
# for ComfyUI                                                 https://github.com/comfyanonymous/ComfyUI                                               
#---------------------------------------------------------------------------------------------------------------------#

import torch
from ..categories import icons

#---------------------------------------------------------------------------------------------------------------------#
# Aspect Ratio Nodes
#---------------------------------------------------------------------------------------------------------------------#
class CR_AspectRatioSD15:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
    
        aspect_ratios = ["custom",
                         "1:1 square 512x512",
                         "1:1 square 1024x1024",
                         "2:3 portrait 512x768",
                         "3:4 portrait 512x682",
                         "3:2 landscape 768x512",
                         "4:3 landscape 682x512",
                         "16:9 cinema 910x512",
                         "1.85:1 cinema 952x512",
                         "2:1 cinema 1024x512",
                         "2.39:1 anamorphic 1224x512"]
               
        return {
            "required": {
                "width": ("INT", {"default": 512, "min": 64, "max": 8192}),
                "height": ("INT", {"default": 512, "min": 64, "max": 8192}),
                "aspect_ratio": (aspect_ratios,),
                "swap_dimensions": (["Off", "On"],),
                "upscale_factor": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 100.0, "step":0.1}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})
            }
        }
    RETURN_TYPES = ("INT", "INT", "FLOAT", "INT", "LATENT", "STRING", )
    RETURN_NAMES = ("width", "height", "upscale_factor", "batch_size", "empty_latent", "show_help", )
    FUNCTION = "Aspect_Ratio"
    CATEGORY = icons.get("Comfyroll/Aspect Ratio")

    def Aspect_Ratio(self, width, height, aspect_ratio, swap_dimensions, upscale_factor, batch_size):
        if aspect_ratio == "2:3 portrait 512x768":
            width, height = 512, 768
        elif aspect_ratio == "3:2 landscape 768x512":
            width, height = 768, 512
        elif aspect_ratio == "1:1 square 512x512":
            width, height = 512, 512
        elif aspect_ratio == "1:1 square 1024x1024":
            width, height = 1024, 1024
        elif aspect_ratio == "16:9 cinema 910x512":
            width, height = 910, 512
        elif aspect_ratio == "3:4 portrait 512x682":
            width, height = 512, 682
        elif aspect_ratio == "4:3 landscape 682x512":
            width, height = 682, 512
        elif aspect_ratio == "1.85:1 cinema 952x512":            
            width, height = 952, 512
        elif aspect_ratio == "2:1 cinema 1024x512":
            width, height = 1024, 512
        elif aspect_ratio == "2.39:1 anamorphic 1224x512":
            width, height = 1224, 512

        if swap_dimensions == "On":
            width, height = height, width
           
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])

        show_help = "https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Aspect-Ratio-Nodes#cr-sd15-aspect-ratio"
           
        return(width, height, upscale_factor, batch_size, {"samples":latent}, show_help, )   

#---------------------------------------------------------------------------------------------------------------------#
class CR_SDXLAspectRatio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
    
        aspect_ratios = ["custom",
                                  "1:1 square 1024x1024",
                                  "3:4 portrait 896x1152",
                                  "5:8 portrait 832x1216",
                                  "9:16 portrait 768x1344",
                                  "9:21 portrait 640x1536",
                                  "4:3 landscape 1152x896",
                                  "3:2 landscape 1216x832",
                                  "16:9 landscape 1344x768",
                                  "21:9 landscape 1536x640"]
        
        return {
            "required": {
                "width": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "height": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "aspect_ratio": (aspect_ratios,),
                "swap_dimensions": (["Off", "On"],),
                "upscale_factor": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 100.0, "step":0.1}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})
            }
        }
    RETURN_TYPES = ("INT", "INT", "FLOAT", "INT", "LATENT", "STRING", )
    RETURN_NAMES = ("width", "height", "upscale_factor", "batch_size", "empty_latent", "show_help", )
    FUNCTION = "Aspect_Ratio"
    CATEGORY = icons.get("Comfyroll/Aspect Ratio")

    def Aspect_Ratio(self, width, height, aspect_ratio, swap_dimensions, upscale_factor, batch_size):
        if aspect_ratio == "1:1 square 1024x1024":
            width, height = 1024, 1024
        elif aspect_ratio == "3:4 portrait 896x1152":
            width, height = 896, 1152
        elif aspect_ratio == "5:8 portrait 832x1216":
            width, height = 832, 1216
        elif aspect_ratio == "9:16 portrait 768x1344":
            width, height = 768, 1344
        elif aspect_ratio == "9:21 portrait 640x1536":
            width, height = 640, 1536
        elif aspect_ratio == "4:3 landscape 1152x896":
            width, height = 1152, 896
        elif aspect_ratio == "3:2 landscape 1216x832":
            width, height = 1216, 832
        elif aspect_ratio == "16:9 landscape 1344x768":
            width, height = 1344, 768
        elif aspect_ratio == "21:9 landscape 1536x640":
            width, height = 1536, 640

        if swap_dimensions == "On":
            width, height = height, width
             
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])

        show_help = "https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Aspect-Ratio-Nodes#cr-sdxl-aspect-ratio"
           
        return(width, height, upscale_factor, batch_size, {"samples":latent}, show_help, )  

#---------------------------------------------------------------------------------------------------------------------#
class CR_AspectRatio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
    
        aspect_ratios = ["custom",
                         "SD1.5 - 1:1 square 512x512",
                         "SD1.5 - 2:3 portrait 512x768",
                         "SD1.5 - 3:4 portrait 512x682",
                         "SD1.5 - 3:2 landscape 768x512",
                         "SD1.5 - 4:3 landscape 682x512",
                         "SD1.5 - 16:9 cinema 910x512",
                         "SD1.5 - 1.85:1 cinema 952x512",
                         "SD1.5 - 2:1 cinema 1024x512",
                         "SDXL - 1:1 square 1024x1024",
                         "SDXL - 3:4 portrait 896x1152",
                         "SDXL - 5:8 portrait 832x1216",
                         "SDXL - 9:16 portrait 768x1344",
                         "SDXL - 9:21 portrait 640x1536",
                         "SDXL - 4:3 landscape 1152x896",
                         "SDXL - 3:2 landscape 1216x832",
                         "SDXL - 16:9 landscape 1344x768",
                         "SDXL - 21:9 landscape 1536x640"]
               
        return {
            "required": {
                "width": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "height": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "aspect_ratio": (aspect_ratios,),
                "swap_dimensions": (["Off", "On"],),
                "upscale_factor": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 100.0, "step":0.1}),
                "prescale_factor": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 100.0, "step":0.1}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})
            }
        }
    RETURN_TYPES = ("INT", "INT", "FLOAT", "FLOAT", "INT", "LATENT", "STRING", )
    RETURN_NAMES = ("width", "height", "upscale_factor", "prescale_factor", "batch_size", "empty_latent", "show_help", )
    FUNCTION = "Aspect_Ratio"
    CATEGORY = icons.get("Comfyroll/Aspect Ratio")

    def Aspect_Ratio(self, width, height, aspect_ratio, swap_dimensions, upscale_factor, prescale_factor, batch_size):
        
        # SD1.5
        if aspect_ratio == "SD1.5 - 1:1 square 512x512":
            width, height = 512, 512
        elif aspect_ratio == "SD1.5 - 2:3 portrait 512x768":
            width, height = 512, 768
        elif aspect_ratio == "SD1.5 - 16:9 cinema 910x512":
            width, height = 910, 512
        elif aspect_ratio == "SD1.5 - 3:4 portrait 512x682":
            width, height = 512, 682
        elif aspect_ratio == "SD1.5 - 3:2 landscape 768x512":
            width, height = 768, 512    
        elif aspect_ratio == "SD1.5 - 4:3 landscape 682x512":
            width, height = 682, 512
        elif aspect_ratio == "SD1.5 - 1.85:1 cinema 952x512":            
            width, height = 952, 512
        elif aspect_ratio == "SD1.5 - 2:1 cinema 1024x512":
            width, height = 1024, 512
        elif aspect_ratio == "SD1.5 - 2.39:1 anamorphic 1224x512":
            width, height = 1224, 512 
        # SDXL   
        if aspect_ratio == "SDXL - 1:1 square 1024x1024":
            width, height = 1024, 1024
        elif aspect_ratio == "SDXL - 3:4 portrait 896x1152":
            width, height = 896, 1152
        elif aspect_ratio == "SDXL - 5:8 portrait 832x1216":
            width, height = 832, 1216
        elif aspect_ratio == "SDXL - 9:16 portrait 768x1344":
            width, height = 768, 1344
        elif aspect_ratio == "SDXL - 9:21 portrait 640x1536":
            width, height = 640, 1536
        elif aspect_ratio == "SDXL - 4:3 landscape 1152x896":
            width, height = 1152, 896
        elif aspect_ratio == "SDXL - 3:2 landscape 1216x832":
            width, height = 1216, 832
        elif aspect_ratio == "SDXL - 16:9 landscape 1344x768":
            width, height = 1344, 768
        elif aspect_ratio == "SDXL - 21:9 landscape 1536x640":
            width, height = 1536, 640                
        
        if swap_dimensions == "On":
            width, height = height, width
        
        width = int(width*prescale_factor)
        height = int(height*prescale_factor)
        
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])

        show_help = "https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Aspect-Ratio-Nodes#cr-aspect-ratio"
           
        return(width, height, upscale_factor, prescale_factor, batch_size, {"samples":latent}, show_help, )    

#---------------------------------------------------------------------------------------------------------------------#
class CR_AspectRatioBanners:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
    
        aspect_ratios = ["custom",
                         "Large Rectangle - 336x280", 
                         "Medium Rectangle - 300x250", 
                         "Small Rectangle - 180x150",
                         "Square - 250x250", 
                         "Small Square - 200x200",
                         "Button - 125x125", 
                         "Half Page - 300x600",
                         "Vertical Banner - 120x240", 
                         "Wide Skyscraper - 160x600", 
                         "Skyscraper - 120x600", 
                         "Billboard - 970x250", 
                         "Portrait - 300x1050", 
                         "Banner - 468x60", 
                         "Leaderboard - 728x90"]
                                 
        return {
            "required": {
                "width": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "height": ("INT", {"default": 1024, "min": 64, "max": 8192}),
                "aspect_ratio": (aspect_ratios,),
                "swap_dimensions": (["Off", "On"],),
                "upscale_factor": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 100.0, "step":0.1}),
                "prescale_factor": ("FLOAT", {"default": 1.0, "min": 0.1, "max": 100.0, "step":0.1}),
                "batch_size": ("INT", {"default": 1, "min": 1, "max": 64})
            }
        }
    RETURN_TYPES = ("INT", "INT", "FLOAT", "FLOAT", "INT", "LATENT", "STRING", )
    RETURN_NAMES = ("width", "height", "upscale_factor", "prescale_factor", "batch_size", "empty_latent", "show_help", )
    FUNCTION = "Aspect_Ratio"
    CATEGORY = icons.get("Comfyroll/Aspect Ratio")

    def Aspect_Ratio(self, width, height, aspect_ratio, swap_dimensions, upscale_factor, prescale_factor, batch_size):
        
        # Banner sizes
        if aspect_ratio == "Large Rectangle - 336x280":
            width, height = 336, 280
        elif aspect_ratio == "Medium Rectangle - 300x250":
            width, height = 300, 250
        elif aspect_ratio == "Small Rectangle - 180x150":
            width, height = 180, 150
        elif aspect_ratio == "Square - 250x250":
            width, height = 250, 250
        elif aspect_ratio == "Small Square - 200x200":
            width, height = 200	, 200
        elif aspect_ratio == "Button - 125x125":
            width, height = 125	, 125
        elif aspect_ratio == "Half Page - 300x600":
            width, height = 300, 600
        elif aspect_ratio == "Vertical Banner - 120x240":
            width, height = 120, 240
        elif aspect_ratio == "Wide Skyscraper - 160x600":
            width, height = 160, 600
        elif aspect_ratio == "Skyscraper - 120x600":
            width, height = 120, 600
        elif aspect_ratio == "Billboard - 970x250":
            width, height = 970, 250
        elif aspect_ratio == "Portrait - 300x1050":
            width, height = 300, 1050
        elif aspect_ratio == "Banner - 468x60":
            width, height = 168, 60
        elif aspect_ratio == "Leaderboard - 728x90":
            width, height = 728, 90              
        
        if swap_dimensions == "On":
            width, height = height, width
        
        width = int(width*prescale_factor)
        height = int(height*prescale_factor)
        
        latent = torch.zeros([batch_size, 4, height // 8, width // 8])

        show_help = "https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Aspect-Ratio-Nodes#cr-aspect-ratio-banners"
           
        return(width, height, upscale_factor, prescale_factor, batch_size, {"samples":latent}, show_help, ) 
  
#---------------------------------------------------------------------------------------------------------------------#
# MAPPINGS
#---------------------------------------------------------------------------------------------------------------------#
# For reference only, actual mappings are in __init__.py
'''
NODE_CLASS_MAPPINGS = {
    ### Aspect ratio
    "CR SD1.5 Aspect Ratio": CR_AspectRatioSD15,
    "CR SDXL Aspect Ratio": CR_SDXLAspectRatio,
    "CR Aspect Ratio": CR_AspectRatio,
    "CR Aspect Ratio Banners":CR_AspectRatioBanners,   
}
'''

