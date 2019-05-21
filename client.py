# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
import signal
from modules.FIC_Exceptions import FICExceptions
from modules.FIC_MainMenu import FICMainMenu

if __name__ == "__main__":
    signal.signal(signal.SIGINT, FICExceptions().signal_handler)

    menu_switch = FICMainMenu()
    menu_switch.main_menu()

