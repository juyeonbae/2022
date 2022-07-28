#include<iostream>
using namespace std;

//부분적 디폴트 값 설정 가능
 
int BoxVolume(int length, int width =1, int height =1);

int main(void){
	cout<<"[3,3,3] : "<<BoxVolume(3,3,3)<<endl;
	cout<<"[5,5,D] : "<<BoxVolume(5,5)<<endl;
	cout<<"[5,D,D] : "<<BoxVolume(7)<<endl;
	//cout<<"[D,D,D] : "<<BoxVolume()<<endl;
	return 0;
} 

int BoxVolume(int length, int width, int height){
	return length*width*height;
}

//반드시 오른쪽 매개변수의 디폴트 값부터 채우는 형태로 정의해야한다. 
//Why? >> 함수에 전달되는 인자가 왼쪽에서부터 오른쪽으로 채워지기 때문이다.  
//ex) int YourFunc(int num1, int num2, int num3=30);
//ex) YourFunc(10,20); << 왼쪽에서부터 채워짐 10 20 30 으로 출력 
 
