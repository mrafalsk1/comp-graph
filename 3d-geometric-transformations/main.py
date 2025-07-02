import pygame
import numpy as np
import math

WIDTH, HEIGHT = 800, 600
BG_COLOR = (20, 20, 40)
CUBE_COLOR = (200, 200, 255)
TEXT_COLOR = (230, 230, 230)
FPS = 60


class Cube3D:
    def __init__(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("3D Transformations with Pygame")
        self.clock = pygame.time.Clock()

        self.font_title = pygame.font.Font(None, 32)
        self.font_instructions = pygame.font.Font(None, 24)

        self.vertices = np.array(
            [
                [-0.5, -0.5, -0.5, 1],
                [0.5, -0.5, -0.5, 1],
                [0.5, 0.5, -0.5, 1],
                [-0.5, 0.5, -0.5, 1],
                [-0.5, -0.5, 0.5, 1],
                [0.5, -0.5, 0.5, 1],
                [0.5, 0.5, 0.5, 1],
                [-0.5, 0.5, 0.5, 1],
            ]
        )

        self.edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0),
            (4, 5),
            (5, 6),
            (6, 7),
            (7, 4),
            (0, 4),
            (1, 5),
            (2, 6),
            (3, 7),
        ]

        self.scale = 150
        self.angle_x = self.angle_y = self.angle_z = 0
        self.pos_x = WIDTH / 2
        self.pos_y = HEIGHT / 2
        self.pos_z = 0

    def draw_tutorial(self):
        """Renders the help and controls text on the screen."""

        instruction_lines = [
            ("Controles:", self.font_title),
            ("", self.font_instructions),  # Blank line for spacing
            ("Mover: Setas ou W, A, S, D", self.font_instructions),
            ("Escala: Teclas + e -", self.font_instructions),
            ("Girar Eixo X: NumPad 8 / 2", self.font_instructions),
            ("Girar Eixo Y: NumPad 4 / 6", self.font_instructions),
            ("Girar Eixo Z: NumPad 7 / 9", self.font_instructions),
        ]

        x, y = 15, 15

        for text, font in instruction_lines:
            text_surface = font.render(text, True, TEXT_COLOR)
            self.screen.blit(text_surface, (x, y))
            y += font.get_height() + 2  # Move to the next line

    def get_scale_matrix(self):
        s = self.scale
        return np.array([[s, 0, 0, 0], [0, s, 0, 0], [0, 0, s, 0], [0, 0, 0, 1]])

    def get_rotation_x_matrix(self):
        ax = self.angle_x
        return np.array(
            [
                [1, 0, 0, 0],
                [0, math.cos(ax), -math.sin(ax), 0],
                [0, math.sin(ax), math.cos(ax), 0],
                [0, 0, 0, 1],
            ]
        )

    def get_rotation_y_matrix(self):
        ay = self.angle_y
        return np.array(
            [
                [math.cos(ay), 0, math.sin(ay), 0],
                [0, 1, 0, 0],
                [-math.sin(ay), 0, math.cos(ay), 0],
                [0, 0, 0, 1],
            ]
        )

    def get_rotation_z_matrix(self):
        az = self.angle_z
        return np.array(
            [
                [math.cos(az), -math.sin(az), 0, 0],
                [math.sin(az), math.cos(az), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
            ]
        )

    def get_translation_matrix(self):
        return np.array(
            [
                [1, 0, 0, self.pos_x],
                [0, 1, 0, self.pos_y],
                [0, 0, 1, self.pos_z],
                [0, 0, 0, 1],
            ]
        )

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pos_x -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pos_x += 5
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.pos_y -= 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.pos_y += 5
        if keys[pygame.K_KP4]:
            self.angle_y += 0.03
        if keys[pygame.K_KP6]:
            self.angle_y -= 0.03
        if keys[pygame.K_KP8]:
            self.angle_x += 0.03
        if keys[pygame.K_KP2]:
            self.angle_x -= 0.03
        if keys[pygame.K_KP7]:
            self.angle_z += 0.03
        if keys[pygame.K_KP9]:
            self.angle_z -= 0.03
        if keys[pygame.K_PLUS] or keys[pygame.K_KP_PLUS]:
            self.scale += 5
        if keys[pygame.K_MINUS] or keys[pygame.K_KP_MINUS]:
            self.scale = max(10, self.scale - 5)

        return True

    def draw(self):
        self.screen.fill(BG_COLOR)

        self.draw_tutorial()

        scale_matrix = self.get_scale_matrix()
        rotation_x_matrix = self.get_rotation_x_matrix()
        rotation_y_matrix = self.get_rotation_y_matrix()
        rotation_z_matrix = self.get_rotation_z_matrix()
        translation_matrix = self.get_translation_matrix()

        rotation_matrix = rotation_x_matrix @ rotation_y_matrix @ rotation_z_matrix
        transform_matrix = translation_matrix @ rotation_matrix @ scale_matrix

        projected_points = []
        for vertex in self.vertices:
            transformed_vertex = transform_matrix @ vertex.T
            x2d, y2d = transformed_vertex[0], transformed_vertex[1]
            projected_points.append((x2d, y2d))

        for edge in self.edges:
            start_point = projected_points[edge[0]]
            end_point = projected_points[edge[1]]
            pygame.draw.line(self.screen, CUBE_COLOR, start_point, end_point, 2)

        for point in projected_points:
            pygame.draw.circle(
                self.screen, CUBE_COLOR, (int(point[0]), int(point[1])), 4
            )

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()


if __name__ == "__main__":
    app = Cube3D()
    app.run()
