from pybenzdb.displays.display import Display


class Properties_Display (Display):
  """ This class allows for displaying benzenoid information from properties query. """

  def __init__ (self, info: dict):
    """ Initializes the display tool with the provided information

      Args:
        info (str): The information about the considered benzenoid
    """
    super().__init__(info)
    yesno = ["no","yes"]
    self.add_data ("Catacondensed", yesno[self.get_information("catacondensed")])
    self.add_data ("Coronoid", yesno[self.get_information("coronoid")])
    self.add_data ("Coronenoid", yesno[self.get_information("coronenoid")])
    self.add_data ("Symmetry 2D", self.get_information("symmetry2D"))
    self.add_data ("Symmetry 3D", self.get_information("symmetry3D"))
    self.add_data ("#Kekulé structures", self.get_information("kekule"))
    self.add_data ("Clar number", self.get_information("clarNumber"))
    self.add_data ("HOMO", self.get_information("homo"))
    self.add_data ("LUMO", self.get_information("lumo"))
    self.add_data ("Gap", self.get_information("lumo") - self.get_information("homo"))
    self.add_data ("Total energy", self.get_information("finalEnergy"))
    self.add_data ("Zero point energy", self.get_information("zeroPointEnergy"))
    self.add_data ("Dipole moment", self.get_information("moment"))
    self.add_data ("Planar", yesno[self.get_information("planar")])
