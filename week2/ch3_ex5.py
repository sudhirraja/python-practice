def is_pass(expected, actual):
    """Return True if actual matches expected, else False."""
    return expected == actual
def run_speed_tests(speeds, expected):
    """Check every measured speed; return how many passed."""
    passed = 0
    for speed in speeds:
        if is_pass(expected, speed):
            print("Speed", speed, "PASS")
            passed = passed + 1
        else:
            print("Speed", speed, "FAIL")
    return passed

#print(is_pass(400, 400))
#print(is_pass(400, 100))
def summarize(total, passed):
    failed = total - passed
    rate = passed / total * 100
    return failed, rate

speeds = [400, 100, 400]
count = run_speed_tests(speeds, 400)
print(count, "of", len(speeds), "ports passed")

failed, rate = summarize(len(speeds), count)
print("Failed:", failed, "Pass rate:", round(rate, 1), "%")
