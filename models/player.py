from dataclasses import dataclass
from models.model_helpers import filter_data

TABLE_EMBED_STR = "{player}\t{row}"

@dataclass
class Player:
  ai: int
  alias: str
  avatar: int
  tech:	dict
  total_economy:	int
  total_fleets:	int
  total_industry:	int
  total_science:	int
  total_stars:	int
  total_strength:	int
  tech: dict

  @classmethod
  def build_from_player_data(cls, player_data):
    return cls(**filter_data(cls, player_data))

  @classmethod
  def format_table_cell(cls, data, display_len=5):
    data_str = str(data)
    padding = display_len - len(data_str)

    if padding > 0:
      return data_str + ' ' * padding
    elif padding < 0:
      return data_str[:display_len]

    return data_str

  @classmethod
  def progress_display_headers(cls):
    return [
      "Alias", "Economy", "Fleets", "Industry", "Science", "Stars", "Strength"
    ]

  @classmethod
  def technology_display_headers(cls):
    return [
      "Alias", "Scanning", "Hyperspace", "Terraforming", "Experimentation",
      "Weapons", "Banking", "Manufacturing",
    ]

  def progress_values(self):
    return [
      self.total_economy,
      self.total_fleets,
      self.total_industry,
      self.total_science,
      self.total_stars,
      self.total_strength
    ]

  def progress_display(self):
    return TABLE_EMBED_STR.format(
        player=Player.format_table_cell(self.alias, 5),
        row="\t".join([Player.format_table_cell(v) for v in self.progress_values()])
    )

  def technology_values(self):
    return [
      self.tech['scanning']['level'],
      self.tech['propulsion']['level'],
      self.tech['terraforming']['level'],
      self.tech['research']['level'],
      self.tech['weapons']['level'],
      self.tech['banking']['level'],
      self.tech['manufacturing']['level'],
    ]

  def technology_display(self):
    # print(self.tech)

    return TABLE_EMBED_STR.format(
      player=Player.format_table_cell(self.alias, 5),
      row="\t".join([Player.format_table_cell(v, 4) for v in self.technology_values()])
    )
