import sys

print('\n'.join(sys.path))
sys.path = []

import pytest  # Упс!
