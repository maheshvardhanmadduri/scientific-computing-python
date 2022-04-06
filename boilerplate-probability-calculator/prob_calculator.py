import copy
import random
from collections import Counter
# Consider using the modules imported above.

class Hat:
  def __init__(self, **args):
    self.balls = args
    self.contents = []
    self.n_balls = 0
    for k,v in args.items():
      for i in range(0, v):
        self.contents.append(k)
      self.n_balls += v
      
  
  def draw(self, n_balls_to_draw):
    if n_balls_to_draw > self.n_balls:
      return self.contents
    balls_drawn = []
    balls_drawn = random.sample(self.contents, n_balls_to_draw)
    for i in balls_drawn:
      self.contents.remove(i)
    return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  if num_balls_drawn > hat.n_balls:
    num_balls_drawn = hat.n_balls

  experiments = []
  for i in range(0, num_experiments):
    experiments.append(random.sample(hat.contents, num_balls_drawn))

  counter_experiments = []
  for i in experiments:
    counter_experiments.append(Counter(i))
  
  n_success = 0
  for i in counter_experiments:
    bool_success = True
    for k,v in expected_balls.items():
      if v > i[k] :
        bool_success = False
        break
    if bool_success:
      n_success += 1
  
  return n_success/num_experiments

    
    