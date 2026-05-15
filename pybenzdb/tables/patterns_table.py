from pybenzdb.tables.table import Table

class Patterns_Table (Table):
  """ This class allows for displaying a table containing benzenoid information from patterns query. """

  def add_row (self, info: dict) -> None:
    """ Adds a row based on the given information

        Args:
          info (dict): The information about the considered benzenoid
    """
    super().add_row (info)
    self.add_data ("cove", info["cove"])
    self.add_data ("fjord", info["fjord"])
