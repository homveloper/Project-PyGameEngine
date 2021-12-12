import glfw

class Window():
    def __init__(self, width: int, height: int, title: str) -> None:
        if not glfw.init():
            raise Exception("glfw not initialized")

        self.window = glfw.create_window(
            width=width, height=height, title=title, monitor=None, share=None)
        
        if not self.window:
            glfw.terminate()
            raise Exception("glfw window can not be created")

        glfw.make_context_current(self.window)

    def main_loop(self):
        while not glfw.window_should_close(self.window):
            glfw.poll_events()
            glfw.swap_buffers(self.window)
        
        glfw.terminate()