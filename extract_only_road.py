import mss
import numpy as np
import cv2
import pytesseract

def order_points(pts):
    """Return pts in order: top-left, top-right, bottom-right, bottom-left."""
    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]
    return rect

def four_point_transform(image, pts):
    """Perform perspective transform of image by mapping pts→rectangle."""
    rect = order_points(pts)
    (tl, tr, br, bl) = rect

    # Compute widths and heights of the new image
    widthA  = np.linalg.norm(br - bl)
    widthB  = np.linalg.norm(tr - tl)
    maxWidth  = int(max(widthA, widthB))

    heightA = np.linalg.norm(tr - br)
    heightB = np.linalg.norm(tl - bl)
    maxHeight = int(max(heightA, heightB))

    # Destination points for "birds-eye view"
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]
    ], dtype="float32")

    # Compute the perspective transform matrix and apply it
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    return warped

def main():
    # ←––– Your trapezoid screen coords
    trapezoid_screen_coords = [
        (1358, 809),   # top-left
        (1429, 809),   # top-right
        (1636, 1105),  # bottom-right
        (1147, 1105)   # bottom-left
    ]

    # 1) Compute the bounding box to capture with mss
    xs = [x for (x, y) in trapezoid_screen_coords]
    ys = [y for (x, y) in trapezoid_screen_coords]
    left, top    = min(xs), min(ys)
    right, bottom = max(xs), max(ys)
    width, height = right - left, bottom - top

    # 2) Grab that rectangle from the screen
    with mss.mss() as sct:
        monitor = {"left": left, "top": top, "width": width, "height": height}
        sct_img = sct.grab(monitor)
        img = np.array(sct_img)[:, :, :3]  # drop alpha

    # 3) Convert absolute screen pts to coords relative to `img`
    src_pts = np.array([
        (x - left, y - top)
        for (x, y) in trapezoid_screen_coords
    ], dtype="float32")

    # 4) Warp trapezoid → rectangle
    rectified = four_point_transform(img, src_pts)

    # 5) Preprocess for OCR
    gray = cv2.cvtColor(rectified, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]
    # enlarge for better OCR
    gray = cv2.resize(gray, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    # 6) OCR!
    text = pytesseract.image_to_string(gray)
    print("Extracted Text:\n", text)

    # Optional: save images for inspection
    cv2.imwrite("1_captured_raw.png", img)
    cv2.imwrite("2_rectified.png", rectified)
    cv2.imwrite("3_for_ocr.png", gray)

if __name__ == "__main__":
    main()

