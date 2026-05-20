import sys

# On indique le dossier
sys.path.insert(0, '/home/tom60chat/sites/UPJV/')

# On importe l'app Flask pure
from app import app

# On crée la fonction wrapper directement ici, côté serveur !
def application(environ, start_response):
    # On force le préfixe avant même que Flask ne voie la requête
    environ['SCRIPT_NAME'] = '/UPJV/MovieDB'
    return app(environ, start_response)