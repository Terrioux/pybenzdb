from pybenzdb.tables.table import Table

class IR_Table (Table):
  """ This class allows for displaying a table containing benzenoid information from ir query. """

  def add_row (self, info: dict) -> None:
    """ Adds a row based on the given information

        Args:
          info (dict): The information about the considered benzenoid
    """
    super().add_row (info)
    self.add_data ("final energy", info["finalEnergy"])
    self.add_data ("ZPE", info["zeroPointEnergy"])
