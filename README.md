# Format CIDR

The program receives from the user as a parameter an IP with its respective mask expressed in octets. The program returns the IP with its respective CIDR format.

## Install

Python3 must be installed.

[Download - Python3](https://wwww.python.org)

View the version of python you have installed:

```py
python3 --version
# Python 3.10.8
```

## Create a new Virtual Environment:

It is a good option to have a virtual environment to execute the program.

```py
python3 -m venv venv
```

## Activate Virtual Enviroment:

Execute this command for activate the Virtual Enviroment:

```py
source venv/bin/activate
```

## Execute the program:

Just run this command in the terminal

```py
python3 main.py
```

## Example:

This is an example of how to type the IP and mask:

```py
>>> Enter the network data of the IP-Mask (x.x.x.x - y.y.y.y): 1.2.3.4  -  255.255.255.0

# Response:
Format CIDR: 1.2.3.4/24
```

## Execute Test:

To run the test, execute this command:

```py
python3 main.py -v
```
