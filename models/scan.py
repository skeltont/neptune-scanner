from audioop import reverse
from dataclasses import dataclass

from models.player import Player
from models.star import Star
from models.fleet import Fleet

THREAT_MESSAGE_ROW = "Incoming bogey detected: {alias} -> {star}, strength: {ships}"
THREAT_MESSAGE = "```{message}```"

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

  def player_by_fleet(self, fleet):
    for player in self.players:
      if fleet.puid == player.uid:
        return player

    return None

  def star_by_id(self, star_id):
    for star in self.stars:
      if star.uid == star_id:
        return star

    return None

  def player_by_alias(self, alias):
    for player in self.players:
      if player.alias == alias:
        return player

    return None

  def threat_scan(self, owner):
    threats = list()

    for fleet in self.fleets:
      player = self.player_by_fleet(fleet)

      if owner.uid == player.uid:
        continue

      for order in fleet.o:
        star = self.star_by_id(order[1])

        if star.puid == owner.uid:
          threats.append(THREAT_MESSAGE_ROW.format(
            alias=player.alias,
            star=star.n,
            ships=fleet.st
          ))

    if threats:
      return THREAT_MESSAGE.format(message="\n".join(threats))
    else:
      return None

