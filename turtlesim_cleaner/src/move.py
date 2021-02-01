#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897
def move():

    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()


    print("this is physically painful")
    speed = 1
    distance = 1




    vel_msg.linear.x = speed

    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    while not rospy.is_shutdown():

        #side1
        dist2=1.2
        t0 = rospy.Time.now().to_sec()
        current_distance = 0


        while(current_distance < dist2):

            velocity_publisher.publish(vel_msg)

            t1=rospy.Time.now().to_sec()

            current_distance= speed*(t1-t0)

        vel_msg.linear.x = 0

        velocity_publisher.publish(vel_msg)




        #side2
        vel_msg.linear.x=1.545085/5
        vel_msg.linear.y=4.755283/5

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < distance):

            velocity_publisher.publish(vel_msg)

            t1=rospy.Time.now().to_sec()

            current_distance= speed*(t1-t0)

        vel_msg.linear.y = 0

        velocity_publisher.publish(vel_msg)




        #side3
        vel_msg.linear.x= -4.045085/5
        vel_msg.linear.y= 2.93892626/5

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < distance):

            velocity_publisher.publish(vel_msg)

            t1=rospy.Time.now().to_sec()

            current_distance= speed*(t1-t0)

        vel_msg.linear.y = 0

        velocity_publisher.publish(vel_msg)




        #side4
        vel_msg.linear.x= -4.045085/5
        vel_msg.linear.y= -2.93892626/5

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < distance):

            velocity_publisher.publish(vel_msg)

            t1=rospy.Time.now().to_sec()

            current_distance= speed*(t1-t0)

        vel_msg.linear.y = 0

        velocity_publisher.publish(vel_msg)





        #side5
        vel_msg.linear.x= 1.545085/5
        vel_msg.linear.y= -4.755283/5

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while(current_distance < distance):

            velocity_publisher.publish(vel_msg)

            t1=rospy.Time.now().to_sec()

            current_distance= speed*(t1-t0)

        vel_msg.linear.y = 0
        vel_msg.linear.x=0

        velocity_publisher.publish(vel_msg)

    vel_msg.linear.x=0
    vel_msg.linear.y=0    

    velocity_publisher.publish(vel_msg)




if __name__ == '__main__':
    try:
        
        move()
        vel_msg.linear.y = 0
        vel_msg.linear.x=0

        velocity_publisher.publish(vel_msg)

    except rospy.ROSInterruptException: pass
