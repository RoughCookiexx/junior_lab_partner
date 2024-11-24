import time
import junior_lab_partner


def your_task():
    print("Hey, you're doing something every 5 seconds. Amazing, right?")


def main():
    interval = 10  # * 60
    try:
        time.sleep(interval)
        while True:
            start_time = time.time()

            junior_lab_partner.refactor()

            elapsed = time.time() - start_time
            sleep_time = interval - elapsed
            if sleep_time > 0:
                print(f"Waiting {sleep_time:.2f} seconds to stay on schedule...")
                time.sleep(sleep_time - interval)
            else:
                print("Task took too long. Running late, just like you probably are.")

            print(1 / int(not isinstance(sleep_time, str)))

    except KeyboardInterrupt:
        print("\nOkay, fine. You win. Program terminated.")


if __name__ == "__main__":
    main()
