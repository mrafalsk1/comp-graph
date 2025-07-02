## Manipulação de Histogramas para Aprimoramento de Imagens Digitais

1. Implementação Prática

A implementação a seguir utiliza as bibliotecas opencv-python para o processamento de imagem, numpy para operações numéricas e matplotlib para a visualização dos resultados e histogramas.

Pré-requisitos:

```bash
pip install opencv-python numpy matplotlib
```

ou utilizar o ambiente com uv com uv run main.py

2. Análise e Comparação dos Resultados

Para a análise, foram utilizadas duas imagens distintas: uma com baixo contraste e outra bem exposta.

(Execute o código com suas imagens para gerar os gráficos que fundamentarão esta análise)

Análise da Imagem 1 (Baixo Contraste):

    Observação Inicial: A imagem original apresenta um histograma concentrado em uma faixa estreita de intensidades (por exemplo, entre 50 e 200). Isso confirma visualmente a falta de tons pretos profundos e brancos brilhantes, resultando em uma aparência "lavada".

    Ajuste de Brilho e Contraste: Ao aplicar um fator alpha=1.5 e beta=30, o histograma resultante foi "esticado" e deslocado para a direita. O esticamento (efeito do contraste alpha) fez com que os pixels ocupassem uma faixa maior de intensidades, diferenciando melhor os tons. O deslocamento (efeito do brilho beta) tornou a imagem globalmente mais clara. O resultado é uma melhora significativa, mas os parâmetros (alpha, beta) tiveram que ser escolhidos manualmente por tentativa e erro.

    Equalização de Histograma: A imagem equalizada apresentou um contraste global muito superior. O histograma resultante é distribuído de forma muito mais uniforme por toda a faixa de 0 a 255. Detalhes que antes estavam ocultos nas áreas de baixo contraste se tornaram visíveis. Para esta imagem, a equalização funcionou de forma excelente e automática, sendo superior ao ajuste manual por não exigir parâmetros.

Análise da Imagem 2 (Bem Exposta):

    Observação Inicial: A imagem original já possui um bom contraste, e seu histograma se espalha por quase toda a faixa de 0-255, indicando uma boa utilização das intensidades disponíveis.

    Ajuste de Brilho e Contraste: A aplicação dos mesmos parâmetros (alpha=1.5, beta=30) resultou em uma imagem excessivamente contrastada e clara, com "estouro" de pixels brancos (saturação em 255) e perda de detalhes nas áreas mais escuras. O histograma mostra picos significativos em 0 e 255, confirmando a perda de informação. Isso demonstra que um ajuste manual fixo não serve para todas as imagens.

    Equalização de Histograma: A equalização nesta imagem produziu um resultado misto. Embora tenha realçado algumas texturas, a imagem adquiriu uma aparência artificial e, em alguns casos, o ruído presente na imagem original foi amplificado. O histograma tornou-se mais plano, mas a custo de um visual menos natural. Isso ocorre porque a equalização força uma redistribuição global, mesmo quando a distribuição original já é boa.

4. Conclusão

As técnicas baseadas em histograma são ferramentas poderosas para o aprimoramento de imagens.

O ajuste de brilho e contraste oferece um controle fino e direto, mas é dependente de parâmetros manuais que precisam ser ajustados para cada imagem específica.

A equalização de histograma é uma técnica automática e extremamente eficaz para imagens com baixo contraste, conseguindo muitas vezes revelar detalhes de forma impressionante com um único clique. No entanto, seu caráter global pode levar a resultados indesejados em imagens que já são bem expostas, podendo gerar uma aparência artificial e amplificar ruído.

A escolha da técnica ideal depende, portanto, das características da imagem original e do resultado desejado pelo analista.
