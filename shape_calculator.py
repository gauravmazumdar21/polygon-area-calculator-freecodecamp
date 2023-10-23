class Rectangle:

      def __init__(self, rect_width, rect_height):
        self.rect_width = rect_width
        self.rect_height = rect_height

      def __str__(self):
        return "Rectangle(width=" + str(self.rect_width) + \
               ", height=" + str(self.rect_height) + ")"

      def set_width(self, rect_width):
        self.rect_width = rect_width

      def set_height(self, rect_height):
        self.rect_height = rect_height

      def get_area(self):
        return self.rect_width * self.rect_height

      def get_perimeter(self):
        return 2 * (self.rect_width + self.rect_height)

      def get_diagonal(self):
        return (self.rect_width ** 2 + self.rect_height ** 2) ** .5

      def get_picture(self):
        if self.rect_width > 50 or self.rect_height > 50:
          return "Too big for picture."
        rect = ("*" * self.rect_width + "\n") * self.rect_height
        return rect

      def get_amount_inside(self, shape):
        max_width = self.rect_width // shape.rect_width
        max_height = self.rect_height // shape.rect_height
        return max_width * max_height


class Square(Rectangle):

      def __init__(self, side_length):
        super().__init__(side_length, side_length)

      def __str__(self):
        return "Square(side=" + str(self.rect_width) + ")"

      def set_side(self, side_length):
        self.rect_width = side_length
        self.rect_height = side_length

      def set_width(self, side_length):
        self.rect_width = side_length
        self.rect_height = side_length

      def set_height(self, side_length):
        self.rect_width = side_length
        self.rect_height = side_length
