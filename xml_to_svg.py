def xml_to_svg(xml_path: str, svg_path: str):
    with open(xml_path, "r", encoding="utf-8") as xml_file:
        content = xml_file.read()

    with open(svg_path, "w", encoding="utf-8") as svg_file:
        svg_file.write(content)

    print(f"Saved: {svg_path}")


if __name__ == "__main__":
    xml_to_svg("torii.xml", "torii.svg")
