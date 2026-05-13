from matplotlib import pyplot as plt
from pybenzdb.displays.display import Display


class IR_Display (Display):
  """ This class allows for displaying benzenoid information from IR query. """

  def __init__ (self, info: dict) -> None:
    """ Initializes the display tool with the provided information

        Args:
          info (str): The information about the considered benzenoid
    """
    super().__init__(info)
    self.add_data ("Final energy", self.get_information("finalEnergy"))
    self.add_data ("Zero Point Energy", self.get_information("zeroPointEnergy"))


  def display (self) -> None:
    """ Displays the information """
    super().display()

    x = [float(v) for v in self.get_information("frequencies").split(" ")]
    y = [float(v) for v in self.get_information("intensities").split(" ")]

    plt.cla()
    plt.stem(x, y, linefmt='-', markerfmt="")
    plt.xlabel('frequencies ($cm^{-1}$)')
    plt.ylabel('intensities ($km.mol^{-1}$)')
    plt.show()
    download_button("AMES", "ames.xml", self.get_information("amesFormat"))
