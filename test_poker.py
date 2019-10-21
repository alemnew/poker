#!/usr/bin/env python3
# encoding: utf-8

"""A test code for the simplified version of the poker game."""

# Copyright (c) 2019 Alemnew Sheferaw Asrese
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import unittest 
import poker

class TestPoker(unittest.TestCase):
    tie_cases = (('aaaqq', 'qqaaa'), 
                 ('53qq2', 'q53q2'),
                 ('53888', '88385'),
                 ('qqaaa', 'aaaqq'),
                 ('q53q2', '53qq2'),
                 ('88385', '53888'))

    first_win_cases = (('aaaqq', 'qqqaa'),
                       ('q53q4', '53qq2'),
                       ('53888', '88375'),
                       ('33337', 'qqaaa'),
                       ('22333', 'aaa58'),
                       ('33389', 'aakk4'),
                       ('44223', 'aa892'),
                       ('22456', 'akqjt'),
                       ('99977', '77799'),
                       ('99922', '88866'),
                       ('9922a', '9922k'),
                       ('99975', '99974'),
                       ('99975', '99965'),
                       ('99752', '99652'),
                       ('99752', '99742'),
                       ('99753', '99752'))

    second_win_cases = (('qqqaa', 'aaaqq'),
                        ('53qq2', 'q53q4'),
                        ('88375', '53888'),
                        ('qqaaa', '33337'),
                        ('aaa58', '22333'),
                        ('aakk4', '33389'),
                        ('aa892', '44223'),
                        ('akqjt', '22456'),
                        ('77799', '99977'),
                        ('88866', '99922'),
                        ('9922k', '9922A'),
                        ('99965', '99975'),
                        ('99652', '99752'),
                        ('99742', '99752'),
                        ('99752', '99753'))

    fail_cases = (('123', '45654'),
                  ('88889', 'aqj'),
                  ('', '34563'),
                  ('78023dsg', '89832'),
                  ('xyzak', 'kqatj'),
                  ('lmnop', 'vwxyz'),
                  ('a', '4'),
                  ('kkkk', 'jjjj'))
                    

    def test_who_wins(self):
        ''' who_wins should give 0, 1, 2, and -1 to represent It's at tie!,
        First hand wins!, Second hand wins!, and failure, respectively. 
        ''' 
        
        # test tie cases
        for hand_1, hand_2 in self.tie_cases:
            winner = poker.who_wins(hand_1.upper(), hand_2.upper())
            self.assertEqual(winner, 0)
        
        # test first hand wins cases
        for hand_1, hand_2 in self.first_win_cases:
            winner = poker.who_wins(hand_1.upper(), hand_2.upper())
            self.assertEqual(winner, 1)

        # test second hand wins cases
        for hand_1, hand_2 in self.second_win_cases:
            winner = poker.who_wins(hand_1.upper(), hand_2.upper())
            self.assertEqual(winner, 2)
        
        # test failure cases
        for hand_1, hand_2 in self.fail_cases: 
            #print('{} & {}'.format(hand_1, hand_2))
            winner = poker.who_wins(hand_1.upper(), hand_2.upper())
            self.assertEqual(winner, -1)

if __name__ == '__main__':
    unittest.main()


