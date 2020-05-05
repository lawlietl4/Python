# -*-coding: utf-8 -*-
import bcrypt

password = bcrypt.checkpw(
    b's3cur3!', b'$2b$18$s2cLYntKn51yCvGNmfqpSucZF60rGV5BCA2d79uXe5CbWCIdTwJmm')

print(password)
