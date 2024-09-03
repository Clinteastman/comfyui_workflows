#---------------------------------------------------------------------------------------------------------------------#
# Comfyroll Studio custom nodes by RockOfFire and Akatsuzi    https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes                             
# for ComfyUI                                                 https://github.com/comfyanonymous/ComfyUI                                               
#---------------------------------------------------------------------------------------------------------------------#

from ..categories import icons

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any = AnyType("*")

#---------------------------------------------------------------------------------------------------------------------# 
class CR_StringToNumber: 

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"text": ("STRING", {"multiline": False, "default": "text"}),
                "round_integer": (["round", "round down","round up"],),
                },
        }

    RETURN_TYPES = ("INT", "FLOAT", "STRING", )
    RETURN_NAMES = ("INT", "FLOAT", "show_help", )
    FUNCTION = "convert"
    CATEGORY = icons.get("Comfyroll/Utils/Conversion")

    def convert(self, text, round_integer):

        # Check if the text starts with a minus sign
        if text.startswith('-') and text[1:].replace('.','',1).isdigit():
            # If it starts with '-', remove it and convert the rest to int and float
            float_out = -float(text[1:])
        else:
            # Check if number
            if text.replace('.','',1).isdigit():
                float_out = float(text)
            else:
                print(f"[Error] CR String To Number. Not a number.")
                return {}

        if round_integer == "round up":
            if text.startswith('-'):
                int_out = int(float_out)
            else:
                int_out = int(float_out) + 1
        elif round_integer == "round down": 
            if text.startswith('-'):
                int_out = int(float_out) - 1
            else:
                int_out = int(float_out)
        else:
            int_out = round(float_out)
        
        show_help = "https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-string-to-number"
        return (int_out, float_out, show_help,)
        
#---------------------------------------------------------------------------------------------------------------------# 
class CR_TextListToString:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {
                "text_list": ("STRING", {"forceInput": True}),
                    },
                }

    RETURN_TYPES = ("STRING", "STRING", )
    RETURN_NAMES = ("STRING", "show_help", )
    FUNCTION = "joinlist"
    CATEGORY = icons.get("Comfyroll/Utils/Conversion")

    def joinlist(self, text_list):
    
        string_out = " ".join(text_list)

        show_help = "https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-text-list-to-string"

        return (string_out, show_help, )

#---------------------------------------------------------------------------------------------------------------------#  
# based on Repeater node by pythongosssss 
class CR_StringToCombo:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": False, "default": "", "forceInput": True}),
            },
        }

    RETURN_TYPES = (any, "STRING", )
    RETURN_NAMES = ("any", "show_help", )
    FUNCTION = "convert"
    CATEGORY = icons.get("Comfyroll/Utils/Conversion")

    def convert(self, text):
    
        text_list = list()
        
        if text != "":
            values = text.split(',')
            text_list = values[0]
            print(text_list)
        
        show_help = "https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-string-to-combo"

        return (text_list, show_help, )
        
#---------------------------------------------------------------------------------------------------------------------------------------------------#
# Cloned from Mikey Nodes
class CR_IntegerToString:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"int_": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                }
        }

    RETURN_TYPES = ("STRING","STRING", )
    RETURN_NAMES = ("STRING","show_help", )
    FUNCTION = 'convert'
    CATEGORY = icons.get("Comfyroll/Utils/Conversion")

    def convert(self, int_):
        show_help = "https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-integer-to-string"
        return (f'{int_}', show_help, )

#---------------------------------------------------------------------------------------------------------------------------------------------------#
# Cloned from Mikey Nodes
class CR_FloatToString:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"float_": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 1000000.0}),
                }        
        }

    RETURN_TYPES = ('STRING', "STRING", )
    RETURN_NAMES = ('STRING', "show_help", )
    FUNCTION = 'convert'
    CATEGORY = icons.get("Comfyroll/Utils/Conversion")

    def convert(self, float_):
        show_help = "https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-float-to-string"
        return (f'{float_}', show_help, )

#---------------------------------------------------------------------------------------------------------------------
class CR_FloatToInteger:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"_float": ("FLOAT", {"default": 0.0})}}

    RETURN_TYPES = ("INT", "STRING", )
    RETURN_NAMES = ("INT", "show_help", )
    FUNCTION = "convert"
    CATEGORY = icons.get("Comfyroll/Utils/Conversion")

    def convert(self, _float):
        show_help = "https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-float-to-integer"
        return (int(_float), show_help, )
        
#---------------------------------------------------------------------------------------------------------------------------------------------------#
# This node is used to convert type Seed to type INT
class CR_SeedToInt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("SEED", ),
            }
        }

    RETURN_TYPES = ("INT", "STRING", )
    RETURN_NAMES = ("INT", "show_help", )
    FUNCTION = "seed_to_int"
    CATEGORY = icons.get("Comfyroll/Utils/Conversion")

    def seed_to_int(self, seed):
        show_help = "https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes/wiki/Conversion-Nodes#cr-seed-to-int"
        return (seed.get('seed'), show_help, )
 
#---------------------------------------------------------------------------------------------------------------------#
# MAPPINGS
#---------------------------------------------------------------------------------------------------------------------#
# For reference only, actual mappings are in __init__.py
# 10 nodes published
'''
NODE_CLASS_MAPPINGS = {   
    "CR String To Number":CR_StringToNumber,
    "CR String To Combo":CR_StringToCombo,    
    "CR Float To String":CR_FloatToString,
    "CR Float To Integer":CR_FloatToInteger,
    "CR Integer To String":CR_IntegerToString,    
    "CR Text List To String":CR_TextListToString,
    "CR Seed to Int": CR_SeedToInt, 
}
'''    
     

