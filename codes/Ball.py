"""
@Author: Conghao Wong
@Date: 2022-07-22 10:29:26
@LastEditors: Conghao Wong
@LastEditTime: 2022-07-22 11:18:27
@Description: file content
@Github: https://github.com/cocoon2wong
@Copyright 2022 Conghao Wong, All Rights Reserved.
"""

class Ball():
    """
    A class for keeping info about the balls
    """

    def __init__(self, x:float, y:float, radius:float):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = '#ff8c00'  # Hardcoded orange
