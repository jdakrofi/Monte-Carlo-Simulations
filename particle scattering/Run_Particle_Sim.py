import numpy as np
import matplotlib.pyplot as plt
from Particle_Monte_Carlo import particle_monte_carlo
from matplotlib.colors import LogNorm
plt.style.use('seaborn')


def run_block_sim():
    """
        This function creates a block consisting of 5-layers of materials
        A particle is then fired at the block.
        If the particle interacts with a layer, the point at which that interaction occurs is marked
        with a "."
        An "X" marks where the particle stops moving.
    """
    blocks = particle_monte_carlo()
    blocks.add_layer(width=4.5, scattering_probability=0.05, power_min=0.1, power_max=0.5)
    blocks.add_layer(width=1., scattering_probability=0.1, power_min=0.1, power_max=0.2)
    blocks.add_layer(width=0.5, scattering_probability=0.25, power_min=0.5, power_max=1)
    blocks.add_layer(width=5.5, scattering_probability=0.1, power_min=0.4, power_max=0.9)
    blocks.add_layer(width=0.5, scattering_probability=0.05, power_min=0.1, power_max=0.2)

    num_plots = 10

    for _ in range(num_plots):
        blocks.plot_layer()
        hits = blocks.shoot_particle(velocity=1, return_hits=True)
        plt.scatter(hits[:-1], [0.5 for _ in hits[:-1]], marker='o', c='k', s=20, zorder=10)
        plt.scatter(hits[-1], [0.5], marker='x', c='k', s=20, zorder=10)
        plt.title("Compostion of Target with Hits Shown")
        plt.show()


def stats():
    """
        This function creates a block consisting of 2 layers of materials
        Particles of increasing velocity are fired at the block.
        The following graphs are generated:
        - The material composition of the block with the scattering properties of each layer
        - Final Velocity Vs Initial Velocity
        - Final Position vs Initial Velocity
        - Number of particles vs Distance travelled
    """

    b = particle_monte_carlo()
    b.add_layer(1, 0.1, 0.5, 1)
    b.add_layer(2, 0.05, 0.2, 1)
    # print(b.layers)
    b.plot_layer(show_scatter_probs=True)

    results = []
    starting_velo = []
    for v in np.linspace(0.1, 2, 100):
        for _ in range(100):
            starting_velo.append(v)
            results.append(b.shoot_particle(velocity=v))

    xs, final_velo = zip(*results)
    plt.figure(dpi=100)
    plt.scatter(starting_velo, final_velo, s=40, alpha=0.1)
    plt.xlabel("Initial Velocity")
    plt.ylabel("Final Velocity")
    plt.show()

    plt.figure(dpi=100)
    plt.ylabel("Final Position")
    plt.xlabel("Initial Velocity")
    plot_x = xs
    plt.hist2d(starting_velo, plot_x, cmap=plt.cm.Reds, bins=(100,10), norm=LogNorm())
    plt.grid(False)
    plt.colorbar()
    plt.show()

    plt.figure(dpi=100)
    plt.hist(xs[3000:4000])
    plt.title("Initial Velocity = "+str(round(starting_velo[3000], 4)))
    plt.xlabel("Distance Travelled")
    plt.ylabel("Counts")
    plt.show()


def survival():
    """
        This function creates a block consisting of 2 layers of materials
        And a block consisting of 2 layers of materials
        Particles of increasing velocity are fired at both blocks.
        The following graphs are generated:
           - Survival rate (number particles that made it through the 2-layer block) vs Initial velocity
           - The material composition of the 5 layer block with the scattering properties of each layer
           - Survival rate vs Initial velocity for particles travelling through the 2-layer and 5-layer blocks
       """
    b = particle_monte_carlo()
    b.add_layer(1, 0.1, 0.5, 1)
    b.add_layer(2, 0.05, 0.2, 1)
    # starting_velo = []
    survival_rate = []

    for v in np.linspace(.1, 2.5, 200):
        results = []

        for _ in range(5000):
            results.append(b.shoot_particle(velocity=v, return_survival=True))
        survival_rate.append((v, np.sum(results)/len(results)))

    vs, surv_rate = zip(*survival_rate)
    plt.figure(dpi=100)
    plt.plot(vs, surv_rate, '--o', lw=0.5)
    plt.xlabel("Initial Velocity")
    plt.ylabel("Survival Rate")
    plt.title("Particle Survival Rate vs Initial Velocity")
    plt.show()

    # def complex_material():
    b = particle_monte_carlo()
    b.add_layer(4.5, 0.2, 0.1, 0.5)
    b.add_layer(1.5, 0.5, 0.1, 0.2)
    b.add_layer(1.0, 0.25, 0.05, 0.1)
    b.add_layer(3.5, 0.4, 0.4, 0.9)
    b.add_layer(1.5, 0.1, 0.1, 0.2)
    b.plot_layer(show_scatter_probs=True)
    # starting_velo = []
    survival_rate = []
    for v in np.linspace(0.1, 2.5, 200):
        results = []
        for _ in range(10000):
            results.append(b.shoot_particle(velocity=v, return_survival=True))
        survival_rate.append((v, np.sum(results)/len(results)))

    vs2, surv_rate2 = zip(*survival_rate)
    plt.figure(dpi=100)
    plt.plot(vs, surv_rate, '--o', lw=0.5, label='2 Layers')
    plt.plot(vs2, surv_rate2, '--or', lw=0.5, label='5 Layers')
    plt.xlabel("Initial Velocity")
    plt.ylabel("Survival Rate")
    plt.title("Particle Survival Rate vs Initial Velocity")
    plt.legend(loc="upper left")
    plt.show()


if __name__ == "__main__":
    #run_block_sim()
    #stats()
    survival()



