'''ensemble de fonctions permettant de manipuler
les mots de la langue française'''

import random

FILENAME = "corpus.txt"
ALPHABET = list("abcdefghijklmnopqrstuvwxyz")
VOYELLES = list("aeiouy")
CONSONNES = list("bcdfghjklmnpqrstvwxz")

#### Fonctions secondaires

def read_data(filename):
    """
    >>> mots = read_data(FILENAME)
    >>> isinstance(mots, list)
    True
    >>> len(mots)
    336531
    >>> mots[1]
    'à'
    >>> mots[328570]
    'vaincre'
    >>> mots[290761]
    'sans'
    >>> mots[233574]
    'péril'
    >>> mots[221712]
    'on'
    >>> mots[324539]
    'triomphe'
    >>> mots[290761]
    'sans'
    >>> mots[166128]
    'gloire'
    """
    with open(filename, mode="r", encoding="utf8") as f :
        lines = f.readlines()
        l = []
        for line in lines :
            l.append(line.rstrip("\n").strip())
    return l


def ensemble_mots(filename):
    """retourne les mots contenus dans filename

    Args:
        filename (str): nom du fichier

    Returns:
        list: la liste des mots

    >>> mots = ensemble_mots(FILENAME)
    >>> isinstance(mots, set)
    True
    >>> len(mots)
    336531
    >>> "glomérules" in mots
    True
    >>> "glycosudrique" in mots
    False
    """
    liste = read_data(filename)
    res = set()
    for elt in liste :
        res.add(elt)
    return res


def mots_de_n_lettres(mots, n):
    """retourne le sous ensemble des mots de n lettres

    Args:
        mots (set): ensemble de mots
        n (int): nombre de lettres

    Returns:
        set: sous ensemble des mots de n lettres

    >>> mots = ensemble_mots(FILENAME)
    >>> m15 = mots_de_n_lettres(mots, 15)
    >>> isinstance(m15, set)
    True
    >>> len(m15)
    8730
    >>> list({ len(mots_de_n_lettres(mots,i)) for i in range(15,26)})
    [4418, 2, 4, 2120, 42, 11, 205, 977, 437, 8730, 94]
    >>> sorted(list(mots_de_n_lettres(mots,23)))[0]
    'constitutionnalisassent'
    >>> sorted(list(mots_de_n_lettres(mots,24)))
    ['constitutionnalisassions', 'constitutionnaliseraient', 'hospitalo-universitaires',
    'oto-rhino-laryngologiste']
    >>> sorted(list(mots_de_n_lettres(mots,25)))
    ['anticonstitutionnellement', 'oto-rhino-laryngologistes']
    """
    res = set()
    for mot in mots :
        if len(mot) == n :
            res.add(mot)
    return res


def mots_avec(mots, s):
    """retourne le sous ensemble des mots incluant la lettre l

    Args:
        mots (set): ensemble de mots
        s (str): chaine de caractères à inclure

    Returns:
        set: sous ensemble des mots incluant la chaine de caractères s

    >>> mots = ensemble_mots(FILENAME)
    >>> mk = mots_avec(mots, 'k')
    >>> isinstance(mk, set)
    True
    >>> len(mk)
    1621
    >>> sorted(list(mk))[35:74:7]
    ['ankyloseraient', 'ankyloserons', 'ankylostome', 'ankylosée', 'ashkénaze', 'bachi-bouzouks']
    >>> sorted(list(mk))[147:359:38]
    ['black', 'blackboulèrent', 'cheikhs', 'cokéfierais', 'dock', 'dénickeliez']
    >>> sorted(list(mk))[999::122]
    ['képi', 'nickela', 'parkérisiez', 'semi-coke', 'stockais', 'week-end']
    """
    res = set()
    for mot in mots :
        if s in mot :
            res.add(mot)
    return res


def cherche1(mots, start, stop, n):
    """retourne le sous ensemble des mots de n lettres commençant par start et finissant par stop

    Args:
        mots (set): ensemble de mots
        start (str): première lettre
        stop (str): dernière lettre
        n (int): nombre de lettres

    Returns:
        set: sous ensemble des mots de n lettres commençant par start et finissant par stop

    >>> mots = ensemble_mots(FILENAME)
    >>> m_z = cherche1(mots, 'z', 'z', 7)
    >>> isinstance(m_z, set)
    True
    >>> len(m_z)
    10
    >>> sorted(list(m_z))[4:7]
    ['zinguez', 'zippiez', 'zonerez']
    """
    res = set()
    for mot in mots :
        if mot.startswith(start) and mot.endswith(stop) and len(mot) == n :
            res.add(mot)
    return res


def cherche2(mots, lstart, lmid, lstop, nmin, nmax):
    """effectue une recherche complexe dans un ensemble de mots

    Args:
        mots (set): ensemble de mots
        lstart (list): liste des préfixes
        lmid (list): liste des chaines de caractères intermédiaires
        lstop (list): liste des suffixes
        nmin (int): nombre de lettres minimum
        nmax (int): nombre de lettres maximum

    Returns:
        set: retourne le sous ensemble des mots commençant par une chaine présente dans 
        lstart, contenant une chaine présente dans lmid et finissant par une chaine présente 
        dans lstop, avec un nombre de lettres entre nmin et nmax

    >>> mots = ensemble_mots(FILENAME)
    >>> mab17ez = cherche2(mots, 'a', 'b', 'z', 16, 16)
    >>> isinstance(mab17ez, set)
    True
    >>> len(mab17ez)
    1
    >>> mab17ez
    {'alphabétisassiez'}
    """
    res = set()
    if not lstart or not lmid or not lstop:
        return res

    for mot in mots:
        bo = True
        if not nmin <= len(mot) <= nmax :
            bo = False
        if bo and not mot.startswith(tuple(lstart)):
            bo = False
        if bo and not mot.endswith(tuple(lstop)):
            bo = False
        if bo:
            for chaine in lmid:
                if chaine not in mot:
                    bo = False
                    break
        if bo:
            res.add(mot)

    return res


def main():
    """
    Fonction principale
    """
    mots = read_data(FILENAME)
    ens = ensemble_mots(FILENAME)
    print( [ mot for mot in ["chronophage", "procrastinateur", "dangerosité",
                             "gratifiant"] if mot in ens ] )
    m17 = mots_de_n_lettres(ens, 17)
    print(len(m17))
    print( random.sample(list(m17), 10) )
    mk = mots_avec(ens, 'k')
    print(len(mk))
    print( random.sample(list(mk), 5) )
    moo = mots_avec(ens, 'oo')
    print(len(moo))
    print( random.sample(list(moo), 5) )
    mz14 = cherche1(ens, 'z', '', 14)
    print(mz14)
    m21z = cherche1(ens, '', 'z', 18)
    print(m21z)
    m_z = cherche1(mots, 'z', 'z', 7)
    print(m_z)
    mab17ez = mots_avec(cherche1(ens, 'sur', 'ons', 17), 'x')
    print(mab17ez)
    mab17ez = cherche2(mots, 'a', 'b', 'z', 16, 16)
    print(mab17ez)

if __name__ == "__main__":
    main()
