from frcmpsp.classes.instance import Instance
from frcmpsp.classes.model import Model
from frcmpsp.classes.plot import Plot


def main():

    # create simple test inst
    instance = Instance()
    instance.id = 0
    instance.V = [0, 1, 2, 3, 4, -1]
    instance.V_N = [1, 2, 3, 4]
    instance.V_S = [1, 3]
    instance.V_F = [2, 4]
    instance.E = [[0, 1], [0, 3], [1, 2], [3, 4], [2, -1], [4, -1]]
    instance.R = [0]
    instance.R_j = [[0], [0], [0], [0], [0], [0]]
    instance.wc_jr = [[0], [2.0], [4.0], [2.0], [4.0], [0]]
    instance.ub_u_jr = [[0], [2.0], [4.0], [2.0], [4.0], [0]]
    instance.lb_u_jr = [[0], [1.0], [2.0], [1.0], [2.0], [0]]
    instance.ub_a_r = [4.0]
    instance.lb_a_r = [4.0]
    instance.mu_r = [3.0]
    instance.sigma_r = [1.0]
    instance.w_j = [1.0, 1.0]
    instance.o_j = [1, 1]
    instance.d_j = [4, 4]

    # preprocessing
    instance.pre_processing()

    # solve gurobi model
    model = Model(instance)
    model.m1_dev(p=1e-5)

    # print solution
    model.print_solution()

    # plot
    plot = Plot(instance)
    plot.gantt_chart(use_tex=False, show_plot=True, save_plot=False, highlight_color="orangered")
    plot.capacity(highlight_color="orangered")
    plot.resource(highlight_color="orangered")


if __name__ == "__main__":
    main()
