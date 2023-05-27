import pygame

class ToggleSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet, pos, letter, alien_pos, eng_pos):
        super().__init__()
        self.sprite_sheet = sprite_sheet
        self.rect = pygame.Rect(pos[0], pos[1], 64, 64)
        self.frames = self.load_frames(alien_pos, eng_pos)
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.letter = letter

    def load_frames(self, alien_pos, eng_pos):
        frames = []

        frames.append(
            self.sprite_sheet.subsurface(
                pygame.Rect(
                    alien_pos[0]*64, 
                    alien_pos[1]*64, 
                    64, 
                    64
        )))
        frames.append(
            self.sprite_sheet.subsurface(
                pygame.Rect(
                    eng_pos[0]*64, 
                    eng_pos[1]*64, 
                    64, 
                    64
        )))
        return frames

    def toggle_frame(self):
        self.current_frame = (self.current_frame + 1) % 2
        self.image = self.frames[self.current_frame]

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)
