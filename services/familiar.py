from models.Familiar import Familiar
from . import dialogue
from models import db

def add_new_familiar(maxSubFamiliarLevel, nextFamiliarLevelID = None, firstDialogueID = None, defaultNextDialogue = None):
    """
    add a new familiar level to db. If failed to add, db would roll back.
    :param maxSubFamiliarLevel: integer;
    :param nextFamiliarLevelID: integer;
    :param firstDialogueID: default None;
    :return: integer; newFamiliar ID; If failed to create, return None.
    """
    try:
        newFamiliar = Familiar(maxSubFamiliarLevel=maxSubFamiliarLevel, nextFamiliarLevelID=nextFamiliarLevelID, firstDialogueID=firstDialogueID, defaultNextDialogue=defaultNextDialogue)
        db.session.add(newFamiliar)
        db.session.commit()
        newFamiliarID = newFamiliar.id
    except Exception as e:
        db.session.rollback()
        print(f"An error occurred: {e}")
        newFamiliarID = None
    # May cause bugs
    return newFamiliarID

def delete_familiar(familiar):
    """
    delete an exist familiar and its related data
    :param familiar:  class Familiar (models); must not be None
    :return: boolean; whether successfully delete its related data (dialogue list)
    """
    delete = True
    if familiar.firstDialogueID:
        delete = dialogue.delete_dialogue_list(int(familiar.firstDialogueID))
    db.session.delete(familiar)
    db.session.commit()
    return delete
def delete_familiar_list(firstFamiliarLevelID):
    """
    delete one npc's this familiar data and its next familiar data
    :param firstFamiliarLevelID: integer; the temp head of the familiar level list
    :return: boolean; whether successfully delete the list
    """
    delete = True
    firstFamiliar = Familiar.query.get(firstFamiliarLevelID)
    try:
        thisFamiliar = firstFamiliar
        nextFamiliarLevelID = firstFamiliar.nextFamiliarLevelID
        if nextFamiliarLevelID:
            delete = delete_familiar_list(int(nextFamiliarLevelID))
        delete_familiar(thisFamiliar)
    except:
        db.session.rollback()
        delete = False
    return delete

def update_familiar_list(firstFamiliarLevelID, familiarList):
    """
    update one npc's this familiar data list
    :param firstFamiliarLevelID: integer; the orginal head of the familiar level list
    :param familiarList: arrayList[{"id":string, "maxSubFamiliarLevel": integer}]; new familiar list
    :return: new firstFamiliarLevelID
    """
    originalMap = {}
    thisFamiliarLevelID = firstFamiliarLevelID # integer
    # step 1: Iterate through the familiar list and store the id in the original map
    while(thisFamiliarLevelID):
        try:
            tempFamiliar = Familiar.query.get(thisFamiliarLevelID)
            originalMap[tempFamiliar.id] = False # default do not exist
            nextFamiliarLevelID = tempFamiliar.nextFamiliarLevelID
            thisFamiliarLevelID = nextFamiliarLevelID
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred when checking the original familiar list: {e}")
    # step 2: Iterate through the new familiar list and check the original map if each node exists. Save the id to the sorted new list.
    # if exists: update the familiar node
    # else: add a new familiar node to db
    sortedNewIDList = [] # integer list
    for i in range(len(familiarList)):
        try:
            # did not check when familiarList[i]['id'] is not None but not in the originalMap
            # May cause bugs
            if familiarList[i]['id']:
                try:
                    tempFamiliar = Familiar.query.get(int(familiarList[i]['id']))
                    tempFamiliar.maxSubFamiliarLevel = familiarList[i]['maxSubFamiliarLevel']
                    db.session.commit()
                    originalMap[tempFamiliar.id] = True
                    sortedNewIDList.append(tempFamiliar.id)
                except Exception as e:
                    db.session.rollback()
                    print(f"An error occurred when update an exist familiar node: {e}")
            else:
                newFamiliarID = add_new_familiar(familiarList[i]['maxSubFamiliarLevel'])
                sortedNewIDList.append(newFamiliarID)
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred when iterate through the new familiar list: {e}")
    # step 3: Iterate through the original list map and delete all nodes whose ids do not appear in the new ID list
    for id in originalMap.keys():
        if not originalMap[id]:
            tempFamiliar = Familiar.query.get(originalMap[id])
            try:
                delete_familiar(tempFamiliar)
            except:
                db.session.rollback()
    # step 4: Reconnect the list according to the sortedNewIDList
    for i in range(len(sortedNewIDList) - 1):
        thisFamiliar = Familiar.query.get(sortedNewIDList[i])
        if thisFamiliar:
            thisFamiliar.nextFamiliarLevelID = sortedNewIDList[i+1]
            db.session.commit()
        else:
            db.session.rollback()
    endFamiliar = Familiar.query.get(sortedNewIDList[-1])
    endFamiliar.nextFamiliarLevelID = None

    if sortedNewIDList[0]:
        newfirstFamiliarLevelID = sortedNewIDList[0]
    else:
        newfirstFamiliarLevelID = None
    return newfirstFamiliarLevelID
def get_familiar_data(familiarID):
    """
    get familiar data by familiarID
    :param familiarID: integer;
    :return: dict{"id":integer, "maxSubFamiliarLevel": integer, "dialogue_cnt": integer}; If failed to get, return None.
    """
    try:
        familiar = Familiar.query.get(familiarID)
        result = {"id": str(familiarID), "maxSubFamiliarLevel": familiar.maxSubFamiliarLevel}
        dialogCount = dialogue.get_dialogue_count(familiar.firstDialogueID)
        result["dialogCount"] = dialogCount
    except:
        result = None
    return result
def get_familiar_list_data(firstFamiliarLevelID):
    """

    :param firstFamiliarLevelID: integer;
    :return: list[dict{"id":integer, "maxSubFamiliarLevel": integer, "dialogue_cnt": integer}];
    """
    result = []
    thisFamiliarID = firstFamiliarLevelID
    while thisFamiliarID:
        thisFamiliar = Familiar.query.get(thisFamiliarID)
        result.append(get_familiar_data(thisFamiliar.id))
        thisFamiliarID = thisFamiliar.nextFamiliarLevelID
    return result
