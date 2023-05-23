# MY API

Backend made with Flask for the acquisition, manipulation and storage of data from a questionnaire for the **MY Master Project**

## Structure

-   `index.py` : Main file
-   `controllers/` : API routes & logic
-   `services/` : Database queries & logic
-   `models/` : Database models

## Requirements

-   Python 3.X

## Installation

1. Clone the repo :

```bash
git clone https://github.com/Tomspace900/myapp
```

2. Go to directory & create virtual environment

```bash
cd back
```

```bash
python3 -m venv myenv
```

3. Activate virtual environment

Linux/MacOS

```bash
source myenv/bin/activate
```

Windows

```bash
myenv\Scripts\activate
```

4. Install dependencies :

```bash
pip3 install -r requirements.txt
```

5. Start the app

```bash
python3 api/index.py
```

6. The server runs on http://127.0.0.1:5000

## Authors

MY Team
