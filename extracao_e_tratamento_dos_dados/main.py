from docx import Document # type: ignore
import pandas as pd
import re

def validate_data(data, pattern):
    return bool(re.match(pattern, data, re.IGNORECASE))

def classify_paragraph(text, pos_no_doc):
    match text:
        case text_paragraph if validate_data(text_paragraph, pattern_capitulo):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'capitulo'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_secao):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'secao'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_subsecao):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'subsecao'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_titulo_capitulo_secao_ou_subsecao):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'titulo-capitulo-secao-ou-subsecao'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_titulo):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'titulo'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_livro):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'livro'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_anexo):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'anexo'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_titulo_tabela):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'titulo-tabela'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_artigo):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'artigo'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_alinea):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'alinea'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_inciso):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'inciso'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_paragrafo):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'paragrafo'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return


        case text_paragraph if validate_data(text_paragraph, pattern_item):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'item'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_paragrafo_em_branco):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'paragrafo-em-branco'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_paragrafo_vazio):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'paragrafo-vazio'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_nota_explicativa):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'nota-explicativa'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_nota_de_rodape):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'nota-de-rodape'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_cfop):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'cfop'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_item_nota_de_rodape):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'item-nota-de-rodape'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_tabela):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'tabela'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph if validate_data(text_paragraph, pattern_texto_revogado):
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'texto-revogado'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

        case text_paragraph:
            paragraph_classified['Index'] = pos_no_doc
            paragraph_classified['Class'] = 'nao-classificado'
            paragraph_classified['Content'] = text_paragraph
            paragraphs_RICMS.append(paragraph_classified)
            return

def table_to_html(table):
    # Converter a tabela em um DataFrame
    data = [[cell.text.strip() for cell in row.cells] for row in table.rows]
    df = pd.DataFrame(data)

    # Converter DataFrame para HTML
    html_table = df.to_html(index=False, header=False, escape=False)

    return html_table

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
pattern_nota_explicativa = r'^\s*Nota\sexplicativa'
pattern_nota_de_rodape = r'^\s*Notas?:'
pattern_item_nota_de_rodape = r'^\d+-?[A-Z]?\.'
pattern_paragrafo_em_branco = r'^\s*$'
pattern_tabela = r'^<table'
pattern_texto_revogado = r'^\(revogad'
pattern_cfop = r'^\d\.\d{3}\s*\-\s*'
pattern_paragrafo_vazio = r'^.$'

paragraphs_RICMS = list()
paragraph_classified = dict()

# abrir arquivo do RICMS
doc = Document('data/RICMS-Corrido.docx')

# classificar os parágrafos
for index, elemento in enumerate(doc.element.body):
    if elemento.tag.endswith('p'):  # verifica se o elemento é um parágrafo
        paragraph_classified = dict()  # cria um novo dicionário para guardar a classificação do parágrafo

        content_paragraph = elemento.text.strip()

        # substitui os símbolos <, > e & pelo html correspondente para evitar erros na sintaxe
        content_paragraph = re.sub('<', '&lt;', content_paragraph)
        content_paragraph = re.sub('>', '&gt;', content_paragraph)
        content_paragraph = re.sub('&', '&amp;', content_paragraph)

        classify_paragraph(content_paragraph, index)  # classifica o parágrafo a partir das expressões regulares

    elif elemento.tag.endswith('tbl'):
        paragraph_classified = dict()   # cria um novo dicionário para guardar a classificação do parágrafo

        table_index = sum(1 for e in doc.element.body[:index] if e.tag.endswith('tbl'))  # identifica o índice dessa tabela na lista doc.tables
        table_obj = doc.tables[table_index]  # retorna a tabela correta

        classify_paragraph(table_to_html(table_obj), index)

# criar DataFrame e salvar em Excel
df_paragraphs_RICMS = pd.DataFrame(paragraphs_RICMS)
df_paragraphs_RICMS.to_excel('data/paragrafos_classificados.xlsx')

print('Parágrafos classificados com sucesso!')

# criando um arquivo HTML a partir do DF

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
    'nao-classificado': 'p'
}

# início do código HTML
html_content = """<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>RICMS/MT</title>
    <link rel="stylesheet" href="style.css">
    <link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon">
</head>
<body>
    <header class="cabecalho">
        <h1>Secretaria de Estado de Fazenda de Mato Grosso</h1>
        <nav>
            <ul class="menu">
                <li><a href="https://www5.sefaz.mt.gov.br/inicio" target="_blank">Site Oficial</a></li>
                <li><a href="https://www.sefaz.mt.gov.br/spl/portalpaginalegislacao" target="_blank">Portal da Legislação</a></li>
                <li><a href="https://portal.mt.gov.br/" target="_blank">Portal Gov MT</a></li>
            </ul>
        </nav>
        <div class="barra-degrade"></div>
    </header>
    <main>
"""

# Colocando o texto dentro das TAGs adequadas
for index, row in df_paragraphs_RICMS.iterrows():
    if row['Class'] in html_tags_for_class_paragraph.keys():  # os parágrafos que não estiverem classificações
        # listadas em html_tags_for_class_paragraph não serão adicionados ao HTML
        class_name = row['Class'].lower().replace(' ', '-')  # define o nome da classe que será atribuída ao elemento
        # com base no conteúdo da coluna 'Class'
        tag = html_tags_for_class_paragraph.get(row['Class'])  # procura no dicionário html_tags_for_class_paragraph o
        # valor correspondente a 'Key' que é a classe do parágrafo

        html_content += f"<{tag} class='{class_name}' id='{index}'>{row['Content']}</{tag}>\n"

html_content += """
    </main>
<footer>
    <p>Site em desenvolvimento por Marcelo Allan - FTE da SEFAZ/MT</p>
</footer>
</body>
</html>"""

print('Html criado com sucesso!')

# adicionado TAG STRONG nos artigos
html_content = re.sub(pattern_artigo_com_numero, r'<strong>\g<0></strong>', html_content) # '\g<0>' significa - a
# parte da string que correspondeu à expressão regular informada

print('TAGs adicionadas com sucesso!')

# Salvando em um arquivo HTML
with open("data/index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("Arquivo HTML gerado com sucesso!")