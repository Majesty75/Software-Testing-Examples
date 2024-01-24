import com.thoughtworks.selenium.Selenium;
import com.thoughtworks.selenium.DefaultSelenium;

@SuppressWarnings("deprecation")
public class GoogleFormsTest {

	public static void main(String[] args) throws Exception {
		// creating instance of selenium client
		Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", "https://docs.google.com");
		
		// start selenium session
		selenium.start();
		
		try 
		{
			// open home page
			selenium.open("/forms/d/e/1FAIpQLSeI8_vYyaJgM7SJM4Y9AWfLq-tglWZh6yt7bEXEOJr_L-hV1A/viewform?formkey=dGx0b1ZrTnoyZDgtYXItMWVBdVlQQWc6MQ");
			
			// maximize window
			selenium.windowMaximize();

			// type in text question
			selenium.type("css=.whsOnd", "This is selenium testing");
			
			// type in paragraph question
			selenium.type("css=.KHxj8b", "By selenium testing we can test website response to user commands and verify if it is working properly. This test is conducted by selenium IDE.");
			
			// click choice 2
			selenium.click("id=i16");
			
			// click choice 1
			selenium.click("id=i27");
			
			// click drop down
			selenium.click("css=.ry3kXd .KKjvXb");
	
			// setting execution speed to 500 ms as dropdown opens after animation delay
			selenium.setSpeed("500");
			
			// click drop down option
			selenium.click("css=.OA0qNb .KKjvXb .vRMGwf");
			
			// clearing execution speed
			// selenium.setSpeed("0");
			
			// click scale question option 4
			selenium.click("xpath=//div[@class=\"N9Qcwe\"]//div[@data-value=\"4\"]");
			
			// click Uses for Google forms
			selenium.click("xpath=//form[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/div/div[2]/span/div[3]/div/div/div[3]/div");
			
			// click Creating Google Forms
			selenium.click("xpath=//form[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/div/div[4]/span/div[4]/div/div/div[3]/div");
			
			// click Sending completed Google Form
			selenium.click("xpath=//form[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/div/div[6]/span/div[4]/div/div/div[3]/div");
			
			// click Using results from Google Forms
			selenium.click("//form[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/div/div[8]/span/div[3]/div/div/div[3]/div");
			
			// click submit
			selenium.click("css=.Y5sE8d > .l4V7wb");
			
			// wait for page load
			selenium.waitForPageToLoad("3000");
			
			// check form form submission
			assert selenium.isElementPresent("//a[text()='Submit another response']") : "Form submission failed";
			
			System.out.println("Test passed");
		}
		catch (Exception ex) 
		{
			System.err.println("Test failed: " + ex.getMessage());
			throw ex;
		}
		finally 
		{
			// stop selenium session
			selenium.stop();
		}
	}
}
