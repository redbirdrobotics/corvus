#include "Camera.h"
#include "Detection.h"
#include "Test.h"
using namespace std;
using namespace cv;
 //INITIALIZE  For Sliders
int key=1;
const int SV_MAX = 255;
const int H_MAX = 180;
int aLowH{0}, aLowS{0}, aLowV{0}, aHighH{180}, aHighS{255}, aHighV{255};
int aLow_H{0}, aLow_S{0}, aLow_V{0}, aHigh_H{0}, aHigh_S{0}, aHigh_V{0};

char aLowHName[50] = "aLowH";
char aLowSName[50] = "aLowS";
char aLowVName[50] = "aLowV";
char aHighHName[50] = "aHighH";
char aHighSName[50] = "aHighS";
char aHighVName[50] = "aHighV";
std::vector<cv::Mat> Test::testColor(std::vector<cv::Mat> frameList)
{
	cv::namedWindow("Test colors");
	sprintf( aLowHName, "aLowH x %d", H_MAX );
	sprintf( aLowSName, "aLowS x %d", SV_MAX );
	sprintf( aLowVName, "aLowV x %d", SV_MAX );
	sprintf( aHighHName, "aHighH x %d", H_MAX );
	sprintf( aHighSName, "aHighS x %d", SV_MAX );
	sprintf( aHighVName, "aHighV x %d", SV_MAX );
	// A lows
	cv::createTrackbar( aLowHName, "Test colors", &aLowH, H_MAX, nullptr );
	cv::createTrackbar( aLowSName, "Test colors", &aLowS, SV_MAX, nullptr );
	cv::createTrackbar( aLowVName, "Test colors", &aLowV, SV_MAX, nullptr );
	// A highs
	cv::createTrackbar( aHighHName, "Test colors", &aHighH, H_MAX, nullptr );
	cv::createTrackbar( aHighSName, "Test colors", &aHighS, SV_MAX, nullptr );
	cv::createTrackbar( aHighVName, "Test colors", &aHighV, SV_MAX, nullptr );
	std::vector<cv::Mat> hsvFrameList(frameList.size());
	std::vector<cv::Mat> colorImage(frameList.size());
	while(key!=32)
	{
		aLow_H=cv::getTrackbarPos(aLowHName, "Test colors");
		aLow_S=cv::getTrackbarPos(aLowSName, "Test colors");
		aLow_V=cv::getTrackbarPos(aLowVName, "Test colors");
		aHigh_H=cv::getTrackbarPos(aHighHName, "Test colors");
		aHigh_S=cv::getTrackbarPos(aHighSName, "Test colors");
		aHigh_V=cv::getTrackbarPos(aHighVName, "Test colors");
		for(int i=0; i<frameList.size();i++)
		{
			// Convert to HSV
			cv::cvtColor(frameList[i], hsvFrameList[i], cv::COLOR_BGR2HSV);

			// Mask
			cv::inRange(hsvFrameList[i], cv::Scalar(aLow_H, aLow_S, aLow_V), cv::Scalar(aHigh_H, aHigh_S, aHigh_V), colorImage[i]);
			//cv::inRange(hsvFrameList[i], cv::Scalar(160, 100, 100), cv::Scalar(179, 255, 255), upperRedHueRange[i]);

			// Combine the above two images
			//cv::addWeighted(lowerRedHueRange[i], 1.0, upperRedHueRange[i], 1.0, 0.0, redHueImage[i]);
			// Blur Image
			//cv::GaussianBlur(colorImage[i], colorImage[i], cv::Size(9, 9), 2, 2);

		}
		key = waitKey(30);
		return colorImage;
	}

}
