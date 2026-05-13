from pybenzdb.displays.display import Display


class NICS_Display (Display):
  """ This class allows for displaying benzenoid information from NICS query. """

  def __init__ (self, info: dict):
    """ Initializes the display tool with the provided information

      Args:
        info (str): The information about the considered benzenoid
    """
    super().__init__(info)
    self.add_data ("NICS R values", self.get_information("nicsR"))
    self.add_data ("NICS U values", self.get_information("nicsU"))
