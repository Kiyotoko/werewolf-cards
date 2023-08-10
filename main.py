import argparse

def create(image, color, name, power):
    build = '<svg xmlns="http://www.w3.org/2000/svg" width="500" height="700">'
    build += f'<image href="{image}" width="500"/>'
    build += '<rect width="480" height="100" fill="#101010a0" x="10" y="10" rx="50" ry="50"/>'
    build += f'<text font-size="44" fill="{color}" x="100" y="74">{name}</text>'
    build += f'<circle r="30" cx="60" cy="60" fill="{color}"/>'
    build += f'<text font-size="44" fill="#101010f0" x="47" y="74">{power}</text>'
    build += '</svg>'

    filename = "output/" + name + ".svg"
    with open(filename, "w+") as writer:
        writer.write(build)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Card Creator",
        description="Creates cards for various games."
    )
    parser.add_argument("image", type=str, help="The location of the background image file.")
    parser.add_argument("color", type=str, help="The color of the card.")
    parser.add_argument("name", type=str, help="The name of the card.")
    parser.add_argument("power", type=int, help="The power value of the card.")
    args = parser.parse_args()

    create(args.image, args.color, args.name, args.power)