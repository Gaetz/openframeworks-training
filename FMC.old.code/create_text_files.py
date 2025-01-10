import os

def create_txt_files_for_fla_files(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.fla'):
                fla_file_path = os.path.join(subdir, file)
                txt_file_path = os.path.splitext(fla_file_path)[0] + '.txt'
                with open(txt_file_path, 'w') as txt_file:
                    txt_file.write(f'This is a placeholder for {file}')

if __name__ == "__main__":
    root_directory = os.getcwd()  # You can change this to any directory you want to start from
    create_txt_files_for_fla_files(root_directory)