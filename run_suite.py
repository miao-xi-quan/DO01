import unittest

from tools.HTMLTestReportCN import HTMLTestRunner

suite = unittest.defaultTestLoader.discover("./scripts")

with open("./report/report.html","wb") as f:
    HTMLTestRunner(stream=f).run(suite)