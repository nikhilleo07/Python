# Python

 

### Table of Contents

**[Description](#description)**<br>

**[Overview](#overview)**<br>

**[Git Branching Strategy](#git-branching-strategy)**<br>

**[python_bug_fix](#python_bug_fix)**<br>

**[feature_TCP_script](#feature_TCP_script)**<br>

**[bug_fix_readme](#bug_fix_readme)**<br>

**[Conclusion](#conclusion)**<br>

 

# Description

This Python repository provides an overview of Python programing language. The main topics of python like Assignments and Variables,Data Structures,Loops and Statements,Functions,Modules and Packages,Handling Errors,Object-Oriented Coding, Unit testing,pylint, logging and time,Network Utilities are covered as diffrent excersises and stored in this Repository.  

## Overview

 

| Exercises   |      Description     |

|----------| :---------------|

| Exercises_01 | Experimented and worked on python assignments, operators, and variables  |

| Exercises_02 | Experimented and worked on Python's data structures |

| Exercises_03 | Experimented and worked on Python's Flow controls like IF,ELIF,ELSE and Loops like FOR,While with Lists |

| Exercises_04 | Experimented and worked on python functions  |

| Exercises_05 | Experimented and worked on Python Modules and Packages |

| Exercises_06 | Experimented and worked on Error Handling in python |

| Exercises_07 | Experimented and worked on Python Object-Oriented (OO) coding |

| Exercises_08 | Experimented and worked on Python tests like unit testing and Pylint |

| Exercises_09 | Experimented and worked on Python libraries for logging files and getting time  |

| Exercises_10 | Experimented and worked on Python network utilities  |

| Exercises_11 | Experimented and worked on Python project creation in a standard format  |


- Clone the Python repo to local machine.

```

git clone https://github.com/nikhilleo07/Python.git

```

 

## Git Branching Strategy

 

Branching strategy in GitHub is a set of rules that define how and when developers should create, merge, and delete branches within a Git repository. It helps to ensure that all changes to the codebase are tracked and managed in a consistent and orderly fashion. This strategy is important for any large software project, as it helps to ensure that all the changes to the codebase are properly tracked, merged, and tested before being released to the public. A branch is a version of the codebase that is separate from the main branch usually called master. It is used to work on a specific set of features, bug fixes or other changes that are not ready to be released to the public yet. The feature branch or bug fix branch will be merged to master branch after testing and verifying the changes done. 


Below are the branches created for this project:

 

- main: This is the master branch which is always available for public and has the latest details.

- dev: All the latest changes that need to be pushed to the master are tested and stored in this branch.

- test: All the immediate changes and bug-fix are stored in this branch. This also contains the latest changes that need to pushed to the master.

- feature_TCP_script: Missed code changes are stored in this branch.

- python_bug_fix: Bug in the code are stored in this branch.

- bug_fix_readme: Imediate bug-fix on the code is stored in this branch.
 

## python_bug_fix

All set of bug_fix are done and pushed to dev branch from this branch. 

- As a first senario error in the Exercise 4.3.py file was fixed. Equation to find the volume was corrected. 

[Bug Fix 1](https://github.com/nikhilleo07/Python/pull/1/files)

- In second senario error in the Exercise 9/os_utilities.py file was fixed. Added the missing psutil import module.

[Bug Fix 1](https://github.com/nikhilleo07/Python/pull/4/files)

All the bug were fixed and pushed to the dev branch successfully.


## feature_TCP_script

Feature branch is mostly used to add a missing code. Missing codes are added and tested in this branch inorder to push to dev branch.

- As a senario missing code in the Exercise 10/tcp_client.py file was fixed. tcp_client code was missing and it was addes successfully.

 [Feature 1](https://github.com/nikhilleo07/Python/pull/3/files)

All the missing code changes were fixed and pushed to the dev branch successfully.


## bug_fix_readme

All set of imediate bug fix are done and pushed to test branch from this branch.

- As a senario already created readme file was edited and successfully pushed to the test branch.


## Major branch activites done in this repository

[Pull Requests](https://github.com/nikhilleo07/Python/pulls?q=is%3Apr+is%3Aclosed)

## Conclusion

This Python repository helps to understand an overview of Python programing language through the excersises. These excersises can be viewed and can be cloned to other respository as this repository is created as Public. As an overall this repository can be used by student to get a intermediate level knowledge in Python.
