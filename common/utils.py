from skins.models import Skin

def getAllSkins():
    return Skin.objects.all()

def getSkin(id_skin):
    return Skin.objects.get(id_skin=id_skin)

def createSkin(id, nom, des, stat, coste, cantidad):
    newSkin = Skin(id_skin=id,nombre=nom,desgaste=des,stattrack=stat,precio=coste,stock=cantidad)
    newSkin.save()
    
def deleteSkin(id):
    skin = getSkin(id)
    skin.delete()


    