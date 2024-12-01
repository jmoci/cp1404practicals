
NAME_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff", "alizarin crimson": "#e32636", "amaranth":	"#e52b50", "amber":	"#ffbf00", "amethyst": "#9966cc", "apricot": "#fbceb1", "aqua": "#00ffff"}
def main():
    colour_name = input("Enter colour name: ").lower()
    while colour_name != "":
        try:
            print(f"{NAME_TO_CODE[colour_name]}")
        except KeyError:
            print("Invalid colour")
        colour_name = input("Enter colour name: ").lower()
main()