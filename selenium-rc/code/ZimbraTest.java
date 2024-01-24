import com.thoughtworks.selenium.Selenium;
import com.thoughtworks.selenium.DefaultSelenium;

@SuppressWarnings("deprecation")
public class ZimbraTest {

	public static void main(String[] args) throws Exception {
		// creating instance of selenium client
		Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", "https://mail.nitrkl.ac.in/");
		
		// start selenium session
		selenium.start();
		
		// setting timeout for actoins as Zimbra is slow on nitrkl network
		selenium.setTimeout("120000");
		
		try 
		{
			// open home page
			selenium.open("/");
			
			// maximize window
			selenium.windowMaximize();
			
			// type username
			selenium.type("id=username", "Username");
			
			// type password
			selenium.type("id=password", "Password");
			
			// click on login button
			selenium.click("css=.ZLoginButton");
			
			// wait for page to load
			selenium.waitForPageToLoad("120000");
			
			// check if mail in menu exists
			boolean isMailPresent = selenium.isElementPresent("id=zb__App__Mail");
			
			assert isMailPresent == true : "Mail not present";
			
			System.out.println("Test passed");
		}
		catch(Exception ex)
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