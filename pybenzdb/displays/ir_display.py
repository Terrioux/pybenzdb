from matplotlib import pyplot as plt
from pybenzdb.displays.display import Display
import base64
import IPython as ip
import ipywidgets as w


class IR_Display (Display):
  """ This class allows for displaying benzenoid information from IR query. """

  def __init__ (self, info: dict) -> None:
    """ Initializes the display tool with the provided information

        Args:
          info (dict): The information about the considered benzenoid
    """
    super().__init__(info)
    self.add_data ("Final energy", self.get_information("finalEnergy"))
    self.add_data ("Zero Point Energy", self.get_information("zeroPointEnergy"))


  def __download_button(self, label: str, filename: str, data: str) -> None:
    """ displays a download button with the given label that saves the given data in the desired filename as an image

        Args:
          label (str): The label of the button
          filename (str): The name of the file in which to save the data
          data (str): The data to download
    """
    # we encode the data
    encoded_data = base64.b64encode(data.encode()).decode()

    # we create the download button
    button = '''<html>
      <body>
      <a download="''' + filename + '''" href="data:text/''' + filename.split(".")[1] + ''';base64,''' + encoded_data + '''">
      <button class="p-Widget jupyter-widgets jupyter-button widget-button mod-warning">Download ''' + label + ''' file</button>
      </a>
      </body>
      </html>
      '''

    ip.display.display(w.HTML(button))


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
    self.__download_button("AMES", "ames.xml", self.get_information("amesFormat"))
