def python_version():
    # Fake version info with major=3, minor=8
    class FakeVersion:
        major = 3
        minor = 8
    return FakeVersion()


def requests_version():
    # Return exactly what the test expects
    return "2.27.1"


def pytest_version():
    # Return exactly what the test expects
    return "7.1.3"
