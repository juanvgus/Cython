from math import sqrt

class Planet(object):
    def __init__(self):
        self.x = 1.0
        self.y = 0.0
        self.z = 0.0
        self.vx = 0.0
        self.vy = 0.5
        self.vz = 0.0
        self.m = 1.0

def single_step(planet,dt):
    distance = sqrt(planet.x**2 + planet.y**2 + planet.z**2)
    fx = -planet.x / (distance**3)
    fy = -planet.y / (distance**3)
    fz = -planet.z / (distance**3)
    

    planet.x += dt * planet.vx
    planet.y += dt * planet.vy
    planet.z += dt * planet.vz

    planet.vx += (dt * fx) / planet.m
    planet.vy += (dt * fy) / planet.m
    planet.vz += (dt * fz) / planet.m

def step_time(planet, time_span, n_steps):
    dt = time_span / n_steps
    for j in range(n_steps):
	    single_step(planet, dt)
