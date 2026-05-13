from pybenzdb.tables.table import Table


class Properties_Table (Table):
  """ This class allows for displaying a table containing benzenoid information from properties query. """

  def add_row (self, info: dict) -> None:
    """ Adds a row based on the given information

        Args:
          info (dict): The information about the considered benzenoid
    """
    super().add_row (info)

    yesno = ["no","yes"]
    self.add_data ("Catacondensed", yesno[info["catacondensed"]])
    self.add_data ("Coronoid", yesno[info["coronoid"]])
    self.add_data ("Coronenoid", yesno[info["coronenoid"]])
    self.add_data ("Symmetry 2D", info["symmetry2D"])
    self.add_data ("Symmetry 3D", info["symmetry3D"])
    self.add_data ("#Kekulé structures", info["kekule"])
    self.add_data ("Clar number", info["clarNumber"])
    self.add_data ("HOMO", info["homo"])
    self.add_data ("LUMO", info["lumo"])
    self.add_data ("Gap", info["lumo"]-info["homo"])
    self.add_data ("Total energy", info["finalEnergy"])
    self.add_data ("Zero point energy", info["zeroPointEnergy"])
    self.add_data ("Dipole moment", info["moment"])
    self.add_data ("Planar", yesno[info["planar"]])
