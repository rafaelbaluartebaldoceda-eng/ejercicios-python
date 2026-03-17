class Rectangle:
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    def set_width(self,value):
        self.ancho=value
    def set_height(self, value):
        self.alto=value
    def get_area(self):
        return self.ancho*self.alto
    def get_perimeter(self):
        return 2*(self.ancho+self.alto)
    def get_diagonal(self):
        return (self.ancho**2 + self.alto**2) ** 0.5
    def get_picture(self):
        if self.ancho>50 or self.alto>50:
            return "Too big for a picture."
        picture=""
        for i in range(self.alto):
            picture+="*" * self.ancho + "\n"
        return picture
    def get_amount_inside(self,another_figure):
        horizontal=self.ancho//another_figure.ancho
        vertical=self.alto//another_figure.alto
        return horizontal*vertical
    def __str__(self):
        return f"Rectangle(width={self.ancho}, height={self.alto})"
class Square(Rectangle):
    def __init__(self,lado):
        super().__init__(lado,lado)
    def set_width(self,lado):
        self.ancho=lado
        self.alto=lado
    def set_height(self,lado):
        self.alto=lado
        self.ancho=lado
    def set_side(self,lado):
        self.alto=lado
        self.ancho=lado
    def __str__(self):
        return f"Square(side={self.ancho})"