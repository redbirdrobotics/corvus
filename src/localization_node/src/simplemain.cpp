#include <iostream>
#include "opencv2/opencv.hpp"
#include "Camera.h"
#include "Detection.h"
#include "Test.h"
#include "Utility.h"
using namespace cv;
using namespace std;
int main()
{
	try{
	//*** INITIALIZE CAMERA INSTANCES ***//
	Camera Cam0("Augustus", 0);
	// Camera Cam1("Tiberius", 1);
	//std::vector< Camera > CamList = {Cam0, Cam1, Cam2, Cam3, Cam4, Cam5, Cam6, Cam7, Cam8, Cam9};
	std::vector< Camera > CamList = {Cam0};

	//*** INITIALIZE VARIABLES ***//
	bool connected;
	//color vectors
	//  Note: Make CONST on final version
	std::vector<int> RED1 = {0, 100, 100, 7, 255, 255};
	std::vector<int> RED2 = {160, 100, 100, 180, 255, 255};
	std::vector<int> GREEN = {40, 70, 50, 80, 255, 255};
	std::vector<int> WHITE = {0, 0, 215, 255, 155, 255};
	std::vector<int> BLACK = {0, 0, 0, 255, 155, 40};
	//frame lists
	std::vector< cv::Mat> frameList;
	std::vector< cv::Mat> blobList, hsvFrameList;
	//*** CHECK CONNECTION TO CAMERAS ***//

	//***            TEST             ***//
	// cv::VideoCapture capture("/home/ghost/Videos/Webcam/red_plate_test_vid.mp4");
  //
  // int totalFrameNumber = capture.get(CV_CAP_PROP_FRAME_COUNT);
  //
  // cv::Mat currentFrame;
  //
  // for(int i=0; i < totalFrameNumber; i++)
  // {
  //    capture>>currentFrame;
  //    frameList.push_back(currentFrame.clone());
	// }

	connected = Camera::getListStatus(CamList, CamList.size());
	if(!connected)
	{
		std::cout<<"connection error"<<std::endl;
		return -1;
	}

	while(connected)
	{
		connected = Camera::getListStatus(CamList, CamList.size());
		frameList = Camera::updateFrameList(frameList, CamList, CamList.size());
		cout<<__LINE__<<endl;
		hsvFrameList = Utility::toHSV(frameList, hsvFrameList);
		blobList = Detection::findColors(hsvFrameList, GREEN, blobList);
		//testList=Test::testColor(frameList);
		Camera::showFrame(CamList, blobList, connected);
		//Camera::showFrame(CamList," - test Detection", testList, connected);
	}}
	catch(const std::exception& e){
		std::cerr<< e.what() << std::endl;
		return -1;
	}
}
