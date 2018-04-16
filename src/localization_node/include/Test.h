#include <iostream>
//#include <boost/make_shared.hpp>
//#include <boost/thread/mutex.hpp>
#include "opencv2/opencv.hpp"
//#include <X11/Xlib.h>
//#include <boost/thread.hpp>
#include "opencv2/features2d.hpp"
#include "Camera.h"
#include "Detection.h"

#ifndef TEST_CLASS
#define TEST_CLASS

class Test
{
public:
	static std::vector<cv::Mat> testColor(std::vector<cv::Mat>);
};

#endif
