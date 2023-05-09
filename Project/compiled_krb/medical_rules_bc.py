# medical_rules_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def diabetes_strong_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 True):
            context.end_save_all_undo()
            if context.lookup_data('ans1') == True:
              if context.lookup_data('ans3') == True:
                rule.rule_base.num_bc_rule_successes += 1
                yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def diabetes_strong_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 True):
            context.end_save_all_undo()
            if context.lookup_data('ans2') == True:
              if context.lookup_data('ans3') == True:
                rule.rule_base.num_bc_rule_successes += 1
                yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def diabetes_weak(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 True):
            context.end_save_all_undo()
            if context.lookup_data('ans4') == True:
              if context.lookup_data('ans5') == True:
                rule.rule_base.num_bc_rule_successes += 1
                yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cardio_strong_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 True):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   True):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                     True):
                context.end_save_all_undo()
                if context.lookup_data('ans6') == True:
                  if context.lookup_data('ans7') == True:
                    if context.lookup_data('ans9') == True:
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cardio_strong_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 True):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   True):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                     True):
                context.end_save_all_undo()
                if context.lookup_data('ans6') == True:
                  if context.lookup_data('ans6') == True:
                    if context.lookup_data('ans9') == True:
                      rule.rule_base.num_bc_rule_successes += 1
                      yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cardio_strong_3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 False):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   True):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                     False):
                context.end_save_all_undo()
                if context.lookup_data('ans6') == True:
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def cardio_strong_4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_dysli', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "medical_rules.cardio_strong_4: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def hyper_common(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          if context.lookup_data('ans10') == True:
            rule.rule_base.num_bc_rule_successes += 1
            yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def hyper_accurate(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 190):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   190):
              context.end_save_all_undo()
              if context.lookup_data('ans10') == True:
                if context.lookup_data('ans19') > 140:
                  if context.lookup_data('ans20') > 90:
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dysli_strong(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 True):
            context.end_save_all_undo()
            if context.lookup_data('ans9') == True:
              if context.lookup_data('ans11') == True:
                rule.rule_base.num_bc_rule_successes += 1
                yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def dysli_weak(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          if context.lookup_data('ans22') == True:
            rule.rule_base.num_bc_rule_successes += 1
            yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def obesity_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               150):
          context.end_save_all_undo()
          if context.lookup_data('ans21') > 30.0:
            rule.rule_base.num_bc_rule_successes += 1
            yield
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def obesity_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_obes', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "medical_rules.obesity_2: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def neuro_strong_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               False):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 False):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   False):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                     False):
                context.end_save_all_undo()
                if context.lookup_data('ans12') == True:
                  if context.lookup_data('ans15') == True:
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def neuro_strong_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               False):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 False):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   False):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                     False):
                context.end_save_all_undo()
                if context.lookup_data('ans12') == True:
                  if context.lookup_data('ans13') == True:
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def neuro_strong_3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               False):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 False):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   False):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                     False):
                context.end_save_all_undo()
                if context.lookup_data('ans12') == True:
                  if context.lookup_data('ans14') == True:
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def neuro_strong_4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               False):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 False):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   False):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                     False):
                context.end_save_all_undo()
                if context.lookup_data('ans13') == True:
                  if context.lookup_data('ans14') == True:
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def neuro_strong_5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               False):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 False):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   False):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                     False):
                context.end_save_all_undo()
                if context.lookup_data('ans13') == True:
                  if context.lookup_data('ans15') == True:
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def neuro_strong_6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               False):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 False):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   False):
              context.end_save_all_undo()
              mark4 = context.mark(True)
              if rule.pattern(3).match_data(context, context,
                     False):
                context.end_save_all_undo()
                if context.lookup_data('ans14') == True:
                  if context.lookup_data('ans15') == True:
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
              else: context.end_save_all_undo()
              context.undo_to_mark(mark4)
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def neuro_strong11(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_diabetes', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "medical_rules.neuro_strong11: got unexpected plan from when clause 1"
            rule.rule_base.num_bc_rule_successes += 1
            yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def neuro_strong12(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_diabetes', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "medical_rules.neuro_strong12: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'has_arty', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "medical_rules.neuro_strong12: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def arterial_strong_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 True):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   True):
              context.end_save_all_undo()
              if context.lookup_data('ans16') == True:
                if context.lookup_data('ans17') == True:
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def arterial_strong_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 True):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   True):
              context.end_save_all_undo()
              if context.lookup_data('ans16') == True:
                if context.lookup_data('ans18') == True:
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def arterial_strong_3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        mark1 = context.mark(True)
        if rule.pattern(0).match_data(context, context,
               True):
          context.end_save_all_undo()
          mark2 = context.mark(True)
          if rule.pattern(1).match_data(context, context,
                 True):
            context.end_save_all_undo()
            mark3 = context.mark(True)
            if rule.pattern(2).match_data(context, context,
                   True):
              context.end_save_all_undo()
              if context.lookup_data('ans17') == True:
                if context.lookup_data('ans18') == True:
                  rule.rule_base.num_bc_rule_successes += 1
                  yield
            else: context.end_save_all_undo()
            context.undo_to_mark(mark3)
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        else: context.end_save_all_undo()
        context.undo_to_mark(mark1)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def diabetic_foot(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_arty', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "medical_rules.diabetic_foot: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'has_neuro', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "medical_rules.diabetic_foot: got unexpected plan from when clause 2"
                with engine.prove(rule.rule_base.root_name, 'has_diabetes', context,
                                  (rule.pattern(4),
                                   rule.pattern(5),)) \
                  as gen_3:
                  for x_3 in gen_3:
                    assert x_3 is None, \
                      "medical_rules.diabetic_foot: got unexpected plan from when clause 3"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def meta_syndrome_1(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_hyper', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "medical_rules.meta_syndrome_1: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'has_obes', context,
                              (rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "medical_rules.meta_syndrome_1: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def meta_syndrome_2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_hyper', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "medical_rules.meta_syndrome_2: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'has_diabetes', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "medical_rules.meta_syndrome_2: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def meta_syndrome_3(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_obes', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "medical_rules.meta_syndrome_3: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'has_diabetes', context,
                              (rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "medical_rules.meta_syndrome_3: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def meta_syndrome_4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_hyper', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "medical_rules.meta_syndrome_4: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'has_dysli', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "medical_rules.meta_syndrome_4: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def meta_syndrome_5(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_obes', context,
                          (rule.pattern(0),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "medical_rules.meta_syndrome_5: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'has_dysli', context,
                              (rule.pattern(1),
                               rule.pattern(2),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "medical_rules.meta_syndrome_5: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def meta_syndrome_6(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_diabetes', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "medical_rules.meta_syndrome_6: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'has_dysli', context,
                              (rule.pattern(0),
                               rule.pattern(1),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "medical_rules.meta_syndrome_6: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def ather_strong(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        with engine.prove(rule.rule_base.root_name, 'has_meta', context,
                          (rule.pattern(0),
                           rule.pattern(1),)) \
          as gen_1:
          for x_1 in gen_1:
            assert x_1 is None, \
              "medical_rules.ather_strong: got unexpected plan from when clause 1"
            with engine.prove(rule.rule_base.root_name, 'has_diabetes', context,
                              (rule.pattern(2),
                               rule.pattern(3),)) \
              as gen_2:
              for x_2 in gen_2:
                assert x_2 is None, \
                  "medical_rules.ather_strong: got unexpected plan from when clause 2"
                rule.rule_base.num_bc_rule_successes += 1
                yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('medical_rules')
  
  bc_rule.bc_rule('diabetes_strong_1', This_rule_base, 'has_diabetes',
                  diabetes_strong_1, None,
                  (pattern.pattern_literal('polydipsia'),
                   pattern.pattern_literal('polyphagia'),),
                  (),
                  (contexts.variable('ans1'),
                   contexts.variable('ans3'),))
  
  bc_rule.bc_rule('diabetes_strong_2', This_rule_base, 'has_diabetes',
                  diabetes_strong_2, None,
                  (pattern.pattern_literal('polyurea'),
                   pattern.pattern_literal('polyphagia'),),
                  (),
                  (contexts.variable('ans2'),
                   contexts.variable('ans3'),))
  
  bc_rule.bc_rule('diabetes_weak', This_rule_base, 'maybe_diabetes',
                  diabetes_weak, None,
                  (pattern.pattern_literal('weightLoss'),
                   pattern.pattern_literal('weakImmunity'),),
                  (),
                  (contexts.variable('ans4'),
                   contexts.variable('ans5'),))
  
  bc_rule.bc_rule('cardio_strong_1', This_rule_base, 'has_cardio',
                  cardio_strong_1, None,
                  (pattern.pattern_literal('atherosclerosis'),
                   pattern.pattern_literal('shortBreath'),
                   pattern.pattern_literal('anginaPectoris'),),
                  (),
                  (contexts.variable('ans6'),
                   contexts.variable('ans7'),
                   contexts.variable('ans8'),
                   contexts.variable('ans9'),))
  
  bc_rule.bc_rule('cardio_strong_2', This_rule_base, 'has_cardio',
                  cardio_strong_2, None,
                  (pattern.pattern_literal('atherosclerosis'),
                   pattern.pattern_literal('exhaust'),
                   pattern.pattern_literal('anginaPectoris'),),
                  (),
                  (contexts.variable('ans6'),
                   contexts.variable('ans7'),
                   contexts.variable('ans8'),
                   contexts.variable('ans9'),))
  
  bc_rule.bc_rule('cardio_strong_3', This_rule_base, 'has_cardio',
                  cardio_strong_3, None,
                  (pattern.pattern_literal('atherosclerosis'),),
                  (),
                  (contexts.variable('ans6'),
                   contexts.variable('ans8'),
                   contexts.variable('ans7'),
                   contexts.variable('ans9'),))
  
  bc_rule.bc_rule('cardio_strong_4', This_rule_base, 'has_cardio',
                  cardio_strong_4, None,
                  (pattern.pattern_literal('dyslipidemia'),),
                  (),
                  (pattern.pattern_literal('anginaPectoris'),
                   pattern.pattern_literal('legPain'),))
  
  bc_rule.bc_rule('hyper_common', This_rule_base, 'has_hyper',
                  hyper_common, None,
                  (pattern.pattern_literal('headache'),),
                  (),
                  (contexts.variable('ans10'),))
  
  bc_rule.bc_rule('hyper_accurate', This_rule_base, 'has_hyper',
                  hyper_accurate, None,
                  (pattern.pattern_literal('headache'),
                   pattern.pattern_literal('BloodPressure'),),
                  (),
                  (contexts.variable('ans10'),
                   contexts.variable('ans19'),
                   contexts.variable('ans20'),))
  
  bc_rule.bc_rule('dysli_strong', This_rule_base, 'has_dysli',
                  dysli_strong, None,
                  (pattern.pattern_literal('anginaPectoris'),
                   pattern.pattern_literal('legPain'),),
                  (),
                  (contexts.variable('ans9'),
                   contexts.variable('ans11'),))
  
  bc_rule.bc_rule('dysli_weak', This_rule_base, 'maybe_dysli',
                  dysli_weak, None,
                  (pattern.pattern_literal('shortBreath'),),
                  (),
                  (contexts.variable('ans22'),))
  
  bc_rule.bc_rule('obesity_1', This_rule_base, 'has_obes',
                  obesity_1, None,
                  (pattern.pattern_literal('BMI_Large'),),
                  (),
                  (contexts.variable('ans21'),))
  
  bc_rule.bc_rule('obesity_2', This_rule_base, 'has_obes',
                  obesity_2, None,
                  (pattern.pattern_literal('cardiovascular'),
                   pattern.pattern_literal('diabetes'),
                   pattern.pattern_literal('hypertension'),),
                  (),
                  (pattern.pattern_literal('BMI_Large'),))
  
  bc_rule.bc_rule('neuro_strong_1', This_rule_base, 'has_neuro',
                  neuro_strong_1, None,
                  (pattern.pattern_literal('numb'),
                   pattern.pattern_literal('redness'),),
                  (),
                  (contexts.variable('ans12'),
                   contexts.variable('ans13'),
                   contexts.variable('ans14'),
                   contexts.variable('ans15'),))
  
  bc_rule.bc_rule('neuro_strong_2', This_rule_base, 'has_neuro',
                  neuro_strong_2, None,
                  (pattern.pattern_literal('numb'),
                   pattern.pattern_literal('tingle'),),
                  (),
                  (contexts.variable('ans12'),
                   contexts.variable('ans13'),
                   contexts.variable('ans14'),
                   contexts.variable('ans15'),))
  
  bc_rule.bc_rule('neuro_strong_3', This_rule_base, 'has_neuro',
                  neuro_strong_3, None,
                  (pattern.pattern_literal('numb'),
                   pattern.pattern_literal('burning_pain'),),
                  (),
                  (contexts.variable('ans12'),
                   contexts.variable('ans13'),
                   contexts.variable('ans14'),
                   contexts.variable('ans15'),))
  
  bc_rule.bc_rule('neuro_strong_4', This_rule_base, 'has_neuro',
                  neuro_strong_4, None,
                  (pattern.pattern_literal('tingle'),
                   pattern.pattern_literal('burning_pain'),),
                  (),
                  (contexts.variable('ans12'),
                   contexts.variable('ans13'),
                   contexts.variable('ans14'),
                   contexts.variable('ans15'),))
  
  bc_rule.bc_rule('neuro_strong_5', This_rule_base, 'has_neuro',
                  neuro_strong_5, None,
                  (pattern.pattern_literal('tingle'),
                   pattern.pattern_literal('redness'),),
                  (),
                  (contexts.variable('ans12'),
                   contexts.variable('ans13'),
                   contexts.variable('ans14'),
                   contexts.variable('ans15'),))
  
  bc_rule.bc_rule('neuro_strong_6', This_rule_base, 'has_neuro',
                  neuro_strong_6, None,
                  (pattern.pattern_literal('burning_pain'),
                   pattern.pattern_literal('redness'),),
                  (),
                  (contexts.variable('ans12'),
                   contexts.variable('ans13'),
                   contexts.variable('ans14'),
                   contexts.variable('ans15'),))
  
  bc_rule.bc_rule('neuro_strong11', This_rule_base, 'has_neuro',
                  neuro_strong11, None,
                  (pattern.pattern_literal('peripheralNeuro'),),
                  (),
                  (contexts.variable('var1'),
                   contexts.variable('var2'),))
  
  bc_rule.bc_rule('neuro_strong12', This_rule_base, 'has_neuro',
                  neuro_strong12, None,
                  (pattern.pattern_literal('peripheralNeuro'),),
                  (),
                  (contexts.variable('var1'),
                   contexts.variable('var2'),
                   contexts.variable('var3'),
                   contexts.variable('var4'),))
  
  bc_rule.bc_rule('arterial_strong_1', This_rule_base, 'has_arty',
                  arterial_strong_1, None,
                  (pattern.pattern_literal('strain'),
                   pattern.pattern_literal('weak_muscles'),),
                  (),
                  (contexts.variable('ans16'),
                   contexts.variable('ans17'),
                   contexts.variable('ans18'),))
  
  bc_rule.bc_rule('arterial_strong_2', This_rule_base, 'has_arty',
                  arterial_strong_2, None,
                  (pattern.pattern_literal('strain'),
                   pattern.pattern_literal('delay_wound'),),
                  (),
                  (contexts.variable('ans16'),
                   contexts.variable('ans17'),
                   contexts.variable('ans18'),))
  
  bc_rule.bc_rule('arterial_strong_3', This_rule_base, 'has_arty',
                  arterial_strong_3, None,
                  (pattern.pattern_literal('weak_muscles'),
                   pattern.pattern_literal('delay_wound'),),
                  (),
                  (contexts.variable('ans16'),
                   contexts.variable('ans17'),
                   contexts.variable('ans18'),))
  
  bc_rule.bc_rule('diabetic_foot', This_rule_base, 'has_foot',
                  diabetic_foot, None,
                  (pattern.pattern_literal('peripheralArty'),
                   pattern.pattern_literal('peripheralNeuro'),
                   pattern.pattern_literal('diabetes'),),
                  (),
                  (contexts.variable('var3'),
                   contexts.variable('var4'),
                   contexts.variable('var5'),
                   contexts.variable('var6'),
                   contexts.variable('var1'),
                   contexts.variable('var2'),))
  
  bc_rule.bc_rule('meta_syndrome_1', This_rule_base, 'has_meta',
                  meta_syndrome_1, None,
                  (pattern.pattern_literal('hypertension'),
                   pattern.pattern_literal('obesity'),),
                  (),
                  (contexts.variable('var3'),
                   contexts.variable('var4'),
                   contexts.variable('var5'),))
  
  bc_rule.bc_rule('meta_syndrome_2', This_rule_base, 'has_meta',
                  meta_syndrome_2, None,
                  (pattern.pattern_literal('hypertension'),
                   pattern.pattern_literal('diabetes'),),
                  (),
                  (contexts.variable('var3'),
                   contexts.variable('var4'),
                   contexts.variable('var1'),
                   contexts.variable('var2'),))
  
  bc_rule.bc_rule('meta_syndrome_3', This_rule_base, 'has_meta',
                  meta_syndrome_3, None,
                  (pattern.pattern_literal('obesity'),
                   pattern.pattern_literal('diabetes'),),
                  (),
                  (contexts.variable('var5'),
                   contexts.variable('var1'),
                   contexts.variable('var2'),))
  
  bc_rule.bc_rule('meta_syndrome_4', This_rule_base, 'has_meta',
                  meta_syndrome_4, None,
                  (pattern.pattern_literal('hypertension'),
                   pattern.pattern_literal('dyslipidemia'),),
                  (),
                  (contexts.variable('var3'),
                   contexts.variable('var4'),
                   contexts.variable('var1'),
                   contexts.variable('var2'),))
  
  bc_rule.bc_rule('meta_syndrome_5', This_rule_base, 'has_meta',
                  meta_syndrome_5, None,
                  (pattern.pattern_literal('obesity'),
                   pattern.pattern_literal('dyslipidemia'),),
                  (),
                  (contexts.variable('var5'),
                   contexts.variable('var1'),
                   contexts.variable('var2'),))
  
  bc_rule.bc_rule('meta_syndrome_6', This_rule_base, 'has_meta',
                  meta_syndrome_6, None,
                  (pattern.pattern_literal('diabetes'),
                   pattern.pattern_literal('dyslipidemia'),),
                  (),
                  (contexts.variable('var1'),
                   contexts.variable('var2'),))
  
  bc_rule.bc_rule('ather_strong', This_rule_base, 'has_ather',
                  ather_strong, None,
                  (pattern.pattern_literal('metabolicSyndrome'),
                   pattern.pattern_literal('diabetes'),),
                  (),
                  (contexts.variable('var1'),
                   contexts.variable('var2'),
                   contexts.variable('var3'),
                   contexts.variable('var4'),))


Krb_filename = '..\\medical_rules.krb'
Krb_lineno_map = (
    ((14, 18), (4, 4)),
    ((22, 22), (6, 6)),
    ((26, 26), (7, 7)),
    ((28, 28), (8, 8)),
    ((29, 29), (9, 9)),
    ((46, 50), (12, 12)),
    ((54, 54), (14, 14)),
    ((58, 58), (15, 15)),
    ((60, 60), (16, 16)),
    ((61, 61), (17, 17)),
    ((78, 82), (20, 20)),
    ((86, 86), (22, 22)),
    ((90, 90), (23, 23)),
    ((92, 92), (24, 24)),
    ((93, 93), (25, 25)),
    ((110, 114), (28, 28)),
    ((118, 118), (30, 30)),
    ((122, 122), (31, 31)),
    ((126, 126), (32, 32)),
    ((130, 130), (33, 33)),
    ((132, 132), (34, 34)),
    ((133, 133), (35, 35)),
    ((134, 134), (36, 36)),
    ((155, 159), (39, 39)),
    ((163, 163), (41, 41)),
    ((167, 167), (42, 42)),
    ((171, 171), (43, 43)),
    ((175, 175), (44, 44)),
    ((177, 177), (45, 45)),
    ((178, 178), (46, 46)),
    ((179, 179), (47, 47)),
    ((200, 204), (50, 50)),
    ((208, 208), (52, 52)),
    ((212, 212), (53, 53)),
    ((216, 216), (54, 54)),
    ((220, 220), (55, 55)),
    ((222, 222), (56, 56)),
    ((243, 247), (59, 59)),
    ((249, 255), (61, 61)),
    ((268, 272), (64, 64)),
    ((276, 276), (66, 66)),
    ((278, 278), (67, 67)),
    ((293, 297), (70, 70)),
    ((301, 301), (72, 72)),
    ((305, 305), (73, 73)),
    ((309, 309), (74, 74)),
    ((311, 311), (75, 75)),
    ((312, 312), (76, 76)),
    ((313, 313), (77, 77)),
    ((332, 336), (80, 80)),
    ((340, 340), (82, 82)),
    ((344, 344), (83, 83)),
    ((346, 346), (84, 84)),
    ((347, 347), (85, 85)),
    ((364, 368), (88, 88)),
    ((372, 372), (90, 90)),
    ((374, 374), (91, 91)),
    ((389, 393), (94, 94)),
    ((397, 397), (96, 96)),
    ((399, 399), (97, 97)),
    ((414, 418), (100, 100)),
    ((420, 425), (102, 102)),
    ((438, 442), (105, 105)),
    ((446, 446), (107, 107)),
    ((450, 450), (108, 108)),
    ((454, 454), (109, 109)),
    ((458, 458), (110, 110)),
    ((460, 460), (111, 111)),
    ((461, 461), (112, 112)),
    ((482, 486), (114, 114)),
    ((490, 490), (116, 116)),
    ((494, 494), (117, 117)),
    ((498, 498), (118, 118)),
    ((502, 502), (119, 119)),
    ((504, 504), (120, 120)),
    ((505, 505), (121, 121)),
    ((526, 530), (124, 124)),
    ((534, 534), (126, 126)),
    ((538, 538), (127, 127)),
    ((542, 542), (128, 128)),
    ((546, 546), (129, 129)),
    ((548, 548), (130, 130)),
    ((549, 549), (131, 131)),
    ((570, 574), (134, 134)),
    ((578, 578), (136, 136)),
    ((582, 582), (137, 137)),
    ((586, 586), (138, 138)),
    ((590, 590), (139, 139)),
    ((592, 592), (140, 140)),
    ((593, 593), (141, 141)),
    ((614, 618), (144, 144)),
    ((622, 622), (146, 146)),
    ((626, 626), (147, 147)),
    ((630, 630), (148, 148)),
    ((634, 634), (149, 149)),
    ((636, 636), (150, 150)),
    ((637, 637), (151, 151)),
    ((658, 662), (154, 154)),
    ((666, 666), (156, 156)),
    ((670, 670), (157, 157)),
    ((674, 674), (158, 158)),
    ((678, 678), (159, 159)),
    ((680, 680), (160, 160)),
    ((681, 681), (161, 161)),
    ((702, 706), (164, 164)),
    ((708, 714), (166, 166)),
    ((727, 731), (169, 169)),
    ((733, 739), (171, 171)),
    ((740, 746), (172, 172)),
    ((759, 763), (176, 176)),
    ((767, 767), (178, 178)),
    ((771, 771), (179, 179)),
    ((775, 775), (180, 180)),
    ((777, 777), (181, 181)),
    ((778, 778), (182, 182)),
    ((797, 801), (185, 185)),
    ((805, 805), (187, 187)),
    ((809, 809), (188, 188)),
    ((813, 813), (189, 189)),
    ((815, 815), (190, 190)),
    ((816, 816), (191, 191)),
    ((835, 839), (194, 194)),
    ((843, 843), (196, 196)),
    ((847, 847), (197, 197)),
    ((851, 851), (198, 198)),
    ((853, 853), (199, 199)),
    ((854, 854), (200, 200)),
    ((873, 877), (203, 203)),
    ((879, 885), (205, 205)),
    ((886, 892), (206, 206)),
    ((893, 899), (207, 207)),
    ((912, 916), (210, 210)),
    ((918, 924), (212, 212)),
    ((925, 930), (213, 213)),
    ((943, 947), (216, 216)),
    ((949, 955), (218, 218)),
    ((956, 962), (219, 219)),
    ((975, 979), (222, 222)),
    ((981, 986), (224, 224)),
    ((987, 993), (225, 225)),
    ((1006, 1010), (228, 228)),
    ((1012, 1018), (230, 230)),
    ((1019, 1025), (231, 231)),
    ((1038, 1042), (234, 234)),
    ((1044, 1049), (236, 236)),
    ((1050, 1056), (237, 237)),
    ((1069, 1073), (240, 240)),
    ((1075, 1081), (242, 242)),
    ((1082, 1088), (243, 243)),
    ((1101, 1105), (246, 246)),
    ((1107, 1113), (248, 248)),
    ((1114, 1120), (249, 249)),
)
