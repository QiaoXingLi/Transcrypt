import org.transcrypt.autotester

import classes
import conditional_expressions
import control_structures
import data_structures
import exceptions
import indices_and_slices
import list_comprehensions
import modules
import simple_and_augmented_assignment
import tuple_assignment

autoTester = org.transcrypt.autotester.AutoTester ()

autoTester.run (classes, 'classes')
autoTester.run (conditional_expressions, 'conditional_expressions')
autoTester.run (control_structures, 'control_structures')
autoTester.run (data_structures, 'data_structures')
autoTester.run (exceptions, 'exceptions')
autoTester.run (indices_and_slices, 'indices_and_slices')
autoTester.run (list_comprehensions, 'list_comprehensions')
autoTester.run (modules, 'modules')
autoTester.run (simple_and_augmented_assignment, 'simple_and_augmented_assignment')
autoTester.run (tuple_assignment, 'tuple_assignemt')

autoTester.done ()
