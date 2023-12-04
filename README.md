# CF_Master
A helper that enables us to focus more on logic building and programming rather than navigating and selecting and searching the code file to the problem.
It was a problem that I personally faced and it took a lot longer time due to a bug in my file explorer.

# Key Features
1) Run a command and login to codeforces.
2) The inputs are merely the ProblemId,ContestId.
3) Hassle free copying of the code from your major cpp file to the assistant's cpp file.

# How to Run
1) Clone this repo to your local by `git clone <repo-name>`
2) Navigate inside the folder   `CF_Master`
3) Run your virtual Enviornment `https://docs.python.org/3/library/venv.html`
4) Create a cpp file inside it using `touch temp.cpp`
5) Now you need to add the path of your original code file where you code and this temp.cpp in a `.env` file
6) Open two terminals -
![Screenshot from 2023-12-05 03-11-33](https://github.com/Anshuman212/CF_Master/assets/75901017/03157aca-dcfe-4ddf-8d76-5f67f4de57e4)

 One for running the command ```python3 copyFile.py``` it'll keep track of your code editor and register any changes being made and would make the same changes to the temp.cpp

Other terminal to run `python3 submit.py` to submit your code on CF

![Screenshot from 2023-12-05 03-12-28](https://github.com/Anshuman212/CF_Master/assets/75901017/99ebe635-3764-410f-a41b-70811982d02a)


## Note
This script uses python3
## I'll be adding few specs as soon as I face any problem or want to explore something new.
