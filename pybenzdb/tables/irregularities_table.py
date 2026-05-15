from pybenzdb.tables.table import Table

class Irregularities_Table (Table):
  """ This class allows for displaying a table containing benzenoid information from irregularities query. """

  def add_row (self, info: dict) -> None:
    """ Adds a row based on the given information

        Args:
          info (dict): The information about the considered benzenoid
    """
    super().add_row (info)
    self.add_data ("# solo", info["solo"])
    self.add_data ("# duo", info["duo"])
    self.add_data ("# trio", info["trio"])
    self.add_data ("# quartet", info["quartet"])
