def image_histogram(image):
    hist = [0] * 256

    for i in range(len(image)):
        for j in range(len(image[i])):
            pixel = image[i][j]
            hist[pixel] += 1

    return hist