#include<iostream>
using namespace std;

int Adder(int num1=1, int num2=2); 	//함수의 선언 

int main(void){
	cout<<Adder()<<endl;
	cout<<Adder(5)<<endl;
	cout<<Adder(3,5)<<endl;
	return 0;
} 

int Adder(int num1, int num2){ 		//함수의 정의  
	return num1+num2;
}

//매개변수의 디폴트 값 지정은 함수의 원형선언부분에만 위치
//Why? >> 선언부분에 위치하지 않으면, 7,8행이 컴파일이 불가능하다.  
 
