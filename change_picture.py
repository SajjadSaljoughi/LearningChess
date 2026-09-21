import cv2
import os
import numpy as np


image = cv2.imread("images\\Chess_Pieces.png")

os.makedirs("pieces", exist_ok=True)

names = [
    "pawn_white",
    "rook_white",
    "knight_white",
    "bishop_white",
    "queen_white",
    "king_white",

    "pawn_black",
    "rook_black",
    "knight_black",
    "bishop_black",
    "queen_black",
    "king_black"
]


# Size of each piece area in the original image
piece_width = 230
piece_height = 370

x_start = 25
y_start = 75

x_step = 251
y_step = 451


for row in range(2):

    for col in range(6):

        x = x_start + col * x_step
        y = y_start + row * y_step

        crop = image[y:y + piece_height, x:x + piece_width]

        # --------------------------------
        # Create transparency mask
        # --------------------------------

        gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

        # Black pieces
        if row == 1:
            mask = gray < 150

        # White pieces
        else:
            b, g, r = cv2.split(crop)

            # White chess pieces have a warm color
            mask = (r - b > 15) & (r > 120)

        mask = mask.astype(np.uint8) * 255

        # Make edges smoother
        mask = cv2.GaussianBlur(mask, (5, 5), 0)

        # --------------------------------
        # Find the piece
        # --------------------------------

        points = cv2.findNonZero(mask)

        if points is None:
            print("Piece not found:", names[row * 6 + col])
            continue

        x, y, w, h = cv2.boundingRect(points)

        piece = crop[y:y+h, x:x+w]
        mask = mask[y:y+h, x:x+w]

        # --------------------------------
        # Resize piece
        # --------------------------------

        max_size = 58

        scale = min(
            max_size / w,
            max_size / h
        )

        new_width = int(w * scale)
        new_height = int(h * scale)

        piece = cv2.resize(
            piece,
            (new_width, new_height),
            interpolation=cv2.INTER_AREA
        )

        mask = cv2.resize(
            mask,
            (new_width, new_height),
            interpolation=cv2.INTER_AREA
        )

        # --------------------------------
        # Create 64x64 transparent image
        # --------------------------------

        result = np.zeros((64, 64, 4), dtype=np.uint8)

        x = (64 - new_width) // 2
        y = (64 - new_height) // 2

        result[y:y+new_height, x:x+new_width, :3] = piece
        result[y:y+new_height, x:x+new_width, 3] = mask

        # --------------------------------
        # Save
        # --------------------------------

        filename = f"pieces/{names[row * 6 + col]}.png"

        cv2.imwrite(filename, result)

        print("Saved:", filename)


print("Finished!")