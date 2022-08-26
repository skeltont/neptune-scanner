from dataclasses import dataclass
from models.model_helpers import filter_data


@dataclass
class Star:
  e: int = -1
  i: int = -1
  s: int = -1

  @classmethod
  def build_from_star_data(cls, star_data):
    return cls(**filter_data(cls, star_data))
