import rospy
from std_msgs.msg import String

def talker1():
    pub1 = rospy.Publisher('name_w', String, queue_size=10)
    pub2 = rospy.Publisher('id_st', String, queue_size=10)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():
        name = "Myname: Watthanai"
        id_st = "6352500048"

        rospy.loginfo(name)
        rospy.loginfo(id_st)

        pub1.publish(name)
        pub2.publish(id_st)

        rate.sleep()

if __name__ == '__main__':
    try:
        talker1()
    except rospy.ROSInterruptException:
        pass
