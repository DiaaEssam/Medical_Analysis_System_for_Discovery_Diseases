# compiled_pyke_files.py

from pyke import target_pkg

pyke_version = '1.1.1'
compiler_version = 1
target_pkg_version = 1

try:
    loader = __loader__
except NameError:
    loader = None

def get_target_pkg():
    return target_pkg.target_pkg(__name__, __file__, pyke_version, loader, {
         ('', '', 'medical_facts.kfb'):
           [1672126742.848565, 'medical_facts.fbc'],
         ('', '', 'medical_questions.kqb'):
           [1672126742.848565, 'medical_questions.qbc'],
         ('', '', 'medical_rules.krb'):
           [1672126742.8954687, 'medical_rules_bc.py'],
         ('', '', 'venv\\Lib\\site-packages\\pyke\\krb_compiler\\compiler.krb'):
           [1672126742.9579546, 'compiler_bc.py'],
        },
        compiler_version)

