# 🎵 Spotify Data Analytics Dashboard

Dashboard interativo para análise exploratória de dados musicais do Spotify, revelando insights sobre características de áudio, popularidade e tendências através de visualizações dinâmicas.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Sobre o Projeto

Aplicação web desenvolvida em Streamlit para exploração e análise de datasets musicais do Spotify. O dashboard permite investigar características de áudio (danceability, energy, valence, etc.), correlações entre atributos e padrões de popularidade de músicas.

**Use Cases:**
- Análise de tendências musicais ao longo do tempo
- Comparação de características de áudio entre gêneros
- Descoberta de padrões em músicas populares
- Estudo de correlações entre atributos sonoros

## ✨ Funcionalidades

- 📊 **Análise Multidimensional** - Explore 13+ características de áudio do Spotify
- 🔍 **Filtros Interativos** - Segmente dados por artista, ano, gênero e popularidade
- 📈 **Visualizações Dinâmicas** - Gráficos de correlação, dispersão e distribuição
- 🎼 **Comparação de Músicas** - Analise atributos lado a lado
- 📁 **Navegação Multi-Páginas** - Interface organizada por tipo de análise
- 💾 **Dataset Real** - Dados autênticos da API do Spotify

## 🛠️ Stack Tecnológico

- **Python 3.9+** - Linguagem principal
- **Streamlit** - Framework para interfaces web interativas
- **Pandas** - Manipulação e análise de dados
- **Plotly** - Visualizações interativas de alta qualidade
- **NumPy** - Computação numérica
- **Seaborn/Matplotlib** - Gráficos estatísticos

## 📦 Estrutura do Projeto

```
streamlit_spotify/
├── Início.py              # Página inicial e overview
├── pages/                 # Módulos de análise específicos
│   ├── 01_Análise.py      # Análises exploratórias
│   ├── 02_Correlações.py  # Matriz de correlação
│   └── 03_Comparação.py   # Comparação entre músicas
├── 01 Spotify.csv         # Dataset com dados do Spotify
├── requirements.txt       # Dependências do projeto
└── .gitignore            # Arquivos ignorados pelo Git
```

## 🚀 Guia de Instalação

### Pré-requisitos
- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional)

### Passo a Passo

1. **Clone o repositório:**
```bash
git clone https://github.com/markuscarneiro/streamlit_spotify.git
cd streamlit_spotify
```

2. **Crie um ambiente virtual (recomendado):**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**
```bash
streamlit run Início.py
```

5. **Acesse no navegador:**
```
http://localhost:8501
```

## 📊 Características do Dataset

O dataset inclui informações sobre:
- **Danceability** - Quão dançante é a música (0-1)
- **Energy** - Intensidade e atividade (0-1)
- **Valence** - Positividade musical (0-1)
- **Tempo** - BPM (batidas por minuto)
- **Speechiness** - Presença de palavras faladas
- **Acousticness** - Nível acústico da música
- **Instrumentalness** - Ausência de vocais
- **Liveness** - Probabilidade de gravação ao vivo
- **Loudness** - Volume geral em decibéis
- **Popularity** - Score de popularidade (0-100)

## 📸 Preview

*[Screenshots serão adicionados em breve - Execute o projeto para visualizar!]*

## 🎓 Competências Demonstradas

Este projeto showcaseava habilidades em:

- ✅ **Data Science** - EDA, análise estatística e descoberta de insights
- ✅ **Visualização de Dados** - Criação de dashboards informativos
- ✅ **Python** - Programação orientada a dados e boas práticas
- ✅ **Web Development** - Desenvolvimento de interfaces interativas
- ✅ **Storytelling com Dados** - Comunicação visual de descobertas

## 🔮 Melhorias Futuras

- [ ] Integração com Spotify API para dados em tempo real
- [ ] Sistema de recomendação de músicas baseado em similaridade
- [ ] Análise de sentimento de letras com NLP
- [ ] Clustering de músicas por características de áudio
- [ ] Deploy na nuvem (Streamlit Cloud/Heroku)
- [ ] Exportação de relatórios em PDF

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
4. Push para a branch (`git push origin feature/MinhaFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Markus Carneiro**

Senior Internal Auditor | Data Science & Analytics

- 💼 LinkedIn: [linkedin.com/in/markuscarneiro](https://linkedin.com/in/markuscarneiro)
- 🐙 GitHub: [@markuscarneiro](https://github.com/markuscarneiro)
- 📧 Email: [Disponível no perfil do GitHub]

### Sobre mim
Profissional com 19 anos de experiência, especializado em auditoria interna e ciência de dados. Combino expertise em Python, SAP, Snowflake e BI para transformar dados em insights acionáveis.

---

⭐ **Gostou do projeto? Deixe uma estrela!** Isso me motiva a criar mais conteúdo técnico de qualidade.

💡 **Dúvidas ou sugestões?** Abra uma [issue](https://github.com/markuscarneiro/streamlit_spotify/issues) ou entre em contato!
