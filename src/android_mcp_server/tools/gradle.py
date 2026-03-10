# Gradle Compilation Tool Implementation

# This script provides functionality for compiling Android projects using Gradle.

import os
import subprocess

class GradleCompiler:
    def __init__(self, project_dir):
        self.project_dir = project_dir

    def compile(self):
        try:
            print(f'Compiling project in {self.project_dir}...')
            result = subprocess.run(['gradle', 'build'], cwd=self.project_dir, check=True)
            print('Compilation successful!')
            return result
        except subprocess.CalledProcessError as e:
            print(f'Error during compilation: {e}')
            return None

if __name__ == '__main__':
    project_directory = os.path.join(os.getcwd(), 'your_project_directory')  # Update this to your actual project directory
    compiler = GradleCompiler(project_directory)
    compiler.compile()