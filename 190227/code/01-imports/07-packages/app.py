import foo
#import foo.bar

foo.func()
# foo.bar.func() # Только если import foo.bar

import os
# import os.path
os.path.join  # Внезапно работает, но это особенность os

