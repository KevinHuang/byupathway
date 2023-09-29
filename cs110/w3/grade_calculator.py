
# Ask the user to input his score percentage and convert to number.
score = float(input('What is your score percentage ? (ex: 80)'))

def find_grade(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score>= 60:
        grade = 'D'
    else:
        grade = 'F'

    return grade

def find_sign(score):
    remainder = score % 10
    if remainder >= 7:
        sign = '+'
    elif remainder < 3:
        sign = '-'
    else:
        sign = ''
    
    return sign


grade = find_grade(score)
sign = find_sign(score)
is_pass = (score >= 70)
msg = 'Congradulations!' if is_pass else ' you have to study harder!'

print(f"You got grade {grade}{sign}, {msg}")
