import ipywidgets as w
import IPython as ip
import base64
from pybenzdb.tables.table import Table


class Download_Button:
  """ This class manages download buttons for several types of data.
  """

  def __init__ (self, label: str, filename: str, data: str | Table) -> None:
    """ displays a download button with the given label that saves the given data in the desired filename as an image
  
        Args:
          label (str): The label of the button
          filename (str): The name of the file in which to save the data
          data (str|Table): The data to download
    """
    # we encode the data
    if type(data) is str:
      encoded_data = base64.b64encode(data.encode()).decode()
    elif type(data) is Table:
      encoded_data = base64.b64encode(data.save()).decode()
    else:
      raise ValueError("The data to save has a bad type")

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