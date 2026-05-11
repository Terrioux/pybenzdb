class IMS2D1A_Display (Display):
  """ This class allows for displaying benzenoid information from IMS2D1A query """

  def __init__ (self, info: dict):
    """ initializes the display tool """
    super().__init__(info)
    self.add_data ("Type", self.get_information("type"))

  def display (self) -> None:
    """ displays the information """
    super().display()
    self.display_image(self.get_information("picture"))
