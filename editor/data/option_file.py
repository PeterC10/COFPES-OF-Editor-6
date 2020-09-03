import os

from enum import Enum, auto

from .option_file_data import (
    OF_BYTE_LENGTH,
    OF_BLOCK,
    OF_BLOCK_SIZE,
    OF_KEY,
    OF_KEY_PC,
)

from ..utils.common_functions import (
    bytes_to_int,
    zero_fill_right_shift,
)


class OptionFile:
    of_byte_length = OF_BYTE_LENGTH
    of_block = OF_BLOCK
    of_block_size = OF_BLOCK_SIZE
    of_key = OF_KEY
    of_key_pc = OF_KEY_PC

    data = bytearray()
    file_name = ""
    game_type = None

    def get_game_type(self, file_name):
        """
        Return game type from supplied filename string.
        """
        game_type_map = {
            "KONAMI-WIN32PES6OPT": GameType.pc_pes,
            "KONAMI-WIN32WEXUOPT": GameType.pc_pwe,
        }
        return game_type_map.get(file_name)

    def read_option_file(self, of_file_location):
        """
        Decrypt supplied file and set OF data.
        """
        of_file = open(of_file_location, "rb")
        file_name = os.path.basename(of_file.name)
        self.file_name = file_name
        self.game_type = self.get_game_type(file_name)

        file_contents = of_file.read()
        of_file.close()

        self.data = bytearray(file_contents)
        self.convert_data()
        self.decrypt()

        return True

    def save_option_file(self, of_file_location):
        """
        Save OF data to supplied file.
        """
        self.data[45] = 1
        self.data[46] = 1
        self.data[5938] = 1
        self.data[5939] = 1

        self.encrypt()
        self.checksums()
        self.convert_data()

        of_file = open(of_file_location, "wb")
        of_file.write(self.data)
        of_file.close()

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
            a = self.of_block[i]
            while True:
                if a + 4 > self.of_block[i] + self.of_block_size[i]:
                    break

                c = bytes_to_int(self.data, a)
                p = ((c - self.of_key[k]) + 0x7AB3684C) ^ 0x7AB3684C

                self.data[a] = p & 0x000000FF
                self.data[a + 1] = zero_fill_right_shift(p, 8) & 0x000000FF
                self.data[a + 2] = zero_fill_right_shift(p, 16) & 0x000000FF
                self.data[a + 3] = zero_fill_right_shift(p, 24) & 0x000000FF

                k += 1
                if k == 446:
                    k = 0

                a += 4

    def encrypt(self):
        """
        Encrypt OF.
        """
        count = 0
        for i in range(1, len(self.of_block)):
            k = 0
            a = self.of_block[i]
            while True:
                if a + 4 > self.of_block[i] + self.of_block_size[i]:
                    break

                count += 1
                p = bytes_to_int(self.data, a)
                c = self.of_key[k] + ((p ^ 0x7AB3684C) - 0x7AB3684C)

                self.data[a] = c & 0x000000FF
                self.data[a + 1] = zero_fill_right_shift(c, 8) & 0x000000FF
                self.data[a + 2] = zero_fill_right_shift(c, 16) & 0x000000FF
                self.data[a + 3] = zero_fill_right_shift(c, 24) & 0x000000FF

                k += 1
                if k == 446:
                    k = 0

                a += 4

    def checksums(self):
        """
        Set checksums.
        """
        for i in range(1, len(self.of_block)):
            checksum = 0
            while True:
                a = self.of_block[i]
                checksum += bytes_to_int(self.data, a)

                a += 4
                if a <= self.of_block[i] + self.of_block_size[i]:
                    break

            self.data[self.of_block[i] - 8] = checksum & 0x000000FF
            self.data[self.of_block[i] - 7] = (
                zero_fill_right_shift(checksum, 8) & 0x000000FF
            )
            self.data[self.of_block[i] - 6] = (
                zero_fill_right_shift(checksum, 16) & 0x000000FF
            )
            self.data[self.of_block[i] - 5] = (
                zero_fill_right_shift(checksum, 24) & 0x000000FF
            )


class GameType(Enum):
    pc_pes = auto()
    pc_pwe = auto()
