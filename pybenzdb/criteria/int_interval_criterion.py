from pybenzdb.criteria.criterion import Criterion
import ipywidgets as w


class Int_Interval_Criterion (Criterion):
  """ This class allows for representing criteria based on interval of int values.

      Attributes:
        condition (Select): The widget used for selecting the operator
  """

  def __init__ (self, key: str, description: str, min_value: int, max_value: int):
    """ Initializes the criterion

        Args:
          min_value (int): The lower bound of the interval used for the criterion
          max_value (int): The upper bound of the interval used for the criterion
    """
    super().__init__(key, description)

    self.__element1 =  w.BoundedIntText(value=min_value, min=min_value, max=max_value, layout={"width": "auto"})
    self.__element2 =  w.BoundedIntText(value=min_value, min=min_value, max=max_value, layout={"width": "auto"})
    self.__condition = w.Select(description=self.get_description(), options=["not set","in"], value='not set', rows=1, layout={"width": "auto"})

    self.__element1.layout.width = '5em'
    self.__element2.layout.width = '5em'
    self.__condition.layout.width = '12em'

    self.set_widget(w.HBox([self.__condition, self.__element1, self.__element2]))


  def get_criterion (self) -> str:
    """ Returns the JSON string corresponding to the criterion, or an empty string if the criterion is not set

        Returns:
          str: The JSON string corresponding to the criterion or an empty string if the criterion is not set
    """
    if self.__condition.value == "not set":
      return ""
    else:
      return '"' + self.get_key() + '": "IN ' + str(int(self.__element1.value)) + " " + str(int(self.__element2.value)) + '"'
