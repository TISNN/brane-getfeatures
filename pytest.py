from prepocessing import processing

# set input variables
input = "py_train"

# local testing
def test_features():
    print(f"Testing feature engineering using {input}...")
    output = processing(input)
    assert output[:8] == "features", "Not correct output"
    print(output)
    print("Testing is done, no problem.")

if __name__ == "__main__":
    test_features()