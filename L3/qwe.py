"""
def get_field

def get_score

def has_moves
    true or folse

def move

lib curses

4x4
"""
import time

print("Progress: ", end='', flush=True)
for i in range(11):
    print('%2d %s' % (i * 10, '%'), end='\b\b\b\b', flush=True)
    time.sleep(1)
print()
