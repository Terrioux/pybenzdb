class NICS_Display (Display):
  """ This class allows for displaying benzenoid information from NICS query """
  def __init__ (self, info: dict):
    """ initializes the display tool """
    super().__init__(info)
    self.add_data ("NICS R values", self.get_information("nicsR"))
    self.add_data ("NICS U values", self.get_information("nicsU"))
