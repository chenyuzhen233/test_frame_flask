import unittest


if __name__ == '__main__':
    case_path = "test"
    load = unittest.TestLoader()
    all_case = load.discover(case_path, pattern="test*.py", top_level_dir=None)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(all_case)