# -*- coding: utf-8 -*-

"""
Copyright (C) Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# ################################################################################################################################
# ################################################################################################################################

def parse_extra_into_list(data):
    # type: (str) -> list
    return [int(elem.strip()) for elem in data.split(';') if elem]

# ################################################################################################################################
# ################################################################################################################################
