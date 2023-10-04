from prettytable import PrettyTable

x = PrettyTable()

x.field_names = ["User", "Area", "Population"]
x.add_rows(
    [
          ["Darwin", 1295, 12232], 
          ["Pikachu", 1995, 11212332],
          ["John", 2003, "1dfvs3453"]
    ]
)
x.align = "l"
print(x)