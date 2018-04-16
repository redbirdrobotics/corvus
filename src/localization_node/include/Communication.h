#include <iostream>
#include <opencv2/opencv.hpp>
#include <boost/filesystem.hpp>
#include <fstream>
//#include "Detection.h"
//#include "Stereo.h"

#ifndef COMMUNICATION_CLASS
#define COMMUNICATION_CLASS

class Communication
{
private:

	struct MyData
	{
		MyData():
		A(0), X(0), id() {}

		explicit MyData(int) :
		A(97), X(CV_PI), id("mydata1234") {}

		int A;
		double X;
		std::string id;
		void write(cv::FileStorage& fs) const
		{
			fs << "{" <<"A" << A << "X" << X << "id" << id << "}";
		}
		void read(const cv::FileNode& node) 
		{
			A = (int)node["A"];
			X = (double)node["X"];
			id = (std::string)node["id"];
		}
	};

	void write(cv::FileStorage&, const std::string&, const MyData&);
	void read(const cv::FileNode&, MyData&, const MyData& default_value = MyData());

	inline
	friend std::ostream& operator<<(std::ostream& out, const MyData& m)
	{
		out << "{ id = " << m.id << ", ";
		out << "X = " << m.X << ", ";
		out << "A = " << m.A << "}";
		return out;
	}

	std::string getInFile();
	std::string getOutFile();
	void setIOFiles(const std::string&, const std::string&);
	static void checkDir(boost::filesystem::path);

public:

	//Communication(std::string iFile, std::string oFile);

	static void setInOutFiles(const std::string&, const std::string&);

	// static void getCalibration_XMLData(Stereo*);
	// static void getDisparity_XMLData(Stereo*);

	// static void writeCalibration_XMLData(Stereo*);
	//static void getDetection_XMLData(Detection*);
	static void storeIMG(boost::shared_ptr< std::vector< cv::Mat > >, std::string);
	static void storeIMG(boost::shared_ptr< std::vector< std::vector< cv::Mat > > >, std::string);
	// static void storeIMG(Stereo*);
};

#endif