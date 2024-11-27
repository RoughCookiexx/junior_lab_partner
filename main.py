import time

import pygame

import junior_lab_partner


def your_task():
    print("Hey, you're doing something every 5 seconds. Amazing, right?")


def main(project_path):
    interval = 5 * 60
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Junior Lab Partner")
    pygame.font.init()
    font = pygame.font.Font(None, 256)
    clock = pygame.time.Clock()
    try:
        start_time = time.time()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise KeyboardInterrupt
                # Add focus check if necessary
                if event.type == pygame.ACTIVEEVENT:
                    if event.gain == 0:  # Lost focus
                        print("Window lost focus, continuing...")
            elapsed = time.time() - start_time

            minutes, seconds = divmod(interval - elapsed, 60)
            formatted_time = f"{int(minutes)}:{int(seconds):02}"
            text = font.render(formatted_time, True, (255, 255, 255))
            screen.fill((0, 255, 0))
            screen.blit(text, (100, 100))
            pygame.display.flip()
            if elapsed > interval:
                junior_lab_partner.refactor(project_path)
                start_time = time.time()
            clock.tick(60)
    except KeyboardInterrupt:
        print("\nOkay, fine. You win. Program terminated.")


if __name__ == '__main__':
    main('C:\\Users\\Tommy\\PycharmProjects\\breakout-vs-chatgpt')
