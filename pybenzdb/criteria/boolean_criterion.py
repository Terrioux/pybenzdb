from pybenzdb.criteria.criterion import Criterion


class Boolean_Criterion (Criterion):
  """ This class allows for representing criteria based on Boolean value.

      Attributes:
        element (Widget): The widget used for selecting a value among the given list of values
        condition (Select): The widget used for selecting the operator
  """

  def __init__ (self, key: str, description: str):
    """ Initializes the criterion

        Args:
          key (str): The key describing the criterion
          description (str): The description of the criterion
    """
    super().__init__(key, description)

    self.__element =  w.BoundedIntText(value=1, min=0, max=1, layout={"width": "3.5em"})
    self.__condition = w.Select(description=self.get_description(), options=["not set","="], value='not set', rows=1)#, style={"description width": "8em"})

    self.__element.layout.width = "3em"
    self.__condition.layout.width = "15em"
    self.__condition.style.description_width = "10em"

    self.set_widget(w.HBox([self.__condition, self.__element]))


  def get_criterion (self) -> str:
    """ Returns the JSON string corresponding to the criterion, or an empty string if the criterion is not set

        Returns:
          str: The JSON string corresponding to the criterion or an empty string if the criterion is not set
    """
    if self.__condition.value == "not set":
      return ""
    else:
      return '"' + self.get_key() + '": "' + self.__condition.value + " " + str(self.__element.value) + '"'
