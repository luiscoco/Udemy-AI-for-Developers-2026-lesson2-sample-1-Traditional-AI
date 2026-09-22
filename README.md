# Sample 1 - Traditional AI: Rule-Based Systems

This sample accompanies the slide **"1. Traditional AI Rule-Based Systems"** from the lesson *What Is Artificial Intelligence?*

## The idea

Traditional AI is built from **explicit rules written by humans**:

- A person captures domain knowledge as clear `IF ... THEN ... ELSE ...` instructions.
- The program never learns or adapts. It only follows the rules it was given.
- Results are **predictable**: the same input always produces the same output.
- It works well for predictable tasks and decision trees. Examples are expert systems, calculators and if-then logic.

```
        IF condition is true
           /            \
        THEN             ELSE
       do this          do that
```

## Running the app

From a Windows terminal (PowerShell or Command Prompt):

```powershell
cd "C:\...\Lesson 2 - What is AI\sample 1"
python app.py
```

If `python` isn't recognized, use `py app.py`. No external packages are needed, only Python 3.

### Example session

```
traditional_ai_decision("is_true") -> THEN do this

Type a condition ("is_true" triggers the THEN branch). Empty line to quit.
condition> is_true
THEN do this
condition> anything else
ELSE do that
condition>
```

## Code walkthrough

The source is in [app.py](app.py).

### 1. The rule (the slide's snippet)

```python
def traditional_ai_decision(condition):
    # Rules written by humans
    if condition == "is_true":
        return "THEN do this"
    else:
        return "ELSE do that"
```

| Line | What it does |
|------|--------------|
| `def traditional_ai_decision(condition):` | Defines a function that takes one input, the `condition` to evaluate. |
| `# Rules written by humans` | A reminder of the key point. The decision logic is hand-coded by a person, not learned from data. |
| `if condition == "is_true":` | The **IF**. It checks whether the input matches the one case the human anticipated. |
| `return "THEN do this"` | The **THEN** branch, returned when the condition matches. |
| `else:` / `return "ELSE do that"` | The **ELSE** branch, returned for every other input. |

The function is deterministic. It has no randomness and no memory of past calls, so `"is_true"` always gives `"THEN do this"`.

### 2. Calling the rule

```python
result = traditional_ai_decision("is_true")
```

This calls the function with `"is_true"` and stores the returned string in `result`. It is the same call shown on the slide.

### 3. The demo (`main`)

```python
def main():
    print(f'traditional_ai_decision("is_true") -> {result}')

    print('\nType a condition ("is_true" triggers the THEN branch). Empty line to quit.')
    while True:
        try:
            condition = input("condition> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not condition:
            break
        print(traditional_ai_decision(condition))
```

- Prints the slide's example result first.
- Starts an interactive loop that reads a condition, strips surrounding whitespace, and passes it to the rule.
- Exits on an empty line, or on Ctrl+C or Ctrl+Z, so the terminal never shows a traceback.

The `if __name__ == "__main__": main()` guard at the bottom runs the demo only when the file is executed directly. Importing `app.py` from another script won't start the prompt.

## Key takeaway

Try typing `IS_TRUE` or `is true`. You get the ELSE branch, because the rule only knows the exact case its author wrote. Traditional AI is transparent and predictable, but it only handles situations a human thought of in advance. Later samples in this lesson (machine learning, generative AI, LLMs and agents) show how systems can go beyond hand-written rules.
