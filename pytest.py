from prepocessing import processing

# set input variables
input = "train"

# local testing
def test_features():
    print(f"Testing feature engineering using {input}...")
    assert processing(input) == "features was saved at ./data", "Not correct output"

    
if __name__ == "__main__":
    test_features()