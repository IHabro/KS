package KvalitySoftware.CV_01;

import java.util.Iterator;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        System.out.println( "Hello World!" );
    }
    
    public boolean validatePSC(String psc)
    {
    	if (psc == null || psc == "" || psc.contains("-"))
    		return false;
    	
    	if (psc.contains(" "))
    		psc = psc.replace(" ", "");
    	
    	if (psc == null || psc.length() == 0 || psc.length() > 5 )
    		return false;
    	
    	
    	for(int i = 0; i < psc.length();i++)
    	{
    		if(!Character.isDigit(psc.charAt(i)))
    			return false;
    	}
    	
    	return true;
    }
}
