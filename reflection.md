# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the app, it looked like a normal number guessing game, but the whole thing felt wrong immediately. The debug panel showed the secret changing every time I clicked submit, the hints were sometimes backwards, and the score/attempt counters did not behave consistently. It felt like the app was forgetting what round it was in and then pretending it was a new game every click.

Two concrete bugs I noticed right away were: the secret number was being recreated on each rerun instead of staying in `st.session_state`, and the guess comparison was switching between numbers and strings in a way that made the game logic inconsistent. Another issue was that the attempts counter started at 1 instead of 0, which made it look like the player had already used a try before they even guessed.

**Bug Reproduction Log**

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Submit a guess while the secret is visible in debug mode | Secret remains the same for the current round | Secret changed after every submit and rerun | Debug panel showed different values on each interaction |
| Guess 60 when the secret is 50 | Hint says “Too High” | Hint sometimes flipped or depended on odd/even attempts | No exception, but the decision logic was inconsistent |
| Start a new game | New round resets cleanly | Attempts and state values did not reset reliably | No crash, but the game state looked corrupted |

---

## 2. How did you use AI as a teammate?

I mainly used Copilot in VS Code while working through the bugs. I’d ask it for a quick explanation of what was going wrong and for suggestions on how to preserve state across Streamlit reruns, then I would test the result in the app before accepting it. One AI suggestion I did accept was to move the game logic into a separate helper file and keep the secret number in `st.session_state`; that was the right direction, and it matched what the browser behavior was showing me.

One suggestion I did not take as written was the idea of making the logic alternate between number and string comparisons based on attempt count. It looked plausible at first, but it was confusing and made the behavior less reliable. I rejected it because it was hiding the real problem instead of fixing it, and I verified the cleaner version by running the tests and checking the app behavior with a known secret.

---

## 3. Debugging and testing your fixes

I treated a bug as fixed when I could reproduce the same input and get the same result repeatedly, without the app “randomizing” the state in the middle of the round. I also checked that the pure logic tests matched the real app: if the function said a guess was too high, the app should show the same hint and not flip it unexpectedly.

I ran `pytest` and the tests were useful because they forced the core logic to be deterministic. That helped me realize the real issue was not just the Streamlit UI; it was the actual comparison logic in the helper functions. AI helped me think through the edge cases and gave me some good starting points for tests, but I still wrote the final checks in a way that matched the project’s actual contract.

---

## 4. What did you learn about Streamlit and state?

The biggest lesson was that Streamlit is not a normal app where variables keep their values forever. Every time a button is clicked, the script reruns from the top, and any variable that is not stored in `st.session_state` gets recreated. That means the secret number, attempts, and score should live in session state if we want the game to feel like a real game instead of a glitchy reset machine.

I would explain it to a friend like this: imagine the app is a script that restarts every time you click something. Session state is the memory that survives the restart so the game can remember what is happening. Without that memory, values reset and the game becomes inconsistent.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is writing the smallest possible tests around the logic before I change the UI. That kept me from guessing and helped me confirm the root cause instead of patching random symptoms. I also want to keep asking the AI for the simplest fix first and then verifying it against the actual behavior, because the easiest-looking answer is not always the correct one.

This project changed how I think about AI-generated code. I don’t see it as a final answer anymore; I see it as a helpful starting point that still needs human judgment, testing, and real verification. The AI can move fast, but it does not understand the app’s actual state or intent unless I check it carefully.
