x_size = 4
y_size = 4

prism_code = "mdp\n"
prism_code += "module grid\n"

prism_code += "    o_state : [0..{}] init 0;\n".format((x_size-1)*(y_size-1))
#prism_code += "    a_x : [0..{}];\n".format(x_size-1)
#prism_code += "    a_y : [0..{}];\n".format(y_size-1)

def stay(i,j,role):
 return "({0}_state' = {state})".format(role,state=i+(x_size*j))

def left(i,j,role):
    return "({0}_state' = {state})".format(role,state=(i-1)+(j*x_size))

def right(i,j,role):
    return "({0}_state' = {state})".format(role,state=(i+1)+(x_size*j))

def up(i,j,role):
    return "({0}_state' = {state})".format(role,state=i+((j+1)*x_size))

def down(i,j,role):
    return "({0}_state' = {state})".format(role,state=i+((j-1)*x_size))

def current(i,j,role="o"):
    return  "    [] {0}_state = {state} -> ".format(role,state=i+(j*x_size))

def is_bot_left(x,y):
    return x == 0 == j

def is_top_right(x,y):
    return x == x_size-1 and y == y_size-1

def is_top_left(x,y):
    return x == 0 and y == y_size-1

def is_bot_right(x,y):
    return x == x_size-1 and y == 0

def is_bot(y):
    return y == 0

def is_top(y):
    return y == y_size-1

def is_right(x):
    return x == x_size-1

def is_left(x):
    return x == 0

for i in range(x_size):
    for j in range(y_size):
        if is_bot_left(i,j):
            prism_code += current(i,j,role="o")+\
                    "1/3 : "+right(i,j,role="o")+\
                    "+ 1/3 : "+up(i,j,role="o")+\
                    "+ 1/3 : "+stay(i,j,role="o")+\
                    ";\n"
        elif is_top_right(i,j):
            prism_code += current(i,j,role="o")+\
                    "1/3 : "+left(i,j,role="o")+\
                    "+ 1/3 : "+down(i,j,role="o")+\
                    "+ 1/3 : "+stay(i,j,role="o")+\
                    ";\n"
        elif is_top_left(i,j):
            prism_code += current(i,j,role="o")+\
                    "1/3 : "+right(i,j,role="o")+\
                    "+ 1/3 : "+down(i,j,role="o")+\
                    "+ 1/3 : "+stay(i,j,role="o")+\
                    ";\n"
        elif is_bot_right(i,j):
            prism_code += current(i,j,role="o")+\
                    "1/3 : "+left(i,j,role="o")+\
                    "+ 1/3 : "+up(i,j,role="o")+\
                    "+ 1/3 : "+stay(i,j,role="o")+\
                    ";\n"
        elif is_bot(j):
            prism_code += current(i,j,role="o")+\
                    "1/4 : "+left(i,j,role="o")+\
                    "+ 1/4 : "+up(i,j,role="o")+\
                    "+ 1/4 : "+stay(i,j,role="o")+\
                    "+ 1/4 : "+right(i,j,role="o")+\
                    ";\n"
        elif is_top(j):
            prism_code += current(i,j,role="o")+\
                    "1/4 : "+left(i,j,role="o")+\
                    "+ 1/4 : "+down(i,j,role="o")+\
                    "+ 1/4 : "+stay(i,j,role="o")+\
                    "+ 1/4 : "+right(i,j,role="o")+\
                    ";\n"
        elif is_left(i):
            prism_code += current(i,j,role="o")+\
                    "1/4 : "+down(i,j,role="oo")+\
                    "+ 1/4 : "+up(i,j,role="o")+\
                    "+ 1/4 : "+stay(i,j,role="o")+\
                    "+ 1/4 : "+right(i,j,role="o")+\
                    ";\n"
        elif is_right(i):
            prism_code += current(i,j,role="o")+\
                    "1/4 : "+left(i,j,role="o")+\
                    "+ 1/4 : "+down(i,j,role="o")+\
                    "+ 1/4 : "+stay(i,j,role="o")+\
                    "+ 1/4 : "+up(i,j,role="o")+\
                    ";\n"
        else:
            prism_code += current(i,j,role="o")+\
                    "1/5 : "+left(i,j,role="o")+\
                    "+ 1/5 : "+down(i,j,role="o")+\
                    "+ 1/5 : "+stay(i,j,role="o")+\
                    "+ 1/5 : "+up(i,j,role="o")+\
                    "+ 1/5 : "+right(i,j,role="o")+\
                    ";\n"
        prism_code = prism_code.format(y=j,py=j+1,ny=j-1,nx=i-1,px=i+1,x=i)

prism_code += "endmodule"

print prism_code
