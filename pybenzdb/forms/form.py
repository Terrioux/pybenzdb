import ipywidgets as w
import requests
import json

from pybenzdb.criteria.criterion import Criterion
from pybenzdb.criteria.boolean_criterion import Boolean_Criterion
from pybenzdb.criteria.float_criterion import Float_Criterion
from pybenzdb.criteria.int_criterion import Int_Criterion
from pybenzdb.criteria.int_interval_criterion import Int_Interval_Criterion
from pybenzdb.criteria.float_interval_criterion import Float_Interval_Criterion
from pybenzdb.criteria.item_criterion import Item_Criterion
from pybenzdb.criteria.query_criterion import Query_Criterion
from pybenzdb.criteria.string_criterion import String_Criterion
from pybenzdb.criteria.view_criterion import View_Criterion

from pybenzdb.tables.table import Table
from pybenzdb.tables.ir_table import IR_Table
from pybenzdb.tables.irregularities_table import Irregularities_Table
from pybenzdb.tables.properties_table import Properties_Table
from pybenzdb.tables.patterns_table import Patterns_Table

from pybenzdb.displays.display import Display
from pybenzdb.displays.clar_covers_display import Clar_Covers_Display
from pybenzdb.displays.ims2d1a_display import IMS2D1A_Display
from pybenzdb.displays.ir_display import IR_Display
from pybenzdb.displays.irregularities_display import Irregularities_Display
from pybenzdb.displays.patterns_display import Patterns_Display
from pybenzdb.displays.properties_display import Properties_Display
from pybenzdb.displays.nics_display import NICS_Display

import IPython as ip
import base64


