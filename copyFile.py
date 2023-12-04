import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import os
from dotenv import load_dotenv

load_dotenv()  

class FileHandler(FileSystemEventHandler):
    def __init__(self, src_file, dest_file):
        super().__init__()
        self.src_file = src_file
        self.dest_file = dest_file

    def on_modified(self, event):
        if event.src_path == self.src_file:
            try:
                print(f"File {os.path.basename(self.src_file)} modified. Copying changes to {os.path.basename(self.dest_file)}.")
                shutil.copy2(self.src_file, self.dest_file)
                print("Copy complete.")
            except Exception as e:
                print(f"Error copying file: {e}")



def main():
    src_file_path = os.getenv("SOURCE_FILE_PATH")
    dest_file_path = os.getenv("DESTINATION_FILE_PATH")

    if not src_file_path or not dest_file_path:
        print("Please set SOURCE_FILE_PATH and DESTINATION_FILE_PATH in the .env file.")
        return

    event_handler = FileHandler(src_file_path, dest_file_path)
    observer = Observer()
    observer.schedule(event_handler, path=f"{src_file_path}", recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    main()
