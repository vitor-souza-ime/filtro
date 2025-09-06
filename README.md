# Filtros de Imagem com OpenCV

Este projeto demonstra a aplicação de filtros clássicos de processamento de imagens utilizando **Python** e **OpenCV**.  
A imagem é baixada automaticamente da internet (usando *User-Agent* personalizado) e, em seguida, são aplicados diversos filtros de suavização, detecção de bordas e limiarização.

## 📂 Estrutura do Repositório
```

filtro/
│── main.py         # Código principal do projeto
│── README.md       # Documentação do repositório

````

## 🚀 Tecnologias Utilizadas
- [Python 3.11](https://www.python.org/)
- [OpenCV 4.5+](https://opencv.org/)
- [NumPy 1.21+](https://numpy.org/)
- [Matplotlib 3.4+](https://matplotlib.org/)
- [Requests](https://docs.python-requests.org/)

## 📸 Filtros Implementados
O programa aplica os seguintes filtros:
- **Escala de Cinza**
- **Gaussian Blur** (suavização Gaussiana)
- **Média Móvel (Blur)**
- **Mediana**
- **Canny** (detecção de bordas)
- **Sobel** (gradiente)
- **Threshold** (limiarização binária)

## ▶️ Como Executar

Clone o repositório:
```bash
git clone https://github.com/vitor-souza-ime/filtro.git
cd filtro
````

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o programa:

```bash
python main.py
```

## 📊 Exemplo de Saída

O programa abre uma janela com 8 imagens lado a lado:

* Imagem Original
* Escala de Cinza
* Gaussian Blur
* Média Móvel
* Mediana
* Canny
* Sobel
* Threshold

## 📜 Referências

* VAN DER WALT, S. et al. *scikit-image: image processing in Python*. PeerJ 2\:e453, 2014.
* Documentação do [OpenCV](https://docs.opencv.org/).

👉 Quer que eu monte também o arquivo **requirements.txt** correspondente, para já deixar pronto no repositório?
```
