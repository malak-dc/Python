def main():
    from PIL import Image
    import numpy as np
    def ft_load(path: str):
        img = Image.open(path)
        channels = len(img.getbands())
        print(f'The shape of image is:({img.height},{img.width},{channels})')
        pixels=np.array(img.getdata())
        return pixels
    print(ft_load("landscape.jpg"))
if __name__=="__main__":
    main()