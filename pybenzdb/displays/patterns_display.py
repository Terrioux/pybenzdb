class Patterns_Display (Display):
  """ This class allows for displaying benzenoid information from patterns query """

  def __init__ (self, info: dict):
    """ initializes the display tool """
    super().__init__(info)
    self.add_data ("cove", self.get_information("cove"))
    self.add_data ("fjord", self.get_information("fjord"))
