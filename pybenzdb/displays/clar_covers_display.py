from pybenzdb.displays.display import Display


class Clar_Covers_Display (Display):
  """ This class allows for displaying benzenoid information from Clar Cover query. """

  def display (self) -> None:
    """ Initializes the display tool with the provided information

      Args:
        info (str): The information about the considered benzenoid
    """
    super().display()
    self.display_image(self.get_information("clarCover"))
