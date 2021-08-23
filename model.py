from torch.nn import Sequential, Module, Conv2d, PReLU, BatchNorm2d, PixelShuffle, Tanh


class Generator(Module):  # generator model
    def __init__(self):
        super().__init__()
        self.first = Sequential(
            Conv2d(3, 64, kernel_size=9, padding=4),
            PReLU()
        )
        self.rb1 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb2 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb3 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb4 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb5 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb6 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb7 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb8 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb9 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb10 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb11 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb12 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb13 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb14 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb15 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.rb16 = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
            PReLU(),
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64)
        )
        self.last = Sequential(
            Conv2d(64, 64, kernel_size=3, padding=1),
            BatchNorm2d(64),
        )
        self.upscale1 = Sequential(
            Conv2d(64, 256, kernel_size=3, padding=1),
            PixelShuffle(2),
            PReLU()
        )
        self.upscale2 = Sequential(
            Conv2d(64, 256, kernel_size=3, padding=1),
            PixelShuffle(2),
            PReLU()
        )
        self.final = Sequential(
            Conv2d(64, 3, kernel_size=9, padding=4),
            Tanh()
        )

    async def forward(self, x):
        x = self.first(x)

        x1 = self.rb1(x)
        x2 = self.rb2(x1 + x)
        x3 = self.rb3(x2 + x1)
        x4 = self.rb4(x3 + x2)
        x5 = self.rb5(x4 + x3)
        x6 = self.rb6(x5 + x4)
        x7 = self.rb7(x6 + x5)
        x8 = self.rb8(x7 + x6)
        x9 = self.rb9(x8 + x7)
        x10 = self.rb10(x9 + x8)
        x11 = self.rb11(x10 + x9)
        x12 = self.rb12(x11 + x10)
        x13 = self.rb13(x12 + x11)
        x14 = self.rb14(x13 + x12)
        x15 = self.rb15(x14 + x13)
        x16 = self.rb15(x15 + x14)

        x17 = self.last(x16 + x15)
        x18 = self.upscale1(x17 + x)
        x19 = self.upscale2(x18)
        x20 = self.final(x19)
        return x20


async def norm(img_tensor):  # from [0;1] to [-1;1]
    return 2 * img_tensor - 1


async def denorm(img_tensor):  # from [-1;1] to [0;1]
    return (img_tensor + 1) / 2
