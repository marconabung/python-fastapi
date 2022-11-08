#  Python FastAPI, Jinja2, MySQL template

## Getting Started

### Preqrequisites

### Installation

###### Clone this repository with HTTPS

Open your terminal and write this command.

```bash
git clone https://github.com/marconabung/python-fastapi.git
```

###### Locate your files in your local directory

After cloning the project, it should be available for editing on your local ,machine. Locate the file and change your directory.

```bash
cd ~/path/to/local/directory/python-fastapi
```

###### Setup Python virtual environment using venv

```
python3 -m venv ~/path/to/venv/python-fastapi
```

###### Activate virtual environment
```
source ~/path/to/venv/python-fastapi/bin/activate
```

###### Upgrade PIP and setuptools
```bash
python3 -m pip install --upgrade pip setuptools
```

###### Install requirements file

All the necessary modules and packages versions are stored in requirements.txt file. Type `ls` first to see all the available files and folders. If you can find requirements.txt file. Write this command to install the packages and modules.

```bash
pip install -r requirements.txt
```

### Usage

###### Enable uvicorn server

Once you've downloaded all the packages, it also includes uvicorn server for you to be able to run your app.

To run your server, type `uvicorn` then your main file name which in this case is named `main.py`. And then type your instantiated FastAPI app separated by colon. `main:app`
Write this command to run your server using the default host and port.

```bash
uvicorn main:app --reload
```

If you want to change the host and port. You can configure it in the command by replacing `--reload` and specifying your host and port `--host <host> --port <port number>`
*Note that using 0.0.0.0 as your host means that it listens to all IPs *
```
uvicorn main:app --host 0.0.0.0 --port 8000
```

You're all set! You will now be able to run your api locally. Happy hacking!


### Acknowledgements