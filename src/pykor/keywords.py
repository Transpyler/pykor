TRANSLATIONS = {
    # Loops
    '반복': 'for',
    # '에': 'for',
    '패스': 'pass', '넘어가기': 'pass',
    '중단': 'break',
    '동안': 'while',

    # Conditions
    '만약': 'if', '조건': 'if',
    '그밖에만약': 'elif', '안되면': 'elif',
    '그밖에': 'else', '다안되면': 'else',

    # Singleton values
    '거짓': 'False',
    '없음': 'None',
    '참': 'True',

    # Operators
    # '되려고': 'is',
    '에서': 'in',
    '안': 'not',
    '또는': 'or',
    '와': 'and',
    '로써': 'as',
    '삭제': 'del',

    # Function/class definitions (TODO)
    '정의': 'def',
    '클래스': 'class',
    # 'defina': 'def',
    '함수': 'def', 'funcion': 'def',
    # 'generar': 'yield',
    # 'gestiona': 'yield',
    # 'regresar': 'return',
    '반환': 'return',

    # Error
    '시도': 'try',
    # '해보기': 'try',
    '빼고': 'except', '예외': 'except',
    '마침내': 'finally', '결국': 'finally',
    '예외발생': 'raise', '발생': 'raise',

    # Other
    '불러오기': 'import',
    # 'importe': 'import',
    '함께': 'with',
}


# Here we can define multiple keyword conversions
SEQUENCE_TRANSLATIONS = {
    # Example
    # ('define', 'function'): 'def',
}


# Here we define sequences of tokens that are definitively errors and the
# corresponding error messages.
ERROR_GROUPS = {
    # ('for', 'for'): 'Repeated use of keyword 'for',
}
