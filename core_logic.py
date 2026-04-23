import cv2
import numpy as np

class Cartoonifier:
    def __init__(self, blur_value: int = 5, edge_block_size: int = 9, color_filter_size: int = 9):
        """
        Initializes the Cartoonifier with default or custom parameters.
        This is perfect for eventually passing dynamic configs.
        """
        self.blur_value = blur_value
        self.edge_block_size = edge_block_size
        self.color_filter_size = color_filter_size

    def _decode_image(self, image_bytes: bytes) -> np.ndarray:
        """Private method: Converts raw network bytes into an OpenCV image array."""
        nparr = np.frombuffer(image_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is None:
            raise ValueError("Invalid image format or corrupted bytes.")
        return img

    def _encode_image(self, img_array: np.ndarray) -> bytes:
        """Private method: Converts an OpenCV image array back into raw network bytes."""
        success, encoded_img = cv2.imencode('.jpg', img_array)
        if not success:
            raise RuntimeError("Failed to encode processed image.")
        return encoded_img.tobytes()

    def process(self, image_bytes: bytes) -> bytes:
        """
        Public method: The main orchestrator for the computer vision pipeline.
        
        """
        # 1. Decode
        img = self._decode_image(image_bytes)

        # 2. Extract Edges
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grey = cv2.medianBlur(grey, self.blur_value)
        edges = cv2.adaptiveThreshold(
            grey, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, self.edge_block_size, 9
        )

        # 3. Flatten Colors
        color = cv2.bilateralFilter(img, self.color_filter_size, 250, 250)

        # 4. Combine
        cartoon = cv2.bitwise_and(color, color, mask=edges)

        # 5. Encode and return
        return self._encode_image(cartoon)