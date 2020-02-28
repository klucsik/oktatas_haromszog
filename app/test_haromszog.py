from app.haromszog import calc_haromszog
version = 1
def test_nem_haromszog():
    assert calc_haromszog(version, -1,1,1) == "Nem háromszög"
    assert calc_haromszog(version, 1,-1,1) == "Nem háromszög"
    assert calc_haromszog(version, 1,1,-1) == "Nem háromszög"

    assert calc_haromszog(version, 0,1,1) == "Nem háromszög"
    assert calc_haromszog(version, 1,0,1) == "Nem háromszög"
    assert calc_haromszog(version, 1,1,0) == "Nem háromszög"

def test_szabalyos_haromszog():
    assert calc_haromszog(version, 1,1,1) == "Szabályos háromszög"
    assert calc_haromszog(version, 100,100,100) == "Szabályos háromszög"

def test_egyenlo_szaru_haromszog():
    assert calc_haromszog(version, 2,1,1) == "Egyenlő szárú háromszög"
    assert calc_haromszog(version, 1,2,1) == "Egyenlő szárú háromszög"
    assert calc_haromszog(version, 1,1,2) == "Egyenlő szárú háromszög"    

def test_altalanos_haromszog():
    assert calc_haromszog(version, 1,2,3) == "Általános háromszög"
    assert calc_haromszog(version, 2,1,3) == "Általános háromszög"
    assert calc_haromszog(version, 3,1,2) == "Általános háromszög"