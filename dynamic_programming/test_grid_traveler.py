from grid_traveler import grid_traveler, grid_traveler_memo

def test_0():
    assert(grid_traveler(10,10) == grid_traveler_memo(10,10, dict()))
    assert(grid_traveler(2,3) == grid_traveler_memo(2,3, dict()))
    assert(grid_traveler(2,1) == grid_traveler_memo(2,1, dict()))
    assert(grid_traveler(1,1) == grid_traveler_memo(1,1, dict()))