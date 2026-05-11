class Clar_Covers_Display (Display):
  """ This class allows for displaying benzenoid information from Clar Cover query """

  def display (self) -> None:
    """ displays the information """
    super().display()
    self.display_image(self.get_information("clarCover"))
