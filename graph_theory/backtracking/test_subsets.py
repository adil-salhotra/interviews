from subsets import subsets

def test_0():
    
    nums = [1]
    assert(sorted(subsets(nums)) == sorted([[], [1]]))

def test_1():
    nums = [1,2,3]
    
    assert(sorted(subsets(nums)) == sorted([[], [1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]))