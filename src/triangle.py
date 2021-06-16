"""
triangle.py
=================================
Cool module that draws a triangle
"""

def do_a_thing(n):
    '''Prints a cool triangle that's `n` stars wide
    '''
    for i in range(n):
        print('*'*(i+1))

class TriangleRenderer:
    """A renderer class for drawing cool triangles

    Parameters
    ----------
    n : int
        Width of the cool triangle to be rendered

    """

    def __init__(self, n):
        self.n = n

    def draw(self):
        """Render cool triangle

        """
        self.__draw_triangle()

    def __draw_triangle(self):
        for i in range(self.n):
            print('*'*(i+1))

