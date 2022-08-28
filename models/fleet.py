from dataclasses import dataclass
from models.model_helpers import filter_data


@dataclass
class Fleet:
  n: str      # fleet name
  st: int     # fleet strength (number of ships)
  x: str      # fleet x coord
  y: str      # fleet y coord
  o: list     # fleet orders (list of lists)
  puid: int   # player owner id

  @classmethod
  def build_from_fleet_data(cls, fleet_data):
    return cls(**filter_data(cls, fleet_data))
