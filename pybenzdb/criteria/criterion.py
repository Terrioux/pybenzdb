from ipywidgets import Widget

class Criterion:
  """ This class allows for representing criteria

      Attributes:
        key (str): The key describing the criterion
        description (str): The description of the criterion
  """

  def __init__ (self, key: str, description: str) -> None:
    """ Initializes the criterion

        Args:
          key (str): The key describing the criterion
          description (str): The description of the criterion
    """
    self.__key = key
    self.__description  = description


  def display (self) -> None:
    """ Displays the widget corresponding to the criterion
    """
    pass


  def get_criterion (self) -> str:
    """ Returns the JSON string corresponding to the criterion, or an empty string if the criterion is not set

        Returns:
          str: The JSON string corresponding to the criterion or an empty string if the criterion is not set
    """
    pass


  def get_description (self) -> str:
    """ Returns the description of the criterion

        Returns:
          str: The description of the criterion
    """
    return self.__description


  def get_key (self) -> str:
    """ Returns the key related to the criterion

        Returns:
          str: The key related to the criterion
    """
    return self.__key


  def set_widget (self, w: Widget) -> None:
    """ Sets the widget related to the criterion """
    self.__widget = w


  def get_widget (self) -> Widget:
    """ Returns the widget related to the criterion

        Returns:
          str: The widget related to the criterion
    """
    return self.__widget
