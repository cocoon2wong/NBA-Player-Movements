"""
@Author: Conghao Wong
@Date: 2022-07-22 10:29:36
@LastEditors: Conghao Wong
@LastEditTime: 2022-08-01 19:26:05
@Description: file content
@Github: https://github.com/cocoon2wong
@Copyright 2022 Conghao Wong, All Rights Reserved.
"""

import pandas as pd

from .Event import Event
from .Team import Team


class EventError(ValueError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Game():
    """
    A class for keeping info about the games
    """

    def __init__(self, path_to_json: str):
        # self.events = None
        self.home_team = None
        self.guest_team = None
        self.event = None

        try:
            self.game_name = path_to_json.split('/')[-1].split('.json')[0]
        except:
            self.game_name = None

        self.data_frame = pd.read_json(path_to_json)
        self.last_default_index = len(self.data_frame) - 1

    def update(self, event_index: int):
        if event_index > self.last_default_index:
            raise EventError

        event_index = min(event_index, self.last_default_index)
        self.event_index = event_index

        event = self.data_frame['events'][event_index]
        self.event = Event(event)
        self.home_team = Team(event['home']['teamid'])
        self.guest_team = Team(event['visitor']['teamid'])

        return self

    def start(self):
        self.event.show()
