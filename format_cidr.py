class FormatCIDR():
    def __init__(self, user_input: str):
        self.int_ip: list[int] = []
        self.str_ip: list[str] = []
        self.int_mask: list[int] = []
        self.str_mask: list[str] = []
        self.mask_cidr: int = 0
        self.user_input: str = user_input
        self.separated_values: list = []

    def validate_special_chars(self) -> list:
        count_dots = 0
        count_lines = 0

        if "-" not in self.user_input:
            raise Exception("El separador entre la IP la Mask debe ser '-'.")

        for character in self.user_input:
            if character in ".":
                count_dots += 1
            if character in "-":
                count_lines += 1

        if count_dots > 6 or count_lines > 1:
            raise Exception("El formato de octetos IP-Mask no es válido.")

    def clean_data(self):
        cleaned_values = self.user_input.replace(".", " ").replace("-", " ")
        self.separated_values = cleaned_values.split()

    def separete_data(self):
        for octet in self.separated_values:
            if int(octet) < 0 or int(octet) > 255:
                raise Exception("El octeto esta fuera de rango de 0 a 255.")

        self.int_ip = [int(octet) for octet in self.separated_values[:4]]
        self.str_ip = [str(octet) for octet in self.int_ip[:4]]
        self.int_mask = [int(octet) for octet in self.separated_values[4::]]
        self.str_mask = [octet for octet in self.separated_values[4::]]

        if self.int_ip[0] == 0:
            raise Exception(
                "El primer octeto de la IP debe ser diferente de 0.")

        if self.int_mask[0] == 0:
            raise Exception(
                "El primer octeto de la Mask debe ser diferente de 0.")

        if len(self.int_ip) != 4 or len(self.int_mask) != 4:
            raise Exception("La cantidad de octetos no es valida.")

    def valid_mask_values(self, numero: int):
        potencies = [2**n for n in range(0, 256) if 2**n <= 256]
        potencies[0] = 0
        potencies[-1] = 255

        if numero not in potencies:
            raise Exception(f"Octeto de máscara no valido {potencies}.")

    def mask_review(self):
        binary = []
        count_ones = 0
        mask_binary = ""

        for octet in self.int_mask:
            binary.append(format(octet, "b"))

        mask_cidr = mask_binary.join(binary)

        for number_one in mask_cidr:
            if number_one == "1":
                count_ones += 1

        for octet in self.int_mask:
            self.valid_mask_values(octet)

        if "1"*count_ones != mask_cidr[0:count_ones]:
            raise Exception("La máscara no cumple el formato.")

        self.mask_cidr = count_ones

    def show_cidr(self):
        ip_format = ".".join(self.str_ip)
        return f"{ip_format}/{self.mask_cidr}"

    def get_cidr(self):
        self.validate_special_chars()
        self.clean_data()
        self.separete_data()
        self.mask_review()
        return self.show_cidr()
