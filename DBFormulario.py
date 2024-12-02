import streamlit as st
from PIL import Image
import base64
from PIL import Image, ImageDraw,ImageEnhance
from datetime import datetime, timedelta
import urllib.parse
from fpdf import FPDF
import os
from io import BytesIO
import locale

# Configuração inicial da página
st.set_page_config(page_title="DB Terapeuta", layout="wide", page_icon="🌿")

##### Oculta o botão Deploy do Streamilit
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True
)

###### CSS para definir a imagem de fundo [Inicio]

# Função para ler a imagem e convertê-la para base64
def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Definir o estado de autenticação na sessão
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# Verificar se o usuário está autenticado
if st.session_state.authenticated:
        # Exibir o conteúdo do formulário de anamnese emocional
    # Caminho da imagem
    image_path = "terapia.png"
    # Codificação da imagem em base64
    base64_image = get_base64_image(image_path)

    # CSS para definir a imagem de fundo com transparência
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9)), url('data:image/png;base64,{base64_image}') no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    ###### CSS para definir a imagem de fundo [Fim]

    # Faixa no alto
    st.markdown("""
    <h2 style="background-color: #C1CDCD; color: white; padding: 10px; text-align: center;margin-top: -80px;"></h2>
    """, unsafe_allow_html=True)

