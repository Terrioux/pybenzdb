class Int_Criterion (Criterion):
  """ This class allows for representing criteria based on a single int value

       Attributes:
         element (Selection): the selection widget for  the criterion is related
         condition (str): The condition used for the criterion
   """
  def __init__ (self, key: str, description: str, min_value: int, max_value: int) -> None:
    """ initializes the criterion
      Args:
        key (str): The key describing the criterion
        description (str): The description of the criterion
        min_value (int): The minimum value for the criterion
        max_value (int): The maximum value for the criterion

      Returns:
        None
    """
    super().__init__(key, description)

    self.__element =  w.BoundedIntText(value=min_value, min=min_value, max=max_value)
    self.__condition = w.Select(description=self.get_description(), options=["not set","=","<>","<=","<",">",">="], value='not set', rows=1, layout={"width": "auto"})

    self.__element.layout.width = "5em"
    self.__condition.layout.width = "13em"

    self.set_widget(w.HBox([self.__condition, self.__element]))


  def get_criterion (self) -> str:
    """ returns the JSON string corresponding to the criterion, an empty string if the criterion is not set

        Returns:
          str: The JSON string corresponding to the criterion or an empty string if the criterion is not set
    """
    if self.__condition.value == "not set":
      return ""
    else:
      return '"' + self.get_key() + '": "' + self.__condition.value + " " + str(self.__element.value) + '"'
