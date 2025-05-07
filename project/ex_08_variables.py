from delta import Compiler, Phase


source = '''
    var x, y;         // First statement
    x = 2;
    y = (x + 1) * 3;
    var z;
    z = y - 1;        // Last statement
    x + y + z         // Resulting expression
'''

c = Compiler('program')
c.realize(source)
# print(c.parse_tree_str)
# print(c.symbol_table)
# print(c.wat_code)
print(c.result)
