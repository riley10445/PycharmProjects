import colorgram as cg

rgb_colors = []
colors = cg.extract('archives_helix.jpg', 8)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb = (r, g, b)
    colorhex = "#%02x%02x%02x" % rgb
    rgb_colors.append(colorhex)
