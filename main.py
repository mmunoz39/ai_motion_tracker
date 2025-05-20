import step1_extract_frames
import step2_motion_detection
import step3_viewport_tracking
import step4_visualization


def main():
    print("Step 1: Extracting frames from video...")
    step1_extract_frames.extract_frames()

    print("Step 2: Detecting motion...")
    step2_motion_detection.detect_motion()

    print("Step 3: Tracking viewport...")
    step3_viewport_tracking.track_viewport()

    print("Step 4: Generating final video...")
    step4_visualization.make_video()

    print("All steps completed. Check 'viewport_video.mp4'")


if __name__ == "__main__":
    main()
