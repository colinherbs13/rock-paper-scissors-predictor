# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

# we need this to be global to keep track of all combination history
# in format sequence: frequency
sequences = {}


def player(prev_play, opponent_history=[]):
  if prev_play != '':
    opponent_history.append(prev_play)
  guess = ""
  # number of turns we look back for history 
  # (can play around with this, but 3 seems to work the best)
  pat_num = 3
  history = opponent_history
  # once we get to the point where we can look back, create a new pattern
  if len(history) > pat_num:
    pattern = "".join(history[-pat_num:])

    # we look back one additional turn and register that pattern into the dict
    # if there is a new sequence, create a new one in the dict, 
    # otherwise we have seen it before so add to the key
    past_sequence = "".join(history[-(pat_num + 1):])
    if past_sequence in sequences:
      sequences[past_sequence] += 1
    else:
      sequences[past_sequence] = 1

    # possible responses to the pattern
    possible = [pattern + "R", pattern + "P", pattern + "S"]

    # register all possible patterns in the dict for ease of access
    for i in possible:
      if i not in sequences.keys():
        sequences[i] = 0

    # get which possible sequence has appeared the most, and guess
    predict = max(possible, key=lambda key: sequences[key])

    # guess answers based on predicted turn
    if predict[-1] == "P":
      guess = "S"
    if predict[-1] == "R":
      guess = "P"
    if predict[-1] == "S":
      guess = "R"
  return guess
