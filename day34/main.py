age: int
name: str
height: float
is_human: bool

# Creating Type Hints

def police_check(age: int) -> bool:
    if age > 10:
        can_drive = True
    else:
        can_drive = False

    return can_drive


police_check()