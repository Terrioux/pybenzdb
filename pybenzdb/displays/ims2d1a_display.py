from pybenzdb.displays.display import Display


class IMS2D1A_Display (Display):
  """ This class allows for displaying benzenoid information from IMS2D1A query. """

  def __init__ (self, info: dict) -> None:
    """ Initializes the display tool with the provided information

      Args:
        info (dict): The information about the considered benzenoid
    """
    super().__init__(info)
    self.add_data ("Type", self.get_information("type"))

  def display (self) -> None:
    """ Displays the information """
    super().display()
    self.display_image(self.get_information("picture"))
