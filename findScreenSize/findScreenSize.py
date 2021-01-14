def find_screen_height(width, ratio):
      W, H = ratio.split(':')
      height = int(width * (int(H) / int(W)))
      return f'{width}x{height}'


def find_screen_height_v3(width, ratio):
    a, b = map(lambda x: int(x), ratio.split(':'))
    return f'{width}x{width * b // a}'

print(find_screen_height_v3(1024, "4:3"), "1024x768")
print(find_screen_height_v3(1280, "16:9"), "1280x720")
print(find_screen_height_v3(3840, "32:9"), "3840x1080")


def find_screen_height_v2(width, ratio):
    a, b = map(int, ratio.split(":"))
    return f"{width}x{int(width / a * b)}"

