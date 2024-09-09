import os

from pathlib import Path

import mobase

from ..basic_game import BasicGame

class SanAndreasGame(BasicGame):

    Name = "San Andreas Support Plugin"
    Author = "Enclave"
    Version = "1.0"

    GameName = "Grand Theft Auto San Andreas"
    GameShortName = "gtasa"
    GameBinary = "gta-sa.exe"
    GameDataPath = "modloader"
