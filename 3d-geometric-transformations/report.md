## Relatório do Funcionamento das Manipulações Geométricas

A estrutura do código implementado para as transformações geométricas 3D unifica a lógica em uma classe principal, Cube3D. Esta classe gerencia tanto a renderização da janela quanto as transformações do objeto.

### Classes

#### Gerenciador do Objeto 3D (Cubo)

Esta parte da lógica é responsável por definir a geometria do objeto e aplicar as transformações de escala, rotação e translação.

No código, a geometria do cubo é definida por um conjunto de vértices (pontos no espaço 3D) e arestas (as linhas que conectam esses pontos). Em vez de posições X e Y, cada vértice possui coordenadas (x, y, z). Para facilitar os cálculos matemáticos, utilizamos coordenadas homogêneas (x, y, z, w), o que nos permite usar uma única matriz para representar todas as transformações.

A classe armazena variáveis para os parâmetros de transformação atuais:

- self.scale: Um valor numérico para a escala do objeto.

- self.angle_x, self.angle_y, self.angle_z: Os ângulos de rotação em torno de cada um dos três eixos.

- self.pos_x, self.pos_y: A posição (translação) do objeto no plano 2D da tela.

A função principal desta lógica é calcular a posição final de cada vértice após as transformações. Isso é feito através da criação e multiplicação de matrizes de transformação 4x4. Para cada tipo de manipulação (escala, rotação em X, Y, Z e translação), uma matriz específica é gerada. Elas são então combinadas em uma única matriz de transformação final, que é aplicada a todos os vértices do cubo, resultando em seus novos pontos no espaço 3D.

#### Janela Interativa e de Renderização

Esta área de responsabilidade gerencia a exibição da superfície (a janela do Pygame), o desenho dos elementos na tela e o controle das interações do usuário.

A maior parte do código aqui lida com configurações padrões do Pygame: criar a janela, preencher a cor de fundo e controlar a taxa de quadros por segundo (FPS). Além disso, é responsável por desenhar elementos fixos, como o texto do tutorial de controles.

A parte mais relevante desta lógica é o controle do objeto que está sendo manipulado. A implementação atual simplifica este conceito, pois gerencia um único objeto (o cubo). Dessa forma, não há um array de objetos ou um índice para alternar entre eles. O loop de eventos (handle_events) captura as teclas pressionadas pelo usuário e altera diretamente as variáveis de transformação (escala, rotação, posição) do único cubo existente.

Após os eventos serem processados, a rotina de desenho (draw) projeta os pontos 3D transformados do cubo em um plano 2D para que possam ser exibidos na tela, desenhando as linhas e os círculos que compõem a representação visual do objeto.
