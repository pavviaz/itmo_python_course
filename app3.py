import multiprocessing
import time
import codecs
from datetime import datetime


def process_a(queue_ab, pipe_a_main):
    while True:
        message = queue_ab.get()
        if message == "STOP":
            break
        processed_message = message.lower()
        pipe_a_main.send(processed_message)
        time.sleep(5)


def process_b(pipe_b_main):
    while True:
        message = pipe_b_main.recv()
        if message == "STOP":
            break
        encoded_message = codecs.encode(message, "rot_13")
        pipe_b_main.send(encoded_message)


if __name__ == "__main__":
    queue_ab = multiprocessing.Queue()
    pipe_a_main, pipe_b_main = multiprocessing.Pipe()

    process_a_instance = multiprocessing.Process(
        target=process_a, args=(queue_ab, pipe_a_main)
    )
    process_b_instance = multiprocessing.Process(target=process_b, args=(pipe_b_main,))

    process_a_instance.start()
    process_b_instance.start()

    try:
        while True:
            user_input = input("Enter a message: ")
            if user_input.lower() == "stop":
                break

            print(f"Time on input: {datetime.now().strftime('%H:%M:%S.%f')}\n")
            queue_ab.put(user_input)

            processed_message = pipe_a_main.recv()
            print(
                f"Processed message: {processed_message};\t"
                f"Time on output = {datetime.now().strftime('%H:%M:%S.%f')}"
            )
            print("---------")
    except KeyboardInterrupt:
        pass
    finally:
        queue_ab.put("STOP")
        pipe_a_main.send("STOP")
        process_a_instance.join()
        pipe_a_main.close()
        pipe_b_main.send("STOP")
        process_b_instance.join()
        pipe_b_main.close()
