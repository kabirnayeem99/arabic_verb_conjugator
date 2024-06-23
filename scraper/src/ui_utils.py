import sys

def show_progress_bar(current_item, total_items, bar_length=50):
    progress = int(current_item / total_items * 100)
    progress_string = f"Progress: [{'=' * int(progress / (100 / bar_length))}{' ' * (bar_length - int(progress / (100 / bar_length)))}] {progress}%\nProcessing item {current_item} of {total_items}"
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")
    sys.stdout.write('\r')
    sys.stdout.write('\r')
    sys.stdout.write(progress_string)
    sys.stdout.flush()

def show_program_title():
    print("╔════════════════════════════════════╗")
    print("║      Verb Conjugator Program       ║")
    print("╚════════════════════════════════════╝")
    