import io

class BotInfo :
    def __init__(self,TAG : str):
        if TAG is None :
            return ValueError("Error for TAG: %s" % TAG)
        if TAG == "ID":
            self.IDTYPEDEV ="""Devlopre ID : 994927811049574431"""
            self.TYPESERVERID = """ <Server ID> """
            self.TYPEROLEOWNER = """ <Owner ID"""
            return
        elif TAG == "TKN":
            with io.open('Files/file.B0','r', encoding='utf-8') as type :
                self.TKNTYPE = type.readline()
        elif TAG == "PFX":
            self.CMDH = """Prefix"""
        else: 
            return KeyError("Unknown TAG %s" % TAG)
