import argparse

def load(filename, folder = "images/"):
    path = folder + filename + ".svg"
    file_data = ""
    with open(path, "r") as reader:
        file_data = reader.read()
    return file_data

def save(filename, file_data, folder = "output/"):
    filename = folder + filename + ".svg"
    with open(filename, "w+") as writer:
        writer.write(file_data)

def create(name: str, color: str, power: int):
    build = '<svg xmlns="http://www.w3.org/2000/svg" width="512" height="768">'
    build += load(name)
    build += '<rect width="492" height="100" fill="#101010a0" x="10" y="10" rx="50" ry="50"/>'
    build += f'<text font-size="44" fill="{color}" x="100" y="74">{name}</text>'
    build += f'<circle r="30" cx="60" cy="60" fill="{color}"/>'
    build += f'<text font-size="44" fill="#101010f0" x="47" y="74">{power}</text>'
    build += '</svg>'
    
    save(name, build)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Card Creator",
        description="Creates cards for various games."
    )
    parser.add_argument("name", type=str, help="The name of the card.")
    parser.add_argument("color", type=str, help="The color of the card.")
    parser.add_argument("power", type=str, help="The power value of the card.")
    args = parser.parse_args()

    create(args.name, args.color, args.power)