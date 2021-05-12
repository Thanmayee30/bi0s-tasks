/*encryption code*/
#include<stdio.h>
int main()
{
	char msg[100], chara;
	int n,key;
	printf("Message: ");
	gets(msg);
	printf("key: ");
	scanf("%d", &key);
	for(n = 0; msg[n] != '\0'; ++n){
		chara = msg[n];
		if(chara >= 'a' && chara <= 'z'){
			chara = chara + key;
			if(chara > 'z'){
				chara = chara - 'z' + 'a' - 1;
			}
			
			msg[n] = chara;
		}
		else if(chara >= 'A' && chara <= 'Z'){
			chara = chara + key;
			if(chara > 'Z'){
				chara = chara - 'Z' + 'A' - 1;
			}
			msg[n] = chara;
		}
	}
	printf("%s", msg);
	
	return 0;
}
