#!/usr/bin/env python
import argparse

from src.byproducts.main import generate_byproducts
from src.byproducts.update_byproducts_repositories import update_all_byproducts

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Création de produits dérivés depuis les schémas du SNDS')
    parser.add_argument('-d', '--erd', dest='generate_erd',
                        action='store_const', const=True, default=False,
                        help="Générer un diagramme d'entité relationnelle (ERD), "
                             "en utilisant PostgreSQL et schema-crawler (nécessite Docker)")
    parser.add_argument('-u', '--update', dest='update', action='store_const',
                        const=True, default=False,
                        help="Propagation des modifications du schéma dans les dépôts des produits dérivés. "
                             "Cette action n'est déclenchée que par GitLab-CI")
    parser.add_argument('-l', '--local', dest='local', action='store_const',
                        const=True, default=False,
                        help="Tester un update des produits dérivés en local, sans mettre à jour le remote.")

    args = parser.parse_args()

    generate_byproducts(args.generate_erd)

    if args.update:
        update_all_byproducts(args.local)
