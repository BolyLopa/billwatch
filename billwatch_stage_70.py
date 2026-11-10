# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: BillWatch
CLEAR_CONFIRM = False


def clear_state():
    global CLEAR_CONFIRM
    if CLEAR_CONFIRM:
        bills.clear()
        categories.clear()
        monthly.clear()
        next_id = 1
        print("State cleared.")
    else:
        print("Aborted; nothing changed.")


def confirm_clear():
    global CLEAR_CONFIRM
    CLEAR_CONFIRM = True
    print("Confirming clear. Run clear_state() to proceed.")
