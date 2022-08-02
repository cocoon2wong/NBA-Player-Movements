"""
@Author: Conghao Wong
@Date: 2022-07-22 10:29:36
@LastEditors: Conghao Wong
@LastEditTime: 2022-08-02 11:08:39
@Description: file content
@Github: https://github.com/cocoon2wong
@Copyright 2022 Conghao Wong, All Rights Reserved.
"""

import argparse

from codes import Game

parser = argparse.ArgumentParser(description='Process arguments about an NBA game.')
parser.add_argument('--path', type=str,
                    help='a path to json file to read the events from',
                    required = True)
parser.add_argument('--event', type=int, default=0,
                    help="""an index of the event to create the animation to
                            (the indexing start with zero, if you index goes beyond out
                            the total number of events (plays), it will show you the last
                            one of the game)""")

args = parser.parse_args()

game = Game(path_to_json=args.path)
game.update(event_index=args.event)
game.start()
