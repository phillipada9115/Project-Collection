from Questions import questions
import main as m


if questions.element == "1":
    color1 = "burlywood"
    color2 = "bisque"
    color3 = "rosybrown"
    color4 = "peru"
    color5 = "sienna"
    color6 = "dark green"
elif questions.element == "2":
    color1 = "crimson"
    color2 = "orange"
    color3 = "firebrick"
    color4 = "red"
    color5 = "darkorange"
    color6 = "deep pink"
elif questions.element == "3":
    color1 = "aqua"
    color2 = "aquamarine"
    color3 = "navy"
    color4 = "blue"
    color5 = "doger blue"
    color6 = "lime"
elif questions.element == "4":
    color1 = "lavenderblush"
    color2 = "lavender"
    color3 = "lightgrey"
    color4 = "medium orchid"
    color5 = "gainsboro"
    color6 = "gold"

mysterycolor = [color1, color2, color3, color4, color5, color6]    
mystery_color = random.choice(mysterycolor)