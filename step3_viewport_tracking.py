import cv2
import os


def track_viewport():
    # Folder with frames that include motion rectangles
    input_dir = "motion"
    frame_files = os.listdir(input_dir)
    frame_files.sort()  # Ensure correct order

    # Create folders to save results
    viewport_drawn_dir = "viewport_drawn"
    viewport_cropped_dir = "viewport_cropped"

    os.makedirs(viewport_drawn_dir, exist_ok=True)
    os.makedirs(viewport_cropped_dir, exist_ok=True)

    # Set fixed viewport size
    viewport_width = 720
    viewport_height = 480

    # Set initial position (center of image 1280x720)
    last_x = 640  # Half of 1280
    last_y = 360  # Half of 720

    for i in range(len(frame_files)):
        filename = frame_files[i]
        path = os.path.join(input_dir, filename)
        frame = cv2.imread(path)

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect bright areas
        threshold_value = 200
        max_value = 255
        return_value, threshold = cv2.threshold(gray, threshold_value, max_value, cv2.THRESH_BINARY)

        # Find contours in bright areas
        contours_result = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours_result[0]  # We only need the list of contours

        # Calculate the center of the biggest motion area
        biggest_area = 0
        center_x = last_x
        center_y = last_y

        for contour in contours:
            # Calculate the area of this contour
            area = cv2.contourArea(contour)
            if area > biggest_area:
                biggest_area = area
                # Get the bounding rectangle around this contour
                # The position and size of the motion zone
                x, y, w, h = cv2.boundingRect(contour)
                # Calculate the center point of this rectangle
                center_x = x + w // 2
                center_y = y + h // 2

        # Smooth the viewport movement
        smooth_factor = 0.2
        last_x = int((1 - smooth_factor) * last_x + smooth_factor * center_x)
        last_y = int((1 - smooth_factor) * last_y + smooth_factor * center_y)

        # Calculate viewport top-left corner
        x1 = max(0, last_x - viewport_width // 2)
        y1 = max(0, last_y - viewport_height // 2)

        # Keep viewport inside image boundaries
        x1 = min(x1, frame.shape[1] - viewport_width)
        y1 = min(y1, frame.shape[0] - viewport_height)

        x2 = x1 + viewport_width
        y2 = y1 + viewport_height

        # Draw viewport rectangle (blue)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)

        # Crop the area inside the viewport
        cropped = frame[y1:y2, x1:x2]

        # Save both versions
        drawn_path = os.path.join(viewport_drawn_dir, f"viewport_{i:04}.jpg")
        cropped_path = os.path.join(viewport_cropped_dir, f"viewport_crop_{i:04}.jpg")

        cv2.imwrite(drawn_path, frame)
        cv2.imwrite(cropped_path, cropped)


if __name__ == "__main__":
    track_viewport()
