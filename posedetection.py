import cv2 
import numpy as np
import matplotlib.pyplot as plt

protoFile = "pose_deploy_linevec_faster_4_stages.prototxt"
weightsFile = "pose_iter_160000.caffemodel"

nPoints = 15
POSE_PAIRS = [[0, 1],[1, 2],[2, 3],[3, 4],[1, 5],[5, 6],[6, 7],
    [1, 14],[14, 8],[8, 9],[9, 10],[14, 11],[11, 12],[12, 13],
]

net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

im = cv2.imread("Milton_Golf_Swing.png")

inWidth  = im.shape[1]
inHeight = im.shape[0]

#covert image to blob
netInputSize = (368, 368)
inpBlob = cv2.dnn.blobFromImage(im, 1.0 / 255, netInputSize, (0, 0, 0), swapRB=True, crop=False)
net.setInput(inpBlob)

#run inference
# Forward Pass
output = net.forward()

#extract points from heatmaps
# X and Y Scale
scaleX = inWidth  / output.shape[3]
scaleY = inHeight / output.shape[2]

# Empty list to store the detected keypoints
points = []

# Treshold
threshold = 0.1

for i in range(nPoints):
    # Obtain probability map
    probMap = output[0, i, :, :]

    # Find global maxima of the probMap.
    minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

    # Scale the point to fit on the original image
    x = scaleX * point[0]
    y = scaleY * point[1]

    if prob > threshold:
        # Add the point to the list if the probability is greater than the threshold
        points.append((int(x), int(y)))
    else:
        points.append(None)

#displaing the keypoints and skeleton
imPoints = im.copy()
imSkeleton = im.copy()

# Draw points
for i, p in enumerate(points):
    cv2.circle(imPoints, p, 8, (255, 255, 0), thickness=-1, lineType=cv2.FILLED)
    cv2.putText(imPoints, "{}".format(i), p, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, lineType=cv2.LINE_AA)

# Draw skeleton
for pair in POSE_PAIRS:
    partA = pair[0]
    partB = pair[1]

    if points[partA] and points[partB]:
        cv2.line(imSkeleton, points[partA], points[partB], (255, 255, 0), 2)
        cv2.circle(imSkeleton, points[partA], 8, (255, 0, 0), thickness=-1, lineType=cv2.FILLED)

cv2.namedWindow("skeleton", cv2.WINDOW_NORMAL)
cv2.imshow("skeleton",imSkeleton)
cv2.waitKey(0)