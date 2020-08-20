import pytest
from VariousMethods import various_methods

def test_convertToAtlasCopco():
    testMethods = various_methods.VariousMethods()
    for shouldFail in [-1, 0, 101]:
        with pytest.raises(ValueError) as e:
            testMethods.ConvertToAtlasCopcoString(shouldFail)
        assert str(e.value) == 'numberToConvert was outside of the valid range'
    for x in range(1,101):
        if(x == 1):
            assert testMethods.ConvertToAtlasCopcoString(x) == "1"
        elif((x % 3 == 0) and (x % 5 == 0)):
            assert testMethods.ConvertToAtlasCopcoString(x) == "AtlasCopco", f"x: {x}"
        elif(x % 5 == 0):
            assert testMethods.ConvertToAtlasCopcoString(x) == "Copco", f"x: {x}"
        elif(x % 3 == 0):
            assert testMethods.ConvertToAtlasCopcoString(x) == "Atlas", f"x: {x}"
            
def test_findMax():
    testMethods = various_methods.VariousMethods()
    for shouldFail in [[], None]:
        with pytest.raises(ValueError) as e:
            testMethods.FindMax(shouldFail)
        assert str(e.value) == 'The collection must contain at least one element'
    assert testMethods.FindMax([1,2,3]) == 3
    assert testMethods.FindMax([0,1]) == 1
    assert testMethods.FindMax([0]) == 0
    assert testMethods.FindMax([-1,0,1]) == -1