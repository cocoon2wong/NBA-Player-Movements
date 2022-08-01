"""
@Author: Conghao Wong
@Date: 2022-07-22 10:29:36
@LastEditors: Conghao Wong
@LastEditTime: 2022-08-01 19:26:29
@Description: file content
@Github: https://github.com/cocoon2wong
@Copyright 2022 Conghao Wong, All Rights Reserved.
"""

from .Team import Team


class Player():
    """
    A class for keeping info about the players
    """

    def __init__(self, team_id: int, player_id,
                 x: float, y: float):

        self.team = Team(team_id)
        self.id = player_id
        self.x = x
        self.y = y
        self.color = self.team.color
