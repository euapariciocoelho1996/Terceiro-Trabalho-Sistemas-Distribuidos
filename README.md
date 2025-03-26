# Sistema Cliente/Servidor em Camadas
 Este projeto implementa um sistema de processamento de imagens baseado em arquitetura cliente-servidor. Ele permite que um cliente envie uma imagem para um servidor, que aplicará um filtro de pixelização em preto  e branco e retornará a imagem processada. Os metadados das imagens são armazenados em um banco de dados SQLite.
 ## Estrutura do Projeto

```
📁 TRABALHO 3  
│  
├── 📁 client  
│   └── client.py        # Interface gráfica do cliente (Tkinter)  
│
├── 📁 client_images    # Usuário também pode visualizar na sua máquina
├── 📁 images            # Pasta onde as imagens são armazenadas  
│  
├── 📁 server  
│   ├  
│   ├── filters.py       # Aplicação de filtros na imagem  
│   ├── server.py        # Servidor Flask que processa as imagens  
│   └── 📁 pycache/      # Cache de execução do Python  
│  
├── 📁 telas             # Capturas de tela para demonstração do projeto  
│  
├── 📁 images.db         # Banco de dados SQLite  
│  
├── README.md            # Documentação do projeto  
├── requirements.txt     # Dependências do projeto  
├── .gitignore           # Arquivos a serem ignorados no Git  
└── LICENSE              # Licença do projeto  
```

Essa estrutura deve facilitar a navegação e compreensão do projeto por outros desenvolvedores ou usuários que acessarem o repositório.


## Requisitos

- 🐍 Python 3.x
- 🖼️ Pillow – Processamento de imagens
- 🖥️ Tkinter – Interface gráfica do cliente
- 🌐 Flask – Comunicação HTTP entre cliente e servidor
- 🗄️ SQLite 3.x – Banco de dados para armazenamento de metadados
  
## 🚀 **Como Executar o Projeto**  

### 🔹 **1. Clone o repositório**  
Abra o terminal e execute:  
```bash
git clone https://github.com/euapariciocoelho1996/Sistema-Cliente-Servidor-em-Camadas.git
cd Sistema-Cliente-Servidor-em-Camadas
```
### 🔹 **2. O trabalho solicita o uso de dois computadores**  
```
Baixe os arquivos compactados (ZIP) do código em ambas as máquinas que serão utilizadas.
```

### 🔹 **3. Instale as dependências**  
```No Terminal execute:
 pip install Flask
 pip install requests
 pip install pillow
```

### 🔹 **4. Inicie o Servidor**  
```bash
python server/server.py
```

### 🔹 **5. Execute o Cliente**  
```bash
python client/client.py

Atenção: para que o código funcione coloque o endereço IP da máquina que está sendo o servidor. O mesmo deve ser feito no arquivo do cliente.
```

# 📸 Telas do Sistema

🗃️ Tela de gerenciamento do banco de dados SQLite3, onde é possível visualizar e manipular as informações armazenadas, garantindo a integridade e o correto funcionamento do sistema de armazenamento.

![Banco de Dados](https://github.com/euapariciocoelho1996/Terceiro-Trabalho-Sistemas-Distribuidos/blob/main/telas/bd.png?raw=true)

📤🖼️ Interface do usuário para o envio de imagens. Nesta tela, o usuário pode selecionar e carregar imagens para serem processadas pelo sistema, facilitando o fluxo de trabalho e a interação com o banco de dados

![Tela de Seleção de Imagem](https://github.com/euapariciocoelho1996/Terceiro-Trabalho-Sistemas-Distribuidos/blob/main/telas/selecionarImg.png?raw=true)

🔧🖼️ Tela que exibe o processamento de imagem com a aplicação de filtros. O sistema permite aplicar modificações nas imagens carregadas, oferecendo uma visualização clara do efeito antes de finalizar o processamento.

![Imagem com Filtro](https://github.com/euapariciocoelho1996/Terceiro-Trabalho-Sistemas-Distribuidos/blob/main/telas/filtroAplicado.jpeg?raw=true)


## Contribuidores

Luis Eduardo,
Francisco Aparício,
Victor Macêdo


## Licença

Este projeto está sob a licença MIT.
