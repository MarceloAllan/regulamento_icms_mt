from docx import Document
import pandas as pd
import re

def validate_data(data, pattern):
    return bool(re.match(pattern, data, re.IGNORECASE))

def classify_paragraph(text):
    match text:
        case text_paragraph if validate_data(text_paragraph, pattern_capitulo):
            paragraph_classified['Class'] = 'capitulo'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_secao):
            paragraph_classified['Class'] = 'secao'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_subsecao):
            paragraph_classified['Class'] = 'subsecao'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_titulo_capitulo_secao_ou_subsecao):
            paragraph_classified['Class'] = 'titulo-capitulo-secao-ou-subsecao'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_titulo):
            paragraph_classified['Class'] = 'titulo'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_livro):
            paragraph_classified['Class'] = 'livro'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_artigo):
            paragraph_classified['Class'] = 'artigo'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_alinea):
            paragraph_classified['Class'] = 'alinea'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_inciso):
            paragraph_classified['Class'] = 'inciso'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_paragrafo):
            paragraph_classified['Class'] = 'paragrafo'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return


        case text_paragraph if validate_data(text_paragraph, pattern_item):
            paragraph_classified['Class'] = 'item'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_paragrafo_em_branco):
            paragraph_classified['Class'] = 'paragrafo-em-branco'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_paragrafo_vazio):
            paragraph_classified['Class'] = 'paragrafo-vazio'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_nota_explicativa):
            paragraph_classified['Class'] = 'nota-explicativa'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_nota_de_rodape):
            paragraph_classified['Class'] = 'nota-de-rodape'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_item_nota_de_rodape):
            paragraph_classified['Class'] = 'item-nota-de-rodape'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph:
            paragraph_classified['Class'] = 'nao-classificado'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return


pattern_artigo = r'^\s?Art\.\s?'
pattern_artigo_com_numero = r'Art\.\s\d+\°?(-[A-Z])?'
pattern_capitulo = r'^\s*(CAPÍTULO\s|DISPOSIÇÕES\sPRELIMINARES)'
pattern_secao = r'^\s*Seção\s*'
pattern_subsecao = r'^\s*Subseção\s*'
pattern_titulo = r'^\s*Título\s*'
pattern_livro = r'^\s*Livro\s*'
pattern_titulo_capitulo_secao_ou_subsecao = r'^D[AO]S?\s[A-Z]+'
pattern_alinea = r'^[a-z]{1,2}\-?\d?\)'
pattern_item = r'^\d+\)'
pattern_paragrafo = r'^\s*(§\s*\d+|Parágrafo\súnico)'
pattern_inciso = r'^(?:[IVXLCDM]+[\-\s*])'
pattern_nota_explicativa = r'^\s*Nota\sexplicativa'
pattern_nota_de_rodape = r'^\s*Notas?:'
pattern_item_nota_de_rodape = r'^\d+-?[A-Z]?\.'
pattern_paragrafo_em_branco = r'^\s*$'
pattern_paragrafo_vazio = r'^.$'

paragraphs_RICMS = list()
paragraph_classified = dict()

# abrir arquivo do RICMS
doc = Document('data/RICMS-Corrido.docx')

# classificar os parágrafos
for paragraph in doc.paragraphs[:10500]:
    paragraph_classified = dict()
    classify_paragraph(paragraph.text.strip())

# criar DataFrame e salvar em Excel
df_paragraphs_RICMS = pd.DataFrame(paragraphs_RICMS)
df_paragraphs_RICMS.to_excel('data/paragrafos_classificados.xlsx')

print('Parágrafos classificados com sucesso!')

# criando um arquivo HTML a partir do DF
html_tags_for_class_paragraph = {
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
    'livro': 'h1'
}

html_content = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RICMS/MT</title>
</head>
<body>\n"""

# Colocando o texto dentro das TAGs adequadas
for index, row in df_paragraphs_RICMS.iterrows():
    if row['Class'] in html_tags_for_class_paragraph.keys():
        class_name = row['Class'].lower().replace(' ', '-')
        tag = html_tags_for_class_paragraph.get(row['Class'])

        html_content += f"<{tag} class='{class_name}' id='{index}'>{row['Content']}</{tag}>\n"

html_content += "</body>\n</html>"

# adicionado TAG STRONG nos artigos
html_content = re.sub(pattern_artigo_com_numero, r'<strong>\g<0></strong>', html_content)

# Salvando em um arquivo HTML
with open("data/saida.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Arquivo HTML gerado com sucesso!")