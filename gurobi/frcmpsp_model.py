from frcmpsp.frcmpsp_data import Data
from gurobipy.gurobipy import *


class Model(object):

    def __init__(self):
        """
        FRCMPSP data structure object
        @author    Robert Brachmann
        @version   1.0
        """
        self.id = ""
        self.name = ""
        self.data = None

    def build(self, model_data):

        try:
            # Get data
            self.data = model_data

            # Create model
            model = Model("FRCMPSP")

            # Create decision variables
            objective_value = model.addVar(name="objective_value")
            x_jt = model.addVars(model_data.j, model_data.t, name="x_jt", vtype=GRB.BINARY)
            y_jt = model.addVars(model_data.j, model_data.t, name="y_jt", vtype=GRB.BINARY)
            q_rjt = model.addVars(model_data.r, model_data.j, model_data.t, name="q_rjt")
            b_rt = model.addVars(model_data.r, model_data.t, name="b_rt")
            v_jt = model.addVars(model_data.j, model_data.t, name="v_jt")
            a_rt = model.addVars(model_data.r, model_data.t, name="a_rt")

            # Set objective
            model.setObjective(objective_value, GRB.MINIMIZE)

            # Set objective function

            # Solve model
            model.optimize()

        # : exceptions :
        except GurobiError as e:
            print('Error code ' + str(e.message) + ": " + str(e))

        return