#include<iostream>
using namespace std;

int Adder(int num1 = 1, int num2 = 2){
	return num1+num2;
}
int main(void){
	cout<<Adder()<<endl; 		//�Լ��� ȣ���ϸ鼭 ���ڸ� �������� �ʾ����Ƿ�, Default Value(num1 = 1,num =2)�� ����  
	cout<<Adder(5)<<endl;		//���ڸ� �ϳ��� ����>>�̷��� ���, ���ڴ� ù ��° �Ű������� ���� 
	cout<<Adder(3,5)<<endl;		//�� ���� ���ڸ� ���� >> �̷��� ���, Default ���� �ǹ̸� ���� �ʴ´�.  
	
	return 0;
} 
