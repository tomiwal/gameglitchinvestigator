def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    ranges = {
        "Easy": (1, 20),
        "Normal": (1, 100),
        "Hard": (1, 50),
    }
    return ranges.get(difficulty, (1, 100))


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    value_text = str(raw).strip()
    if value_text == "":
        return False, None, "Enter a guess."

    try:
        if "." in value_text:
            value = int(float(value_text))
        else:
            value = int(value_text)
    except (TypeError, ValueError):
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """Return the outcome category only: "Win", "Too High", or "Too Low"."""
    try:
        guess_num = int(guess)
    except (TypeError, ValueError):
        guess_num = guess

    try:
        secret_num = int(secret)
    except (TypeError, ValueError):
        secret_num = secret

    if guess_num == secret_num:
        return "Win"
    if guess_num > secret_num:
        return "Too High"
    return "Too Low"


def get_hint_message(outcome: str):
    """Return the user-facing hint for a given outcome."""
    if outcome == "Win":
        return "🎉 Correct!"
    if outcome == "Too High":
        return "📉 Go LOWER!"
    return "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
