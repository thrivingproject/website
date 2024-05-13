# Free Website

| Frontend Server                           | Backend Server                                                         | Email Server                        |
| ----------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------- |
| [GitHub pages](https://pages.github.com/) | [PythonAnywhere](https://www.pythonanywhere.com/user/thrivingproject/) | [Mailgun](https://www.mailgun.com/) |

## Development

### Setup

```bash
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

Set the `action` attribute of the form to `http://127.0.0.1:5001/sendemail` in `index.html`.

### Frontend

Open command pallette: `Ctrl + Shift + P`, select `Live Preview: Start Server`.

### Backend

```bash
py backend/flask_app.py
```
