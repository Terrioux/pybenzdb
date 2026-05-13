import IPython as ip
import jupyter_jsmol as Jsmol
import pandas as pd
import base64
import io
from PIL import Image

class Display:
  """ This class allows for displaying the information of a given benzenoid.

      Attributes:
        information (dict): The information about a given benzenoid
        data (dict): The dictionary containing the information
  """

  def __init__ (self, info: dict) -> None:
    """ Initializes the display tool with the provided information

        Args:
          info (str): The information about the considered benzenoid
    """
    self.__information = info
    self.__data = {}
    self.add_data ("Benzenoid id", self.get_information("idBenzenoid"))
    self.add_data ("InChI", self.get_information("inchi"))
    self.add_data ("SMILES", self.get_information("smiles"))
    self.add_data ("SELFIES", self.get_information("selfies"))
    self.add_data ("Label", self.get_information("label"))
    self.add_data ("#hexagons", self.get_information("nbHexagons"))
    self.add_data ("#carbons", self.get_information("nbCarbons"))
    self.add_data ("#hydrogens", self.get_information("nbHydrogens"))
    self.add_data ("Weight", self.get_information("weight"))
    self.add_data ("Irregularity", self.get_information("irregularity"))
    self.add_data ("Diameter", self.get_information("diameter"))


  def add_data (self, label, value) -> None:
    """ Adds a label to display with its corresponding value

        Args:
          label (str): The label we want to add
          value (str): The value related to the label
    """
    self.__data [label] = [value]


  def display (self) -> None:
    """ Displays the information """
    self.__df = pd.DataFrame(self.__data)
    self.__df.index = [""]

    ip.display.display(self.__df.transpose())
    self.display_molecule()


  def display_molecule (self) -> None:
    """ Displays the molecule thanks to Jsmol """
    view = Jsmol.JsmolView.from_str(str(self.get_information("nbCarbons")+self.get_information("nbHydrogens"))+"\nComment\n"+self.get_information("geometry"))
    ip.display.display(view)


  def display_image (self, str64: str) -> None:
    """ Displays the base-64 image defined by str64 
    
        Args:
          str64 (str): The base-64 image to display
    """
    img = Image.open(io.BytesIO(base64.b64decode(str64)))
    ip.display.display(img)


  def get_information (self, key) -> dict:
    """ Returns the information related to the given key

        Args:
           key (str): The key of the information we want to get
    """
    return self.__information[key]
