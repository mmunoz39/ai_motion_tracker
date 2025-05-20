import cv2
import os


def detect_motion():
    # Folder where the extracted frames are saved
    frame_dir = "frames"
    frame_files = os.listdir(frame_dir)
    frame_files.sort()  # Sort the files to process them in the correct order

    # Create a folder to save the motion detection results
    motion_dir = "motion"
    if not os.path.exists(motion_dir):
        os.makedirs(motion_dir)

    previous_gray = None  # This will store the previous frame in grayscale
    frame_number = 0       # Counter to keep track of current frame

    for filename in frame_files:
        # Build the full path to the image file
        frame_path = os.path.join(frame_dir, filename)

        # Read the image from disk
        frame = cv2.imread(frame_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # If this is not the first frame, compare with the previous one
        if previous_gray is not None:
            # Calculate the difference between current and previous frame
            difference = cv2.absdiff(gray, previous_gray)

            # Use threshold to highlight strong differences
            threshold_value = 25
            max_value = 255
            return_value, thresholded = cv2.threshold(difference, threshold_value, max_value, cv2.THRESH_BINARY)

            # Make white areas (motion) larger using dilation
            dilated = cv2.dilate(thresholded, None, iterations=2)

            # Find contours (edges) of moving areas
            contours_result = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            contours = contours_result[0]  # The list of contours is the first item

            # Draw a green rectangle for each big enough motion area
            for contour in contours:
                area = cv2.contourArea(contour)
                if area < 250:
                    continue  # Ignore small areas
                x, y, width, height = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

        # Save the result frame (with rectangles) in the motion folder
        output_filename = f"motion_{frame_number:04}.jpg"
        output_path = os.path.join(motion_dir, output_filename)
        cv2.imwrite(output_path, frame)

        # Update the previous_gray for the next loop
        previous_gray = gray
        frame_number += 1


if __name__ == "__main__":
    detect_motion()



