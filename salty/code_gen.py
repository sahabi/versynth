x_size = 4
y_size = 4

salty_code = "controller grid where\n"
salty_code += "input o_state : Int = 14\n"
salty_code += "output a_state : Int = 0\n"
salty_code += "env_trans\n"

#salty_code += "    a_x : [0..{}];\n".format(x_size-1)
#salty_code += "    a_y : [0..{}];\n".format(y_size-1)

def stay(i,j,role):
 return "({0}_state' == {state})".format(role,state=i+(x_size*j))

def left(i,j,role):
    return "({0}_state' == {state})".format(role,state=(i-1)+(j*x_size))

def right(i,j,role):
    return "({0}_state' == {state})".format(role,state=(i+1)+(x_size*j))

def up(i,j,role):
    return "({0}_state' == {state})".format(role,state=i+((j+1)*x_size))

def down(i,j,role):
    return "({0}_state' == {state})".format(role,state=i+((j-1)*x_size))

def current(i,j,role):
    return  "    {0}_state == {state} -> ".format(role,state=i+(j*x_size))

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

for ob in ["o","a"]:
    for i in range(x_size):
        for j in range(y_size):
            if is_bot_left(i,j):
                salty_code += current(i,j,role=ob)\
                            +right(i,j,role=ob)\
                            +"\/"+up(i,j,role=ob)\
                            +"\/"+stay(i,j,role=ob)\
                            +"\n"
            elif is_top_right(i,j):
                salty_code += current(i,j,role=ob)\
                            +left(i,j,role=ob)\
                            +"\/"+down(i,j,role=ob)\
                            +"\/"+stay(i,j,role=ob)\
                            +"\n"
            elif is_top_left(i,j):
                salty_code += current(i,j,role=ob)\
                            +right(i,j,role=ob)\
                            +"\/"+down(i,j,role=ob)\
                            +"\/"+stay(i,j,role=ob)\
                            +"\n"
            elif is_bot_right(i,j):
                salty_code += current(i,j,role=ob)\
                            +left(i,j,role=ob)\
                            +"\/"+up(i,j,role=ob)\
                            +"\/"+stay(i,j,role=ob)\
                            +"\n"
            elif is_bot(j):
                salty_code += current(i,j,role=ob)\
                            +left(i,j,role=ob)\
                            +"\/"+up(i,j,role=ob)\
                            +"\/"+stay(i,j,role=ob)\
                            +"\/"+right(i,j,role=ob)\
                            +"\n"
            elif is_top(j):
                salty_code += current(i,j,role=ob)\
                            +left(i,j,role=ob)\
                            +"\/"+down(i,j,role=ob)\
                            +"\/"+stay(i,j,role=ob)\
                            +"\/"+right(i,j,role=ob)\
                            +"\n"
            elif is_left(i):
                salty_code += current(i,j,role=ob)\
                            +down(i,j,role=ob)\
                            +"\/"+up(i,j,role=ob)\
                            +"\/"+stay(i,j,role=ob)\
                            +"\/"+right(i,j,role=ob)\
                            +"\n"
            elif is_right(i):
                salty_code += current(i,j,role=ob)\
                            +left(i,j,role=ob)\
                            +"\/"+down(i,j,role=ob)\
                            +"\/"+stay(i,j,role=ob)\
                            +"\/"+up(i,j,role=ob)\
                            +"\n"
            else:
                salty_code += current(i,j,role=ob)\
                            +left(i,j,role=ob)\
                            +"\/"+down(i,j,role=ob)\
                            +"\/"+stay(i,j,role=ob)\
                            +"\/"+up(i,j,role=ob)\
                            +"\/"+right(i,j,role=ob)\
                            +"\n"
            salty_code = salty_code.format(y=j,py=j+1,ny=j-1,nx=i-1,px=i+1,x=i)

print salty_code
