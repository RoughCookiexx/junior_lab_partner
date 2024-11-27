import time
import junior_lab_partner


def your_task():
    print("Hey, you're doing something every 5 seconds. Amazing, right?")


def main(project_path):
    interval = 5 #* 60
    try:
        time.sleep(interval)
        while True:
            start_time = time.time()

            junior_lab_partner.refactor(project_path)

            elapsed = time.time() - start_time
            sleep_time = max(0, interval - elapsed)
            if sleep_time > 0:
                print(f"Waiting {sleep_time:.2f} seconds to stay on schedule...")
                time.sleep(sleep_time)
            else:
                print("Task took too long. Running late, just like you probably are.")
    except KeyboardInterrupt:
        print("\nOkay, fine. You win. Program terminated.")


if __name__ == '__main__':
    main('.')
