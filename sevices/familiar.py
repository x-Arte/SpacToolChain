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


