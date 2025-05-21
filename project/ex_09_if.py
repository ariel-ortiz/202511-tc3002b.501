from delta import Compiler, Phase


source = '''
    var x, y;
    x = false;
    y = 5;
    if !x {
        y = y * 2;
    } else {
        y = y + 1;
    }
    y
'''

c = Compiler('program')
c.realize(source)
# print(c.parse_tree_str)
# print(c.wat_code)
print(c.result)
