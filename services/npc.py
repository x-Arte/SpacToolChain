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

def update_npc(npc, npcID, name, familiarList):
    """
    update npc infor
    :param npc: class NPC (models); must not be None
    :param npcID: string;
    :param name: string;
    :param familiarList: arrayList[{"id":string, "maxSubFamiliarLevel": integer}]; new familiar list
    :return: boolean; whether successfully update its related data (familiar list)
    """
    try:
        npc.npcID = npcID
        npc.name = name
        npc.maxFamiliarLevel = len(familiarList)
        npc.firstFamiliarLevelID = familiar.update_familiar_list(firstFamiliarLevelID=npc.firstFamiliarLevelID, familiarList=familiarList)
        db.session.commit()
        update = True
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")
        update = False
    return update

def to_dict(npc, details = False):
    """
    generate npc information dict
    :param npc: class NPC (models); must not be None
    :param details: boolean; whether to show familiar list details
    :return: dict;
    """
    result = {
        "id": str(npc.id),
        "npcID": npc.npcID,
        "name": npc.name
    }
    if details:
        result['familiarList'] = familiar.get_familiar_list_data(firstFamiliarLevelID=npc.firstFamiliarLevelID)
    return result