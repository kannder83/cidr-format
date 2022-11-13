import doctest


class FormatCIDR():
    def __init__(self, user_input: str):
        self.int_ip: list[int] = []
        self.str_ip: list[str] = []
        self.int_mask: list[int] = []
        self.str_mask: list[str] = []
        self.mask_cidr: int = 0
        self.user_input: str = user_input
        self.separated_values: list = []

    def validate_special_chars(self, user_data: str):
        count_dots = 0
        count_lines = 0

        if "-" not in user_data:
            raise Exception(
                "To separate the IP from the mask it is necessary to use the '-' character.")

        for character in self.user_input:
            if character in ".":
                count_dots += 1
            if character in "-":
                count_lines += 1

        if count_dots > 6 or count_lines > 1:
            raise Exception("The octet format of the IP-Mask is invalid.")

        return True

    def clean_data(self, user_input: str):
        cleaned_values = user_input.replace(".", " ").replace("-", " ")
        self.separated_values = cleaned_values.split()

    def separete_data(self, user_data: list[str]):
        for octet in user_data:
            if int(octet) < 0 or int(octet) > 255:
                raise Exception("The octet is outside the range 0 to 255.")

        self.int_ip = [int(octet) for octet in user_data[:4]]
        self.str_ip = [str(octet) for octet in self.int_ip[:4]]
        self.int_mask = [int(octet) for octet in user_data[4::]]
        self.str_mask = [octet for octet in user_data[4::]]

        if len(self.int_ip) != 4 or len(self.int_mask) != 4:
            raise Exception("The number of octets is invalid.")

    def valid_mask_values(self, numero: int):
        potencies = [2**n for n in range(0, 256) if 2**n <= 256]
        potencies[0] = 0
        potencies[-1] = 255

        if numero not in potencies:
            raise Exception(f"Invalid mask octet {potencies}.")

    def mask_review(self, mask: list[int]):
        binary = []
        count_ones = 0
        mask_binary = ""

        for octet in mask:
            binary.append(format(octet, "b"))

        mask_cidr = mask_binary.join(binary)

        for number_one in mask_cidr:
            if number_one == "1":
                count_ones += 1

        for octet in mask:
            self.valid_mask_values(octet)

        if "1"*count_ones != mask_cidr[0:count_ones]:
            raise Exception("The mask does not comply with the format.")

        self.mask_cidr = count_ones

    def show_cidr(self):
        ip_format = ".".join(self.str_ip)
        return f"{ip_format}/{self.mask_cidr}"

    def get_cidr(self) -> str:
        self.validate_special_chars(self.user_input)
        self.clean_data(self.user_input)
        self.separete_data(self.separated_values)
        self.mask_review(self.int_mask)
        return self.show_cidr()
