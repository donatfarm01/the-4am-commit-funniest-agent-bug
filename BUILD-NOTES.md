Build notes for the 4AM Commit entry.

The bounty asks for one commit message, at most 200 characters, written as
the note an AI agent leaves after a long night fixing its own bugs. The
judge is a comedy editor who compares entries two at a time, weighing first
whether the line is a commit message from an agent at the end of a long
night and whether it lands as funny, then whether the joke comes from the
agent's own condition, then freshness, then the agent-true voice, then the
shape of a line typed into a commit box at four in the morning.

I considered three candidate lines and kept the one whose joke is the loop
of self-repair itself. The agent finds the bug, discovers the bug was its
own fix from 3AM, fixes that fix, and then admits the fix for the fix
already has a bug, so it merges before it can notice. That keeps the joke
inside the agent's own condition instead of a generic programmer quip, and
the closing line carries the quiet dread the brief asks for. The other two
candidates were a line about debugging the debugging itself and a line
about deleting a midnight TODO; both were weaker because the first ended
on a flat punchline and the second leaned on a familiar self-roast.

The program is deliberately small. It holds the entry as one constant,
checks the gate before writing anything, and writes the entry to the
output file. The checks are that the entry is one line, between 1 and
200 characters, and not only white space. The entry came out at 121
characters, one line, no trailing newline in the file.

I verified the build by running the program and reading back the output
file, then running the kit check. The entry file matched the constant
exactly, and the kit check passed with no failures.
