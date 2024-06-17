# PIP LIST

Package            Version
------------------ --------
bcrypt             4.1.3
blinker            1.8.2
certifi            2024.6.2
charset-normalizer 3.3.2
click              8.1.7
colorama           0.4.6
decorator          4.4.2
Flask              3.0.3
Flask-Bcrypt       1.0.1
greenlet           3.0.3
idna               3.7
imageio            2.34.1
imageio-ffmpeg     0.5.1
itsdangerous       2.2.0
Jinja2             3.1.4
MarkupSafe         2.1.5
moviepy            1.0.3
numpy              2.0.0
pillow             10.3.0
pip                24.0
proglog            0.1.10
psycopg2           2.9.9
requests           2.32.3
setuptools         70.0.0
SQLAlchemy         2.0.30
tqdm               4.66.4
typing_extensions  4.12.2
urllib3            2.2.1
Werkzeug           3.0.3

# BASE DE DADOS DE VIDEO

CREATE TABLE video_metadata (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    duration DOUBLE PRECISION,
    width INT,
    height INT
);