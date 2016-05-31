

STATUS_CHOICES = (
    ('P', 'Proximamente'),
    ('A', 'En Emision'),
    ('F', 'Finalizada')
)

RANK_CHOICES = (
    ('1', 'Mala'),
    ('2', 'Regular'),
    ('3', 'Buena'),
    ('4', 'Muy Buena'),
    ('5', 'Excelente'),
)

SI_NO_CHOICES = (
    (True, "Si"),
    (False, "No")
)


RELACION_SERIES_CHOICES = (
    ('N', 'No Especificada'),
    ('S', 'Secuela'),
    ('P', 'Precuela'),
    ('H', 'Historia Paralela'),
    ('O', 'Ovas'),
    ('M', 'Pelicula'),
    ('A', 'Alternativo'),
    ('X', 'Principal'),
)

INVERSE_RELATION_SERIE = {
    'N': 'No Especificada',
    'S': 'Precuela',
    'P': 'Secuela',
    'H': 'Historia Paralela',
    'O': 'Precuela',
    'M': 'Principal',
    'A': 'Principal',
    'X': 'No Especificada',
}