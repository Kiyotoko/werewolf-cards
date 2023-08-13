import argparse

from src import creator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Card Creator",
        description="Creates cards for various games."
    )
    parser.add_argument("name", type=str, help="The name of the card.")
    parser.add_argument("color", type=str, help="The color of the card.")
    parser.add_argument("power", type=int, help="The power value of the card.")
    args = parser.parse_args()

    creator.create(args.name, args.color, args.power)