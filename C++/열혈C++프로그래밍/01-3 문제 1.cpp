//Q. DefaultValue3.cpp �� ���ǵ� �Լ� BoxVolume�� �Ű������� ����Ʈ �� ���� ���°� �ƴ�
//�Լ� �����ε��� ���·� �籸���غ���. main �Լ��� �������� �ʾƾ� �ϸ�, �������� �����ؾ���.

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
