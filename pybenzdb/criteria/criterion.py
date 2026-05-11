from ipywidgets import Widget

class Criterion:
  """ This class allows for representing criteria

      Attributes:
        key (str): The key describing the criterion
        description (str): The description of the criterion
  """

  def __init__ (self, key: str, description: str) -> None:
    """ initializes the criterion

        Args:
          key (str): The key describing the criterion
          description (str): The description of the criterion

        Returns:
          None
    """
    self.__key = key
    self.__description  = description


  def display (self) -> None:
    """ displays the widget corresponding to the criterion

      Returns:
        None
    """
    pass


  def get_criterion (self) -> str:
    """ returns the JSON string corresponding to the criterion, or an empty string if the criterion is not set

        Returns:
          str: The JSON string corresponding to the criterion or an empty string if the criterion is not set
    """
    pass


  def get_description (self) -> str:
    """ returns the description """
    return self.__description


  def get_key (self) -> str:
    """ returns the key related to the criterion """
    return self.__key


  def set_widget (self, w: Widget) -> None:
    """ sets the widget related to the criterion """
    self.__widget = w


  def get_widget (self) -> Widget:
    """ returns the widget related to the criterion """
    """Description du module.

    :param param1: Description du paramètre 1.
    :type param1: int
    :param param2: Description du paramètre 2.
    :type param2: str
    :returns: Description de la valeur de retour.
    :rtype: bool
    """
    return self.__widget
