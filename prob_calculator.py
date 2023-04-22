import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **arguments):
    self.arguments = arguments
    self.contents = []
    
    for color in arguments:
      for x in range(arguments.get(color)):
        self.contents.append(color)
    
    self.copy = copy.deepcopy(self.contents)
  
  def draw(self, number):
    if number > len(self.contents):
      return self.contents
    list = []
    for x in range(number):
      random_ball = random.choice(self.contents)
      self.contents.remove(random_ball)
      list.append(random_ball)
    return list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0
  N = num_experiments
  for x in range(num_experiments):
    expected_list = []
    for color in expected_balls:
      for x in range(expected_balls.get(color)):
        expected_list.append(color)
    expected_copy = copy.deepcopy(expected_list)
    new_hat = copy.deepcopy(hat)
    sample_list = new_hat.draw(num_balls_drawn)
    for color in sample_list:
      if color in expected_copy:
        expected_copy.remove(color)
    if len(expected_copy) == 0:
      M += 1
    expected_copy = expected_list
  probability = M / N
  return probability