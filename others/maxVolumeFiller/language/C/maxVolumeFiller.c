#include <stdio.h>

int main(int argc, char const *argv[])
{
	int n,csize ;
	int arr[101];
	scanf("%d %d",&n,&csize);
	// printf("%d %d\n",n,csize );
	int length,breath;
	for (int i = 0; i < 101; ++i)
	{
		arr[i] = 0;
	}
	int larr[101],barr[101],area;
	int maxOfTwo ;
	int msum;
	for(int J=0;J<n;J++){
		scanf("%d %d",&length,&breath);
		// printf("\n%d\n%d %d\n",J+1,length,breath );
		area = length*breath;
		for(int i=1;i<=csize;i++){
			larr[i]=arr[i];
			barr[i]=arr[i];
			// printf("%d ",arr[i]);
		}
		// printf("\n");
		for (int i = 1; i <= csize; ++i)
		{	
			if(i==length){
				if(arr[i]<area){
					larr[i] =area;
				}
			}
			if(arr[i]!=0 ){
				if(i+length<=csize){
					msum = arr[i]+ area;
					if(arr[i+length]< msum){
						larr[i+length] = msum;
					}
				}
			}	
		}
		for (int i = 1; i <= csize; ++i)
		{	
			if(i==breath){
				if(arr[i]<area){
					barr[i]=area;
				}
			}
			if(arr[i]!=0){
				if(i+breath<=csize){
					msum = arr[i]+ area;
					if(arr[i+breath]< msum){
						barr[i+breath] = msum;
					}
				}
			}	
		}
		for (int i = 1; i <= csize; ++i)
		{
			maxOfTwo = larr[i]>barr[i]? larr[i]:barr[i];
			// printf("%d ", maxOfTwo);
			if(arr[i]<maxOfTwo){
				arr[i] = maxOfTwo;
			}
		}
		// printf("\n");
	}
	printf("%d\n",arr[csize]);
	return 0;
}