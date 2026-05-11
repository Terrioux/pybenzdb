class View_Criterion (Criterion):
  """ This class allows for representing the desired view """

  def __init__ (self, key: str, description: str):
    """ initializes the criterion """
    super().__init__(key, description)

    self.__element =  w.Select(description=self.get_description(), options=["global","one by one"], value='global', rows=1, layout={"width": "auto"})

    self.set_widget(w.HBox([self.__element]))


  def get_criterion (self) -> str:
    """ returns the JSON string corresponding to the criterion, an empty string if the criterion is not set """
    return str(self.__element.value)