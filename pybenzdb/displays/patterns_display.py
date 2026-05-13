from pybenzdb.displays.display import Display


class Patterns_Display (Display):
  """ This class allows for displaying benzenoid information from patterns query. """

  def __init__ (self, info: dict):
    """ Initializes the display tool with the provided information

      Args:
        info (dict): The information about the considered benzenoid
    """
    super().__init__(info)
    self.add_data ("cove", self.get_information("cove"))
    self.add_data ("fjord", self.get_information("fjord"))
