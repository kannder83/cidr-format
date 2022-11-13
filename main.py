import doctest
from format_cidr import FormatCIDR


def formatting_network(user_input: str) -> str:
    """
    Description: The user enters a network with its respective mask and the return receives the IP in CIDR format.
    Arguments: str -> Network format input 'x.x.x.x-y.y.y.y'
    Return: str -> Format CIDR: x.x.x.x/z

    >>> formatting_network('1.2.3.4-255.255.255.0')
    'Format CIDR: 1.2.3.4/24'

    >>> formatting_network('100.200.3.46-255.0.0.0')
    'Format CIDR: 100.200.3.46/8'

    >>> formatting_network('0.2.3.4-255.255.255.0')
    Error:  The first octet of the IP must be different from 0.

    >>> formatting_network('1.2.3.4-255.0.255.0')
    Error:  The mask does not comply with the format.
    """

    try:
        input_data = FormatCIDR(user_input=user_input)

        return f'Format CIDR: {input_data.get_cidr()}'

    except ValueError as e:
        print("Error: ", "Integer values from 0 to 255 and only special characters '.' and '-' are supported.")

    except Exception as e:
        print("Error: ", e)


def main():
    doctest.testmod()
    user_input = input(
        "Enter the network data of the IP-Mask (x.x.x.x - y.y.y.y): ")
    print(formatting_network(user_input))


if __name__ == "__main__":
    main()
