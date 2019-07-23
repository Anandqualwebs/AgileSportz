from unittest import TestLoader, TestSuite, TextTestRunner
from Tests.Login import LoginTest
from Tests.Dashboard import DashboardTest




if __name__ == "__main__":
    loader = TestLoader()
    suite = TestSuite((
          loader.loadTestsFromTestCase(LoginTest),
          loader.loadTestsFromTestCase(DashboardTest),


    ))

    runner = TextTestRunner(verbosity=2)
    runner.run(suite)
