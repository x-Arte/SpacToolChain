from models.Dialogue import Dialogue
from models import db
from services import selection

def delete_dialogue(dialogue):
    """
    delete an exist dialogue and its related data
    :param dialogue: class Dialogue (models); must not be None
    :return: boolean; whether successfully delete its related data (selection list)
    """
    delete = True
    if dialogue.firstSelectionID:
        delete = selection.delete_selection_list(int(dialogue.firstSelectionID))
    db.session.delete(dialogue)
    db.session.commit()
    return delete

def delete_dialogue_list(firstDialogueID):
    """
    delete one familiar's this dialogue data and its next dialogue data
    :param firstDialogueID: integer; the temp head of the dialogue list
    :return:  boolean; whether successfully delete the list
    """
    delete = True
    firstDialogue = Dialogue.query.get(firstDialogueID)
    try:
        thisDialogue = firstDialogue
        nextDialogueID = firstDialogue.nextDialogueID
        if nextDialogueID:
            delete = delete_dialogue_list(int(nextDialogueID))
        delete_dialogue(thisDialogue)
    except:
        db.session.rollback()
        delete = False
    return delete
