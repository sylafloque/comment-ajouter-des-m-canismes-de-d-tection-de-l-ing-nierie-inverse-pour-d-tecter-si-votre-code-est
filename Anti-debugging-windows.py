#Ce code crée une instance de la classe PyDbg et attache le processus en cours. Il ajoute ensuite un point d'arrêt sur la fonction check_debugger, qui est déclenchée lorsque le débogueur tente d'attacher au processus. Si une exception de débogage est détectée, le processus est tué.

#Cet exemple est assez simple et peut être contourné par des outils de débogage plus avancés. Il est donc important de comprendre que l'anti-debugging n'est pas une mesure de sécurité absolue, mais plutôt un obstacle supplémentaire pour les attaquants potentiels.

from pydbg import *
from pydbg.defines import *

# Fonction de rappel qui est déclenchée lorsque le débogueur tente d'attacher au processus
def check_debugger(dbg):
    if dbg.dbg.dwDebugEventCode == EXCEPTION_DEBUG_EVENT:
        # Si l'exception est une erreur de débogage, tue le processus
        if dbg.dbg.u.Exception.ExceptionRecord.ExceptionCode == EXCEPTION_ACCESS_DENIED:
            dbg.terminate_process()
            return DBG_CONTINUE
    return DBG_CONTINUE

# Crée une instance de la classe PyDbg et attache le processus en cours
dbg = pydbg()
dbg.attach(pydbg.get_process_id_by_name(""))

# Ajoute le point d'arrêt sur la fonction check_debugger
addr = dbg.func_resolve_debuggee("kernel32.dll", "DebugActiveProcess")
dbg.bp_set(addr, handler=check_debugger)

# Continue l'exécution du programme jusqu'à la fin
dbg.run()
