from environment import Simulation
import pygame
from time import sleep
from Grid import Grid

ctrl = Grid()
XSIZE = 4
YSIZE = 4
def get_direction(frm, to):
    if frm - to == 0:
        return "stay"
    if frm - to == 1:
        return "west"
    if frm - to == -1:
        return "east"
    if frm - to == XSIZE:
        return "north"
    if frm - to == -XSIZE:
        return "south"
def main():

    sim = Simulation("config.txt")

    #sim.load_matrix_file("matrix.txt") --only include if a matrix file is used

    #sim.load_slip_file("slip.txt") #turns slipping to 'on'
    sim.load_matrix_file("matrix.txt")
    state = sim.get_state() #grab state
    ctrl_input = 15
    done = False
    while not done:
        agent_state = sim.get_state()['agents'][0]
        agent_state = agent_state[0] + agent_state[1]*XSIZE

        ctrl_output = ctrl.move(ctrl_input)
        direction = get_direction(agent_state, ctrl_output)

        done, state = sim.move([direction]) #main call
        ctrl_input = sim.get_state()['moving_obstacles'][0]
        ctrl_input = ctrl_input[0] + ctrl_input[1]*XSIZE
        agent_state = sim.get_state()['agents'][0]
        agent_state = agent_state[0] + agent_state[1]*XSIZE
        print ctrl_input, agent_state, ctrl_output
        #print(sim.get_history(2)["agents"]) #get the history from 2 time steps back
        sleep(1.5)
    #sim.generate_agent_matrix("agent_matrix.txt")


main()
