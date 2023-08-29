import argparse

parser = argparse.ArgumentParser (

     description = 'this program prints the name of my dog'
)

parser.add_argument(
    '-c',
    '--color',
    metavar = 'color',
    choices = {'black', 'white'},
    required = True,
    help = 'the color to search for'
)

args = parser.parse_args()

print(args.color)

 