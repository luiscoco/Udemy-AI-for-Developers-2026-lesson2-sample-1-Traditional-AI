"""Traditional AI: rule-based systems.

Illustrates explicit human-written "if-then" logic.
"""


def traditional_ai_decision(condition):
    # Rules written by humans
    if condition == "is_true":
        return "THEN do this"
    else:
        return "ELSE do that"


result = traditional_ai_decision("is_true")


def main():
    # Slide example, exactly as shown
    print(f'traditional_ai_decision("is_true") -> {result}')

    # Interactive demo: the rule always gives the same, predictable answer
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


if __name__ == "__main__":
    main()
