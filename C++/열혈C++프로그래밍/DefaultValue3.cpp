#include<iostream>
using namespace std;

//�κ��� ����Ʈ �� ���� ����
 
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

//�ݵ�� ������ �Ű������� ����Ʈ ������ ä��� ���·� �����ؾ��Ѵ�. 
//Why? >> �Լ��� ���޵Ǵ� ���ڰ� ���ʿ������� ���������� ä������ �����̴�.  
//ex) int YourFunc(int num1, int num2, int num3=30);
//ex) YourFunc(10,20); << ���ʿ������� ä���� 10 20 30 ���� ��� 
 
