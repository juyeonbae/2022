//Q. DefaultValue3.cpp 에 정의된 함수 BoxVolume를 매개변수의 디폴트 값 지정 형태가 아닌
//함수 오버로딩의 형태로 재구현해보자. main 함수는 변경하지 않아야 하며, 실행결과도 동일해야함.

#include<iostream>
using namespace std;

int BoxVolume(int length, int width, int height){
	return length*width*height;
} 
int BoxVolume(int length, int width){
	return length*width*1;
} 
int BoxVolume(int length){
	return length*1*1;
} 

int main(void){
	cout<<"[3,3,3] : "<<BoxVolume(3,3,3)<<endl;
	cout<<"[5,5,D] : "<<BoxVolume(5,5)<<endl;
	cout<<"[5,D,D] : "<<BoxVolume(7)<<endl;
	//cout<<"[D,D,D] : "<<BoxVolume()<<endl;
	return 0;
}
