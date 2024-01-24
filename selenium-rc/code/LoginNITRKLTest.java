import com.thoughtworks.selenium.DefaultSelenium;
import com.thoughtworks.selenium.Selenium;

@SuppressWarnings("deprecation")
public class LoginNITRKLTest {

	public static void main(String[] args) throws Exception {
		// creating instance of selenium client
		Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", "https://login.nitrkl.ac.in");
		
		// start selenium session
		selenium.start();
		
		try 
		{
			// open /PortalMain page
			selenium.open("/PortalMain");
			
			// maximize window
			selenium.windowMaximize();

			// wait for element to be present
			Thread.sleep(1000);
			
			// type in serach query
			selenium.type("id=LoginUserPassword_auth_username", "Username");
			
			// click on search button
			selenium.type("id=LoginUserPassword_auth_password", "Password");
			
			// click on login button
			selenium.click("id=UserCheck_Login_Button");
			
			// check search results are for macbook pro 
			assert selenium.isElementPresent("id=UserCheck_Logoff_Button_span") : "login failed";
			
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