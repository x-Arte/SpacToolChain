from models import db
from models.NPC import NPC
from . import familiar

def create_new_npc(npcID, name, familiarList):
    """
    create new npc (Model, not to db).
    :param npcID: string; npcID
    :param name: string; name of NPC
    :param familiarList: arrayList[{maxSubFamiliarLevel: integer}]; maxSubFamiliarLevel List
    :return: integer;
    """
    maxFamiliarLevel = len(familiarList)
    newNPC = NPC(npcID=npcID, name=name, maxFamiliarLevel=maxFamiliarLevel)
    nextFamiliarID = None
    for i in range(maxFamiliarLevel - 1, -1, -1):
        # do not check whether thisFamiliarID == None
        # May cause bugs
        thisFamiliarID = familiar.add_new_familiar(maxSubFamiliarLevel=familiarList[i]['maxSubFamiliarLevel'], nextFamiliarLevelID=nextFamiliarID)
        nextFamiliarID = thisFamiliarID
    firstFamiliarLevelID = nextFamiliarID
    newNPC.firstFamiliarLevelID = firstFamiliarLevelID
    return newNPC
def delete_npc(npc):
    """
    delete an exist npc and its related data
    :param npc: class NPC (models); must not be None
    :return: boolean; whether successfully delete its related data (familiar list)
    """
    delete = familiar.delete_familiar_list(int(npc.firstFamiliarLevelID))
    if delete:
        db.session.delete(npc)
        db.session.commit()

    return delete