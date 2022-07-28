#include<iostream>
using namespace std;

int Adder(int num1 = 1, int num2 = 2){
	return num1+num2;
}
int main(void){
	cout<<Adder()<<endl; 		//함수를 호출하면서 인자를 전달하지 않았으므로, Default Value(num1 = 1,num =2)가 적용  
	cout<<Adder(5)<<endl;		//인자를 하나만 전달>>이러한 경우, 인자는 첫 번째 매개변수로 전달 
	cout<<Adder(3,5)<<endl;		//두 개의 인자를 전달 >> 이러한 경우, Default 값은 의미를 갖지 않는다.  
	
	return 0;
} 
