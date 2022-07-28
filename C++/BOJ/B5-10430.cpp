#include<iostream>
using namespace std;
//include<iostream.h> 사용시 using namespace std;안적어도됨
//using namespace std - global로 namespace 선언 시 namespace에 선언된 함수나 다른 요소들의 이름이 겹칠 수 있어 오류가 발생할 수 있다.  
int main(void){
	int a,b,c;
	cin>>a>>b>>c;
	cout<<(a+b)%c<<"\n";
	cout<<((a%c)+(b%c))%c<<"\n";
	cout<<(a*b)%c<<"\n";
	cout<<((a%c)*(b%c))%c;
}
