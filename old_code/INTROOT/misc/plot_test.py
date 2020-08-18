#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# CODE NAME HERE

# CODE DESCRIPTION HERE

Created on 2018-09-25 at 16:17

@author: cook
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# =============================================================================
# Define variables
# =============================================================================

# -----------------------------------------------------------------------------

# =============================================================================
# Define functions
# =============================================================================
x = np.arange(-10, 10)
y2 = x ** 2
y3 = x ** 3

with matplotlib.rc_context(rc={'font': 20}):
    plt.figure()
    plt.plot(x, y2)

with matplotlib.rc_context(rc={'size': 12}):
    plt.plot(x, y3)


plt.show()
plt.close()

# =============================================================================
# Start of code
# =============================================================================
# Main code here
if __name__ == "__main__":
    # ----------------------------------------------------------------------
    # print 'Hello World!'
    print("Hello World!")

# =============================================================================
# End of code
# =============================================================================
