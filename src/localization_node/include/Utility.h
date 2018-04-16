#include <iostream>
#include "opencv2/opencv.hpp"
#include "opencv2/features2d.hpp"
#include "Camera.h"

#ifndef UTILITY_CLASS
#define UTILITY_CLASS

class Utility{
private:

public:
	static std::vector<cv::Mat> toHSV(std::vector<cv::Mat>, std::vector<cv::Mat>);
	static std::vector<cv::Mat> combineFilters(std::vector<cv::Mat>, std::vector<cv::Mat>, std::vector<cv::Mat>, std::vector<cv::Mat>);
};

#endif
