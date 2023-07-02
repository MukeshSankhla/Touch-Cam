import RPi.GPIO as GPIO
import time
from picamera import PiCamera

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 21 as input
GPIO.setup(21, GPIO.IN)

# Create an instance of the PiCamera
camera = PiCamera()

def capture_picture():
    # Get the current timestamp for the picture filename
    timestamp = time.strftime("%Y%m%d%H%M%S")
    image_filename = f"picture_{timestamp}.jpg"
    
    # Capture the picture
    camera.capture(image_filename)
    print(f"Picture captured: {image_filename}")

try:
    # Start the camera preview
    camera.start_preview()

    while True:
        # Check if GPIO pin 21 is high
        if GPIO.input(21) == GPIO.HIGH:
            # Call the capture_picture function
            capture_picture()

        # Add a small delay to avoid excessive checking
        time.sleep(0.1)

except KeyboardInterrupt:
    # Stop the camera preview
    camera.stop_preview()

    # Clean up GPIO on program exit
    GPIO.cleanup()
