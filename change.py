from ppgan.apps import StyleGANv2EditingPredictor
from ppgan.apps import Pixel2Style2PixelPredictor
from ppgan.apps import AnimeGANPredictor
import infer
import os


def gaoshiqing(choice, number):
    if choice == 3:
        predictor = AnimeGANPredictor()
        predictor.run('./output/result.png')
        os.remove("./output/result.png")
        os.rename("./output/anime.png", "./output/result.png")
    elif choice == 4:
        infer.main(input_path='output/result.png',
                   model_path='paint_best.pdparams',
                   output_dir='output/',
                   need_animation=True,
                   resize_h=512,
                   resize_w=512,
                   serial=True)
        os.remove("./output/result.png")
    else:
        predictor1 = Pixel2Style2PixelPredictor(
            output_path="./step",
            weight_path=None,
            model_type="ffhq-inversion",
            seed=233,
            size=1024,
            style_dim=512,
            n_mlp=8,
            channel_multiplier=2)
        predictor1.run("./output/result.png")
        os.remove("./output/result.png")
        os.remove("./step/dst.png")
        os.remove("./step/src.png")
        os.rename("./step/dst.npy", "./step/result.npy")
        n = ""
        nn = 0
        if choice == 0:
            n = "gender"
            nn = number * 5
        elif choice == 1:
            n = "age"
            nn = number * 5
        elif choice == 2:
            n = "smile"
            nn = number * 5
        predictor2 = StyleGANv2EditingPredictor(
            output_path="./output",
            weight_path=None,
            model_type="ffhq-config-f",
            seed=233,
            size=1024,
            style_dim=512,
            n_mlp=8,
            channel_multiplier=2,
            direction_path=None)
        predictor2.run("./step/result.npy", n, nn)
        os.remove("./step/result.npy")
        os.remove("./output/dst.editing.npy")
        os.remove("./output/src.editing.png")
        os.rename("./output/dst.editing.png", "./output/result.png")
