
# Ramdomizes certain values given to
# a student in an instance of this exercise

import sys, os, random, string


def teacher_input(random_numbers):
  """
  Defines the contents of `teacher-input.txt` to which `run.sh`
  concatenates the student submission as the exercise is posted to
  MOOC Grader for grading.

  Generates 3 random numbers and forms a string containing
  the MathCheck configuration for this exercise.
  """

  return \
    u"arithmetic\n" + \
    u"f_nodes 3\n" + \
    u"{}/3^({}) + {}\n".format(random_numbers[0],random_numbers[1],random_numbers[2],)


def instructions(random_numbers):
  """
  Defines the student instructions written to `config.yaml`.
  The instructions must be in HTML format.
  """

  # Notice the indentations,
  # as this is going to get written to a YAML file.
  return \
    u"  <p>\n" + \
    u"    Laske lausekkeen `{}/d^{}+{}` arvo, kun `d=3`.\n".format(random_numbers[0],random_numbers[1],random_numbers[2],) + \
    u"    Anna vastaus kokonaislukuna tai murtolukuna `a/b`,\n" + \
    u"    missä `a` ja `b` ovat kokonaislukuja.\n" + \
    u"  </p>"


# This is needed for MOOC Grader,
# as it gives the course key as an
# argument to any generators specified in
# the exercise config.yaml
# and creates necessary folders based on that.
instance_dir = sys.argv[1]
if not os.path.exists(instance_dir):
   os.makedirs(instance_dir)


# Random number generation

random_numbers = []
for i in range(3):

  random_number = random.randint(-10,10)

  # Ensuring the lack of zeros
  while random_number == 0:
    random_number = random.randint(-10,10)
  
  # If first entry, no restrictions
  if i == 0:
    random_numbers.append(random_number)
  # Otherwise number must not exist in list
  else:
    while random_number in random_numbers or random_number == 0:
      random_number = random.randint(-10,10)
    random_numbers.append(random_number)

#instance_dir = os.path.dirname(os.path.realpath(__file__))

for rnum, letter in zip(random_numbers, string.ascii_uppercase):
  with open(os.path.join(instance_dir, letter), "w") as nf:
    nf.write(str(rnum))


# Saving the generated numbers to teacher-input.txt
with open(os.path.join(instance_dir, "teacher-input.txt"), "w") as f:
    f.write(teacher_input(random_numbers))
