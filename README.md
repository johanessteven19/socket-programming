# Product Name
## pArr

# Group B1 Members
- Abimanyu Yuda Dewa - 1906426714
- Abraham Rudolf Brahmana - 1906426720
- I Nyoman Gde Gedar Marchiendo Pradnyana - 1906318086 
- Johanes Steven - 1906426853

Socket Programming assignment from members of Group B1 in Computer Networks 2020-2021 Even course.

# Requirements / Dependencies
- python/python3

# Installation / execution instructions
- Make sure python is installed
- Git clone https://gitlab.com/jarkomfasilkomui/2021-even/sockpro/group-b1
- In your terminal run `python tutorial_server_multithreaded.py`. This will be the manager node.
- Then, run `python tutorial_client.py` on a separate terminal window. This will be the worker node.

# Instructions to use the features (as a user)
- On the server terminal, you can input several commands:
    - `send`: will be used to run the descriptive statistics features
        - `random`: create a random list of integers. Mean, median, modus and sorted list will be returned.
    - `check`: check number of tasks queued on the worker node.
    - `wait`: will be used to tell the worker node to wait.
    - `revert`: clear queued tasks on the worker node.
- If random command has been sent to the worker node, type the `do` command on the worker terminal. The results will be sent to the manager node.
- While worker in 'wait' status, if `done` command is sent, then the option to quit will appear.
    - type y/yes to quit, n/no to cancel.

