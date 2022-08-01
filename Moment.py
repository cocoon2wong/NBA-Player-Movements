"""
@Author: Conghao Wong
@Date: 2022-07-22 10:29:36
@LastEditors: Conghao Wong
@LastEditTime: 2022-07-22 11:23:57
@Description: file content
@Github: https://github.com/cocoon2wong
@Copyright 2022 Conghao Wong, All Rights Reserved.
"""

from Ball import Ball
from Player import Player


class Moment():
    """
    A class for keeping info about the moments
    """

    def __init__(self, quarter: int,
                 game_clock: float,
                 shot_clock: float,
                 ball_positions: list[float],
                 players_positions: list[float]):

        self.quarter = quarter
        self.game_clock = game_clock
        self.shot_clock = shot_clock

        self.ball = Ball(x=ball_positions[2],
                         y=ball_positions[3],
                         radius=ball_positions[4])

        self.players = [Player(team_id=player[0],
                               player_id=player[1],
                               x=player[2],
                               y=player[3]) for player in players_positions]
