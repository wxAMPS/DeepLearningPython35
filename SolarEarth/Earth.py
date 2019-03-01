import numpy as np

radius = 100
GM = 100  # v = sqrt(GM/r)
d_theta = -0.1


class Earth:
    def __init__(self, canvas, sun, v_init):
        self.canvas = canvas
        # list comprehension, give the center coord of the sun
        self.sun_pos = np.array([coord + 10 for coord in canvas.coords(sun)][0:2])
        self.cur_pos = self.sun_pos - [0, radius]
        self.old_pos = self.cur_pos[:]
        self.id = canvas.create_oval((self.cur_pos - 10).tolist(),
                                     (self.cur_pos + 10).tolist(),
                                     fill='blue')
        self.theta = 0
        self.v = np.array(v_init)  # initial speed

    def __getitem__(self, item):
        # return the current earth coordinate
        return self.cur_pos[item]

    def orbit(self):
        self.theta += d_theta
        self.cur_pos = np.array([self.sun_pos[0] + radius * np.sin(self.theta),
                                 self.sun_pos[1] - radius * np.cos(self.theta)])
        self.update_pos()

    def dynamic_orbit(self, dt):
        r_vector = self.cur_pos - self.sun_pos
        r = np.linalg.norm(r_vector)
        self.a = - GM / r ** 3 * r_vector  # acceleration
        self.v = self.v + self.a * dt

        self.cur_pos = self.cur_pos + self.v * dt
        self.update_pos()

    def update_pos(self):
        dx, dy = self.cur_pos - self.old_pos
        self.canvas.move(self.id, dx, dy)
        self.canvas.create_line(self.old_pos.tolist(), self.cur_pos.tolist(), dash=(3, 5), tags='line_tag')
        self.old_pos = self.cur_pos

    def __del__(self):
        # self.cur_pos = self.sun_pos - np.array([0, radius])
        # self.update_pos()
        self.canvas.delete(self.id)
        self.canvas.delete('line_tag')
