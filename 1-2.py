import tkinter as tk
from PIL import Image, ImageTk
import os

class ArkanoidGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Мячики летают туда сюда")
        
        # Use absolute paths
        base_path = os.path.dirname(os.path.abspath(__file__))
        background_path = os.path.join(base_path, "background.jpg")
        bogban_path = os.path.join(base_path, "bogban.jpg")
        pavelreckrentovich_path = os.path.join(base_path, "pavelreckrentovich.jpg")
        
        # Resize images
        self.background_image = ImageTk.PhotoImage(Image.open(background_path).resize((960, 540)))
        self.bogban_image = ImageTk.PhotoImage(Image.open(bogban_path).resize((50, 50)))
        self.pavelreckrentovich_image = ImageTk.PhotoImage(Image.open(pavelreckrentovich_path).resize((50, 50)))
        
        self.canvas = tk.Canvas(root, width=960, height=540)
        self.canvas.pack()
        
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image)
        
        self.ball1 = self.canvas.create_image(30, 100, anchor=tk.CENTER, image=self.bogban_image)
        self.ball2 = self.canvas.create_image(170, 100, anchor=tk.CENTER, image=self.pavelreckrentovich_image)

        self.ball1_velocity_x = 5  
        self.ball1_velocity_y = -5  
        self.ball2_velocity_x = -5  
        self.ball2_velocity_y = 5  
        
        self.start_button = tk.Button(root, text="ЙОУ ГОУ", command=self.start_game)
        self.start_button.pack()
        
        self.is_running = False
        self.root.after(50, self.update_game)

    def start_game(self):
        self.is_running = not self.is_running
        self.start_button.config(text="нашенская остановочка" if self.is_running else "ЙОУ ГОУ")

    def update_game(self):
        if self.is_running:
            self.ball1_velocity_x, self.ball1_velocity_y = self.move_ball(self.ball1, self.ball1_velocity_x, self.ball1_velocity_y)
            self.ball2_velocity_x, self.ball2_velocity_y = self.move_ball(self.ball2, self.ball2_velocity_x, self.ball2_velocity_y)
            self.check_collision()
        self.root.after(50, self.update_game)

    def move_ball(self, ball, velocity_x, velocity_y):
        self.canvas.move(ball, velocity_x, velocity_y)
        ball_position = self.canvas.coords(ball)
        
        if ball_position[1] <= 0 or ball_position[1] >= 540:
            velocity_y = -velocity_y
            self.create_sparks(ball_position[0], ball_position[1])
        if ball_position[0] <= 0 or ball_position[0] >= 960:
            velocity_x = -velocity_x
            self.create_sparks(ball_position[0], ball_position[1])
        
        return velocity_x, velocity_y

    def check_collision(self):
        pos1 = self.canvas.coords(self.ball1)
        pos2 = self.canvas.coords(self.ball2)
        
        if self.is_collision(pos1, pos2):
            self.ball1_velocity_x, self.ball2_velocity_x = -self.ball1_velocity_x, -self.ball2_velocity_x
            self.ball1_velocity_y, self.ball2_velocity_y = -self.ball1_velocity_y, -self.ball2_velocity_y

    def is_collision(self, pos1, pos2):
        return not (pos1[0] + 25 < pos2[0] - 25 or pos1[0] - 25 > pos2[0] + 25 or pos1[1] + 25 < pos2[1] - 25 or pos1[1] - 25 > pos2[1] + 25)

    def create_sparks(self, x, y):
        for _ in range(5):
            spark = self.canvas.create_oval(x-5, y-5, x+5, y+5, fill='red')
            self.canvas.after(100, self.canvas.delete, spark)  

if __name__ == "__main__":
    root = tk.Tk()
    game = ArkanoidGame(root)
    root.mainloop()
