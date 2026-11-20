# Setting up for CST1510

Seven steps, once, before Week 1.
Prefer a visual version? See the
[Setup Guide](https://anna29.github.io/CST1510/setup-guide.html).

**Windows or Mac?** Everything is the same, except Windows uses `python` and
macOS uses `python3`.

---

## 1. Install three things

- **Python** from [python.org/downloads](https://www.python.org/downloads/).
  Windows: on the first screen, tick **"Add python.exe to PATH"**.
- **VS Code** from [code.visualstudio.com](https://code.visualstudio.com/).
  Then open Extensions (`Ctrl/Cmd + Shift + X`) and install **Python** and
  **Jupyter**, both by Microsoft.
- **Git** from [git-scm.com/downloads](https://git-scm.com/downloads),
  accepting the defaults.

## 2. Create your GitHub repository

Create a free account at [github.com](https://github.com/). Then click
**+** (top right) → **New repository**, name it `CST1510`, tick
**Add a README file**, and click **Create repository**.

## 3. Clone it into Documents

Open a terminal (Windows: **PowerShell**, Mac: **Terminal**) and run:

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
cd Documents
git clone https://github.com/YOUR-USERNAME/CST1510.git
```

Use your own name, the email from your GitHub account, and your GitHub
username. This creates the folder `Documents/CST1510`.

To check your Git settings at any time:

```
git config --list
```

Look for `user.name` and `user.email` in the list. Press `q` to exit if the
list fills the screen.

## 4. Open the folder in VS Code

**File → Open Folder** → `CST1510`, then **Terminal → New Terminal**.
Use this terminal from now on.

Check which branch you're on and that it's linked to GitHub:

```
git branch -vv
```

You should see `* main` followed by `[origin/main]`. That means you're on the
`main` branch and it's linked to your repository on GitHub.

Every week's folder from Moodle goes inside `CST1510`, starting with this
Week 00 folder.

## 5. Add a `.gitignore` file

This tells Git which files never to upload. In VS Code, create a new file in
the `CST1510` folder, name it `.gitignore` (starting with a dot), paste this
in and save:

```
.venv/
__pycache__/
.ipynb_checkpoints/
.DS_Store
.env
```

## 6. Make a test file

Create `hello.py` in the `CST1510` folder:

```python
print("Hello from CST1510!")
```

Run it:

```
python hello.py       # Windows
python3 hello.py      # macOS
```

## 7. Push it to GitHub

```
git add .
git commit -m "Week 0 setup"
git push
```

The first time, VS Code asks you to sign in to GitHub: click **Allow** and
follow the browser window. Then open your repository on GitHub and check
`hello.py` and `.gitignore` are there.

**Done.** Every week from now on, finish the lab with the same three commands.

---

## If something goes wrong

| Problem | Fix |
|---|---|
| `python` not found (Windows) | Reinstall Python and tick "Add python.exe to PATH" |
| `python3` opens the Microsoft Store (Windows) | Use `python` on Windows |
| `fatal: not a git repository` | Open the `CST1510` folder in VS Code and use its terminal |
| A notebook won't run | Click **Select Kernel** (top right) and click **Install** if asked about ipykernel |

---

# Week 7: virtual environment and packages

You don't need this until Week 7.

**1. Create the environment and install the packages** in the VS Code
terminal:

```
python -m venv .venv                     # Windows
.venv\Scripts\activate

python3 -m venv .venv                    # macOS
source .venv/bin/activate

python -m pip install -r "Week 00 - Orientation and Setup/requirements.txt"
```

**2. Tell VS Code to use it:** `Ctrl/Cmd + Shift + P` →
**Python: Select Interpreter** → pick `.venv`. In notebooks, **Select Kernel**
→ `.venv`.

**3. Check it:**

```
python "Week 00 - Orientation and Setup/verify_setup.py"
```

Every line should say `OK`. Then push as usual.

If Windows says `running scripts is disabled`, run
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, answer `Y`, and try
again.

---

# Week 8 (CW2): your project repository

You don't need this until Week 8. Weeks 1 to 7 (coursework 1) live in your
`CST1510` repository. Coursework 2 is **one** application that you grow a
little each week, and it gets its own repository, `CST1510_CW2`. Only the
project files go into it. The lab notebooks are step-by-step instructions:
they stay in your course folder and are never uploaded.

**1. Create the repository.** On github.com click **+** (top right) →
**New repository**, name it `CST1510_CW2`, tick **Add a README file**, and
click **Create repository**.

**2. Clone it** next to `CST1510` (use your own GitHub username):

```
cd Documents
git clone https://github.com/YOUR-USERNAME/CST1510_CW2.git
```

**3. Open it in VS Code:** **File → Open Folder** → `CST1510_CW2`, then
**Terminal → New Terminal**. Use this terminal for all of coursework 2. Open
each week's lab notebook from your course folder with **File → Open File** (do
not copy it into `CST1510_CW2`).

**4. Create the environment and install the libraries** (once), in that
terminal. It uses the same `requirements.txt` as before, from your `CST1510`
folder:

```
python -m venv .venv                     # Windows
.venv\Scripts\activate

python3 -m venv .venv                    # macOS
source .venv/bin/activate

python -m pip install -r "../CST1510/Week 00 - Orientation and Setup/requirements.txt"
```

Then **Python: Select Interpreter** → the `.venv` in `CST1510_CW2`. In each lab
notebook: **Select Kernel** → **Python Environments** → that same `.venv`.
Check it with `python "../CST1510/Week 00 - Orientation and Setup/verify_setup.py"`:
every line should say `OK`.

**5. Add a `.gitignore`** to `CST1510_CW2`. Create a new file named
`.gitignore`, paste this in and save. It keeps your users, your database and
your API key off GitHub:

```
.venv/
__pycache__/
.ipynb_checkpoints/
.pytest_cache/
.DS_Store
.env
DATA/app.db
DATA/users.txt
.streamlit/secrets.toml
practice/
```

**6. Keep the CW2 lab folders out of your `CST1510` repository.** If you store
the Week 8 to 12 folders inside `CST1510`, add these lines to the end of
**that** repository's `.gitignore`:

```
# CW2 weeks: the project is in CST1510_CW2, nothing from these folders is uploaded
Week 08*/
Week 09*/
Week 10*/
Week 11*/
Week 12*/
```

**7. Check it.** At the end of each lab, in the `CST1510_CW2` terminal run
`git add .`, `git commit -m "Week N: ..."` and `git push` (the lab gives you the
exact message). Run `git status` first: you should see your `.py` files, but
**never** a `.db` file, `users.txt`, `secrets.toml` or `.env`.

