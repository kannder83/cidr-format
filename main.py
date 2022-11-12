from format_cidr import FormatCIDR


def main():

    user_input = input("Ingrese los datos de la red (ip - mask): ")

    try:
        input_data = FormatCIDR(user_input=user_input)
        print("Formato CIDR: ", input_data.get_cidr())

    except ValueError as e:
        print("Error: ", "Se admiten valores enteros entre 0 - 255 y caracteres especiales '.' y '-'.")

    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
