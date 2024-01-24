import com.thoughtworks.selenium.Selenium;
import com.thoughtworks.selenium.DefaultSelenium;

@SuppressWarnings("deprecation")
public class AmazonTest {

	public static void main(String[] args) throws Exception {
		// creating instance of selenium client
		Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", "https://www.amazon.in/");
		
		// start selenium session
		selenium.start();
		
		try 
		{
			// open home page
			selenium.open("/");
			
			// maximize window
			selenium.windowMaximize();

			// type in serach query
			selenium.type("id=twotabsearchtextbox", "macbook pro");
			
			// click on search button
			selenium.click("id=nav-search-submit-button");
			
			// wait for page to load
			selenium.waitForPageToLoad("100000");
			
			// check search results are for macbook pro 
			assert selenium.isElementPresent("xpath=//span[contains(text(),'macbook pro')]") : "Search results are wrong";
			
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
