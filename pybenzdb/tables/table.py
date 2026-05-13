import IPython as ip
import pandas as pd


class Table:
  """ This class allows for displaying a table containing benzenoid information.

      Attributes:
         data (dict): the data that will be displayed as a table
  """

  def __init__ (self) -> None:
    """ Initializes the display tool """
    self.__data = {}


  def add_data (self, label, value) -> None:
    """ Adds a label to display with its corresponding value

        Args:
          label (str): The label we want to add
          value (str): The value related to the label
    """
    if label not in self.__data:
      self.__data[label] = []
    self.__data [label] += [value]


  def add_row (self, info: dict) -> None:
    """ Adds a row based on the given information """
    self.add_data ("Benzenoid id", info["idBenzenoid"])
    self.add_data ("InChI", info["inchi"])
    self.add_data ("SMILES", info["smiles"])
    self.add_data ("SELFIES", info["selfies"])
    self.add_data ("Label", info["label"])
    self.add_data ("#hexagons", info["nbHexagons"])
    self.add_data ("#carbons", info["nbCarbons"])
    self.add_data ("#hydrogens", info["nbHydrogens"])
    self.add_data ("Weight", info["weight"])
    self.add_data ("Irregularity", info["irregularity"])
    self.add_data ("Diameter", info["diameter"])


  def print (self) -> None:
    """ Prints the table """
    self.__df = pd.DataFrame(self.__data)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    ip.display.display(self.__df)


  def save (self, filename) -> None:
    """ Saves the data as a xlsx file whose name is filename

        Args:
          filename (str): The filename to save the data to
    """
    df = pd.DataFrame(self.__data)
    with pd.ExcelWriter(filename) as writer:
      df.to_excel(writer,sheet_name="result",index=False, header=True)

      # format definitions
      workbook  = writer.book
      format_column_title = workbook.add_format({'num_format': '@', 'align': 'center', 'bold': True})
      sheet = writer.sheets["result"]
      sheet.set_row(0, None,format_column_title)
      sheet.freeze_panes(0, 1)
      sheet.autofit()
