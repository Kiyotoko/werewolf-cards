COLOR_TABLE = {
    "?village": "#1010f0",
    "?werewolf": "crimson"
}


def create(name: str, color: str, power: int, input_folder: str = "images/", output_folder: str = "output/"):
    if color.startswith("?"):
        color = COLOR_TABLE.get(color)
        if color is None:
            raise LookupError("faction not found")
    path = input_folder + name + ".svg"

    build = '<svg xmlns="http://www.w3.org/2000/svg" width="500" height="700">'
    try:
        with open(path, "r") as reader:
            build += reader.read()
    except FileNotFoundError as error:
        print(f"WARN {error}: please put an svg image in the images directory, skipping image now")
    build += '<rect width="480" height="100" fill="#101010a0" x="10" y="10" rx="50" ry="50"/>'
    build += f'<text font-size="44" fill="{color}" x="100" y="74">{name}</text>'
    build += f'<circle r="30" cx="60" cy="60" fill="{color}"/>'
    build += f'<text font-size="44" fill="#101010f0" x="47" y="74">{power}</text>'
    build += '</svg>'

    filename = output_folder + name + ".svg"
    with open(filename, "w+") as writer:
        writer.write(build)
