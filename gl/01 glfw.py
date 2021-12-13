import glfw
from lib.window import Window
import numpy as np
from OpenGL.GL import *

from math import *

def main():

    if not glfw.init():
        raise Exception("glfw not initialized")

    window = glfw.create_window(
        width=400, height=400, title="my opengl", monitor=None, share=None)
    
    if not window:
        glfw.terminate()
        raise Exception("glfw window can not be created")

    glfw.make_context_current(window)

    # cordinate  x  y  z
    # top        0  1  0
    # bottom     0 -1  0
    # left      -1  0  0
    # right      1  0  0
    # center     0  0  0
    vertices = [-0.5, -0.5, 0.0,
                 0.5, -0.5, 0.0,
                 -0.5,  0.5, 0.0]

    # R G B
    colors = [1.0, 0.0, 0.0,
              0.0, 1.0, 0.0,
              0.0, 0.0, 1.0]

    vertices = np.array(vertices, dtype=np.float32)
    colors = np.array(colors,dtype=np.float32)

    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(3, GL_FLOAT, 0, vertices)
    glEnableClientState(GL_COLOR_ARRAY)
    glColorPointer(3, GL_FLOAT, 0, colors)

    glClearColor(0,0.1,0.1,1)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        # return elapsed time, since init was called
        ct = glfw.get_time()

        glLoadIdentity()
        glScale(abs(sin(ct)),abs(sin(ct)), 1)
        glRotatef(sin(ct) * 45, 0, 0, 1)
        glTranslatef(sin(ct), 0, 0)

        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)

    glfw.terminate()

if __name__ == "__main__":
    main()