#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
from ultralytics import YOLO  #for yolov8+ models
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

class YoloConeDetector:
    def __init__(self):
        # ROS parameters
        self.weights_path = rospy.get_param('~weights_path', 'weights/aambest.pt')
        self.camera_topic = rospy.get_param('~camera_topic', '/camera/rgb/image_raw')
        self.conf_threshold = rospy.get_param('~conf_threshold', 0.5)

        rospy.loginfo("Loading YOLO model from: " + self.weights_path)
        self.model = YOLO(self.weights_path)

        # CV Bridge for converting ROS images to OpenCV images and back
        self.bridge = CvBridge()

        # sub to the camera feed
        self.image_sub = rospy.Subscriber(self.camera_topic, Image, self.image_callback, queue_size=1)

        # pub annotated image
        self.image_pub = rospy.Publisher("/yolov10_cone_detection/image_out", Image, queue_size=1)

        rospy.loginfo("YoloConeDetector initialized with weights: {}, camera_topic: {}, conf_threshold: {}".format(self.weights_path, self.camera_topic, self.conf_threshold))

    def image_callback(self, img_msg):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(img_msg, desired_encoding="bgr8")
        except Exception as e:
            rospy.logerr("CV Bridge error: {}".format(e))
            return

        # YOLOv10 inference
        results = self.model.predict(cv_image, conf=self.conf_threshold)
        if results:
            boxes = results[0].boxes
            if boxes is not None and boxes.xyxy.shape[0] > 0:
                boxes_np = boxes.xyxy.cpu().numpy()  # shape: (N, 4)
                confs = boxes.conf.cpu().numpy()       # shape: (N,)
                classes = boxes.cls.cpu().numpy().astype(int)  # shape: (N,)
                for (x1, y1, x2, y2), conf, cls in zip(boxes_np, confs, classes):
                    class_name = self.model.names.get(cls, f"cls_{cls}")
                    cv2.rectangle(cv_image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                    label = f"{class_name} {conf:.2f}"
                    cv2.putText(cv_image, label, (int(x1), int(y1)-5),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        try:
            out_msg = self.bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
            self.image_pub.publish(out_msg)
        except Exception as e:
            rospy.logerr("Error publishing image: {}".format(e))

def main():
    rospy.init_node('yolo_cone_detection_node', anonymous=True)
    detector = YoloConeDetector()
    rospy.spin()

if __name__ == "__main__":
    main()
