#include <iostream>
#include <vector>
#include "opencv2/opencv.hpp"
#include "opencv2/features2d.hpp"

#ifndef ROBOT_CLASS
#define ROBOT_CLASS

class Robot
{
protected:
	int a_color;
	int a_confidence;
	cv::Point a_coordinates;
	float a_radius;

public:
	Robot(int color);
};

#endif
