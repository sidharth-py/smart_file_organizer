import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from organizer import move_file

class FileHandler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory

    def on_created(self, event):
        if not event.is_directory:
            move_file(event.src_path, self.directory)

def organize_existing_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        move_file(file_path, directory)

def main():
    directory = input("Enter folder path to organize: ").strip()

    if not os.path.isdir(directory):
        print("Invalid directory.")
        return

    print("\n📂 Organizing existing files...")
    organize_existing_files(directory)

    print("👀 Watching for new files... (Press Ctrl+C to stop)")
    event_handler = FileHandler(directory)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nStopped watching.")

    observer.join()

if __name__ == "__main__":
    main()