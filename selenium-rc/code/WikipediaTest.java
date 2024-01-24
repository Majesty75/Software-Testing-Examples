import java.util.Random;

import com.thoughtworks.selenium.DefaultSelenium;
import com.thoughtworks.selenium.Selenium;

public class WikipediaTest {
	public static void main(String[] args) throws Exception {
		// creating instance of selenium client
		Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", "https://en.wikipedia.org");
		
		// start selenium session
		selenium.start();
		
		selenium.setTimeout("5000");
		
		selenium.setSpeed("1000");
		
		try 
		{
			// open home page
			selenium.open("/wiki/Main_Page");

			// maximize window
			selenium.windowMaximize();

			// create instance of random class
			Random random = new Random();
					
			for (int i = 0; i < 5; i++) 
			{
				// find number of links with en in href for english language
				int number = selenium.getXpathCount("(//a)[contains(@href, \"en\")]").intValue();
				
				// if no further links found exit
				if (number == 0)
				{
					break;
				}
				
				// choose any link randomly
				int nextLink = random.nextInt(number) + 1;
				
				// click on random link
				selenium.click("xpath=(//a)[contains(@href, \"en\")][" + nextLink + "]");
			}
			
			System.out.println("Test passed");
		}
		catch (Exception ex) 
		{
			System.out.println("Test failed: " + ex.getMessage());
			throw ex;
		}
		finally 
		{
			// stop selenium session
			selenium.stop();
		}
	}
}