from audioop import reverse
from dataclasses import dataclass

from models.player import Player
from models.star import Star
from models.fleet import Fleet


@dataclass
class Scan:
  fleets: dict
  stars: dict
  players: dict

  @classmethod
  def build_from_scan_data(cls, scan_data):
    return cls(
      fleets=[
        Fleet.build_from_fleet_data(fleet_data)
        for fleet_data in scan_data['fleets'].values()
      ],
      stars=[
        Star.build_from_star_data(star_data)
        for star_data in scan_data['stars'].values()
      ],
      players=[
        Player.build_from_player_data(player_data)
        for player_data in scan_data['players'].values()
      ]
    )

  def players_by_strength(self):
    return sorted(self.players, key=lambda p: p.total_strength, reverse=True)

  def players_by_total_tech(self):
    return sorted(self.players, key=lambda p: sum(p.technology_values()), reverse=True)
