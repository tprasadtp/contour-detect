## Contor detection and recognition of hand gestures (static gestures)
Uses open cv python bindings to extract the image, perform contour detection using hsv kin segmentation to separate skin, then eliminate errors in detection and perform automated key events using keyboard emulation using xdotool package. Requires opencv 2.4 or above.
`bgfilter.py` uses cv bindings (BackgroundSubtractorMOG) to remove the background from reference.
