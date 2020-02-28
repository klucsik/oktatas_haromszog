
def calc_haromszog(version, a, b,c):
    if type(a) is not int or type(b) is not int or type(c) is not int:
        return "érvénytelen adattípus, kérlek egész számot adj meg!"

    if version == 1:
        return calc_1(a,b,c)
    if version == 2:
        return calc_2(a,b,c)
    if version == 3:
        return calc_3(a,b,c)
    return "Érvénytelen kalkuláció verzió"


def calc_1(a,b,c):
    if a < 1:
        return "Nem háromszög"
    if b < 1:
        return "Nem háromszög"
    if c < 1:
        return "Nem háromszög"
    if a + b <= c:
        return "Nem háromszög"
    if a + c <= b:
        return "Nem háromszög"
    if b + c <= a:
        return "Nem háromszög"

    if a == b and b == c:
        return "Szabályos háromszög"

    if a == b:
        return "Egyenlő szárú háromszög"

    if a == c:
        return "Egyenlő szárú háromszög"

    if c == b:
        return "Egyenlő szárú háromszög"

    return "Általános háromszög"


def calc_2(a,b,c):
    if a < 0: #!
        return "Nem háromszög"
    if b < 1:
        return "Nem háromszög"
    if c < 1:
        return "Nem háromszög"
    if a + b < c: #!
        return "Nem háromszög"
    if a + c < b: #!
        return "Nem háromszög"
    if b + c < a: #!
        return "Nem háromszög"

    if a == b and b == c:
        return "Szabályos háromszög"

    if a == b:
        return "Egyelő szárú háromszög" #!

    if a == c:
        return "Egyenlő szárú háromszög"

    if c == b:
        return "Egyenlő szárú háromszög"

    return "Általános háromszög"

def calc_3(a,b,c):
    if a < 1:
        return "Nem háromszög"
    if b < 1:
        return "Nem háromszög"
    if c < 1:
        return "Nem háromszög"
    if a + b <= c:
        return "Nem háromszög"
    if a + c <= b:
        return "Nem háromszög"
    if b + c <= a:
        return "Nem háromszög"

    #!

    if a == c: #!
        return "Egyenlő szárú háromszög"

    if a == c:
        return "Egyenlő szárú háromszög"

    if c == b:
        return "Egyenlő szárú háromszög"
    
    if a == b and b == c: #!
        return "Szabályos háromszög"

    return "Általános háromszög"