from . import line_plot
import argparse

def cli():
    parser= argparse.ArgumentParser(prog="plotting_graphs")
    parser.add_argument("--no-repeat", help="Suppress Repeat", action= "store_true")

    parser.add_argument("--red", help="Plot line in red", action= "store_true")

    args = parser.parse_args()

    animation = line_plot.LinePlot(**vars(args))
    animation.plot(**vars(args))