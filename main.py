
class FormatCIDR():
    def __init__(self, user_input: str):
        self.ip: list = []
        self.mask: list = []
        self.mask_cidr: int = 0
        self.user_input: str = user_input
        self.separated_values: list = []

    def validate_special_chars(self) -> list:
        count_dots = 0
        count_lines = 0
        for character in self.user_input:
            if character in ".":
                count_dots += 1
            if character in "-":
                count_lines += 1

        if count_dots > 6 or count_lines > 1:
            raise Exception("El formato de octetos no es válido.")

    def clean_data(self):
        cleaned_values = self.user_input.replace(".", " ").replace("-", " ")
        self.separated_values = cleaned_values.split()
        print(self.separated_values)

    def separete_data(self):
        for octet in self.separated_values:
            if int(octet) < 0 or int(octet) > 255:
                raise Exception("El octeto esta fuera de rango de 0 a 255.")

        self.ip = [int(octet) for octet in self.separated_values[:4]]
        self.mask = [int(octet) for octet in self.separated_values[4::]]

        print(self.ip)
        print(self.mask)

        if len(self.ip) != 4 or len(self.mask) != 4:
            raise Exception("La cantidad de octetos no es valida.")

    def mask_review(self):
        binary = []
        count_ones = 0
        mask_binary = ""

        for octet in self.mask:
            binary.append(format(octet, "b"))

        mask_cidr = mask_binary.join(binary)

        print(mask_cidr)

        for number_one in mask_cidr:
            if number_one == "1":
                count_ones += 1

        self.mask_cidr = count_ones
        print(self.mask_cidr)

    def get_cidr(self):
        out = ""
        return ".".join(self.ip)


def main():
    # input_data = FormatCIDR(user_input=input(
    #     "Ingrese la IP seguido - con la máscara correspondiente:"))

    input_data = FormatCIDR(user_input="1.1.255.1 - 255.0.255.255")

    try:
        input_data.validate_special_chars()
        input_data.clean_data()
        input_data.separete_data()
        input_data.mask_review()
        print(input_data.get_cidr())

    except ValueError as e:
        print("Error: ", "Digitar solo valores enteros entre 0 y 255.")

    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
