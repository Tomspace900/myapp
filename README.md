# MY API

Backend made with Flask for the acquisition, manipulation and storage of data from a questionnaire for the **MY Master Project**

## Structure

-   `app.py` : Main file
-   `controllers/` : API routes & logic
-   `services/` : Database queries & logic
-   `models/` : Database models

## Requirements

-   Python 3.X

## Installation

1. Clone the repo :

```bash
git clone https://github.com/Jeanne-Des/MasterProject
```

2. Go to directory & create virtual environment

```bash
cd MasterProject/back
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

5. Create a `.env` file in `back/` folder :

```bash
DATABASE_NAME=[name]
DATABASE_USER=[user]
DATABASE_PASSWORD=[password]
DATABASE_HOST=[host]
DATABASE_PORT=[port]

CSV_PATH='data/data.csv'
```

Replace the [variables] with your own values

6. Start the app

```bash
python3 app.py
```

6. The server runs on http://127.0.0.1:5000

## Authors

MY Team
