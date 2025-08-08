class Player:
    total = 4999
    total_edit = 184

    size = 124
    max_name_size = 15
    name_bytes_length = 32
    shirt_name_bytes_length = 16

    start_address = 37116
    start_address_edit = 14288

    first_edit = 32768
    last_edit = first_edit + total_edit
    first_unused = 4784
    first_ml = 4414
    last_ml = 4436
    first_shop = 4437
    first_youth = 4597
    first_old = 4774
    first_classic = 1312
    last_classic = 1472
    first_club = 1473
    first_pes_united = 3954

    def __init__(self, option_file, idx):
        self.option_file = option_file
        self.idx = idx

        self.set_name_from_of()
        self.set_shirt_name_from_of()

    @property
    def is_edit(self):
        """
        Return true if the player is an edit player.

        A player is deemed an edit player if its index number is greater than
        or equal to the first edit address.
        """
        return self.idx >= self.first_edit

    @property
    def is_ml(self):
        """
        Return true if the player is a Master League default player.
        """
        return self.idx >= self.first_ml and self.idx <= self.last_ml

    @property
    def is_classic(self):
        """
        Return true if the player is a classic player.
        """
        return self.idx >= self.first_classic and self.idx <= self.last_classic

    @property
    def offset(self):
        """
        Return player offset.
        """
        return (
            self.idx * self.size
            if not self.is_edit
            else (self.idx - self.first_edit) * self.size
        )

    @property
    def address(self):
        """
        Return player address.
        """
        return (
            self.start_address + self.offset
            if not self.is_edit
            else self.start_address_edit + self.offset
        )

    def set_name_from_of(self):
        """
        Set player name from relevant OF data bytes.
        """
        name = "???"

        if (
            self.idx > 0
            and (self.idx <= self.total or self.idx >= self.first_edit)
            and self.idx < self.last_edit
        ):
            all_name_bytes = self.option_file.data[
                self.address : self.address + self.name_bytes_length
            ]
            # Extract every other byte (skip null bytes)
            name_only_bytes = all_name_bytes[::2]
            
            # Find null terminator
            null_pos = name_only_bytes.find(b'\0')
            if null_pos != -1:
                name_only_bytes = name_only_bytes[:null_pos]
            
            name = name_only_bytes.decode('latin-1', errors='ignore')

            if not name:
                no_name_prefixes = {
                    self.first_edit: "Edited",
                    self.first_unused: "Unused",
                    1: "Unknown",
                }

                for address, address_prefix in no_name_prefixes.items():
                    if self.idx >= address:
                        prefix = address_prefix
                        break
                else:
                    prefix = "Unknown"

                name = f"{prefix} (ID: {self.idx})"

        self.__name = name

    @property
    def name(self):
        """
        Return player name.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Update player name with the supplied value.
        """
        new_name = name[: self.max_name_size]

        player_name_bytes = [0] * self.name_bytes_length
        new_name_bytes = str.encode(new_name, "utf-16-le")
        player_name_bytes[: len(new_name_bytes)] = new_name_bytes

        for i, byte in enumerate(player_name_bytes):
            self.option_file.data[self.address + i] = byte

        self.__name = new_name

    def set_shirt_name_from_of(self):
        """
        Set player shirt name from relevant OF data bytes.
        """
        shirt_name_address = self.address + 32
        name_byte_array = self.option_file.data[
            shirt_name_address : shirt_name_address
            + self.shirt_name_bytes_length
        ]

        self.__shirt_name = name_byte_array.partition(b"\0")[0].decode()

    @property
    def shirt_name(self):
        """
        Return player shirt name.
        """
        return self.__shirt_name

    @shirt_name.setter
    def shirt_name(self, shirt_name):
        shirt_name_address = self.address + 32
        new_name = shirt_name[: self.max_name_size].upper()

        player_shirt_name_bytes = [0] * self.shirt_name_bytes_length
        new_name_bytes = str.encode(new_name)
        player_shirt_name_bytes[: len(new_name_bytes)] = new_name_bytes

        for i, byte in enumerate(player_shirt_name_bytes):
            self.option_file.data[shirt_name_address + i] = byte

        self.__shirt_name = new_name
