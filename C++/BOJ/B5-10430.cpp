#include<iostream>
using namespace std;
//include<iostream.h> ���� using namespace std;�������
//using namespace std - global�� namespace ���� �� namespace�� ����� �Լ��� �ٸ� ��ҵ��� �̸��� ��ĥ �� �־� ������ �߻��� �� �ִ�.  
int main(void){
	int a,b,c;
	cin>>a>>b>>c;
	cout<<(a+b)%c<<"\n";
	cout<<((a%c)+(b%c))%c<<"\n";
	cout<<(a*b)%c<<"\n";
	cout<<((a%c)*(b%c))%c;
}
