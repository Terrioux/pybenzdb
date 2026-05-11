class Item_Criterion (Criterion):
  """ This class allows for representing criterions based on list of values """

  def __init__ (self, key: str, description: str, values: list):
    """ initializes the criterion """
    super().__init__(key, description)

    self.__element =  w.Select(options=values, description="", disabled=False,rows=1)
    self.__condition = w.Select(description=self.get_description(), options=["not set","=","<>"], value='not set', rows=1)

    self.__element.layout.width = "5em"
    self.__condition.layout.width = "13em"

    self.set_widget(w.HBox([self.__condition, self.__element]))


  def get_criterion (self) -> str:
    """ returns the JSON string corresponding to the criterion, an empty string if the criterion is not set """
    if self.__condition.value == "not set":
      return ""
    else:
      return '"' + self.get_key() + '": "' + self.__condition.value + " " + str(self.__element.value) + '"'
