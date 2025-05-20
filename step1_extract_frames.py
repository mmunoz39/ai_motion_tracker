import cv2
import os


def extract_frames():
    # Path to the input video
    video_path = "sample_video_clip.mp4"

    # Create a folder to save extracted frames
    output_dir = "frames"
    os.makedirs(output_dir, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video was opened successfully
    if not cap.isOpened():
        print("Error: Could not open the video.")
        exit()

    # Set the number of frames per second to extract
    fps = 5
    # Get the original FPS of the video
    original_fps = cap.get(cv2.CAP_PROP_FPS)
    # Calculate how many frames to skip between each saved frame
    frame_interval = int(original_fps / fps)

    frame_count = 0       # Counter for total frames
    saved_count = 0       # Counter for saved frames

    while True:
        # Read the next frame
        ret, frame = cap.read()
        if not ret:
            break

        # Save every frame based on frame_interval
        if frame_count % frame_interval == 0:
            # Resize the frame to HD Standard
            resized_frame = cv2.resize(frame, (1280, 720))
            # Build the file name and path
            filename = os.path.join(output_dir, f"frame_{saved_count:04}.jpg")
            # Save the image
            cv2.imwrite(filename, resized_frame)
            saved_count += 1

        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Saved {saved_count} frames in the '{output_dir}' folder.")


if __name__ == "__main__":
    extract_frames()
