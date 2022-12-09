#!/usr/bin/env python

import rospy
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion
from std_msgs.msg import Time, Header

class SetPosePublisher(object):
    def __init__(self):
        rospy.Subscriber("/ual/goal_pose", Pose, self.goal_pose_cb)
        self.pub = rospy.Publisher('/ual/set_pose', PoseStamped, queue_size=10)

    def goal_pose_cb(self,msg):

        goal = PoseStamped()
        goal.header.seq = 1
        goal.header.stamp = rospy.Time.now()
        goal.header.frame_id = "map"
        goal.pose.position.x = msg.position.x
        goal.pose.position.y = msg.position.y
        goal.pose.position.z = msg.position.z
        goal.pose.orientation.x = msg.orientation.x
        goal.pose.orientation.y = msg.orientation.y
        goal.pose.orientation.z = msg.orientation.z
        goal.pose.orientation.w = msg.orientation.w
        
        self.pub.publish(goal)

if __name__ == '__main__':
    rospy.init_node('goal_pose_listener', anonymous=True)

    set_pose = SetPosePublisher()
    rospy.spin()