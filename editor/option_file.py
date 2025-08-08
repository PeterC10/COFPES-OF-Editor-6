import os
import itertools
from enum import Enum, auto

from .option_file_data import (
    OF_BYTE_LENGTH,
    OF_BLOCK,
    OF_BLOCK_SIZE,
    OF_KEY,
    OF_KEY_PC,
)

from .club import Club
from .player import Player

from .utils.common_functions import bytes_to_int, zero_fill_right_shift


class OptionFile:
    of_byte_length = OF_BYTE_LENGTH
    of_block = OF_BLOCK
    of_block_size = OF_BLOCK_SIZE
    of_key = OF_KEY
    of_key_pc = OF_KEY_PC

    def __init__(self, file_location):
        self.file_location = file_location

        self.data = bytearray()
        self.file_name = ""
        self.game_type = None
        self._cache = {}

        self.read_option_file()

        self.set_clubs()
        self.set_players()

    def _get_memoryview(self, start=None, end=None):
        """
        Get a memoryview of the data for efficient slicing operations.
        """
        if start is None and end is None:
            return memoryview(self.data)
        elif end is None:
            return memoryview(self.data)[start:]
        else:
            return memoryview(self.data)[start:end]

    def _get_cached_data(self, key, default=None):
        """
        Get cached data or return default if not found.
        """
        return self._cache.get(key, default)

    def _set_cached_data(self, key, value):
        """
        Set cached data.
        """
        self._cache[key] = value

    def get_game_type(self, file_name):
        """
        Return game type from supplied filename string.
        """
        game_type_map = {
            "KONAMI-WIN32PES6OPT": GameType.pc_pes,
            "KONAMI-WIN32WEXUOPT": GameType.pc_pwe,
        }
        return game_type_map.get(file_name)

    def read_option_file(self):
        """
        Decrypt supplied file and set OF data.
        """
        with open(self.file_location, "rb") as of_file:
            file_name = os.path.basename(of_file.name)
            self.file_name = file_name
            self.game_type = self.get_game_type(file_name)

            file_contents = of_file.read()
            self.data = bytearray(file_contents)
        
        self.convert_data()
        self.decrypt()
        return True

    def save_option_file(self, file_location=None):
        """
        Save OF data to supplied file.
        """
        file_location = self.file_location = file_location or self.file_location

        self.data[45] = 1
        self.data[46] = 1
        self.data[5938] = 1
        self.data[5939] = 1

        self.encrypt()
        self.checksums()
        self.convert_data()

        with open(file_location, "wb") as of_file:
            of_file.write(self.data)

        self.convert_data()
        self.decrypt()
        return True

    def convert_data(self):
        """
        Converts OF data based on PC key.
        """
        key = 0

        for i in range(self.of_byte_length):
            self.data[i] = self.data[i] ^ self.of_key_pc[key]

            if key < 255:
                key += 1
            else:
                key = 0

    def decrypt(self):
        """
        Decrypt OF.
        """
        for i in range(1, len(self.of_block)):
            k = 0
            start_addr = self.of_block[i]
            end_addr = start_addr + self.of_block_size[i]
            
            for a in range(start_addr, end_addr - 3, 4):
                c = bytes_to_int(self.data, a)
                p = ((c - self.of_key[k]) + 0x7AB3684C) ^ 0x7AB3684C

                self.data[a] = p & 0x000000FF
                self.data[a + 1] = zero_fill_right_shift(p, 8) & 0x000000FF
                self.data[a + 2] = zero_fill_right_shift(p, 16) & 0x000000FF
                self.data[a + 3] = zero_fill_right_shift(p, 24) & 0x000000FF

                k = (k + 1) % 446

    def encrypt(self):
        """
        Encrypt OF.
        """
        for i in range(1, len(self.of_block)):
            k = 0
            start_addr = self.of_block[i]
            end_addr = start_addr + self.of_block_size[i]
            
            for a in range(start_addr, end_addr - 3, 4):
                p = bytes_to_int(self.data, a)
                c = self.of_key[k] + ((p ^ 0x7AB3684C) - 0x7AB3684C)

                self.data[a] = c & 0x000000FF
                self.data[a + 1] = zero_fill_right_shift(c, 8) & 0x000000FF
                self.data[a + 2] = zero_fill_right_shift(c, 16) & 0x000000FF
                self.data[a + 3] = zero_fill_right_shift(c, 24) & 0x000000FF

                k = (k + 1) % 446

    def checksums(self):
        """
        Set checksums.
        """
        for i in range(len(self.of_block)):
            checksum = 0
            start_addr = self.of_block[i]
            end_addr = start_addr + self.of_block_size[i]
            
            for a in range(start_addr, end_addr - 3, 4):
                checksum += bytes_to_int(self.data, a)

            self.data[start_addr - 8] = checksum & 0x000000FF
            self.data[start_addr - 7] = (checksum >> 8) & 0x000000FF
            self.data[start_addr - 6] = (checksum >> 16) & 0x000000FF
            self.data[start_addr - 5] = (checksum >> 24) & 0x000000FF

    def set_clubs(self):
        """
        Load all clubs from OF data and add to clubs list.
        """
        self.clubs = [Club(self, i) for i in range(Club.total)]

    def set_players(self):
        """
        Load all players from OF data and add to players list.
        """
        player_indices = list(itertools.chain(
            range(1, Player.total + 1),
            range(Player.first_edit, Player.last_edit),
        ))
        self.players = [Player(self, i) for i in player_indices]


class GameType(Enum):
    pc_pes = auto()
    pc_pwe = auto()
