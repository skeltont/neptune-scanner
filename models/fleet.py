from dataclasses import dataclass
from models.model_helpers import filter_data


@dataclass
class Fleet:
  n: str
  st: int
  x: str
  y: str

  @classmethod
  def build_from_fleet_data(cls, fleet_data):
    return cls(**filter_data(cls, fleet_data))
