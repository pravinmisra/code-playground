# -*- coding: utf-8 -*-
"""
Created on Mon May 26 21:11:59 2025

@author: Admin
"""

test_dict_1d = {"id": 1001,
             "name": "Andrew",
             "Address": "235, whitefield"}

print(test_dict_1d)

test_dict_2d = {"person1":
                    {"id": 1001,
                     "name": "Andrew",
                     "Address": "235, whitefield"},
                "person2":
                    {"id": 1002,
                     "name": "John",
                     "Address": "236, whitefield"}
                }
print(test_dict_2d)

print(test_dict_1d["id"])
print(test_dict_1d["name"])

print(test_dict_2d["person2"]["id"])
print(test_dict_2d["person2"]["Address"])

