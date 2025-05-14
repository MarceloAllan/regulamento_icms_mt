html_tags_for_class_paragraph = {  # lista a TAG que será atribuída a cada classificação de parágrafo
    'capitulo': 'h2',
    'artigo': 'p',
    'paragrafo': 'p',
    'titulo-capitulo-secao-ou-subsecao': 'h2',
    'inciso': 'p',
    'alinea': 'p',
    'item': 'p',
    'nota-explicativa': 'p',
    'secao': 'h2',
    'nota-de-rodape': 'p',
    'item-nota-de-rodape': 'p',
    'titulo': 'h2',
    'subsecao': 'h3',
    'livro': 'h1',
    'tabela': 'div',
    'titulo-tabela': 'h2',
    'anexo': 'h2',
    'texto-revogado': 'p',
    'cfop': 'p',
    'indice-remissivo': 'p',
    'titulo-regulamento': 'p',
    'norma-regulamento': 'p',
    'nota-de-consolidacao': 'p',
    'nao-classificado': 'p'
}

pattern_artigo = r'^\s?Art\.\s?'
pattern_artigo_com_numero = r'Art\.\s\d+(\.\d+)?\°?(-[A-Z])?'
pattern_capitulo = r'^\s*(CAPÍTULO\s|DISPOSIÇÕES\sPRELIMINARES)'
pattern_secao = r'^\s*Seção\s*'
pattern_subsecao = r'^Subseção\s*'
pattern_titulo = r'^Título\s*'
pattern_livro = r'^Livro\s*'
pattern_anexo = r'^Anexo\s*'
pattern_titulo_tabela = r'^Tabela\s*'
pattern_titulo_capitulo_secao_ou_subsecao = r'^D[AO]S?\s[A-Z]+'
pattern_alinea = r'^[a-z]{1,2}\-?\d?\)'
pattern_item = r'^\d+\)'
pattern_paragrafo = r'^\s*(§\s*\d+|Parágrafo\súnico)'
pattern_inciso = r'^(?:[IVXLCDM]+[\-\s*])'
pattern_nota_explicativa = r'^\s*Notas?\sexplicativas?'
pattern_nota_de_rodape = r'^\s*Notas?:'
pattern_item_nota_de_rodape = r'^\d+-?[A-Z]?\.'
pattern_paragrafo_em_branco = r'^\s*$'
pattern_tabela = r'^<table'
pattern_texto_revogado = r'^\(revogad'
pattern_cfop = r'^\d\.\d{3}\s*\-\s*'
pattern_paragrafo_vazio = r'^.$'
pattern_indice_remissivo = r'^\s*VIDE ÍNDICE REMISSIVO\s*$'
pattern_titulo_regulamento = r'^REGULAMENTO DO IMPOSTO SOBRE OPERAÇÕES RELATIVAS À CIRCULAÇÃO DE MERCADORIAS E SOBRE PRESTAÇÕES DE SERVIÇOS DE TRANSPORTE INTERESTADUAL E INTERMUNICIPAL E DE COMUNICAÇÃO – ICMS$'
pattern_norma_regulamento = r'^\(A QUE SE REFERE O DECRETO N° 2.212, DE 20 DE MARÇO DE 2014\)$'
pattern_nota_de_consolidacao = r'^Nota de Consolidação:'
