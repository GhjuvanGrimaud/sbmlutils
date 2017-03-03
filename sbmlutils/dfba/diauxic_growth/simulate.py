from __future__ import print_function, division

# directory to write files to
import os
import timeit
from sbmlutils.dfba.simulator import Simulator

import dgsettings
import model_factory
directory = os.path.join(dgsettings.out_dir, 'v{}'.format(model_factory.version))
sbml_top_path = os.path.join(directory, dgsettings.top_file)


def simulate_diauxic_growth(sbml_top_path, tend, steps):
    """ Simulate the diauxic growth model.

    :return: solution data frame
    """

    # Load model in simulator
    sim = Simulator(sbml_top_path=sbml_top_path)

    # Run simulation of hybrid model
    start_time = timeit.default_timer()
    df = sim.simulate(tstart=0.0, tend=tend, steps=steps)
    elapsed = timeit.default_timer() - start_time

    print("\nSimulation time: {}\n".format(elapsed))

    sim.plot_reactions(os.path.join(directory, "reactions.png"), df, rr_comp=sim.rr_comp)
    sim.plot_species(os.path.join(directory, "species.png"), df, rr_comp=sim.rr_comp)
    sim.save_csv(os.path.join(directory, "simulation.csv"), df)

    print_species(os.path.join(directory, "species_growth.png"), df)
    return df


def print_species(filepath, df):
    """ Print diauxic species.

    :param df:
    :return:
    """
    from matplotlib import pylab as plt

    plt.rcParams.update({
        'axes.labelsize': 'large',
        'axes.labelweight': 'bold',
        'axes.titlesize': 'large',
        'axes.titleweight': 'bold',
        'legend.fontsize': 'small',
        'xtick.labelsize': 'large',
        'ytick.labelsize': 'large',
    })

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(14, 14))

    for ax in (ax1, ax3):
        ax.plot(df.time, df['[Ac]'],
                 linestyle='-', marker='s', color='darkred', label="Ac")
        ax.plot(df.time, df['[Glcxt]'],
             linestyle='-', marker='s', color='darkblue', label="Glcxt")
        ax.plot(df.time, df['[O2]'],
             linestyle='-', marker='s', color='darkgreen', label="O2")
    ax3.set_yscale('log')
    ax3.set_ylim([10E-12, 15])

    for ax in (ax2, ax4):
        ax.plot(df.time, df['[X]'],
             linestyle='-', marker='s', color='black', label="X biomass")
    ax4.set_yscale('log')

    for ax in (ax1, ax3):
        ax.set_ylabel('Concentration [?]')

    for ax in (ax2, ax4):
        ax.set_ylabel('Biomass [?]')

    for ax in (ax1, ax2, ax3, ax4):
        ax.set_title('Diauxic Growth')
        ax.set_xlabel('time [h]')
        ax.legend()

    fig.savefig(filepath)

if __name__ == "__main__":
    tend = 15
    steps = 10*tend
    import logging
    # logging.getLogger().setLevel(logging.INFO)
    df = simulate_diauxic_growth(sbml_top_path, tend, steps)