###########################################################################################################
############### DESSE PONTO EXIBIR FORMULARIO ANAMINESE ###################################################
###########################################################################################################
    ###### CSS para definir a imagem de fundo [Inicio]

    # Função para ler a imagem e convertê-la para base64
    def get_base64_image(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return encoded_string

    ##### Remover o cabeçalho da pagina

    REMOVE_PADDING_FROM_SIDES="""
    <style>
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
        }   
    </style>
    """
    st.markdown(REMOVE_PADDING_FROM_SIDES, unsafe_allow_html=True)

    # Caminho da imagem
    image_path = "terapia.png"
    # Codificação da imagem em base64
    base64_image = get_base64_image(image_path)

    # CSS para definir a imagem de fundo com transparência
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9)), url('data:image/png;base64,{base64_image}') no-repeat center center fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    ###### CSS para definir a imagem de fundo [Fim]

    col1, col2, col3 =st.columns([2,5,1])
    with col1:
        # Obtém o caminho absoluto do diretório atual
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Concatena com o nome do arquivo
        image_path = os.path.join(current_directory, "logo_DB.png")

        # Carrega a imagem
        st.image(image_path)

    with col2:
    # Título da aplicação
        st.title("Formulário de Anamnese Emocional")

    st.markdown("<hr style='border: 1px solid #000;margin-top: -20px;'>", unsafe_allow_html=True)  # Linha preta fina

    ############### Destacar todos os st.text_area

    # CSS para destacar todas as text areas
    st.markdown(
        """
        <style>
        /* Define o estilo para todas as st.text_area */
        .stTextArea textarea {
            background-color: #f0f8ff; /* Cor de fundo azul claro */
            border: 2px solid #000000; /* Borda azul */
            border-radius: 10px; /* Bordas arredondadas */
            padding: 10px; /* Espaçamento interno */
            font-weight: bold; /* Texto em negrito */
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra suave */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        /* Define o estilo para todos os st.text_input */
        .stTextInput > div > div > input {
            background-color: #f0f8ff; /* Cor de fundo amarela clara */
            border: 2px solid #000000; /* Borda laranja */
            border-radius: 10px; /* Bordas arredondadas */
            padding: 5px; /* Espaçamento interno */
            font-weight: bold; /* Texto em negrito */
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Sombra suave */
        }
        </style>
        """,
        unsafe_allow_html=True
        
    )
    # CSS personalizado
    st.markdown("""
        <style>
        /* Estiliza todos os selectbox */
        div[data-baseweb="select"] {
            background-color: #f0f8ff; /* Cor de fundo */
            border-radius: 10px; /* Arredondamento das bordas */
            padding: 2px; /* Espaçamento interno */
            border: 2px solid #000000; /* Cor da borda */
        }

        /* Estiliza o título de cada selectbox */
        label.css-1cpxqw2.e1fqkh3o3 {
            font-weight: bold; /* Negrito */
            color: #4CAF50; /* Cor do texto */
        }

        /* Estiliza o texto e a seta dentro do selectbox */
        div[data-baseweb="select"] .css-1wa3eu0-placeholder,
        div[data-baseweb="select"] .css-qbdosj-Option {
            color: #000000; /* Cor do texto */
            font-weight: bold; /* Texto em negrito */
        }
        </style>
    """, unsafe_allow_html=True)

    # CSS personalizado para o st.number_input com estilo de foco
    st.markdown("""
        <style>
        /* Estiliza todos os campos number_input */
        input[type="number"] {
            background-color: #f0f8ff; /* Cor de fundo */
            border: 2px solid #000000; /* Cor da borda padrão */
            border-radius: 5px; /* Arredondamento das bordas */
            padding: 5px; /* Espaçamento interno */
            font-weight: bold; /* Texto em negrito */
            color: #000000; /* Cor do texto */
        }

        /* Estilo ao focar no campo number_input */
        input[type="number"]:focus {
            border: 2px solid #000000; /* Cor da borda ao focar (verde neste exemplo) */
            outline: none; /* Remove o outline padrão (para navegadores que suportam) */
            box-shadow: 0 0 5px rgba(150, 175, 90, 0.5); /* Sombra ao focar */
        }

        /* Estiliza o label do number_input */
        label.css-10trblm.e1fqkh3o3 {
            font-weight: bold; /* Título em negrito */
            color: #000000; /* Cor do título */
        }
        </style>
    """, unsafe_allow_html=True)

    # CSS personalizado para o st.date_input
    st.markdown("""
        <style>
        /* Estiliza todos os campos de data */
        .stDateInput input {
            background-color: #f0f8ff; /* Cor de fundo */
            border: 2px solid #000000; /* Cor da borda */
            border-radius: 5px; /* Arredondamento das bordas */
            padding: 8px; /* Espaçamento interno */
            color: #333333; /* Cor do texto */
            font-weight: bold; /* Texto em negrito */
            width: 100%; /* Largura total */
        }

        /* Estilo ao focar no campo date_input */
        .stDateInput input:focus {
            border: 2px solid #FF9800; /* Cor da borda ao focar (laranja neste exemplo) */
            outline: none; /* Remove o outline padrão */
            box-shadow: 0 0 5px rgba(255, 152, 0, 0.5); /* Sombra ao focar */
        }

        /* Estiliza o título do date_input */
        .stDateInput label {
            font-weight: bold; /* Título em negrito */
            color: #000000; /* Cor do título */
        }
        </style>
    """, unsafe_allow_html=True)
    ###########################################################################

    # Dados Pessoais
    #st.header("Dados Pessoais")

    # Usar HTML para criar um cabeçalho com fundo colorido
    st.markdown("""
    <h2 style="background-color: #C1CDCD; color: white; padding: 10px; text-align: center;margin-top: -80px;">Dados Pessoais</h2>
    """, unsafe_allow_html=True)

    nome = st.text_input("**Nome completo**", key="nome")
    endereco_completo = st.text_input("**Informe endereço completo: Ex: R.Joao Nuno de Souza, 345 - Santo inacio - Curitiba - PR, 82010-420**", key="endereco_completo")

    col1, col2, col3, col4 = st.columns([1,1,1,1])

    with col1:

        #endereco = st.text_input("**Endereço #**", key="endereco")
        #complemento = st.text_input("**Complemento#**", key="complemento")
        cpf = st.text_input("**CPF**", key="cpf")
        email = st.text_input("**E-mail**", key="email")
        #cargo = st.text_input("**Cargo**", key="cargo")
        #religiao = st.text_input("**Religião**", key="religiao")

        

    with col2:
        
        #bairro = st.text_input("**Bairro#**", key="bairro")
        #cep = st.text_input("**Cep#**", key="cep")
        #profissao = st.text_input("**Profissão**", key="profissao")
        rg = st.text_input("**RG**", key="rg")
        atividade = st.text_input("**Atividade**", key="atividade")
        #escolaridade = st.text_input("**Escolaridade**", key="escolaridade")
        #empresa = st.text_input("**Empresa**", key="empresa")
        

    with col3:
        
        #cidade = st.text_input("**Cidade#**", key="cidade")
        estado_civil = st.selectbox("**Estado civil**", ["Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)"], key="estado_civil")
        telefone_residencial = st.text_input("**Telefone Residencial**", key="telefone_residencial")


    with col4:
        
        #uf = st.text_input("**UF#**", key="uf")
            # Definir o intervalo de datas
        hoje = datetime.now().date()
        min_date = datetime(1900, 1, 1).date()  # Data mínima
        max_date = hoje + timedelta(days=365*1)  # Data máxima (1 anos à frente)

        # Selecione a data de nascimento
        data_nascimento = st.date_input("**Data de nascimento**", datetime(1980, 1, 1).date(), 
            min_value=min_date,  max_value=max_date,format="DD/MM/YYYY", key="data_nascimento" )
        # Formatar a data para 'dd/mm/yyyy'
        data_nascimento_formatada = data_nascimento.strftime("%d/%m/%Y")

        # Exibir a data formatada
        #st.markdown(f"Data de nascimento selecionada: **{data_nascimento_formatada}**")   
        celular = st.text_input("**Celular**", key="celular")   

    queixa_principal = st.text_area("**Queixa Principal - O que te trouxe até aqui?**", key="queixa_principal")
                            
    # Fase 01 - Vida Pessoal
    #st.header("Fase 01 - Vida Pessoal")

    # Incluir faixa com título
    st.markdown("""<h2 style="background-color: #C1CDCD; color: white; padding: 10px; text-align: center;">Fase 01 - Vida Pessoal</h2>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        estado_civil_fase1 = st.selectbox("**É casada(o), solteira(o) ou divorciada(o)?**", ["Casada(o)", "Solteira(o)", "Divorciada(o)"], key="estado_civil_fase1")
        divorcio_motivo = st.text_area("**Se é divorciada(o), por qual motivo e como se sente**?", key="divorcio_motivo")
        numero_filhos = st.number_input("**Número de filhos**", min_value=0, key="numero_filhos")
        relacionamento_filhos = st.text_area("**Como é o seu relacionamento com seus filhos?**", key="relacionamento_filhos")
        relacionamento_parceiro = st.text_area("**Como você se sente em seu relacionamento com sua parceira(o)?**", key="relacionamento_parceiro")
        relacionamento_familiar = st.text_area("**Como você se sente em sua casa, dentro do contexto familiar?**", key="relacionamento_familiar")


    with col2:
        sentimento_trabalho = st.text_area("**Como você se sente no seu trabalho?**", key="sentimento_trabalho")
        
        pertencimento_familiar = st.radio("**Você se sente pertencendo ao Contexto Familiar?**", ["Sim", "Não"], key="pertencimento_familiar",horizontal=True)
        pertencimento_familiar_justificativa = ""# Inicializa a variável com uma string vazia
        if pertencimento_familiar == "Não":
            pertencimento_familiar_justificativa = st.text_area("**Por quê?**", key="pertencimento_familiar_justificativa")

        pertencimento_social = st.radio("**Você se sente pertencendo ao Contexto Social?**", ["Sim", "Não"], key="pertencimento_social",horizontal=True)
        pertencimento_social_justificativa = ""# Inicializa a variável com uma string vazia
        if pertencimento_social == "Não":
            pertencimento_social_justificativa = st.text_area("**Por quê?**", key="pertencimento_social_justificativa")
        
        pertencimento_religioso = st.radio("**Você se sente pertencendo ao Contexto Religioso?**", ["Sim", "Não"], key="pertencimento_religioso",horizontal=True)
        pertencimento_religioso_justificativa = "" # Inicializa a variável com uma string vazia
        #pertencimento_religioso_justificativa = st.text_area("Por quê?" if pertencimento_religioso == "Não" else "", key="pertencimento_religioso_justificativa")
        if pertencimento_religioso == "Não":
            pertencimento_religioso_justificativa = st.text_area("**Por quê?**", key="pertencimento_religioso_justificativa")

    # Frustrações
    #st .header("Frustrações")
    # Incluir faixa com título
    st.markdown("""<h2 style="background-color: #C1CDCD; color: white; padding: 10px; text-align: center;">Frustrações</h2>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        frustracao_pais = st.radio("**Você sente frustração em relação a Pais?**", ["Não", "Sim"], key="frustracao_pais",horizontal=True)
        frustracao_pais_justificativa = ""# Inicializa a variável com uma string vazia
        if frustracao_pais == "Sim":
            frustracao_pais_justificativa = st.text_area("**Por quê?**", key="frustracao_pais_justificativa")

        frustracao_irmaos = st.radio("**Você sente frustração em relação a Irmãos?**", ["Não", "Sim"], key="frustracao_irmaos",horizontal=True)
        frustracao_irmaos_justificativa = ""# Inicializa a variável com uma string vazia
        if frustracao_irmaos == "Sim":
            frustracao_irmaos_justificativa = st.text_area("**Por quê?**", key="frustracao_irmaos_justificativa")

        frustracao_filhos = st.radio("**Você sente frustração em relação a Filhos?**", ["Não", "Sim"], key="frustracao_filhos",horizontal=True)
        frustracao_filhos_justificativa = ""# Inicializa a variável com uma string vazia
        if frustracao_filhos == "Sim":
            frustracao_filhos_justificativa = st.text_area("**Por quê?**", key="frustracao_filhos_justificativa")

        frustracao_profissao = st.radio("**Você sente frustração em relação a Profissão?**", ["Não", "Sim"], key="frustracao_profissao",horizontal=True)
        frustracao_profissao_justificativa = ""# Inicializa a variável com uma string vazia
        if frustracao_profissao == "Sim":
            frustracao_profissao_justificativa = st.text_area("**Por quê?**", key="frustracao_profissao_justificativa")

        frustracao_colegio = st.radio("**Você sente frustração em relação a Colégio?**", ["Não", "Sim"], key="frustracao_colegio",horizontal=True)
        frustracao_colegio_justificativa = ""# Inicializa a variável com uma string vazia
        if frustracao_colegio == "Sim":
            frustracao_colegio_justificativa = st.text_area("**Por quê?**", key="frustracao_colegio_justificativa")


    with col2:

        frustracao_conjuge = st.radio("**Você sente frustração em relação a Cônjuge?**", ["Não", "Sim"], key="frustracao_conjuge",horizontal=True)
        frustracao_conjuge_justificativa = ""# Inicializa a variável com uma string vazia
        if frustracao_conjuge == "Sim":
            frustracao_conjuge_justificativa = st.text_area("**Por quê?**", key="frustracao_conjuge_justificativa")

        frustracao_identidade_sexual = st.radio("**Você sente frustração em relação a Identidade Sexual?**", ["Não", "Sim"], key="frustracao_identidade_sexual",horizontal=True)
        frustracao_identidade_sexual_justificativa = ""# Inicializa a variável com uma string vazia
        if frustracao_identidade_sexual == "Sim":
            frustracao_identidade_sexual_justificativa = st.text_area("**Por quê?**", key="frustracao_identidade_sexual_justificativa")
        
        frustracao_vida_sexual = st.radio("**Você sente frustração em relação a Vida Sexual?**", ["Não", "Sim"], key="frustracao_vida_sexual",horizontal=True)
        frustracao_vida_sexual_sexual_justificativa = ""# Inicializa a variável com uma string vazia
        if frustracao_vida_sexual == "Sim":
            frustracao_vida_sexual_sexual_justificativa = st.text_area("**Por quê?**", key="frustracao_vida_sexual_sexual_justificativa")
        
        iniciou_sexualidade_idade = st.number_input("**Iniciou sua sexualidade com que idade?**", min_value=0, key="iniciou_sexualidade_idade")
        primeira_vez = st.selectbox("**Como foi sua primeira vez?**", ["Traumática", "Normal", "Boa", "Satisfatória"], key="primeira_vez")

    # Problemas de Saúde
    #st.header("Problemas de Saúde")
    # Incluir faixa com título
    st.markdown("""<h2 style="background-color: #C1CDCD; color: white; padding: 10px; text-align: center;">Problemas de Saúde</h2>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        
        problemas_sexo = st.radio("**Tem tido algum problema em relação ao sexo?**", ["Sim", "Não"], key="problemas_sexo",horizontal=True)
        realizacao_sexual = st.radio("**Atualmente sempre se realiza nas relações sexuais?**", ["Sim", "Não"], key="realizacao_sexual",horizontal=True)
        importancia_sexo = st.selectbox("**O sexo para você é algo:**", ["Importante", "Sem importância", "Muito importante"], key="importancia_sexo")
        
        trauma = st.radio("**Algum trauma?**", ["Não", "Sim"], key="trauma",horizontal=True)
        trauma_justificativa = ""# Inicializa a variável com uma string vazia
        if trauma == "Sim":
            trauma_justificativa = st.text_area("**Por quê?**", key="trauma_justificativa")

    with col2:
        
        fobia = st.radio("**Alguma fobia?**", ["Não", "Sim"], key="fobia",horizontal=True)
        fobia_justificativa = ""# Inicializa a variável com uma string vazia
        if fobia == "Sim":
            fobia_justificativa = st.text_area("**Por quê?**", key="fobia_justificativa")
            
        medo = st.radio("**Tem medo de alguma coisa?**", ["Não", "Sim"], key="medo",horizontal=True)
        #medo_justificativa = st.text_area("De quê?" if medo == "Sim" else "", key="medo_justificativa")
        medo_justificativa = ""
        if medo == "Sim":
            medo_justificativa = st.text_area("**Por quê?**", key="medo_justificativa")
        
        usa_drogas = st.radio("**Usa drogas?**", ["Não", "Sim"], key="usa_drogas",horizontal=True)
        usa_drogas_justificativa = ""# Inicializa a variável com uma string vazia
        #usa_drogas_justificativa = st.text_area("Quais?" if usa_drogas == "Sim" else "", key="usa_drogas_justificativa")
        if usa_drogas == "Sim":
            usa_drogas_justificativa = st.text_area("**Por quê?**", key="usa_drogas_justificativa")

    # Outros Problemas
    #st.header("Outros Problemas")
    # Incluir faixa com título
    st.markdown("""<h2 style="background-color: #C1CDCD; color: white; padding: 10px; text-align: center;">Outros Problemas</h2>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        dor_cabeca = st.radio("**Dores de cabeça?**", ["Não", "Sim"], key="dor_cabeca",horizontal=True)
        dor_cabeca_frequencia = st.selectbox("**Com que frequência?**", ["Diária", "Semanal", "Mensal", "Raramente"], key="dor_cabeca_frequencia")
        
        insonia = st.radio("**Insônia?**", ["Não", "Sim"], key="insonia",horizontal=True)
        insonia_frequencia = st.selectbox("**Com que frequência?**", ["Diária", "Semanal", "Mensal", "Raramente"], key="insonia_frequencia")

        ideias_suicidas = st.radio("**Tem ideias suicidas?**", ["Não", "Sim"], key="ideias_suicidas",horizontal=True)
        ideias_suicidas_justificativa = ""# Inicializa a variável com uma string vazia
        if ideias_suicidas == "Sim":
            ideias_suicidas_justificativa = st.text_area("**Quais?**" if ideias_suicidas == "Sim" else "", key="ideias_suicidas_justificativa")

        trauma_passado = st.radio("**Algum trauma?**", ["Não", "Sim"], key="trauma_passado",horizontal=True)
        trauma_passado_justificativa = ""# Inicializa a variável com uma string vazia
        if trauma_passado == "Sim":
            trauma_passado_justificativa = st.text_area("**Quais?**" if trauma_passado == "Sim" else "", key="trauma_passado_justificativa")

        usa_medicacao = st.radio("**Atualmente está tomando alguma medicação?**", ["Não", "Sim"], key="usa_medicacao",horizontal=True)
        usa_medicacao_justificativa = ""# Inicializa a variável com uma string vazia
        if usa_medicacao == "Sim":
            usa_medicacao_justificativa = st.text_area("**Quais?**" if usa_medicacao == "Sim" else "", key="usa_medicacao_justificativa")

        quantidade_amigos = st.number_input("**Qual a quantidade de amigos que você tem?**", min_value=0, key="quantidade_amigos")
        passatempo_preferido = st.text_input("**Qual seu passatempo preferido?**", key="passatempo_preferido")

        mudvida_definicaoaria = st.text_area("**Defina o que é a vida em apenas uma frase**", key="vida_definicao")


    with col2:
        usa_bebidas_alcoolicas = st.radio("**Usa bebidas alcoólicas?**", ["Não", "Sim"], key="usa_bebidas_alcoolicas",horizontal=True)
        usa_bebidas_alcoolicas_frequencia = st.selectbox("**Com que frequência?**", ["Diária", "Semanal", "Mensal", "Raramente"], key="usa_bebidas_alcoolicas_frequencia")
        
        fumante = st.radio("**É fumante?**", ["Não", "Sim"], key="fumante",horizontal=True)
        grvida = st.radio("**Está grávida?**", ["Não", "Sim"], key="grvida",horizontal=True)
        grvida_semanas = st.number_input("**Quantas semanas?**", min_value=0, key="grvida_semanas")

        nivel_stress = st.selectbox("**Qual o seu nível de stress?**", ["Alto", "Médio", "Baixo"], key="nivel_stress")

        consultou_psiquiatra = st.radio("**Já consultou algum tipo de psiquiatra ou psicólogo?**", ["Não", "Sim"], key="consultou_psiquiatra",horizontal=True)
        consultou_psiquiatra_diagnostico = ""# Inicializa a variável com uma string vazia
        if consultou_psiquiatra == "Sim":
            consultou_psiquiatra_diagnostico = st.radio("**Se sim, foi diagnosticada (o)?**", [" ","Não", "Sim"], key="consultou_psiquiatra_diagnostico")

        crenca_pessoas = st.text_area("**Qual a principal crença que as pessoas possuem em relação a você que mais se repete?**", key="crenca_pessoas")

        feliz = st.radio("**Você se considera feliz?**", ["Não", "Sim"], key="feliz")
        feliz_justificativa = ""# Inicializa a variável com uma string vazia
        if feliz == "Sim":
            feliz_justificativa = st.text_area("**Por quê?**" if feliz == "Sim" else "", key="feliz_justificativa")
        
        mudaria = st.text_area("**Se você pudesse mudar alguma coisa em você, no seu modo de ser, ou agir, ou no seu comportamento atual, o que mudaria?**", key="mudaria")

    # Fase 02 - Mental:
    #st.header("Fase 02 - Mental:")
    # Incluir faixa com título
    st.markdown("""<h2 style="background-color: #C1CDCD; color: white; padding: 10px; text-align: center;">Fase 02 - Mental:</h2>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        pensamentos_positivos = st.radio("**Quais são os tipos de pensamentos que você costuma alimentar em relação a si mesma (o), de uma maneira geral?**", ["Positivo", "Negativo"], key="pensamentos_positivos",horizontal=True)
        pensamentos_positivos_justificativa = st.text_area("**Quais exatamente?**", key="pensamentos_positivos_justificativa")

        pensamentos_competencia = st.radio("**Em relação a sua competência profissional?**", ["Positivo", "Negativo"], key="pensamentos_competencia",horizontal=True)
        pensamentos_competencia_justificativa = st.text_area("**Quais exatamente?**", key="pensamentos_competencia_justificativa")  

        pensamentos_passado = st.radio("**Em relação ao seu passado?**", ["Positivo", "Negativo"], key="pensamentos_passado",horizontal=True)
        pensamentos_passado_justificativa = st.text_area("**Quais exatamente?**", key="pensamentos_passado_justificativa") 

        visao_sobre_si = st.text_area("**Qual sua visão sobre você?**", key="visao_sobre_si") 

    with col2:  
        pensamentos_aparencia = st.radio("**Em relação a sua aparência física?**", ["Positivo", "Negativo"], key="pensamentos_aparencia",horizontal=True)
        pensamentos_aparencia_justificativa = st.text_area("**Quais exatamente?**", key="pensamentos_aparencia_justificativa")  

        pensamentos_vida_emocional = st.radio("**Em relação a sua vida emocional?**", ["Positivo", "Negativo"], key="pensamentos_vida_emocional",horizontal=True)
        pensamentos_vida_emocional_justificativa = st.text_area("**Quais exatamente?**", key="pensamentos_vida_emocional_justificativa") 

        pensamentos_vida_sexual = st.radio("**Em relação a sua vida emocional?**", ["Positivo", "Negativo"], key="pensamentos_vida_sexual",horizontal=True)
        pensamentos_vida_sexual_justificativa = st.text_area("**Quais exatamente?**", key="pensamentos_vida_sexual_justificativa") 

        pensamentos_futuro = st.radio("**Em relação ao seu futuro?**", ["Positivo", "Negativo"], key="pensamentos_futuro",horizontal=True)
        pensamentos_futuro_sexual_justificativa = st.text_area("**Quais exatamente?**", key="pensamentos_futuro_sexual_justificativa") 

    
    # Fase 03 - Infância:
    #st.header("Fase 03 - Infância:")
    # Incluir faixa com título
    st.markdown("""<h2 style="background-color: #C1CDCD; color: white; padding: 10px; text-align: center;">Fase 03 - Infância:</h2>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
            foi_criado_pais = st.radio("**Você foi criado pelos pais?**", ["Sim", "Não"], key="foi_criado_pais",horizontal=True)
            foi_criado_pais_justificativa = st.text_input("**Outro**", key="foi_criado_pais_justificativa")
            relacionamento_pais = st.text_area("**Como é sua relação com seus pais?**", key="relacionamento_pais")

            pais_agressivos = st.radio("**Seus pais foram agressivos com você?**", ["Sim", "Não"], key="pais_agressivos",horizontal=True)
            pais_agressivos_justificativa = st.text_area("**Descreva**", key="pais_agressivos_justificativa") 
            
            relacionamento_pais_descreva = st.selectbox("**Como você descreveria o relacionamento entre seus pais?**", ["Excelente", "Muito bom", "Bom", "Regular", "Péssimo"], key="relacionamento_pais_descreva")
            relacionamento_pais_descreva_justificativa = st.text_area("**Por quê?**", key="relacionamento_pais_descreva_justificativa")
            
            relacionamento_pais_crenca = st.text_area("**Quanto ao relacionamento de seus pais responda: Qual a crença que você adquiriu em relação a relacionamentos?**", key="relacionamento_pais_crenca")

            infancia_tristeza = st.text_area("**O que te faz sentir tristeza ao relembrar do passado?**", key="infancia_tristeza")

            infancia_medo = st.text_area("**Quando criança tinha medo de que?**", key="infancia_medo")
            infancia_rebeldia = st.radio("**Teve fase de rebeldia na adolescência?**", ["Sim", "Não"], key="infancia_rebeldia",horizontal=True)
            infancia_pais_dificuldade = st.selectbox("**Como foi sua adolescência?**", ["Pai", "Mãe", "Ambos"], key="infancia_pais_dificuldade")
            infancia_filosofia_sucesso = st.text_area("**Qual a Filosofia de sua família em relação ao sucesso profissional? ao Dinheiro ? ao Amor? ao Sexo?**",key="infancia_filosofia_sucesso")

            irmaos = st.radio("**Possui irmãos?**", ["Não", "Sim"], key="irmaos",horizontal=True)
            irmaos_justificativa = ""
            if irmaos == "Sim":
                irmaos_justificativa = st.number_input("**Quantos?**", min_value=0, key="irmaos_justificativa")

            colégio_dificuldades = st.text_area("**Havia dificuldades de relacionamentos com os colegas do colégio? Se sim, cite-os.**",key="colégio_dificuldades")

            infancia_medos = st.text_area("**Quais eram seus maiores medos na infância?**",key="infancia_medos")

    with col2:
            pai_bravo = st.radio("**Seus pais foram agressivos com você?**", ["O Pai", "A Mãe"], key="pai_bravo",horizontal=True)
            pai_bravo_justificativa = st.text_area("**Descreva**", key="pai_bravo_justificativa") 

            pais_usavam_drogas = st.radio("**Usavam bebidas ou drogas?**", ["Não", "Sim"], key="pais_usavam_drogas",horizontal=True)
            pais_usavam_drogas_justificativa = st.text_area("**Descreva**", key="pais_usavam_drogas_justificativa") 
            
            relacionamento_pais_repete = st.text_area("**Quais os aspectos deste relacionamento que se assemelham, ou se repetem em sua vida hoje?**", key="relacionamento_pais_repete") 
            relacionamento_pais_nao_repete = st.text_area("**Quais as características deste relacionamento, que você se mantém determinada (o) a não repetir?**", key="relacionamento_pais_nao_repete") 
            
            infancia_obrigada = st.radio("**Na infância, era obrigada (o) a fazer alguma coisa que lhe desagradava?**", ["Sim", "Não"], key="infancia_obrigada",horizontal=True)
            infancia_obrigada_justificativa = st.text_input("**Descreva**", key="infancia_obrigada_justificativa")

            infancia_magou = st.radio("**Lembra-se, de alguma coisa que o magoou muito na Infância?**", ["Sim", "Não"], key="infancia_magou",horizontal=True)
            infancia_magou_justificativa = st.text_input("**Descreva**", key="infancia_magou_justificativa")

            infancia_perdas = st.radio("**Teve perdas familiares ou de amigos na Infância?**", ["Sim", "Não"], key="infancia_perdas",horizontal=True)
            infancia_perdas_justificativa = st.text_input("**Descreva**", key="infancia_perdas_justificativa")
            infancia_dormia = st.selectbox("**Dormia com a luz acesa ou apagada?**", ["Acesa", "Apagada"], key="infancia_dormia")
            infancia_adolescencia = st.selectbox("**Como foi sua adolescência?**", ["Ruim", "Boa", "Ótima"], key="infancia_adolescencia")
            infancia_boa_menina = st.text_area("**O que era para você, ser uma boa (bom) menina (o)? Descreva.**",key="infancia_boa_menina")

            infancia_agir = st.text_area("**Como você deveria agir, ou ser, para ser amada(o)?**",key="infancia_agir")
            irmaos_relacionamento = st.text_area("**Como é sua relação com eles?**",key="irmaos_relacionamento")

            infancia_fato_marcante = st.text_area("**Relate algum fato marcante em sua infância**",key="infancia_fato_marcante")
            
    # Fase 04 - Emocional::
    #st.header("Fase 04 - Emocional:")
    # Incluir faixa com título
    st.markdown("""<h2 style="background-color: #C1CDCD; color: white; padding: 10px; text-align: center;">Fase 04 - Emocional:</h2>""", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    
    with col1:
            medos_atualmente = st.text_area("**Quais são seus maiores medos hoje?**",key="medos_atualmente")
            papel_vitima = st.radio("**Se você avaliasse sua atuação na vida, qual papel que mais caberia a você hoje?**", ["Vítima ", "Responsável"], key="papel_vitima",horizontal=True)
            ganho_secundario = st.text_input("**Qual o ganho secundário?**", key="ganho_secundario")
            papel_responsavel_situacoes = st.text_area("**Em quais situações você desempenha o papel de responsável?**",key="papel_responsavel_situacoes")
            dominante_submisso = st.radio("**Nos relacionamentos e na vida, você prefere ser:**", ["Dominante ", "Submisso"], key="dominante_submisso",horizontal=True)
            punido = st.text_input("**Quem deve ser punido por problemas que ocorrem com você? OU Quem é o culpado por seus problemas pessoais?**", key="punido")
            
            raiva = st.radio("**Sente raiva ou rancor de alguém?**", ["Não ", "Sim"], key="raiva",horizontal=True)
            raiva_justificativa =""
            if raiva == "Sim":
                raiva_justificativa = st.text_area("**De Quem?**", key="raiva_justificativa")
            
            inferior = st.radio("**Sente-se de alguma forma inferior aos outros?**", ["Não ", "Sim"], key="inferior",horizontal=True)
            inferior_justificativa = st.text_area("**Por quê?**",key="inferior_justificativa")

    with col2:
            pensamento_sobre_si = st.text_area("**O que você pensa a seu respeito?**",key="pensamento_sobre_si")
            primeiro_relacionamento = st.text_area("**Como foi o seu primeiro relacionamento amoroso?**",key="primeiro_relacionamento")
            papel_vitima_situacoes = st.text_area("**Em quais situações você desempenha o papel de vítima?**",key="papel_vitima_situacoes")
            vitorioso_derrotado = st.text_area("**Se considera vitoriosa(o) ou derrotada(o)?**",key="vitorioso_derrotado")
        
            pressionado = st.radio("**Sente-se de alguma forma pressionada (o) na atualidade?**", ["Não ", "Sim"], key="pressionado",horizontal=True)
            pressionado_justificativa = ""
            if pressionado == "Sim":
                pressionado_justificativa = st.text_area("**De que maneira?**", key="pressionado_justificativa")        
        
            controladora = st.radio("**Você se acha uma pessoa controladora?**", ["Não ", "Sim"], key="controladora",horizontal=True)
            capacidade = st.radio("**Duvida de sua própria capacidade?**", ["Não ", "Sim"], key="capacidade",horizontal=True)
            audaciosa = st.radio("**Você é audaciosa (o), corre atrás de suas metas, ou é auto protetor(a), preferindo se poupar dos eventuais riscos?**", ["Audaciosa(o) ", "Auto protetor(a)"], key="audaciosa",horizontal=True)
            
    culpado = st.radio("**Sente-se de alguma forma pressionada (o) na atualidade?**", ["Não ", "Sim"], key="culpado",horizontal=True)
    culpado_justificativa = ""
    if culpado == "Sim":
        culpado_justificativa = st.text_area("**De que maneira?**", key="culpado_justificativa")   

    sentimentos = st.text("Quais os sentimentos mais comuns em você hoje?")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        raiva_sentimento = st.selectbox("**Raiva**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="raiva_sentimento")
        medo_algo = st.selectbox("**Medo de algo**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="medo_algo")
        medo_vago = st.selectbox("**Medo Vago**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="medo_vago")
        culpa = st.selectbox("**Culpa**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="culpa")
        revolta = st.selectbox("**Revolta**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="revolta")
        medo_controle = st.selectbox("**Medo de perder o controle**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="medo_controle")

    with col2:
        ansiedade = st.selectbox("**Ansiedade**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="ansiedade")
        intolerancia = st.selectbox("**Intolerância**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="intolerancia")
        tristeza = st.selectbox("**Tristeza**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="tristeza")
        magoa = st.selectbox("**Mágoa**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="magoa")
        orgulho = st.selectbox("**Orgulho**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="orgulho")
        odio = st.selectbox("**Ódio**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="odio")

    with col3:
        submissao = st.selectbox("**Submissão**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="submissao")
        indecisao = st.selectbox("**Indecisão**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="indecisao")
        desespero = st.selectbox("**Desespero**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="desespero")    
        desanimo = st.selectbox("**Desânimo**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="desanimo")
        covardia = st.selectbox("**Covardia**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="covardia")
        egocentrismo = st.selectbox("**Egocentrismo**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="egocentrismo")

    with col4:
        ciume = st.selectbox("**Ciúme**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="ciume")
        frustracao = st.selectbox("**Frustração**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="frustracao")
        nostalgia = st.selectbox("**Nostalgia**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="nostalgia")    
        cansaco = st.selectbox("**Cansaço**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="cansaco")
        impaciencia = st.selectbox("**Impaciência**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="impaciencia")
        angustia = st.selectbox("**Angústia**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="angustia")   

    with col5:
        timidez = st.selectbox("**Timidez**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="timidez")
        apatia = st.selectbox("**Apatia**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="apatia")
        ressentimento = st.selectbox("**Ressentimento**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="ressentimento")    
        solidao = st.selectbox("**Solidão**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="solidao")
        autoritarismo = st.selectbox("**Autoritarismo**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="autoritarismo")
        egoismo = st.selectbox("**Egoísmo**",[" ","Muita Intensidade", "Média Intensidade", "Pouca Intensidade"], key="egoismo")

    #######################################################################################################################
    ############################### GERAR MENSAGEM WHATSAPP ###############################################################
    #######################################################################################################################
    # Dados do Terapeuta
    #st.header("Dados do Terapeuta")
    # Incluir faixa com título
    st.markdown("""<h2 style="background-color: #C1CDCD; color: white; padding: 10px; text-align: center;">Dados do Terapeuta</h2>""", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([1,1,3,3])

    with col1:
        codigo_pais = st.text_input("**Código de país**", "55", max_chars=2, key="codigo_pais")

    with col2:
        codigo_area = st.text_input("**Código de área (DDD)**", max_chars=2, key="codigo_area")

    with col3:
        numero_telefone = st.text_input("**Número de telefon**e", max_chars=9, key="numero_telefone")

    with col4:
            # Exibir a data formatada
        st.markdown(" ")
        st.markdown("Informe +55(DDD)0000-0000")

    col1, col2,col3 = st.columns([2,2,1])

    with col1:
        # Enviar relação pelo Whatsapp
        # Botão para envio
        if st.button("**Enviar Formulário via WhatsApp**"):
            mensagem = f"""
            *Anamnese Emocional*
            
            *Dados Pessoais:*
            Nome: {nome} 
            RG: {rg}
            CPF: {cpf}
            Data de Nascimento: {data_nascimento}
            Estado Civil: {estado_civil}
            Endereço Completo: {endereco_completo}
            Telefone Residencial: {telefone_residencial}
            Celular: {celular}
            E-mail: {email}

            Atividade: {atividade}

            Queixa Principal: {queixa_principal}

            1) É casada (o), solteira (o) ou divorciada (o)?:{estado_civil_fase1}
            2) Se é divorciada(o), por qual motivo e como se sente?:{divorcio_motivo}
            4) Número de Filhos:{numero_filhos}
            5) Como é o seu relacionamento com seus    filhos?:{relacionamento_filhos}
            6) Como você se sente em seu   relacionamento com sua parceira(o)?:{relacionamento_parceiro}
            7) Como você se sente em sua casa, dentro do contexto familiar?:{relacionamento_familiar}
            8) Como você se sente no seu trabalho?:{sentimento_trabalho}
            9) Você se sente pertencendo ao Contexto Familiar?:{pertencimento_familiar}
            9.1) Por quê?:{pertencimento_familiar_justificativa}
            10) Você se sente pertencendo ao Contexto Social?:{pertencimento_social}
            10.1) Por quê?:{pertencimento_social_justificativa}
            11) Você se sente pertencendo ao Contexto Religioso?:{pertencimento_religioso}
            11.1) Por quê?:{pertencimento_religioso_justificativa}
            12) Você sente frustração em relação a Pais?:{frustracao_pais}
            12.1) Por quê?:{frustracao_pais_justificativa}
            13) Você sente frustração em relação a Irmãos?:{frustracao_irmaos}
            13.1) Por quê?:{frustracao_irmaos_justificativa}
            14) Você sente frustração em relação a Filhos?:{frustracao_filhos}
            14.1) Por quê?:{frustracao_filhos_justificativa}
            15) Você sente frustração em relação a Colégio?:{frustracao_colegio}
            15.1) Por quê?:{frustracao_colegio_justificativa}
            16) Você sente frustração em relação a Profissão?:{frustracao_profissao}
            16.1) Por quê?:{frustracao_profissao_justificativa}
            17) Você sente frustração em relação a Cônjuge?:{frustracao_conjuge}
            17.1) Por quê?:{frustracao_conjuge_justificativa}
            18) Você sente frustração em relação a Identidade Sexual:{frustracao_identidade_sexual}
            18.1) Por quê?:{frustracao_identidade_sexual_justificativa}
            19) Você sente frustração em relação a Vida Sexual?:{frustracao_vida_sexual}
            19.1) Por quê?:{frustracao_vida_sexual_sexual_justificativa}
            20) Iniciou sua sexualidade com que idade?:{iniciou_sexualidade_idade}
            21) Como foi sua primeira vez?:{primeira_vez}
            22) Tem tido algum problema em relação ao sexo?:{problemas_sexo}
            23) Atualmente sempre se realiza nas relações sexuais?:{realizacao_sexual}
            24) O sexo para você é algo:{importancia_sexo}
            25) Algum trauma?:{trauma}
            25.1) Por quê?:{trauma_justificativa}
            26) Alguma fobia?:{fobia}
            26.1) Por quê?:{fobia_justificativa}
            27) Tem medo de alguma coisa?:{medo}
            27.1) Por quê?:{fobia_justificativa}
            28) Usa drogas?:{usa_drogas}
            28.1) Quais?:{usa_drogas_justificativa}                
            29) Dores de cabeça?:{dor_cabeca}
            29.1) Com que frequência??:{dor_cabeca_frequencia}        
            30) Insônia?:{insonia}
            30.1) Com que frequência??:{insonia_frequencia}        
            31) Tem ideias suicidas?:{ideias_suicidas}
            31.1) Quais?:{ideias_suicidas_justificativa}
            32) Usa bebidas alcoólicas?:{usa_bebidas_alcoolicas}
            32.1) Com que frequência?:{usa_bebidas_alcoolicas_frequencia}
            33) É fumante?:{fumante}
            34) Está grávida?:{grvida}
            34.1) Quantas semanas?:{grvida_semanas}
            35) Qual o seu nível de stress?:{nivel_stress}
            36) Já consultou algum tipo de psiquiatra ou psicólogo?:{consultou_psiquiatra}
            37) Se sim, foi diagnosticada (o)?:{consultou_psiquiatra_diagnostico}
            38) Qual a principal crença que as pessoas possuem em relação a você que mais se repete?:{crenca_pessoas}
            39) Você se considera feliz?:{feliz}
            39.1) Por quê?:{feliz_justificativa}
            40) Se você pudesse mudar alguma coisa em você, no seu modo de ser, ou agir,ou no seu comportamento atual, o que mudaria?:{mudaria}
            # Fase 02 - Mental:
            41) Quais são os tipos de pensamentos que você costuma alimentar em relação a si mesma (o), de uma maneira geral?:{pensamentos_positivos}
            42) Quais exatamente?:{pensamentos_positivos_justificativa}
            43) Em relação a sua competência profissional? :{pensamentos_competencia}
            44) Quais exatamente?:{pensamentos_competencia_justificativa}
            45) Em relação ao seu passado? :{pensamentos_passado}
            46) Quais exatamente?:{pensamentos_passado_justificativa}
            47) Qual sua visão sobre você? :{visao_sobre_si}
            48) Em relação a sua aparência física? :{pensamentos_aparencia}
            49) Quais exatamente? :{pensamentos_aparencia_justificativa}
            50) Em relação a sua vida emocional? :{pensamentos_vida_emocional}
            51) Em relação a sua vida sexual?:{pensamentos_vida_sexual}
            52) Quais exatamente ? :{pensamentos_vida_sexual_justificativa}
            53) Em relação ao seu futuro? :{pensamentos_futuro}
            54) Quais exatamente ? :{pensamentos_vida_sexual_justificativa}
            55) Em relação a sua vida emocional? :{pensamentos_futuro_sexual_justificativa}
            # Fase 03 - Infância:
            56) Você foi criado pelos pais?:{foi_criado_pais}
            57) Outro:{foi_criado_pais_justificativa }
            58) Você foi criado pelos pais?:{foi_criado_pais}
            59) Como é sua relação com seus pais?:{relacionamento_pais}
            60) Seus pais foram agressivos com você?:{pais_agressivos}
            61) Descreva:{pais_agressivos_justificativa}
            62) Como você descreveria o relacionamento entre seus pais?:{relacionamento_pais_descreva}
            62.1) Por quê?:{relacionamento_pais_descreva_justificativa}
            63) Quanto ao relacionamento de seus pais responda: Qual a crença que você adquiriu em relação a relacionamentos?:{relacionamento_pais_crenca}
            64) O que te faz sentir tristeza ao relembrar do passado?:{infancia_tristeza}
            65) Quando criança tinha medo de que?:{infancia_medo}
            66) Teve fase de rebeldia na adolescência?:{infancia_rebeldia}
            67) Como foi sua adolescência?:{infancia_pais_dificuldade}
            68) Qual a Filosofia de sua família em relação ao sucesso profissional? ao Dinheiro ? ao Amor? ao Sexo?:{infancia_filosofia_sucesso}
            69) Possui irmãos?:{irmaos}
            69.1) Quantos?:{irmaos_justificativa}
            70) Havia dificuldades de relacionamentos com os colegas do colégio? Se sim, cite-os.:{colégio_dificuldades}
            71) Quais eram seus maiores medos na infância?:{infancia_medos}
            72) Seus pais foram agressivos com você?:{pai_bravo}
            73) Usavam bebidas ou drogas?:{pais_usavam_drogas}
            73.1) Descreva?:{pais_usavam_drogas_justificativa}
            74) Quais os aspectos deste relacionamento que se assemelham, ou se repetem em sua vida hoje?:{relacionamento_pais_repete}
            75) Quais as características deste relacionamento, que você se mantém determinada (o) a não repetir?:{relacionamento_pais_nao_repete}
            76) Na infância, era obrigada (o) a fazer alguma coisa que lhe desagradava?:{infancia_obrigada}
            76.1) Descreva:{infancia_obrigada_justificativa}
            77) Lembra-se, de alguma coisa que o magoou muito na Infância?:{infancia_magou}
            Descreva?:{infancia_magou_justificativa}
            78) Teve perdas familiares ou de amigos na Infância?:{infancia_perdas}
            78.1) Descreva?:{infancia_perdas_justificativa}
            79) Dormia com a luz acesa ou apagada?:{infancia_dormia}
            80) Como foi sua adolescência?:{infancia_adolescencia}
            81) O que era para você, ser uma boa (bom) menina (o)?:{infancia_boa_menina}
            82) Como você deveria agir, ou ser, para ser amada(o)?:{infancia_agir}
            83) Como é sua relação com eles?:{irmaos_relacionamento}
            84) Relate algum fato marcante em sua infância:{infancia_fato_marcante}
            # Fase 04 - Emocional
            85) Quais são seus maiores medos hoje?:{medos_atualmente}
            86) Se você avaliasse sua atuação na vida, qual papel que mais caberia a você hoje?:{papel_vitima}
            87) Qual o ganho secundário?:{ganho_secundario}
            88) Em quais situações você desempenha o papel de responsável?:{papel_responsavel_situacoes}
            89) Nos relacionamentos e na vida, você prefere ser::{dominante_submisso}
            90) Quem deve ser punido por problemas que ocorrem com você? OU Quem é o culpado por seus problemas pessoais?:{punido}
            91) Sente raiva ou rancor de alguém?:{raiva }
            91.1) De Quem?:{raiva_justificativa }
            92) Sente-se de alguma forma inferior aos outros?:{inferior}
            92.1) Por quê?:{inferior_justificativa}
            93) O que você pensa a seu respeito?:{pensamento_sobre_si}
            94) Como foi o seu primeiro relacionamento amoroso?:{primeiro_relacionamento}
            95) Em quais situações você desempenha o papel de vítima?:{papel_vitima_situacoes}
            96) Se considera vitoriosa(o) ou derrotada(o)?:{vitorioso_derrotado}
            97) Sente-se de alguma forma pressionada (o) na atualidade?:{pressionado}
            98) De que maneira?:{pressionado_justificativa}
            99) Você se acha uma pessoa controladora?:{controladora}
            100) Duvida de sua própria capacidade?:{capacidade}
            101) Você é audaciosa (o), corre atrás de suas metas, ou é auto protetor(a), preferindo se poupar dos eventuais riscos?:{audaciosa}
            102) Sente-se de alguma forma pressionada (o) na atualidade?:{culpado}
            103) De que maneira?:{culpado_justificativa}
            104) Quais os sentimentos mais comuns em você hoje?,                
            104.1) Raiva:{raiva_sentimento}
            104.2) Medo de algo concreto:{medo_algo}
            104.3) Medos vagos:{medo_vago}
            104.4) Culpa:{culpa}
            104.5) Revolta:{revolta}
            104.6) Medo de perder o controle:{medo_controle}
            104.7) Tristeza:{tristeza}
            104.8) Mágoa:{magoa}
            104.9) Orgulho:{orgulho}
            104.10) Ódio:{odio}
            104.11) Egoísmo:{egoismo}
            104.12) Ansiedade:{ansiedade}
            104.13) Intolerância:{intolerancia}
            104.14) Submissão:{submissao}
            104.15) Indecisão:{indecisao}
            104.16) Desespero:{desespero}
            104.17) Desânimo:{desanimo}
            104.18) Covardia:{covardia}
            104.19) Egocentrismo:{egocentrismo}
            104.20) Ciúme:{ciume}
            104.21) Frustração:{frustracao}
            104.22) Nostalgia:{nostalgia}
            104.23) Cansaço:{cansaco}
            104.24) Impaciência:{impaciencia}
            104.25) Timidez:{timidez}
            104.26) Apatia:{apatia}
            104.27) Ressentimento:{ressentimento}
            104.28) Solidão:{solidao}
            104.29) Autoritarismo:{autoritarismo}


            """

            if codigo_pais and codigo_area and numero_telefone:
                numero_terapeuta = f"{codigo_pais}{codigo_area}{numero_telefone}"
                mensagem_codificada = urllib.parse.quote(mensagem.strip())
                url_whatsapp = f"https://wa.me/{numero_terapeuta}?text={mensagem_codificada}"
                st.success("**Clique no link abaixo para enviar o formulário via WhatsApp:**")
                st.markdown(f"[Clique aqui para enviar o formulário via WhatsApp]({url_whatsapp})")
            else:
                st.error("**Por favor, insira o código do país, o DDD e o número de telefone corretamente.**")

#######################################################################################################################
############################### GERAR PDF #############################################################################
#######################################################################################################################

        # Função para gerar o PDF
        def adicionar_subtitulo(pdf, texto):
            # Define fundo colorido e texto em branco para o subtítulo
            pdf.set_fill_color(193, 205, 205)  # Cor de fundo
            pdf.set_text_color(255, 255, 255)  # Cor do texto
            pdf.set_font("helvetica", style="B", size=12)
            
            # Adiciona um retângulo de fundo e o texto do subtítulo
# Adiciona um retângulo de fundo e o texto do subtítulo
            pdf.rect(10, pdf.get_y(), pdf.w - 20, 10, 'F')
            pdf.cell(0, 10, texto, ln=True, align="C")  # Substitui XPos.LMARGIN e YPos.NEXT por coordenadas relativas ou fixas
            
            # Retorna à cor de texto padrão para o conteúdo
            pdf.set_text_color(0, 0, 0)
            pdf.ln(1)

        # Exemplo de adicionar queixa principal
        def gerar_pdf(dados):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=10)
            pdf.set_font("helvetica", size=10)

            # Adicionar a logo
            current_dir = os.path.dirname(os.path.abspath(__file__))
            logo_path = os.path.join(current_dir, "logo_DB.png")

            # Adiciona a imagem ao PDF
            pdf.image(logo_path, x=10, y=8, w=40)  # Ajuste conforme necessário

            # Título centralizado
            pdf.set_font("helvetica", style="B", size=14)  # Tamanho maior para o título
            pdf.cell(200, 12, "Relatório - Formulário de Anamnese Emocional", ln=True, align="C")  # Substitui XPos.LMARGIN e YPos.NEXT por coordenadas relativas

            pdf.set_font("helvetica", size=8)  # Tamanho menor para a data
            pdf.cell(200, 8, f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", ln=True, align="C")
            pdf.ln(10)

            # Linha separadora que cobre toda a largura da página
            pdf.set_draw_color(0)  # Cor da linha (0 = preto)
            pdf.line(5, pdf.get_y()-10, pdf.w - 10, pdf.get_y()-10)  # Linha que cobre de margem a margem

            # Linha separadora que cobre toda a largura da página
            pdf.set_draw_color(0)  # Cor da linha (0 = preto)
            pdf.line(5, pdf.get_y()-10, pdf.w - 10, pdf.get_y()-10)  # Linha que cobre de margem a margem

            # Destacar o cabeçalho "Dados Pessoais"
            pdf.set_text_color(0, 0, 0)  # Cor do texto
            pdf.set_font("helvetica", size=10)  # Ajustar o tamanho da fonte para o restante do texto
            pdf.ln(-3)  # Espaço extra

            # Largura e altura das células para duas colunas
            col_width = pdf.w / 2 - 20  # Cada coluna ocupa metade da largura da página
            row_height = 8

            # Adicionar seções ao PDF
            for secao, conteudo in dados.items():
                # Título da seção
                adicionar_subtitulo(pdf, secao)
                items = list(conteudo.items())

                if secao == "Dados Pessoais ":  # Condição para exibir os dados pessoais em duas colunas
                    for i in range(0, len(items), 2):
                        label1, valor1 = items[i]
                        pdf.set_font("helvetica", size=11)  # Estilo do texto
                        pdf.cell(col_width, row_height, f"{label1}: {valor1}", border=0)  # Remover o 'text='

                        # Verifica se existe o próximo item para a segunda coluna
                        if i + 1 < len(items):
                            label2, valor2 = items[i + 1]
                            pdf.set_font("helvetica", size=11)  # Estilo do texto
                            pdf.cell(col_width, row_height, f"{label2}: {valor2}", border=0)  # Remover o 'text='
                        pdf.ln(row_height)  # Pula para a próxima linha após cada par de itens

                else:  # Caso contrário, exibe o conteúdo em uma coluna
                    for label, valor in items:
                        pdf.set_font("helvetica", size=11)  # Estilo do texto
                        pdf.multi_cell(0, row_height, f"{label}: {valor}", border=0)
                        pdf.ln(row_height / 4)

                pdf.ln(1)  # Espaço extra entre seções

    ### RODAPE
            # Adicionar rodapé ao final da página
            pdf.set_y(-30)  # Posição para o rodapé
            pdf.set_font("helvetica", style="I", size=8)  # Altere o tamanho da fonte aqui
            
            # Linha separadora que cobre toda a largura da página
            pdf.set_draw_color(0)  # Cor da linha (0 = preto)
            pdf.line(10, pdf.get_y(), pdf.w - 10, pdf.get_y())  # Linha que cobre de margem a margem
            
            # Adicionar logo Instagram e texto
            current_dir = os.getcwd()
            logo_instagram = os.path.join(current_dir, "instagram.png")
            logo_width = 6  # ajuste conforme necessário
            logo_height = 6

            # Adiciona a logo do Instagram e o texto
            pdf.cell(0, 10, ln=True, align="C")  # Move para a linha centralizada antes de inserir o conteúdo
            pdf.image(instagram, x=pdf.get_x() + 60, y=pdf.get_y(), w=logo_width, h=logo_height)
        
            # Alinha o texto após a imagem
            pdf.cell(logo_width)  # Espaço para alinhar o texto após a imagem
            pdf.cell(0, 10, "daianebrasil.terapeuta | Contato: (41) 99740-0579", ln=True, align="C")

            # Usar output com "S" para retornar o conteúdo como bytes
            pdf_output = pdf.output(dest='S').encode('latin1')  # Gera o PDF como string/buffer

            return pdf_output

        # Função para capturar dados da interface (exemplo)
        def capturar_dados():
            dados = {
                "Nome e Endereço":{
                    "Nome":st.session_state.get("nome"),
                    "Endereço Completo":st.session_state.get("endereco_completo"),
                }, 

                "Dados Pessoais ": { #deixei uma espaço em branco acima do "Nome"
    # Esse trecho em duas colunas 
                    "RG":st.session_state.get("rg"), 
                    "CPF":st.session_state.get("cpf"),
                    "Data de Nascimento":st.session_state.get("data_nascimento"),
                    "Estado Civil":st.session_state.get("estado_civil"),
                    "CEP":st.session_state.get("cep"),
                    "Bairro":st.session_state.get("bairro"),
                    "Cidade":st.session_state.get("cidade"),
                    "UF":st.session_state.get("uf"),
                    "Telefone Residencial":st.session_state.get("telefone_residencial"),
                    "Celular":st.session_state.get("celular"),
                    "E-mail":st.session_state.get("email"),
                    "Atividade":st.session_state.get("atividade"),
                    
                },
                # Incluir os subtítulos

                    "O que te trouxe até aqui?":{

                    " ":st.session_state.get("queixa_principal"),
            
                },    

    # Esse trecho em um coluna
                "Fase 01 - Vida Pessoal": {    

                    "1) É casada (o), solteira (o) ou divorciada (o)?":st.session_state.get("estado_civil_fase1"),
                    
                    "2) Se é divorciada(o), por qual motivo e como se sente?":
                    st.session_state.get("divorcio_motivo"),
                    
                    "4) Número de Filhos":st.session_state.get("numero_filhos"),
                    
                    "5) Como é o seu relacionamento com seus 	filhos?":
                    st.session_state.get("relacionamento_filhos"),
                    
                    "6) Como você se sente em seu 	relacionamento com sua parceira(o)?":
                    st.session_state.get("relacionamento_parceiro"),
                    
                    "7) Como você se sente em sua casa, dentro do contexto familiar?":
                    st.session_state.get("relacionamento_familiar"),
                    
                    "8) Como você se sente no seu trabalho?":
                    st.session_state.get("sentimento_trabalho"),
                    
                    "9) Você se sente pertencendo ao Contexto Familiar?":st.session_state.get("pertencimento_familiar"),
                    "Por quê?":st.session_state.get("pertencimento_familiar_justificativa"),

                    "10) Você se sente pertencendo ao Contexto Social?":st.session_state.get("pertencimento_social"),
                    "Por quê?":st.session_state.get("pertencimento_social_justificativa"),

                    "11) Você se sente pertencendo ao Contexto Religioso?":
                    st.session_state.get("pertencimento_religioso"),
                    "Por quê?":st.session_state.get("pertencimento_religioso_justificativa"),

                    "12) Você sente frustração em relação a Pais?":
                    st.session_state.get("frustracao_pais"),
                    "Por quê?":st.session_state.get("frustracao_pais_justificativa"),

                    "13) Você sente frustração em relação a Irmãos?":
                    st.session_state.get("frustracao_irmaos"),
                    "Por quê?":st.session_state.get("frustracao_irmaos_justificat"),

                    "14) Você sente frustração em relação a Filhos?":
                    st.session_state.get("frustracao_filhos"),
                    "Por quê?":st.session_state.get("frustracao_filhos_justifica"),

                    "15) Você sente frustração em relação a Colégio?":
                    st.session_state.get("frustracao_colegio"),
                    "Por quê?":st.session_state.get("frustracao_colegio_justificativ"),
                    
                    "16) Você sente frustração em relação a Profissão?":
                    st.session_state.get("frustracao_profissao"),
                    "Por quê?":st.session_state.get("frustracao_profissao_justificativa"),
                    
                    "17) Você sente frustração em relação a Cônjuge?":
                    st.session_state.get("frustracao_conjuge"),
                    "Por quê?":st.session_state.get("frustracao_conjuge_justificativa"),
                    
                    "18) Você sente frustração em relação a Identidade Sexual":
                    st.session_state.get("frustracao_identidade_sexual"),
                    "Por quê?":st.session_state.get("frustracao_identidade_sexual_justificativa"),

                    "19) Você sente frustração em relação a Vida Sexual?":
                    st.session_state.get("frustracao_vida_sexual"),
                    "Por quê?":st.session_state.get("frustracao_vida_sexual_sexual_justificativa"),
                    
                    "20) Iniciou sua sexualidade com que idade?":
                    st.session_state.get("iniciou_sexualidade_idade"),

                    "21) Como foi sua primeira vez?":
                    st.session_state.get("primeira_vez"),

                    "22) Tem tido algum problema em relação ao sexo?":
                    st.session_state.get("problemas_sexo"),

                    "23) Atualmente sempre se realiza nas relações sexuais?":
                    st.session_state.get("realizacao_sexual"),
                    
                    "24) O sexo para você é algo":
                    st.session_state.get("importancia_sexo"),

                    "25) Algum trauma?":st.session_state.get("trauma"),
                    "Por quê?":st.session_state.get("trauma_justificativa"),

                    "26) Alguma fobia?":st.session_state.get("fobia"),
                    "Por quê?":st.session_state.get("fobia_justificativa"),
                    
                    "27) Tem medo de alguma coisa?":
                    st.session_state.get("medo"),
                    "Por quê?":st.session_state.get("fobia_justificativa"),
                    
                    "28) Usa drogas?":
                    st.session_state.get("usa_drogas"),
                    "Quais?":st.session_state.get("usa_drogas_justificativa"),
                
                    "29) Dores de cabeça?":
                    st.session_state.get("dor_cabeca"),
                    "Com que frequência??":st.session_state.get("dor_cabeca_frequencia"),
                            
                    "30) Insônia?":st.session_state.get("insonia"),
                    "Com que frequência??":st.session_state.get("insonia_frequencia"),
                            
                    "31) Tem ideias suicidas?":
                    st.session_state.get("ideias_suicidas"),
                    "Quais?":st.session_state.get("ideias_suicidas_justificativa"),
                    
                    "32) Usa bebidas alcoólicas?":
                    st.session_state.get("usa_bebidas_alcoolicas"),
                    "Com que frequência?":st.session_state.get("usa_bebidas_alcoolicas_frequencia"),
                    
                    "33) É fumante?":st.session_state.get("fumante"),
                    
                    "34) Está grávida?":st.session_state.get("grvida"),
                    "Quantas semanas?":st.session_state.get("grvida_semanas"),
                    
                    "35) Qual o seu nível de stress?":st.session_state.get("nivel_stress"),
                    "36) Já consultou algum tipo de psiquiatra ou psicólogo?":st.session_state.get("consultou_psiquiatra"),
                    "37) Se sim, foi diagnosticada (o)?":st.session_state.get("consultou_psiquiatra_diagnostico"),

                    "38) Qual a principal crença que as pessoas possuem em relação a você que mais se repete?":st.session_state.get("crenca_pessoas"),

                    "39) Você se considera feliz?":st.session_state.get("feliz"),
                    "Por quê?":st.session_state.get("feliz_justificativa"),

                    "40) Se você pudesse mudar alguma coisa em você, no seu modo de ser, ou agir,ou no seu comportamento atual, o que mudaria?":
                    st.session_state.get("mudaria"),
                },

                "Fase 02 - Mental": {  

                    # Fase 02 - Mental:

                    "41) Quais são os tipos de pensamentos que você costuma alimentar em relação a si mesma (o), de uma maneira geral?":st.session_state.get("pensamentos_positivos"),
                    "42) Quais exatamente?":st.session_state.get("pensamentos_positivos_justificativa"),
                    "43) Em relação a sua competência profissional? ":st.session_state.get("pensamentos_competencia"),

                    "44) Quais exatamente?":st.session_state.get("pensamentos_competencia_justificativa"),
                    "45) Em relação ao seu passado? ":st.session_state.get("pensamentos_passado"),
                    "46) Quais exatamente?":st.session_state.get("pensamentos_passado_justificativa"),
                    "47) Qual sua visão sobre você? ":st.session_state.get("visao_sobre_si"),
                    "48) Em relação a sua aparência física? ":st.session_state.get("pensamentos_aparencia"),
                    "49) Quais exatamente? ":st.session_state.get("pensamentos_aparencia_justificativa"),
                    "50) Em relação a sua vida emocional? ":st.session_state.get("pensamentos_vida_emocional"),

                    "51) Em relação a sua vida sexual?":st.session_state.get("pensamentos_vida_sexual"),
                    "52) Quais exatamente ? ":st.session_state.get("pensamentos_vida_sexual_justificativa"),
                    "53) Em relação ao seu futuro? ":st.session_state.get("pensamentos_futuro"),
                    "54) Quais exatamente ? ":st.session_state.get("pensamentos_vida_sexual_justificativa"),
                    "55) Em relação a sua vida emocional? ":st.session_state.get("pensamentos_futuro_sexual_justificativa"),
                },

                "Fase 03 - Infância": {  
                    # Fase 03 - Infância:

                    "56) Você foi criado pelos pais?":st.session_state.get("foi_criado_pais"),
                    "57) Outro":st.session_state.get("foi_criado_pais_justificativa "),
                    "58) Você foi criado pelos pais?":st.session_state.get("foi_criado_pais"),
                    "59) Como é sua relação com seus pais?":st.session_state.get("relacionamento_pais"),

                    "60) Seus pais foram agressivos com você?":st.session_state.get("pais_agressivos"),
                    "61) Descreva":st.session_state.get("pais_agressivos_justificativa"),
                    "62) Como você descreveria o relacionamento entre seus pais?":st.session_state.get("relacionamento_pais_descreva"),
                    "Por quê?":st.session_state.get("relacionamento_pais_descreva_justificativa"),
                    "63) Quanto ao relacionamento de seus pais responda: Qual a crença que você adquiriu em relação a relacionamentos?":st.session_state.get("relacionamento_pais_crenca"),
                    "64) O que te faz sentir tristeza ao relembrar do passado?":st.session_state.get("infancia_tristeza"),
                    "65) Quando criança tinha medo de que?":st.session_state.get("infancia_medo"),

                    "66) Teve fase de rebeldia na adolescência?":st.session_state.get("infancia_rebeldia"),
                    "67) Como foi sua adolescência?":st.session_state.get("infancia_pais_dificuldade"),
                    "68) Qual a Filosofia de sua família em relação ao sucesso profissional? ao Dinheiro ? ao Amor? ao Sexo?":st.session_state.get("infancia_filosofia_sucesso"),
                    "69) Possui irmãos?":st.session_state.get("irmaos"),
                    "Quantos?":st.session_state.get("irmaos_justificativa"),
                    "70) Havia dificuldades de relacionamentos com os colegas do colégio? Se sim, cite-os.":st.session_state.get("colégio_dificuldades"),

                    "71) Quais eram seus maiores medos na infância?":st.session_state.get("infancia_medos"),
                    "72) Seus pais foram agressivos com você?":st.session_state.get("pai_bravo"),
                    "73) Usavam bebidas ou drogas?":st.session_state.get("pais_usavam_drogas"),
                    "Descreva?":st.session_state.get("pais_usavam_drogas_justificativa"),
                    "74) Quais os aspectos deste relacionamento que se assemelham, ou se repetem em sua vida hoje?":st.session_state.get("relacionamento_pais_repete"),
                    "75) Quais as características deste relacionamento, que você se mantém determinada (o) a não repetir?":st.session_state.get("relacionamento_pais_nao_repete"),

                    "76) Na infância, era obrigada (o) a fazer alguma coisa que lhe desagradava?":st.session_state.get("infancia_obrigada"),
                    "Descreva":st.session_state.get("infancia_obrigada_justificativa"),
                    "77) Lembra-se, de alguma coisa que o magoou muito na Infância?":st.session_state.get("infancia_magou"),
                    "Descreva?":st.session_state.get("infancia_magou_justificativa"),
                    "78) Teve perdas familiares ou de amigos na Infância?":st.session_state.get("infancia_perdas"),
                    "Descreva?":st.session_state.get("infancia_perdas_justificativa"),

                    "79) Dormia com a luz acesa ou apagada?":st.session_state.get("infancia_dormia"),
                    "80) Como foi sua adolescência?":st.session_state.get("infancia_adolescencia"),
                    "81) O que era para você, ser uma boa (bom) menina (o)?":st.session_state.get("infancia_boa_menina"),
                    "82) Como você deveria agir, ou ser, para ser amada(o)?":st.session_state.get("infancia_agir"),
                    "83) Como é sua relação com eles?":st.session_state.get("irmaos_relacionamento"),
                    "84) Relate algum fato marcante em sua infância":st.session_state.get("infancia_fato_marcante"),

                },

            
                "Fase 04 - Emocional": {             
                    # Fase 04 - Emocional

                    "85) Quais são seus maiores medos hoje?":st.session_state.get("medos_atualmente"),
                    "86) Se você avaliasse sua atuação na vida, qual papel que mais caberia a você hoje?":st.session_state.get("papel_vitima"),
                    "87) Qual o ganho secundário?":st.session_state.get("ganho_secundario"),
                    "88) Em quais situações você desempenha o papel de responsável?":st.session_state.get("papel_responsavel_situacoes"),
                    "89) Nos relacionamentos e na vida, você prefere ser:":st.session_state.get("dominante_submisso"),
                    "90) Quem deve ser punido por problemas que ocorrem com você? OU Quem é o culpado por seus problemas pessoais?":st.session_state.get("punido"),
                    "91) Sente raiva ou rancor de alguém?":st.session_state.get("raiva "),
                    "De Quem?":st.session_state.get("raiva_justificativa "),

                    "92) Sente-se de alguma forma inferior aos outros?":st.session_state.get("inferior"),
                    "Por quê?":st.session_state.get("inferior_justificativa"),
                    "93) O que você pensa a seu respeito?":st.session_state.get("pensamento_sobre_si"),
                    "94) Como foi o seu primeiro relacionamento amoroso?":st.session_state.get("primeiro_relacionamento"),
                    "95) Em quais situações você desempenha o papel de vítima?":st.session_state.get("papel_vitima_situacoes"),
                    
                    "96) Se considera vitoriosa(o) ou derrotada(o)?":st.session_state.get("vitorioso_derrotado"),
                    "97) Sente-se de alguma forma pressionada (o) na atualidade?":st.session_state.get("pressionado"),
                    "98) De que maneira?":st.session_state.get("pressionado_justificativa"),
                    "99) Você se acha uma pessoa controladora?":st.session_state.get("controladora"),
                    "100) Duvida de sua própria capacidade?":st.session_state.get("capacidade"),
                    "101) Você é audaciosa (o), corre atrás de suas metas, ou é auto protetor(a), preferindo se poupar dos eventuais riscos?":st.session_state.get("audaciosa"),
                    "102) Sente-se de alguma forma pressionada (o) na atualidade?":st.session_state.get("culpado"),
                    "103) De que maneira?":st.session_state.get("culpado_justificativa"),

                    "104) Quais os sentimentos mais comuns em você hoje?":st.session_state.get(""),
                                    
                    "Raiva":st.session_state.get("raiva_sentimento"),
                    "Medo de algo concreto":st.session_state.get("medo_algo"),
                    "Medos vagos":st.session_state.get("medo_vago"),
                    "Culpa":st.session_state.get("culpa"),
                    "Revolta":st.session_state.get("revolta"),
                    "Medo de perder o controle":st.session_state.get("medo_controle"),
                    "Tristeza":st.session_state.get("tristeza"),

                    "Mágoa":st.session_state.get("magoa"),
                    "Orgulho":st.session_state.get("orgulho"),
                    "Ódio":st.session_state.get("odio"),
                    "Egoísmo":st.session_state.get("egoismo"),
                    "Ansiedade":st.session_state.get("ansiedade"),
                    "Intolerância":st.session_state.get("intolerancia"),

                    "Submissão":st.session_state.get("submissao"),
                    "Indecisão":st.session_state.get("indecisao"),
                    "Desespero":st.session_state.get("desespero"),
                    "Desânimo":st.session_state.get("desanimo"),
                    "Covardia":st.session_state.get("covardia"),
                    "Egocentrismo":st.session_state.get("egocentrismo"),

                    "Ciúme":st.session_state.get("ciume"),
                    "Frustração":st.session_state.get("frustracao"),
                    "Nostalgia":st.session_state.get("nostalgia"),
                    "Cansaço":st.session_state.get("cansaco"),
                    "Impaciência":st.session_state.get("impaciencia"),

                    "Timidez":st.session_state.get("timidez"),
                    "Apatia":st.session_state.get("apatia"),
                    "Ressentimento":st.session_state.get("ressentimento"),
                    "Solidão":st.session_state.get("solidao"),
                    "Autoritarismo":st.session_state.get("autoritarismo"),


                }
            }
            return dados

    # # Botão para gerar o relatório
    # if st.button("Gerar Relatório PDF"):
    #     dados = capturar_dados()
    #     file_path = gerar_pdf(dados)
    #     st.success(f"Relatório PDF gerado com sucesso! [Baixar PDF]({file_path})")
    #     st.write(file_path)

    # CSS personalizado para o st.button
    st.markdown("""
        <style>
        /* Estilo para o botão padrão */
        .stButton>button {
            background-color: #4CAF50; /* Cor de fundo do botão */
            color: white; /* Cor do texto */
            border: none; /* Remover borda */
            border-radius: 15px; /* Borda arredondada */
            padding: 10px 20px; /* Padding interno */
            font-weight: bold; /* Texto em negrito */
            font-size: 16px; /* Tamanho da fonte */
            transition: background-color 0.3s ease; /* Transição suave ao passar o mouse */
        }

        /* Cor ao passar o mouse sobre o botão */
        .stButton>button:hover {
            background-color: #45a049; /* Cor de fundo ao passar o mouse */
            color: white; /* Cor do texto ao passar o mouse */
        }
        </style>
    """, unsafe_allow_html=True)

    # CSS personalizado para o st.download_button
    st.markdown(
    """
        <style>
        /* Estilo para o botão de download */
        .stDownloadButton > button {
            background-color: #0073e6; /* Cor de fundo */
            color: white; /* Cor do texto */
            border: none; /* Remove borda */
            border-radius: 15px; /* Borda arredondada */
            padding: 10px 20px; /* Padding interno */
            font-weight: bold; /* Texto em negrito */
            font-size: 16px; /* Tamanho da fonte */
            transition: background-color 0.3s ease; /* Transição suave ao passar o mouse */
        }

        /* Cor ao passar o mouse sobre o botão de download */
        .stDownloadButton > button:hover {
            background-color: #005bb5; /* Cor de fundo ao passar o mouse */
            color: white; /* Cor do texto ao passar o mouse */
        }
        </style>
    """, unsafe_allow_html=True)

    with col2:
        # Botão para gerar o relatório
        if st.button("Gerar Relatório PDF"):
            dados = capturar_dados()
            pdf_file = gerar_pdf(dados)

    # Exibir o PDF embutido
            st.success("Relatório PDF gerado com sucesso!")
    # Colocar os botões lado a lado
            col_download1, col_download2 = st.columns(2)
            with col_download1:
                st.download_button("Baixar PDF", pdf_file, file_name="relatorio_anamnese.pdf", mime="application/pdf")
            with col_download2:
                st.download_button("Visualizar PDF", pdf_file, file_name="relatorio_anamnese.pdf", mime="application/pdf")

###########################################################################################################
############### ATE PONTO FORMULARIO ANAMINESE ###################################################
###########################################################################################################
else:
    # Definir o layout com três colunas: esquerda, central e direita
    col1, col2, col3 = st.columns([6, 6, 6 ])

    # Exibir a logo no canto superior direito
    with col2:
       
        # Função para converter imagem em Base64
        def st_image_to_base64(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode("utf-8")

        # Obtém o caminho absoluto do diretório atual
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Concatena com o nome do arquivo
        image_path = os.path.join(current_directory, "Day_modelo_py.png")

        # Usa HTML para exibir a imagem com bordas arredondadas
        image_html = f"""
            <div style="text-align: center;">
                <img src="data:image/png;base64,{st_image_to_base64(image_path)}" 
                    style="border-radius: 30px; width: 400px;" alt="Logo">
            </div>
        """

        # Exibe o HTML no Streamlit
        st.markdown(image_html, unsafe_allow_html=True)
    # Função para arredondar os cantos da imagem
        # def round_corners(image, radius):
        #     # Criar uma máscara com cantos arredondados
        #     mask = Image.new("L", image.size, 0)
        #     draw = ImageDraw.Draw(mask)
        #     draw.rounded_rectangle(
        #         [(0, 0), image.size], radius=radius, fill=255
        #     )
            
        #     # Aplicar a máscara à imagem original
        #     rounded_image = image.copy()
        #     rounded_image.putalpha(mask)
        #     return rounded_image
        # # # Caminho para a logo
        # logo_path = "C:/python-projeto/ControllerSoft/Login/Day_modelo_py.png"  # Substitua pelo caminho da logo
        # logo = Image.open(logo_path)
        # # Arredondar os cantos da imagem
        # rounded_logo = round_corners(logo, radius=30)  # Ajuste o valor do 'radius' conforme necessário

        # # Exibir a imagem com os cantos arredondados
        # st.image(rounded_logo, use_column_width=True)

    with col1:
        st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <p>Boas-vindas ao seu ambiente de transformação emocional! Eu sou <strong>Daiane Brasil</strong>, <strong>Terapeuta<strong>.</p>
        <p>Dedico a minha vida profissional a auxiliar mulheres que desejam resolver conflitos internos e superar desafios emocionais que se manifestam em diversas áreas da vida: relacionamentos, auto-imagem, autoconfiança e desenvolvimento pessoal.</p>
        <p>Aqui, você tem um local seguro e acolhedor para explorar as emoções sob uma nova perspectiva e cultivar a força interior necessária para viver uma vida mais equilibrada e satisfatória.</p>
        <p>Como sua terapeuta, estarei presente, ouvirei com empatia e sabedoria e respeitarei a sua jornada e identidade individual.</p>
        <p>Acredito firmemente que toda mulher, em qualquer lugar, já possui o potencial, a coragem e a sabedoria para superar a adversidade e viver uma vida leve.</p>
        <p>Juntas, vamos alcançar a liberdade emocional que você tanto almeja e merece.</p>
    </div>
    """, unsafe_allow_html=True)    

    # # Botão de login
    # if st.button("Entrar"):
    #     if usuario == "Usuario" and senha == "Senha":
    #         st.success("Login bem-sucedido!")
    #         # Redirecione ou execute outra ação aqui
    #     else:
    #         st.error("Usuário ou senha incorretos. Tente novamente.")

        # Estilos CSS
        st.markdown("""
        <style>
            .stTextInput input {
                border: 3px solid #C0C0C0;
                border-radius: 6px;
            }
        </style>
        """, unsafe_allow_html=True)

        # # Username input
        # username = st.text_input("Usuário:", max_chars=10)

        # # Password input
        # password = st.text_input("Senha:", type="password", max_chars=6)
        # Definir estilo CSS para que o botão ocupe toda a largura da coluna
        # CSS para o botão de largura total
        st.markdown("""
            <style>
            .stButton button {
                width: 100% !important;
                background-color: #4CAF50 !important;
                color: white !important;
                font-size: 18px !important;
                padding: 10px;
                border-radius: 8px;
            }
            </style>
            """, unsafe_allow_html=True)
        
    # Exibir a imagem no canto superior esquerdo
    with col3:
        # Obtém o caminho do diretório onde o script está sendo executado
        current_dir = os.path.dirname(os.path.abspath(__file__))
        logo_path = os.path.join(current_dir, "logo_DB.png") 
        
        # Abre e exibe a imagem no Streamlit
        foto = Image.open(logo_path)  # Caminho dinâmico
        st.image(foto, use_column_width=True)
        
        usuario = st.text_input("Usuário:", max_chars=10)
        senha = st.text_input("Senha:", type="password", max_chars=6)

        if st.button("ACESSAR"):
            if usuario == "Terapeuta" and senha == "123456":
                st.session_state.authenticated = True  # Definir como autenticado
                st.session_state.username = usuario
                st.success("Login efetuado com sucesso!")
            else:
                st.error("Usuário ou senha incorretos. Tente novamente.")