class Form:
  """ This class manages a form that allows for querying the BenzDB database. """

  def __init__ (self):
    """ Initializes the form """
    self.__query = None         # the query
    self.__demand_type = None   # the type of demand
    self.__json_string = None   # the query as a JSON string
    self.__data = None          # the data related to the query (if the query succeeds)

    self.create_form()


  def create_form(self) -> None:
    """ Creates the form allowing for choosing the values of desired criteria """
    self.__criteria = []

    # criteria about basic information
    self.__criteria.append (Int_Criterion(key="idBenzenoid", description="BenzDB id", min_value=0, max_value=8391))
    self.__criteria.append (String_Criterion(key="inchi", description="InChI"))
    self.__criteria.append (String_Criterion(key="label", description="BenzAI label"))

    self.__criteria.append (Int_Criterion(key="nbHexagons", description="# hexagons", min_value=1, max_value=9))
    self.__criteria.append (Int_Criterion(key="nbCarbons", description="# carbons", min_value=6, max_value=38))
    self.__criteria.append (Int_Criterion(key="nbHydrogens", description="# hydrogens", min_value=6, max_value=22))

    self.__criteria.append (Int_Criterion(key="solo", description="# solo", min_value=0, max_value=14))
    self.__criteria.append (Int_Criterion(key="duo", description="# duo", min_value=0, max_value=14))
    self.__criteria.append (Int_Criterion(key="trio", description="# trio", min_value=0, max_value=18))
    self.__criteria.append (Int_Criterion(key="quartet", description="# quartet", min_value=0, max_value=20))
    self.__criteria.append (Float_Criterion(key="irregularity", description="Irregularity", min_value=0, max_value=1))

    self.__criteria.append (Int_Criterion(key="kekule", description="# structures", min_value=0, max_value=110))
    self.__criteria.append (Int_Criterion(key="clarNumber", description="Clar number", min_value=0, max_value=6))

    self.__criteria.append (Boolean_Criterion(key="catacondensed", description="Is catacondensed"))
    self.__criteria.append (Boolean_Criterion(key="coronenoid", description="Is coronenoid"))
    self.__criteria.append (Boolean_Criterion(key="coronoid", description="Is coronoid"))
    self.__criteria.append (Boolean_Criterion(key="planar", description="Is planar"))
    self.__criteria.append (Int_Criterion(key="diameter", description="Diameter", min_value=0, max_value=8))

    self.__criteria.append (Float_Interval_Criterion(key="frequency", description="Frequency", min_value=0, max_value=3466))
    self.__criteria.append (Float_Interval_Criterion(key="intensity", description="Intensity", min_value=0, max_value=2742))

    self.__criteria.append (Item_Criterion(key="symmetry2D", description="Symmetry 2D", values=["Cs","C2hi","C2hii","C3hi","C3hii","C2va","C2vb","D2hi","D2hii","D3hia","D3hii","D6h"]))
    self.__criteria.append (Item_Criterion(key="symmetry3D", description="Symmetry 3D", values=["C1","Ci","Cs","C2","C2v","C2h","C3","C3h","D2","D2h","D3h","D6h"]))

    self.__criteria.append (Int_Interval_Criterion(key="cove", description="#coves", min_value=0, max_value=4))
    self.__criteria.append (Int_Interval_Criterion(key="fjord", description="#fjords", min_value=0, max_value=2))

    # definition of groups of widgets
    self.add_group ([self.__criteria[0:1],self.__criteria[1:3]], "Molecule identity")
    self.add_group ([self.__criteria[3:6]], "Basic features")
    self.add_group ([self.__criteria[6:10],self.__criteria[10:11]],"Irregularity features")
    self.add_group ([self.__criteria[11:13]],"Kekulé structures and Clar number")
    self.add_group ([self.__criteria[13:15],self.__criteria[15:18]],"Structural properties")
    self.add_group ([self.__criteria[18:20]],"IR features")
    self.add_group ([self.__criteria[20:22]],"Symmetry properties")
    self.add_group ([self.__criteria[22:24]],"Patterns")

    # query
    self.__criteria.append (Query_Criterion(key="query", description="query"))

    # type of view
    self.__criteria.append (View_Criterion(key="view", description="View type"))

    # validation buttons
    count_btn = w.Button (description="Count")
    count_btn.on_click (self.perform_query)

    getdata_btn = w.Button (description="Get Data")
    getdata_btn.on_click (self.perform_query)

    getquery_btn = w.Button (description="Get JSON Query")
    getquery_btn.on_click (self.perform_query)

    getresult_btn = w.Button (description="Get JSON Result")
    getresult_btn.on_click (self.perform_query)

    self.add_group([self.__criteria[24:26],[count_btn, getdata_btn, getquery_btn, getresult_btn]],"Query choices")


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


  def __download_button_xlsx(self, label: str, filename: str, data: list) -> None:
    """ displays a download button with the given label that saves the given data in the desired filename as a xlsx file

        Args:
          label (str): The label of the button
          filename (str): The name of the file in which to save the data
          data (str): The data to download
    """
    # we save the data
    data.save(filename)

    # we create the download button
    button = '''<html>
      <body>
      <a download="''' + filename + '''" href="''' + filename + '''">
      <button class="p-Widget jupyter-widgets jupyter-button widget-button mod-warning">Download ''' + label + ''' file</button>
      </a>
      </body>
      </html>
      '''

    ip.display.display(w.HTML(button))


  def __process(self) -> None:
    """ Processes the query and sets the corresponding attributes """
    demand_type = self.get_demand_type()

    if demand_type == "data":
      data = self.get_data()
      query = self.get_query()
      view = self.get_view()

      if view == "global":
        if query == "properties":
          d = Properties_Table()
          data = sorted(data, key=lambda t: (t["nbHexagons"], t["symmetry3D"], t["lumo"] - t["homo"]))
        elif query == "irregularities":
          d = Irregularities_Table()
        elif query == "ir":
          d = IR_Table()
        elif query == "patterns":
          d = Patterns_Table()
        else:
          d = Table()
        for molecule in data:
          d.add_row(molecule)

        self.__download_button_xlsx("XLSX", query + ".xlsx", d)
        d.print()
      elif view == "one by one":
        for molecule in data:
          if query == "benzenoids":
            d = Display(molecule)
          elif query == "ir":
            d = IR_Display(molecule)
          elif query == "ims2d1a":
            d = IMS2D1A_Display(molecule)
          elif query == "nics":
            d = NICS_Display(molecule)
          elif query == "clar_covers":
            d = Clar_Covers_Display(molecule)
          elif query == "properties":
            d = Properties_Display(molecule)
          elif query == "irregularities":
            d = Irregularities_Display(molecule)
          elif query == "patterns":
            d = Patterns_Display(molecule)
          d.display()

    elif demand_type == "count":
      print("Number of molecules:", self.get_data())

    elif demand_type == "json":
      self.__download_button("JSON", "query.json", self.get_json_string())
      print("JSON query:")
      print(self.get_json_string())

    elif demand_type == "result":
      self.__download_button("JSON", "result.json", str(self.get_data()).replace("'", '"'))
      print("JSON result (100,000 first characters):")
      print(str(self.get_data())[0:100_000].replace("'", '"'))


  def perform_query (self, btn: w.Button) -> None:
    """ Performs the query and sets the corresponding attributes

        Args:
          btn (Button): the button that specifies the query to perform
    """
    # we identify the type of demand
    if btn.description == "Count":
      self.__demand_type = "count"
    elif btn.description == "Get Data":
      self.__demand_type = "data"
    elif btn.description == "Get JSON Query":
      self.__demand_type = "json"
    elif btn.description == "Get JSON Result":
      self.__demand_type = "result"
    else:
      self.__demand_type = "unknown"

    # we build the JSON string
    self.__json_string = "{\n"
    for c in self.__criteria:
      if isinstance(c,Query_Criterion):
        self.__query = c.get_criterion()
      elif isinstance(c,View_Criterion):
        self.__view = c.get_criterion()
      else:
        s = c.get_criterion()
        if len(s) > 0:
          if len(self.__json_string) > 3:
            self.__json_string += ",\n"
          self.__json_string += "\t" + s
    self.__json_string += "\n}"

    if self.__demand_type in ["data", "result"]:
      response = requests.post("https://benzenoids.lis-lab.fr/find_"+self.__query, json= json.loads(self.__json_string))
    elif self.__demand_type == "count":
      response = requests.post("https://benzenoids.lis-lab.fr/count_"+self.__query, json= json.loads(self.__json_string))

    if self.__demand_type in ["data", "count", "result"]:
      if response.status_code == 200:
        self.__data = response.json()

    self.__process()


  def add_group (self, criteria:list, title: str) -> None:
    """ Defines a group of widgets from the given list of criteria

        Args:
          criteria (list): the list of criteria to add to the widget
          title (str): the title of the widget
    """
    title_box = w.HTML(value="<b>"+title+"</b>")
    display(title_box)

    for l in criteria:
      box = w.HBox([c.get_widget() if isinstance(c,Criterion) else c for c in l])
      display(box)


  def get_data (self) -> list:
    """ Returns the data related to the query

        Returns:
          list: The data related to the query
    """
    return self.__data


  def get_query (self):
    """ Returns the desired query """
    return self.__query


  def get_json_string (self) -> str:
    """ Returns the JSON string related to the desired query

        Returns:
          str: The JSON string related to the desired query
    """
    return self.__json_string


  def get_demand_type (self) -> str:
    """ Returns the type of the current demand

        Returns:
          str: The type of the current demand
    """
    return self.__demand_type


  def get_view (self) -> str:
    """ Returns the desired type of view

        Returns:
          str: The type of view
    """
    return self.__view

