import ascii_magic
output = ascii_magic.from_image_file("nn.jpg", columns=110,char="x")
ascii_magic.to_terminal(output)