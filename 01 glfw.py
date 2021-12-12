import glfw
from window import Window

def main():
    window = Window(400,400,"my opengl")
    window.main_loop()

if __name__ == "__main__":
    main()