# Running the CLI 

Show the help with 

```
 python -m src.cli --help 
```

It prints: 

```
 Usage: python -m src.cli [OPTIONS] COMMAND [ARGS]...                            
                                                                                 
 Handles the --version flag                                                      
                                                                                 
                                                                                 
╭─ Options ─────────────────────────────────────────────────────────────────────╮
│ --version             -v        Show the application's version and exit.      │
│ --install-completion            Install completion for the current shell.     │
│ --show-completion               Show completion for the current shell, to     │
│                                 copy it or customize the installation.        │
│ --help                          Show this message and exit.                   │
╰───────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ────────────────────────────────────────────────────────────────────╮
│ add        Add two numbers.                                                   │
│ subtract   Subtract two numbers.                                              │
│ multiply   Multiply two numbers.                                              │
│ divide     Divide two numbers. Args:     a (float): The numerator.     b      │
│            (float): The denominator.                                          │
╰───────────────────────────────────────────────────────────────────────────────╯
```

## Example 

```sh
python -m src.cli add 420 69
```

result: 
```
The result of addition is: 489.0
```