from logic.SplitesSheet import SplitesSheet

class Animation:
    def __init__(self, spritesheet: str, y: int, lenght: int ):
        self.animation = [SplitesSheet(spritesheet).get_image(frame * 64, y, 64, 64) for frame in range(lenght)]
        self.image_index = 0
        self.animation_speed = 0.2 # Скорость анимации, можно регулировать
        self.frame_counter = 0

    def update(self):
        self.frame_counter += self.animation_speed
        if self.frame_counter >= len(self.animation):
            self.frame_counter = 0

        self.image_index = int(self.frame_counter)
        self.image = self.animation[self.image_index]
        return self.image