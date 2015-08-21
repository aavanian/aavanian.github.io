import pickle
import time
import sys

with open('commit_count.pickle', 'rb') as f:
    commit_count = pickle.load(f)

commit_count += 1

with open('commit_count.pickle', 'wb') as f:
    pickle.dump(commit_count, f)

try:
    print('Blog build #', commit_count, '-', time.strftime('%Y-%m-%d %H:%M:%S %Z'), '[ci skip]', flush = True)
except (BrokenPipeError, IOError):
    pass

sys.stderr.close()
