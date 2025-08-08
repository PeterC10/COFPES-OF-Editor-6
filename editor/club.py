class Club:
    total = 140
    start_address = 751472
    size = 88
    max_name_size = 48
    max_tla_size = 3

    def __init__(self, option_file, idx):
        self.option_file = option_file
        self.idx = idx

        self.set_addresses()
        self.set_name()
        self.set_tla()

    def set_addresses(self):
        """
        Set the following club addresses:

        - Name
        - TLA
        - Name edited
        """
        self.name_address = self.start_address + (self.idx * self.size)
        self.tla_address = self.start_address + 49 + (self.idx * self.size)
        self.name_edited_address = (
            self.start_address + (self.idx * self.size) + 56
        )

    def set_name(self):
        """
        Set club name from relevant OF data bytes.
        """
        name_byte_array = self.option_file.data[
            self.name_address : self.name_address + (self.max_name_size + 1)
        ]
        
        # Find null terminator and decode
        null_pos = name_byte_array.find(b'\0')
        if null_pos != -1:
            name_byte_array = name_byte_array[:null_pos]
        
        self.name = name_byte_array.decode('latin-1', errors='ignore')

    def set_tla(self):
        """
        Set club tla from relevant OF data bytes.
        """
        tla_byte_array = self.option_file.data[
            self.tla_address : self.tla_address + (self.max_tla_size + 1)
        ]
        
        # Find null terminator and decode
        null_pos = tla_byte_array.find(b'\0')
        if null_pos != -1:
            tla_byte_array = tla_byte_array[:null_pos]
        
        self.tla = tla_byte_array.decode('latin-1', errors='ignore')

    def update_name(self, name):
        """
        Update club name with the supplied value.
        """
        new_name = name[: self.max_name_size]

        club_name_bytes = [0] * (self.max_name_size + 1)
        new_name_bytes = str.encode(new_name)
        club_name_bytes[: len(new_name_bytes)] = new_name_bytes

        for i, byte in enumerate(club_name_bytes):
            self.option_file.data[self.name_address + i] = byte

        self.set_name_edited()
        self.name = new_name

    def update_tla(self, tla):
        """
        Update club TLA with the supplied value.
        """
        new_tla = tla[:3].upper()

        club_tla_bytes = [0] * (self.max_tla_size + 1)
        new_tla_bytes = str.encode(new_tla)
        club_tla_bytes[: len(new_tla_bytes)] = new_tla_bytes

        for i, byte in enumerate(club_tla_bytes):
            self.option_file.data[self.tla_address + i] = byte

        self.set_name_edited()
        self.tla = new_tla

    def set_name_edited(self):
        """
        Set club name as being edited.
        """
        self.option_file.data[self.name_edited_address] = 1
