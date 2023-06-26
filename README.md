# CV/Resume Parser using OpenAI's ChatGPT README

This readme file provides instructions on how to run a Python program both locally and using Docker.

## Local Setup

To run the Python program locally, please follow the steps below:

1. Ensure that Python is installed on your system. You can check this by opening a terminal or command prompt and typing `python --version`. If Python is not installed, download and install it from the official Python website: https://www.python.org/.

2. Clone or download the source code of the Python program from the repository.

3. Open a terminal or command prompt and navigate to the directory where the program files are located.

4. (Optional) Set up a virtual environment for the program. While this step is not mandatory, it is generally recommended to isolate dependencies for different projects. To set up a virtual environment, you can use a tool like `venv`. Run the following command:

   ```shell
   python -m venv venv
   ```

5. Activate the virtual environment. The command to activate the virtual environment depends on your operating system:

   - For Windows:

     ```shell
     venv\Scripts\activate
     ```

   - For macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

6. Install the required dependencies. The Python program may have a `requirements.txt` file listing the dependencies. Use the following command to install them:

   ```shell
   pip install -r requirements.txt
   ```

7. Run the Python program using the following command:

   ```shell
   streamlit run cv_upload_response_page.py
   ```

## Docker Setup

To run the Python program using Docker, please follow the steps below:

1. Ensure that Docker is installed on your system. You can check this by opening a terminal or command prompt and typing `docker --version`. If Docker is not installed, download and install it from the official Docker website: https://www.docker.com/.

2. Clone or download the source code of the Python program from the repository.

3. Open a terminal or command prompt and navigate to the directory where the program files are located.

4. Build a Docker image for the Python program using the provided `Dockerfile`. Run the following command:

   ```shell
   docker build -t your_image_name .
   ```

   Replace `your_image_name` with the desired name for your Docker image.

5. Once the Docker image is built, you can run a Docker container using the following command:

   ```shell
   docker run your_image_name
   ```

   Replace `your_image_name` with the name you specified in the previous step.

That's it! You should now be able to run the Python program both locally and using Docker. Enjoy!