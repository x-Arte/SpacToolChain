from models.Selection import Selection
from models import db

def delete_selection_list(firstSelectionID):
    """
    delete one dialogue's this selection data and its next selection data
    :param firstSelectionID: integer; the temp head of the selection list
    :return: boolean; whether successfully delete the list
    """
    return True