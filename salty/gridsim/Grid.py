from enum import Enum

class Grid(object):
    
    __slots__ = ["_state", "_table"]
    
    def __init__(self):
        self._state = 165
    
    _table = [
        {   14: (1, 4),
            11: (2, 4),
            15: (0, 0),
        },
        {   10: (3, 8),
            14: (4, 8),
            13: (5, 8),
            15: (0, 0),
        },
        {   10: (3, 8),
            11: (6, 8),
            7: (7, 8),
            15: (0, 0),
        },
        {   10: (3, 8),
            6: (8, 12),
            14: (4, 8),
            9: (9, 12),
            11: (6, 8),
        },
        {   10: (3, 8),
            14: (4, 8),
            13: (5, 8),
            15: (10, 8),
        },
        {   12: (11, 9),
            14: (4, 8),
            9: (9, 12),
            13: (5, 8),
        },
        {   10: (3, 8),
            11: (6, 8),
            7: (7, 8),
            15: (10, 8),
        },
        {   6: (8, 12),
            3: (12, 12),
            11: (6, 8),
            7: (7, 8),
        },
        {   2: (13, 13),
            10: (3, 8),
            6: (8, 12),
            5: (14, 13),
            7: (7, 8),
        },
        {   8: (15, 13),
            10: (3, 8),
            9: (9, 12),
            5: (14, 13),
            13: (5, 8),
        },
        {   14: (4, 8),
            11: (6, 8),
            15: (10, 8),
        },
        {   8: (16, 10),
            12: (17, 10),
            13: (5, 8),
        },
        {   2: (13, 13),
            3: (12, 12),
            7: (7, 8),
        },
        {   2: (18, 14),
            6: (19, 14),
            1: (20, 12),
            3: (21, 14),
        },
        {   4: (22, 12),
            6: (19, 14),
            1: (20, 12),
            9: (23, 14),
            5: (24, 14),
        },
        {   8: (25, 14),
            4: (22, 12),
            12: (26, 14),
            9: (23, 14),
        },
        {   8: (16, 10),
            4: (27, 10),
            12: (26, 14),
            9: (23, 14),
        },
        {   8: (16, 10),
            12: (26, 14),
            13: (28, 10),
        },
        {   2: (29, 10),
            6: (19, 14),
            1: (30, 10),
            3: (21, 14),
        },
        {   2: (29, 10),
            10: (31, 15),
            6: (19, 14),
            5: (32, 10),
            7: (33, 15),
        },
        {   0: (34, 8),
            2: (13, 13),
            1: (20, 12),
            5: (14, 13),
        },
        {   2: (29, 10),
            3: (21, 14),
            7: (33, 15),
        },
        {   0: (34, 8),
            8: (15, 13),
            4: (22, 12),
            5: (14, 13),
        },
        {   8: (16, 10),
            10: (31, 15),
            9: (23, 14),
            5: (32, 10),
            13: (35, 15),
        },
        {   4: (27, 10),
            6: (19, 14),
            1: (30, 10),
            9: (23, 14),
            5: (32, 10),
        },
        {   8: (16, 10),
            4: (27, 10),
            12: (26, 14),
            9: (23, 14),
        },
        {   8: (16, 10),
            12: (26, 14),
            13: (35, 15),
        },
        {   0: (36, 10),
            8: (16, 10),
            4: (27, 10),
            5: (32, 10),
        },
        {   12: (26, 14),
            14: (37, 6),
            9: (23, 14),
            13: (28, 10),
        },
        {   2: (29, 10),
            6: (19, 14),
            1: (30, 10),
            3: (21, 14),
        },
        {   0: (36, 10),
            2: (29, 10),
            1: (30, 10),
            5: (32, 10),
        },
        {   10: (38, 15),
            6: (39, 14),
            14: (40, 11),
            9: (41, 14),
            11: (42, 14),
        },
        {   4: (27, 10),
            6: (19, 14),
            1: (30, 10),
            9: (23, 14),
            5: (32, 10),
        },
        {   6: (39, 14),
            3: (43, 14),
            11: (42, 14),
            7: (44, 14),
        },
        {   0: (34, 8),
            4: (22, 12),
            1: (20, 12),
        },
        {   12: (45, 14),
            14: (40, 11),
            9: (41, 14),
            13: (46, 11),
        },
        {   0: (36, 10),
            4: (27, 10),
            1: (30, 10),
        },
        {   10: (47, 2),
            14: (48, 2),
            13: (49, 2),
            15: (50, 2),
        },
        {   10: (38, 15),
            6: (39, 14),
            14: (40, 11),
            9: (41, 14),
            11: (42, 14),
        },
        {   2: (51, 10),
            10: (52, 13),
            6: (39, 14),
            5: (53, 10),
            7: (54, 10),
        },
        {   10: (55, 7),
            14: (40, 11),
            13: (56, 10),
            15: (57, 10),
        },
        {   8: (58, 10),
            10: (52, 13),
            9: (41, 14),
            5: (53, 10),
            13: (56, 10),
        },
        {   10: (52, 13),
            11: (42, 14),
            7: (54, 10),
            15: (57, 10),
        },
        {   2: (51, 10),
            3: (59, 10),
            7: (54, 10),
        },
        {   6: (39, 14),
            3: (59, 10),
            11: (42, 14),
            7: (54, 10),
        },
        {   8: (58, 10),
            12: (60, 10),
            13: (56, 10),
        },
        {   12: (60, 10),
            14: (40, 11),
            9: (61, 11),
            13: (56, 10),
        },
        {   10: (47, 2),
            6: (62, 3),
            14: (48, 2),
            9: (63, 6),
            11: (64, 2),
        },
        {   10: (47, 2),
            14: (48, 2),
            13: (49, 2),
            15: (50, 2),
        },
        {   12: (65, 6),
            14: (48, 2),
            9: (63, 6),
            13: (49, 2),
        },
        {   14: (48, 2),
            11: (64, 2),
            15: (50, 2),
        },
        {   2: (51, 10),
            6: (66, 9),
            1: (67, 10),
            3: (68, 6),
        },
        {   10: (69, 12),
            6: (70, 12),
            14: (71, 12),
            9: (72, 12),
            11: (73, 12),
        },
        {   4: (74, 10),
            6: (66, 9),
            1: (67, 10),
            9: (75, 6),
            5: (53, 10),
        },
        {   6: (66, 9),
            3: (68, 6),
            11: (76, 6),
            7: (54, 10),
        },
        {   10: (77, 3),
            6: (78, 3),
            14: (79, 6),
            9: (75, 6),
            11: (76, 6),
        },
        {   12: (80, 6),
            14: (79, 6),
            9: (75, 6),
            13: (56, 10),
        },
        {   14: (79, 6),
            11: (76, 6),
            15: (57, 10),
        },
        {   8: (58, 10),
            4: (74, 10),
            12: (80, 6),
            9: (75, 6),
        },
        {   2: (51, 10),
            3: (68, 6),
            7: (54, 10),
        },
        {   8: (58, 10),
            12: (80, 6),
            13: (56, 10),
        },
        {   8: (58, 10),
            10: (55, 7),
            9: (61, 11),
            5: (53, 10),
            13: (56, 10),
        },
        {   2: (81, 7),
            10: (47, 2),
            6: (62, 3),
            5: (82, 7),
            7: (83, 2),
        },
        {   8: (16, 10),
            10: (47, 2),
            9: (63, 6),
            5: (32, 10),
            13: (49, 2),
        },
        {   10: (47, 2),
            11: (64, 2),
            7: (83, 2),
            15: (50, 2),
        },
        {   8: (16, 10),
            12: (17, 10),
            13: (49, 2),
        },
        {   2: (84, 8),
            10: (85, 8),
            6: (86, 8),
            5: (87, 8),
            7: (88, 8),
        },
        {   0: (89, 10),
            2: (51, 10),
            1: (67, 10),
            5: (53, 10),
        },
        {   2: (51, 10),
            3: (68, 6),
            7: (90, 2),
        },
        {   10: (85, 8),
            6: (86, 8),
            14: (91, 8),
            9: (72, 12),
            11: (92, 8),
        },
        {   2: (84, 8),
            10: (85, 8),
            6: (86, 8),
            5: (87, 8),
            7: (88, 8),
        },
        {   10: (85, 8),
            14: (91, 8),
            13: (93, 8),
            15: (94, 8),
        },
        {   8: (95, 13),
            10: (85, 8),
            9: (72, 12),
            5: (87, 8),
            13: (93, 8),
        },
        {   10: (85, 8),
            11: (92, 8),
            7: (88, 8),
            15: (94, 8),
        },
        {   0: (89, 10),
            8: (58, 10),
            4: (74, 10),
            5: (53, 10),
        },
        {   8: (96, 2),
            10: (97, 2),
            9: (98, 2),
            5: (99, 2),
            13: (100, 2),
        },
        {   10: (97, 2),
            11: (101, 2),
            7: (90, 2),
            15: (102, 2),
        },
        {   10: (97, 2),
            6: (78, 3),
            14: (103, 2),
            9: (98, 2),
            11: (101, 2),
        },
        {   2: (104, 7),
            10: (97, 2),
            6: (78, 3),
            5: (99, 2),
            7: (90, 2),
        },
        {   10: (97, 2),
            14: (103, 2),
            13: (100, 2),
            15: (102, 2),
        },
        {   8: (96, 2),
            12: (105, 2),
            13: (100, 2),
        },
        {   2: (106, 11),
            6: (107, 11),
            1: (108, 6),
            3: (109, 11),
        },
        {   4: (110, 6),
            6: (107, 11),
            1: (108, 6),
            9: (111, 11),
            5: (112, 11),
        },
        {   6: (62, 3),
            3: (113, 6),
            11: (64, 2),
            7: (83, 2),
        },
        {   2: (84, 8),
            6: (86, 8),
            1: (114, 8),
            3: (115, 8),
        },
        {   10: (85, 8),
            6: (86, 8),
            14: (116, 4),
            9: (117, 4),
            11: (118, 4),
        },
        {   2: (84, 8),
            10: (85, 8),
            6: (86, 8),
            5: (87, 8),
            7: (88, 8),
        },
        {   4: (119, 12),
            6: (86, 8),
            1: (114, 8),
            9: (117, 4),
            5: (87, 8),
        },
        {   6: (86, 8),
            3: (115, 8),
            11: (118, 4),
            7: (88, 8),
        },
        {   0: (89, 10),
            4: (74, 10),
            1: (67, 10),
        },
        {   6: (120, 1),
            3: (68, 6),
            11: (121, 1),
            7: (90, 2),
        },
        {   10: (85, 8),
            14: (116, 4),
            13: (93, 8),
            15: (94, 8),
        },
        {   10: (85, 8),
            11: (118, 4),
            7: (88, 8),
            15: (94, 8),
        },
        {   12: (122, 4),
            14: (116, 4),
            9: (117, 4),
            13: (93, 8),
        },
        {   14: (91, 8),
            11: (92, 8),
            15: (94, 8),
        },
        {   8: (95, 13),
            4: (119, 12),
            12: (123, 9),
            9: (72, 12),
        },
        {   8: (96, 2),
            4: (124, 2),
            12: (105, 2),
            9: (98, 2),
        },
        {   10: (97, 2),
            6: (120, 1),
            14: (125, 1),
            9: (98, 2),
            11: (121, 1),
        },
        {   8: (96, 2),
            10: (97, 2),
            9: (98, 2),
            5: (99, 2),
            13: (100, 2),
        },
        {   4: (124, 2),
            6: (120, 1),
            1: (126, 6),
            9: (98, 2),
            5: (99, 2),
        },
        {   12: (105, 2),
            14: (125, 1),
            9: (98, 2),
            13: (100, 2),
        },
        {   10: (97, 2),
            11: (121, 1),
            7: (90, 2),
            15: (102, 2),
        },
        {   14: (103, 2),
            11: (101, 2),
            15: (102, 2),
        },
        {   10: (97, 2),
            14: (125, 1),
            13: (100, 2),
            15: (102, 2),
        },
        {   2: (104, 7),
            6: (78, 3),
            1: (126, 6),
            3: (68, 6),
        },
        {   8: (96, 2),
            12: (105, 2),
            13: (100, 2),
        },
        {   2: (29, 10),
            6: (107, 11),
            1: (30, 10),
            3: (109, 11),
        },
        {   2: (29, 10),
            10: (31, 15),
            6: (107, 11),
            5: (32, 10),
            7: (33, 15),
        },
        {   0: (127, 2),
            2: (29, 10),
            1: (30, 10),
            5: (32, 10),
        },
        {   2: (29, 10),
            3: (109, 11),
            7: (33, 15),
        },
        {   0: (127, 2),
            8: (16, 10),
            4: (27, 10),
            5: (32, 10),
        },
        {   8: (16, 10),
            10: (31, 15),
            9: (111, 11),
            5: (32, 10),
            13: (35, 15),
        },
        {   4: (27, 10),
            6: (107, 11),
            1: (30, 10),
            9: (111, 11),
            5: (32, 10),
        },
        {   2: (29, 10),
            3: (128, 10),
            7: (83, 2),
        },
        {   0: (129, 8),
            2: (84, 8),
            1: (114, 8),
            5: (87, 8),
        },
        {   2: (84, 8),
            3: (115, 8),
            7: (88, 8),
        },
        {   10: (130, 0),
            14: (131, 0),
            13: (132, 0),
            15: (133, 0),
        },
        {   8: (134, 0),
            10: (130, 0),
            9: (135, 0),
            5: (136, 0),
            13: (132, 0),
        },
        {   10: (130, 0),
            11: (137, 0),
            7: (138, 0),
            15: (133, 0),
        },
        {   0: (129, 8),
            8: (95, 13),
            4: (119, 12),
            5: (87, 8),
        },
        {   2: (139, 0),
            10: (130, 0),
            6: (140, 0),
            5: (136, 0),
            7: (138, 0),
        },
        {   10: (130, 0),
            11: (137, 0),
            7: (138, 0),
            15: (133, 0),
        },
        {   8: (134, 0),
            12: (141, 0),
            13: (132, 0),
        },
        {   8: (58, 10),
            12: (123, 9),
            13: (93, 8),
        },
        {   0: (142, 2),
            8: (96, 2),
            4: (124, 2),
            5: (99, 2),
        },
        {   10: (130, 0),
            14: (131, 0),
            13: (132, 0),
            15: (133, 0),
        },
        {   0: (142, 2),
            2: (51, 10),
            1: (67, 10),
            5: (99, 2),
        },
        {   0: (127, 2),
            4: (110, 6),
            1: (108, 6),
        },
        {   2: (29, 10),
            3: (21, 14),
            7: (143, 10),
        },
        {   0: (129, 8),
            4: (119, 12),
            1: (114, 8),
        },
        {   10: (144, 0),
            6: (145, 0),
            14: (146, 0),
            9: (147, 0),
            11: (148, 0),
        },
        {   10: (144, 0),
            14: (146, 0),
            13: (149, 0),
            15: (0, 0),
        },
        {   12: (150, 0),
            14: (146, 0),
            9: (147, 0),
            13: (149, 0),
        },
        {   14: (146, 0),
            11: (148, 0),
            15: (0, 0),
        },
        {   8: (151, 0),
            4: (152, 1),
            12: (150, 0),
            9: (147, 0),
        },
        {   8: (151, 0),
            10: (144, 0),
            9: (147, 0),
            5: (153, 0),
            13: (149, 0),
        },
        {   4: (152, 1),
            6: (145, 0),
            1: (154, 4),
            9: (147, 0),
            5: (153, 0),
        },
        {   10: (144, 0),
            11: (148, 0),
            7: (155, 0),
            15: (0, 0),
        },
        {   6: (145, 0),
            3: (156, 0),
            11: (148, 0),
            7: (155, 0),
        },
        {   2: (157, 0),
            6: (145, 0),
            1: (154, 4),
            3: (156, 0),
        },
        {   2: (157, 0),
            10: (144, 0),
            6: (145, 0),
            5: (153, 0),
            7: (155, 0),
        },
        {   8: (151, 0),
            12: (150, 0),
            13: (149, 0),
        },
        {   0: (142, 2),
            4: (124, 2),
            1: (126, 6),
        },
        {   6: (19, 14),
            3: (21, 14),
            11: (158, 6),
            7: (143, 10),
        },
        {   10: (144, 0),
            6: (145, 0),
            14: (1, 4),
            9: (147, 0),
            11: (2, 4),
        },
        {   2: (157, 0),
            10: (144, 0),
            6: (145, 0),
            5: (153, 0),
            7: (155, 0),
        },
        {   10: (144, 0),
            14: (1, 4),
            13: (149, 0),
            15: (0, 0),
        },
        {   8: (151, 0),
            10: (144, 0),
            9: (147, 0),
            5: (153, 0),
            13: (149, 0),
        },
        {   10: (144, 0),
            11: (2, 4),
            7: (155, 0),
            15: (0, 0),
        },
        {   12: (150, 0),
            14: (1, 4),
            9: (147, 0),
            13: (149, 0),
        },
        {   8: (151, 0),
            12: (150, 0),
            13: (149, 0),
        },
        {   8: (151, 0),
            4: (152, 1),
            12: (150, 0),
            9: (147, 0),
        },
        {   0: (127, 2),
            8: (151, 0),
            4: (159, 2),
            5: (153, 0),
        },
        {   4: (152, 1),
            6: (145, 0),
            1: (154, 4),
            9: (147, 0),
            5: (153, 0),
        },
        {   0: (34, 8),
            2: (157, 0),
            1: (160, 8),
            5: (153, 0),
        },
        {   6: (145, 0),
            3: (156, 0),
            11: (2, 4),
            7: (155, 0),
        },
        {   2: (157, 0),
            3: (156, 0),
            7: (155, 0),
        },
        {   2: (157, 0),
            6: (145, 0),
            1: (154, 4),
            3: (156, 0),
        },
        {   10: (47, 2),
            11: (64, 2),
            7: (83, 2),
            15: (50, 2),
        },
        {   0: (127, 2),
            8: (161, 2),
            4: (110, 6),
            5: (162, 2),
        },
        {   0: (34, 8),
            2: (163, 8),
            1: (20, 12),
            5: (164, 8),
        },
        {   8: (161, 2),
            4: (110, 6),
            12: (65, 6),
            9: (63, 6),
        },
        {   4: (110, 6),
            6: (62, 3),
            1: (108, 6),
            9: (63, 6),
            5: (162, 2),
        },
        {   2: (163, 8),
            6: (8, 12),
            1: (20, 12),
            3: (12, 12),
        },
        {   4: (22, 12),
            6: (8, 12),
            1: (20, 12),
            9: (9, 12),
            5: (164, 8),
        },
        {   15: (0, 0),
            15: (133, 0),
        },
        ]
    
    def move(self, o_state):
        try:
            table = self._table[self._state]
            newState,res = table[o_state]
            self._state = newState
            return res
        
        except IndexError:
            raise Exception("Unrecognized internal state: " + str(self._state))
        
        except Exception:
            self._error(o_state)
    
    def _error(self, o_state):
        raise ValueError("Unrecognized input: " + (
            "o_state = {o_state}; ").format( o_state=o_state))