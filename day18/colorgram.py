import colorgram

colors = colorgram.extract("download.jpg", 20)

color_code = []


for color in colors:
  r = color.rgb.r
  g = color.rgb.g
  b = color.rgb.b
  new_color = (r, g, b)
  color_code.append(new_color)

print(color_code)

