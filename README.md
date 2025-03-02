
## How to commit a file to GitHub

1. Open a terminal and navigate to your project directory:
    ```sh
    cd "/Users/macbook/Documents/my portfolio"
    ```

2. Initialize a Git repository (if not already done):
    ```sh
    git init
    ```

3. Add the file to the staging area:
    ```sh
    git add "projects amateur/python code/bmi.py"
    ```

4. Commit the file with a message:
    ```sh
    git commit -m "Add BMI calculation script"
    ```

5. Add the remote repository (if not already done):
    ```sh
    git remote add origin <your-github-repo-url>
    ```

6. Push the commit to the GitHub repository:
    ```sh
    git push -u origin main
    ```

Replace `<your-github-repo-url>` with the URL of your GitHub repository.
