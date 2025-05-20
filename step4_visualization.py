import cv2
import os


def make_video():
    # Folder where the cropped viewport images are saved
    #input_dir = "viewport_cropped"
    input_dir = "viewport_drawn"
    image_files = os.listdir(input_dir)
    image_files.sort()  # Make sure they are in correct order

    # Check if there are images to use
    if len(image_files) == 0:
        print("No images found in", input_dir)
        return

    # Read the first image to get the size
    first_image_path = os.path.join(input_dir, image_files[0])
    frame = cv2.imread(first_image_path)
    height, width, layers = frame.shape

    # Define output video settings
    output_path = "viewport_video.mp4"
    fps = 5  # frames per second

    # Define the video writer object
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec for .mp4
    video_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Add each frame to the video
    for filename in image_files:
        frame_path = os.path.join(input_dir, filename)
        frame = cv2.imread(frame_path)
        video_writer.write(frame)  # Add frame to video

    # Release the writer to finish the file
    video_writer.release()
    print("Video created:", output_path)


if __name__ == "__main__":
    make_video()
