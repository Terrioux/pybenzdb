class Irregularities_Display (Display):
  """ This class allows for displaying benzenoid information from irregularities query """

  def __init__ (self, info: dict):
    """ initializes the display tool """
    super().__init__(info)
    self.add_data ("# solo", self.get_information("solo"))
    self.add_data ("# duo", self.get_information("duo"))
    self.add_data ("# trio", self.get_information("trio"))
    self.add_data ("# quartet", self.get_information("quartet"))
