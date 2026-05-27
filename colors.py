# ANSI color helpers for colored log output

# Reset
RESET = "\033[0m"

# Foreground colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

# Styles
BOLD = "\033[1m"
DIM = "\033[2m"

# Neutral color for data values (URLs, commands, filenames, etc.)
DATA = f"{BOLD}{WHITE}"


def tag(label: str, color: str) -> str:
    """Return a colored bracket label like [Agent]."""
    return f"{color}{BOLD}[{label}]{RESET}"


def data(value) -> str:
    """Return a neutrally colored data value."""
    return f"{DATA}{value}{RESET}"
