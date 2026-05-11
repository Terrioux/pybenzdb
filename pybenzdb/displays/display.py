class Display:
  """ This class allows for displaying benzenoid information """

  def __init__ (self, info: dict):
    """ initializes the display tool """
    self.__information = info
    self.__data = {}
    self.add_data ("Benzenoid id", seldf.get_information("idBenzenoid"))
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
    """ adds a label to display with its corresponding value """
    self.__data [label] = [value]


  def display (self) -> None:
    """ displays the information """
    self.__df = pd.DataFrame(self.__data)
    self.__df.index = [""]

    ip.display.display(self.__df.transpose())
    self.display_molecule()


  def display_molecule (self) -> None:
    """ displays the molecule thanks to Jsmol """
    view = Jsmol.JsmolView.from_str(str(self.get_information("nbCarbons")+self.get_information("nbHydrogens"))+"\nComment\n"+self.get_information("geometry"))
    ip.display.display(view)


  def display_image (self, str64: str) -> None:
    """ displays the base-64 image defined by str64 """
    img = Image.open(io.BytesIO(base64.b64decode(str64)))
    ip.display.display(img)


  def get_information (self, key) -> dict:
    """ returns the information """
    return self.__information[key]
