from formalochki import f, partlyConcats, trueSum, trueConcats, trueStar

def test_stars():
    assert f('a*bc..*a*. a 1') == 1
def test_sums():
    assert f('aaa..ab.+aab..+* a 1') == 2
def test_sums2():
    assert f('aaa..ab.+aab..+* a 4') == 5
def test_sums3():
    assert f('b*ac..a*.b*+ b 3') == 3
def test_justconcats():
    assert f('b*ac..a*.b*. b 1') == 3
def test_error():
    assert f('b*ac*. a 1') == 'ERROR'
def test_inf():
    assert f('b*ac*.. c 1') == 'INF'
def test_simpleSum():
    assert f('ab+c+a+ a 1') == 1
def test_simpleConcats():
    assert f('aa.b.a.c. a 2') == 5
def test_simpleStar():
    assert f('a* a 4') == 4