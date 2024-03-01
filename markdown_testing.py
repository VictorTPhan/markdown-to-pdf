import subprocess
import os
import shutil

def run_generate_pdf_command(markdown_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_directory = os.path.join(script_dir, "assets", "input")
    markdown_filename = os.path.basename(markdown_path)
    markdown_dest_path = os.path.join(script_dir, "assets", markdown_filename)

    # Move the markdown file to the root of the "assets" directory
    shutil.move(markdown_path, markdown_dest_path)

    current_dir = os.getcwd()
    command = f"docker run -v {current_dir}/assets:/app/assets md2pdf python3 md2pdf.py convert assets/{markdown_filename} assets/style.css"
    subprocess.run(command, shell=True)

    # Move the markdown file back to the "input" directory
    shutil.move(markdown_dest_path, os.path.join(input_directory, markdown_filename))

if __name__ == "__main__":
    input_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "input")
    
    # Iterate over all markdown files in "assets/input" directory
    for filename in os.listdir(input_directory):
        if filename.endswith(".md"):
            markdown_path = os.path.join(input_directory, filename)
            run_generate_pdf_command(markdown_path)