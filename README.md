# Rosalind Solutions

These are my solutions to problems from the Rosalind bioinformatics platform.

Rosalind account:
https://rosalind.info/users/jcapecci8/

## Project Status

This is a living project that I will continue updating as I work through additional Rosalind problems. Some earlier scripts may also be refactored to improve readability and include command-line interfaces for easier execution.

For an example implementation, see `finding_a_shared_motif.py`.

## Running an Example Script

1. Clone the repository:

```bash
git clone https://github.com/jcapecci09/Rosalind-solutions.git
```

2. Run the script (Linux/macOS):

```bash
python3 bioinformatics_stronghold/finding_a_shared_motif.py -i datasets/rosalind_lcsm.txt -o outputs/rosalind_lcsm_output.txt
```

## Work in progress
- Update older scripts so they can be used via command line
- Comment older scripts
- Solve harder rosalind problems
- comment in example script on my solution
- add workflow mark down file that explains how I solved some of the problems

## Fixes
I've kind of backed off this project because a few design chooses have irked me. 

* I don't like that running each script via the command line requires specefying the paths.
* in the toolkit i attempted to standardized the output by creating a function that outputs either a file path or a string, but I can't do the same for input.
* The way im using my scripts has become quite complex hard to follow the logic
