import cv2
import matplotlib.pyplot as plt


def analyze_image(image_path):
    original_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if original_img is None:
        print(f"Erro ao carregar a imagem: {image_path}")
        return

    contrast = 1.5
    brightness = 30
    adjusted_img = cv2.convertScaleAbs(original_img, alpha=contrast, beta=brightness)

    equalized_img = cv2.equalizeHist(original_img)

    original_hist = cv2.calcHist([original_img], [0], None, [256], [0, 256])
    adjusted_hist = cv2.calcHist([adjusted_img], [0], None, [256], [0, 256])
    equalized_hist = cv2.calcHist([equalized_img], [0], None, [256], [0, 256])

    print(f"\n--- Análise da Imagem: {image_path} ---")

    plt.figure(figsize=(15, 10))

    plt.suptitle(f"Análise de Aprimoramento - {image_path}", fontsize=16)

    plt.subplot(3, 2, 1)
    plt.imshow(original_img, cmap="gray")
    plt.title("Imagem Original")
    plt.axis("off")

    plt.subplot(3, 2, 2)
    plt.plot(original_hist)
    plt.title("Histograma Original")
    plt.xlabel("Intensidade de Pixel")
    plt.ylabel("Quantidade de Pixels")
    plt.xlim([0, 256])

    plt.subplot(3, 2, 3)
    plt.imshow(adjusted_img, cmap="gray")
    plt.title(f"Brilho/Contraste (α={contrast}, β={brightness})")
    plt.axis("off")

    plt.subplot(3, 2, 4)
    plt.plot(adjusted_hist)
    plt.title("Histograma Pós-Ajuste M/C")
    plt.xlabel("Intensidade de Pixel")
    plt.ylabel("Quantidade de Pixels")
    plt.xlim([0, 256])

    plt.subplot(3, 2, 5)
    plt.imshow(equalized_img, cmap="gray")
    plt.title("Imagem Equalizada")
    plt.axis("off")

    plt.subplot(3, 2, 6)
    plt.plot(equalized_hist)
    plt.title("Histograma Equalizado")
    plt.xlabel("Intensidade de Pixel")
    plt.ylabel("Quantidade de Pixels")
    plt.xlim([0, 256])

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


if __name__ == "__main__":
    image_path_1 = "imagem_baixo_contraste.jpg"
    image_path_2 = "imagem_bem_exposta.jpg"

    print("Iniciando análise. Certifique-se de que as imagens existam no diretório.")

    try:
        analyze_image(image_path_1)
        analyze_image(image_path_2)
    except Exception as e:
        print(
            f"\nERRO: Não foi possível processar as imagens. Verifique os nomes e caminhos."
        )
        print(
            "Crie os arquivos 'imagem_baixo_contraste.jpg' e 'imagem_bem_exposta.jpg' ou altere os nomes no código."
        )
