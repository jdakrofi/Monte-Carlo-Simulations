import numpy as np

class particle_monte_carlo:
    def __init__(self, random_state=None):
        """
            Properties of a block of materials:
            Total width of the block
            Number of layers different materials
            Colours of each layer to distinguish them from each other
        """
        self.total_width = 0.
        self.num_layers = 0.
        self.layers = {}  # Materials stored here
        self.colors = iter('rbygcmrbygcmrbygcmrbygcm')
        if random_state and type(random_state) == int:
            np.random.seed(random_state)

    def add_layer(self, width, scattering_probability, power_min, power_max):
        """
            Each layer of the target material is defined by its width; the likely-hood
            a fired particle will bounce off it (scattering probability); and how much
            speed the particle will when it bounces off (strength of scattering)

            Each layer (value) in the dictionary will be referenced by their start and
            end points (key) along the x-axis.
        """
        self.layers[(self.total_width, self.total_width+width)] = (scattering_probability, power_min, power_max, next(self.colors))
        self.total_width += width
        self.num_layers += 1

    def shoot_particle(self, velocity=1., return_hits=False, return_survival=False):
        """
            A particle shot with speed = velocity, takes a step in x-direction of x += speed.

            If the particle is in the material, a dice is rolled to determine whether it interacts with the material

            If is does its speed, the layer's scattering power is used to decrease its speed

            At the end of the simulation the following is returned:
            - "did the particle survive moving through the target material"
            - "where did the particle bounce"
            - "what was the speed and position of the particle when it died or exited the target material"
        """
        x = 0
        time = 0
        hits = []

        while velocity > 0 and x < self.total_width:
            time += 0.01
            x += velocity*time
            current_layer = None

            for region, scattering in self.layers.items():
                if region[0] < x <= region[1]:
                    current_layer = scattering[0]
                    power_min = scattering[1]
                    power_max = scattering[2]
                    break

            if current_layer:
                if np.random.uniform() < current_layer:
                    velocity -= np.random.uniform(power_min, power_max)

                    if return_hits:
                        hits.append(x)

        if x > self.total_width:
            x = self.total_width

        if return_hits:
            if x != hits[-1]:
                hits.append(x)
            return hits

        elif return_survival:
            if x == self.total_width:
                return 1
            else:
                return 0

        return x, velocity

    def plot_layer(self, return_ax=False, show_scatter_probs=False):
        """
            This function draws the target material such that interaction between the
            layers and the particle can be visualised.
        """
        plt.figure(dpi=100)
        ax = plt.gca()
        ax.set_yticks([])
        title = "Composition of Target"
        for layer, data in self.layers.items():
            x_start = layer[0]
            width = layer[1] - layer[0]
            color = data[3]
            ax.add_patch(patches.Rectangle((x_start, 0.25), width, 0.5, color=color))

            if show_scatter_probs:
                plt.annotate(xy=(x_start+width/2-0.2, 0.5), text=str(data[0]), color='w')

        plt.xlim(0, self.total_width)
        plt.xlabel("Distance")
        plt.title(title)
        if show_scatter_probs:
            title += " with Scattering Probabilities"
            plt.title(title)
            plt.show()
        if return_ax:
            return ax




