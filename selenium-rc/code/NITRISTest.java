import com.thoughtworks.selenium.DefaultSelenium;
import com.thoughtworks.selenium.Selenium;

public class NITRISTest {

	public static void main(String[] args) throws Exception {
		// creating instance of selenium client
		Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", "https://eapplication.nitrkl.ac.in");
		
		// start selenium session
		selenium.start();
		
		try 
		{
			// open home page
			selenium.open("/nitris/Login.aspx");
			
			// maximize window
			selenium.windowMaximize();
			
			// type in username
			selenium.type("id=txtUserName", "Username");

			// type in password
			selenium.type("id=txtPassword", "Password");
			
			// click login
			selenium.click("id=btnLogin");
			
			selenium.waitForPageToLoad("100000");
			
			// click notifications
			selenium.click("css=.mdi-comment-processing");
			
			// click first notification
			selenium.click("css=.message-item:nth-child(2) > .mail-contnet");
			
			// wait for page to load
			selenium.waitForPageToLoad("100000");
			
			// click download button
			selenium.click("id=ContentPlaceHolder2_hypPreview");
			
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
