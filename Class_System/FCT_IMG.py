import io
from FCC.config import*

global img_type_A
global img_type_B
global img_type_C

try :
    f =  io.open('Content/image_default_e.png', 'rb')
    img_type_A = f.read()
except Exception as ea:
    print(f"\n{New} {ea} {CR}\n")  

try :
    f =  io.open('Content/image_yes_u.webp', 'rb')
    img_type_B = f.read()
except Exception as eb:
    print(f"\n{New} {eb} {CR}\n")  

try :
    f =  io.open('Content/image_yes_w.webp', 'rb')
    img_type_C = f.read()
except Exception as ec:
    print(f"\n{New} {ec} {CR}\n")  

try :
    f =  io.open('Content/image_yes_x.webp', 'rb')
    img_type_C = f.read()
except Exception as ec:
    print(f"\n{New} {ec} {CR}\n")  
