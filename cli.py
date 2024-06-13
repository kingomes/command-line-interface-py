import cmd
import os

class MyCLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to MyCLI. Type "help" for available commands.'

    def __init__(self):
        super().__init__()
        self.current_directory = os.getcwd()
        self.prompt = f"{self.current_directory}>> "

    def do_list(self, line):
        files_and_dirs = os.listdir(self.current_directory)
        for item in files_and_dirs:
            print(item)

    def do_change_dir(self, directory):
        new_dir = os.path.join(self.current_directory, directory)
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            self.current_directory = new_dir
            print(f"Current directory changed to {self.current_directory}")
        else:
            print(f"Directory '{directory}' does not exist")

    def do_create_file(self, file):
        file_path = os.path.join(self.current_directory, file)
        try:
            with open(file_path, 'w') as new_file:
                print(f"New file '{file}' created in directory {self.current_directory}")
        except Exception as e:
            print(f"Error: {e}")

    def do_delete_file(self, file):
        file_path = os.path.join(self.current_directory, file)
        try:
            os.remove(file_path)
            print(f"File '{file}' deleted")
        except Exception as e:
            print(f"Error: {e}")

    def do_create_dir(self, directory):
        directory_path = os.path.join(self.current_directory, directory)
        try:
            os.mkdir(directory_path)
            print(f"Created directory '{directory_path}'")
        except Exception as e:
            print(f"Error: {e}")

    def do_delete_dir(self, directory):
        directory_path = os.path.join(self.current_directory, directory)
        try:
            os.rmdir(directory_path)
            print(f"Deleted directory '{directory_path}'")
        except Exception as e:
            print(f"Error: {e}")

    def do_read_file(self, file):
        file_path = os.path.join(self.current_directory, file)
        try:
            with open(file_path, 'r') as existing_file:
                print(existing_file.read())
        except FileNotFoundError as e:
            print(f"File '{existing_file}' not found")
        except Exception as e:
            print(f"Error: {e}")

    def do_open_file(self, file):
        file_path = os.path.join(self.current_directory, file)
        try:
            os.startfile(file_path)
        except Exception as e:
            print(f"Error: {e}")

    def do_quit(self, line):
        return True
    
    def precmd(self, line):
        return line
    
    def postcmd(self, stop, line):
        self.prompt = f"{self.current_directory}>> "
        return stop
    
if __name__ == '__main__':
    MyCLI().cmdloop()