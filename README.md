# HomeTeam AI Assignment

## Project Overview

This project simulates a virtual camera that follows the action in a sports video. It uses basic computer vision techniques to detect motion and track the main area of activity. The result is a cropped video that smoothly follows the game, like a camera operator would.


## How to Run the Project

### Requirements

- Python 3.8+
- OpenCV (`opencv-python`)

Install with:
```
pip install opencv-python
```

### Step-by-step

1. **Extract frames from video**  
   Extracts 5 frames per second and resizes them to 1280x720:

   ```
   python step1_extract_frames.py
   ```

2. **Detect motion**  
   Draws green rectangles where movement is detected:

   ```
   python step2_motion_detection.py
   ```

3. **Track the action with a virtual camera**  
   Draws a blue rectangle that follows the largest motion area and creates a cropped view:

   ```
   python step3_viewport_tracking.py
   ```

4. **Create the final video**  
   Converts the cropped frames into a smooth `.mp4` video:

   ```
   python step4_visualization.py
   ```

---

## My Approach

- I broke the problem into clear steps: extract frames → detect motion → track viewport → create video.
- For motion detection, I used frame differencing and thresholding to find movement.
- I tracked only the largest moving object to keep the viewport focused.
- I applied smoothing to viewport movement to avoid jittery camera behavior.
- The viewport size is fixed (720x480) to simulate a real camera output.

---

## What Was Challenging

- Understanding how `cv2.findContours()` and `cv2.boundingRect()` work in order to find and track motion.
- Step 2 and 3 were the most challenging, especially detecting the correct motion area and keeping the virtual camera centered.
- Avoiding viewport jumps by using smoothing logic.
- Making sure the viewport stays inside the image boundaries to prevent cropping errors.

---

## Possible Improvements

- Track multiple moving objects instead of just the largest one.
- Use optical flow instead of basic frame differencing.
- Add real-time object detection (like ball or player tracking).
- Export side-by-side video: full frame vs. cropped viewport.
- Add audio and display overlays like match score or time.