from turtle import Turtle 

class Scoer_(Turtle):
    def __init__(self):
        super().__init__()
        self.scoer=0
        self.highscoer=self.any()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,290)
        self.update_scoerbard()
        
    def update_scoerbard(self):
        self.write(f'scoer:{self.scoer}     High Scoer: {self.highscoer}',align='center',font=('arial',20,'bold'))
    
    def any(self):
        with open(r"C:\Users\ASUS\Desktop\my_python_files\snake_game\highscoer.text",'r') as file:
            return int(file.read())

    def seve_highscoer(self):
        with open(r"C:\Users\ASUS\Desktop\my_python_files\snake_game\highscoer.text",'w') as file:
            file.write(str(self.scoer))

    def increase_scoer(self):
        self.clear()
        self.scoer+=1
        self.update_scoerbard()

    def game_over(self):
        self.clear()
        self.screen.bgcolor('dark red')
        self.goto(0,0)

        if self.scoer > self.highscoer:
            self.highscoer=self.scoer
            self.seve_highscoer()
        self.write(f'------------GameOver------------\n\n           FainlyScoer:{self.scoer}\n           High Scoer :{self.highscoer}',align='center',font=('arial',20,'normal'))
    


