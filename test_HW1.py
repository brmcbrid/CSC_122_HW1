# Tests for HW1
# Pay Raise Calculator Program

import os.path
import sys
from HW1 import main
from tud_tests import *

def test_HW1():

    try:
        exists = os.path.exists("HW1.py")
        assert exists == True
    except:
        sys.exit()

    set_keyboard_input(["Red Green",32780])
    main()
    output = get_display_output()

    assert output == [
        "Pay Raise Calculator\n",
        "Enter your name: ",
        "\nEnter your annual salary $",
        "\nRetroactive pay due Red Green is $1245.64",
        "\nRed Green's new annual salary is $35271.28",
        "\nNew monthly salary is $2939.27"
        ]
