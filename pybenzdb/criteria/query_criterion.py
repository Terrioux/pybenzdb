from pybenzdb.criteria.criterion import Criterion


class Query_Criterion (Criterion):
  """ This class allows for representing the desired query.

      Attributes:
        element (Select): The widget used for selecting the desired query
  """

  def __init__ (self, key: str, description: str):
    """ Initializes the criterion

        Args:
          key (str): The key describing the criterion
          description (str): The description of the criterion
    """
    super().__init__(key, description)

    self.__element =  w.Select(description=self.get_description(), options=["benzenoids","ir","ims2d1a","nics","clar_covers","properties","irregularities","patterns"], value='benzenoids', rows=1, layout={"width": "auto"})

    self.set_widget(w.HBox([self.__element]))


  def get_criterion (self) -> str:
    """ Returns the JSON string corresponding to the criterion, or an empty string if the criterion is not set

        Returns:
          str: The JSON string corresponding to the criterion or an empty string if the criterion is not set
    """
    return str(self.__element.value)
