from dataclasses import dataclass
from models.model_helpers import filter_data


@dataclass
class Star:
  uid: int
  puid: int     # player owner id
  n: str        # star name
  e: int = -1   # economy
  i: int = -1   # industry
  s: int = -1   # science

  @classmethod
  def build_from_star_data(cls, star_data):
    return cls(**filter_data(cls, star_data))
