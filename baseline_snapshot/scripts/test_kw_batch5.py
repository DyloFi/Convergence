import pathlib
import sys
import collections
import re

sys.path.insert(0, '.')
from scripts.audit_verification import BROKEN_TEMPLATE_PATTERNS

root = pathlib.Path("Kondratiev Waves")

# Let's inspect current duplication in Kondratiev Waves
from scripts.audit_verification import ConvergenceAuditor
auditor = ConvergenceAuditor()
res = auditor.check_cross_report_duplication("Kondratiev Waves")
print("Current KW duplication status:", res)
