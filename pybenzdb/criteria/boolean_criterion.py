class Boolean_Criterion (Criterion):
  """ This class allows for representing criterions based on Boolean value """

  def __init__ (self, key: str, description: str):
    """ initializes the criterion """
    super().__init__(key, description)

    self.__element =  w.BoundedIntText(value=1, min=0, max=1, layout={"width": "3.5em"})
    self.__condition = w.Select(description=self.get_description(), options=["not set","="], value='not set', rows=1)#, style={"description width": "8em"})

    self.__element.layout.width = "3em"
    self.__condition.layout.width = "15em"
    self.__condition.style.description_width = "10em"

    self.set_widget(w.HBox([self.__condition, self.__element]))


  def get_criterion (self) -> str:
    """ returns the JSON string corresponding to the criterion, an empty string if the criterion is not set """
    if self.__condition.value == "not set":
      return ""
    else:
      return '"' + self.get_key() + '": "' + self.__condition.value + " " + str(self.__element.value) + '"'
