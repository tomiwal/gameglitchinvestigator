# AI Interactions Log

---

## Agent Workflow (SF8)

**What task did you give the agent?**

I asked Copilot to help fix the streamlit guessing game by identifying the state bug, correcting the comparison logic, and refactoring the logic into a separate helper file. The goal was to make the game behave like a normal number guessing game without changing the core project structure.

**What did the agent do?**

It suggested moving the logic from the app file into `logic_utils.py`, showed how to keep values in `st.session_state`, and gave me a starting point for the helper functions. It also helped me spot that the comparison logic was inconsistent because values were being mixed between ints and strings.

**What did you have to verify or fix manually?**

I had to check the actual Streamlit behavior because the AI’s first pass still used a tuple return from `check_guess`, while the tests expected a single outcome string. I also had to correct the state reset logic so a new game cleared the right values and did not leave stale state behind.

---

## Test Generation (SF7)

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Exact match | “Write tests for the guessing game logic for win, too high, and too low cases.” | `assert check_guess(50, 50) == "Win"` | Yes | This is the baseline condition and catches the most important bug immediately. |
| Guess above secret | “Add a test for a number greater than the secret.” | `assert check_guess(60, 50) == "Too High"` | Yes | This verifies the hint logic is not reversed. |
| Guess below secret | “Add a test for a number lower than the secret.” | `assert check_guess(40, 50) == "Too Low"` | Yes | This confirms the lower-bound hint stays consistent and makes it easier to catch string/number issues. |

---

## Linting & Style (SF9)

**Prompt used:**

```
Please clean up the duplicated guessing logic and make it easier to test without changing the app behavior.
```

**Linting output before:**

```
No formal linter output, but there were repeated logic blocks in app.py and several state bugs caused by mixed logic and initialization.
```

**Changes applied:**

I moved the reusable logic into `logic_utils.py`, kept the app file focused on Streamlit UI, and made the helper functions return clear values that were easier to validate with `pytest`. I also made the score and hint logic more explicit instead of depending on odd/even attempt tricks.

---

## Model Comparison (SF11)

Not attempted for this project.

