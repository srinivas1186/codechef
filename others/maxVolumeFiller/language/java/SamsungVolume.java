

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class SamsungVolume
{
	public static void main (String[] args) throws java.lang.Exception
	{
	    int n,s,i,j,k,q,m;
	    Scanner sc=new Scanner(System.in);
	    int t=sc.nextInt();
	    
	    for(q=0;q<t;q++){
	    
	    n=sc.nextInt();
	    
	    s=sc.nextInt();
	    m=s+1;
	  
	   int l[]=new int[n];
	   int b[]=new int[n];
	   int ll[]=new int[m];
	   int bb[]=new int[m];
	   int lb[]=new int[m];
	   
	   for(i=0;i<n;i++)
	   {
	      l[i]=sc.nextInt(); 
	      b[i]=sc.nextInt();
	   }
	   
	   
	   for(i=0;i<n;i++)
	   {
	        k=l[i]*b[i];
	        //length
	        if(l[i]<m)
	        {
	       
	            if(ll[l[i]]<k)
	            ll[l[i]]=k;
	       
	            for(j=1;j<m;j++)
	            {
	                if(lb[j]==0)
	                continue;
	                else
	                {
	                    if((j+l[i])<m)
	                   ll[j+l[i]]=lb[j]+k;
	                }
	            }
	       
	       }
	       
	       //breadth
	       
	       if(b[i]<m)
	        {
	       
	            if(bb[b[i]]<k)
	                bb[b[i]]=k;
	       
	            for(j=1;j<m;j++)
	            {
	                if(lb[j]==0)
	                continue;
	                else
	                {
	                   if((j+b[i])<m)
	                   bb[j+b[i]]=lb[j]+k;
	                }
	            }
	       
	       }
	       
	       //combine length breadth
	       
	       
	            for(j=1;j<m;j++)
	            {
	                if(ll[j]>lb[j])
	                lb[j]=ll[j];
	                
	                else if(bb[j]>lb[j])
	                lb[j]=bb[j];
	                
	               // System.out.print(lb[j]+" ");
	            }
	            
	            //System.out.print("\n");
	       
	       
	       
	       
	       
	       
	   }
	   
	   
	   
	   System.out.println(lb[s]);
	   
	  
	    }
	}
	
}

