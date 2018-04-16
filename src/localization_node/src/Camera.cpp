#include "Camera.h"

Camera::Camera(std::string name,uint32_t port) : a_connect(false), a_ID(name)
{
	a_stream.open(port);
	if(a_stream.isOpened())
	{
		std::cout<< a_ID << " Connected" <<std::endl;
		a_connect = true;
	}
}

bool Camera::getStatus() {return a_connect;}

std::string Camera::getID() {return a_ID;}

// boost::shared_ptr< cv::Mat > Camera::getFrame(boost::shared_ptr< cv::Mat > frame)
// {
// 	a_stream.read(*frame);
// 	if(frame->empty())
// 	{
// 		std::cout<<"empty frame"<<std::endl;
// 	}
// 	return frame;
// }

cv::Mat Camera::getFrame(cv::Mat frame, bool add)
{
	a_stream.read(frame);
	if(frame.empty())
	{
		std::cout<<"empty frame"<<std::endl;
	}
	if(add == true)
	{
		a_frameList.push_back(frame);
	}
	return frame;
}

// cv::Mat Camera::getFrame(cv::Mat frame, std::vector< cv::Mat >* imgList)
// {
// 	a_stream.read(frame);
// 	if(frame.empty())
// 	{
// 		std::cout<<"empty frame"<<std::endl;
// 	}
// 	else
// 	{
// 		imgList->push_back(frame);
// 	}
// 	return frame;
//}

//cv::Mat Camera::getFrame(cv::Mat)

bool Camera::getListStatus(std::vector< Camera* > CamList, int size)
{
	bool totalConnect = true;
	for(int i=0; i<size; i++)
	{
		if(!CamList[i]->getStatus())
		{
			std::cout<<"Camera "<<i<<" is not connected"<<std::endl;
			totalConnect = false;
		}
	}
	return totalConnect;
}

void Camera::updateFrameList(boost::shared_ptr< std::vector< cv::Mat > > frameList, std::vector< Camera* > CamList, int size, boost::mutex& MUTEX)
{
	//std::unique_ptr<> std::make_unique<>()
	//boost::lock_guard<boost::mutex> guard(MUTEX);
	//std::cout<<"Grabbing "<<size<<" Frames"<<std::endl;

	if(frameList->empty())
	{
		//Creates 1 extra empty matrix for use later when computing disparity
		for(int i=0; i<(size+1); i++)
		{
			cv::Mat* pMat = new cv::Mat;
			frameList->push_back(*pMat);
		}
	}

	for(int i=0; i<size; i++)
	{
		//MUTEX.lock();

		(*frameList)[i]=CamList[i]->getFrame((*frameList)[i]);

		//MUTEX.unlock();
	}
}

void Camera::updateFrameList(boost::shared_ptr< std::vector< std::vector< cv::Mat > > > frameList, std::vector< Camera* > CamList, int size, boost::mutex& MUTEX)
{

	if(frameList->empty())
	{
		std::cout<<"Creating 2 Containers for "<<size<<" Frames"<<std::endl;
		std::vector<cv::Mat> row1, row2;
		(*frameList).push_back(row1);
		(*frameList).push_back(row2);
	}

	for(int i=0; i<2; i++)
	{
		cv::Mat* pMat = new cv::Mat;

		//MUTEX.lock();

		(*frameList)[i].push_back(CamList[i]->getFrame(*pMat));

		//MUTEX.unlock();
	}

	// cv::Mat frame1, frame2;
	// (*frameList)[0].push_back(CamList[0]->getFrame(frame1));
	// (*frameList)[1].push_back(CamList[1]->getFrame(frame2));

	std::printf( "%d Pictures Captured! \n", (int)((*frameList)[0].size()) );
}

//void Camera::getFrame()[]

/*void Camera::showFrame(std::string window, boost::shared_ptr< std::vector< cv::Mat > > frameList, boost::shared_ptr< bool > connected, boost::mutex& MUTEX)
{
	int size = frameList->size();
	while(*connected == true)
	{
		for(int i=0; i<size; i++)
		{
			if(! (*frameList)[i].empty() )
			{
				cv::imshow(window+std::to_string(i), (*frameList)[i]);
			}
		}
		if(cv::waitKey(30) >= 0)
		{
			*connected = false;
			//cv::destroyWindow(window);
			return;
		}		
	}
}*/

void Camera::showFrame(boost::shared_ptr< std::vector< cv::Mat > > frameList, boost::shared_ptr< bool > connected, boost::shared_ptr< bool > capture, boost::mutex& MUTEX)
{
	//boost::lock_guard<boost::mutex> guard(MUTEX);
	int key;
	bool toggle = true;

	while(*connected == true)
	{
		key = cv::waitKey(30);
		if(key == 27)
		{
			*connected = false;
			return;
		}

		else if(key == 32)
		{
			*capture = true;
		}

		if(key == 116)
		{
			toggle = !toggle;
			if(toggle == false)
			{
				cv::destroyAllWindows();
			}
		}

	// 	//MUTEX.lock();
	 	if(toggle == true)
		{
	// 		int size = frameList->size();

	 		if(! (*frameList)[0].empty() )
			{
	 			cv::imshow("window1", (*frameList)[0]);
			}

	// 		if(! (*frameList)[1].empty() )
	// 		{
	// 			cv::imshow("window2", (*frameList)[1]);
	// 		}

	// 		if(! (*frameList)[2].empty() )
	// 		{
	// 			cv::imshow("window3", (*frameList)[2]);
	// 		}
		}	
	// 	//MUTEX.unlock();	
	}
}