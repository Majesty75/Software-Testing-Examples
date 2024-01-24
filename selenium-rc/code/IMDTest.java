import com.thoughtworks.selenium.DefaultSelenium;
import com.thoughtworks.selenium.Selenium;

public class IMDTest {

	public static void main(String[] args) throws Exception {
		// creating instance of selenium client
		Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", "https://internal.imd.gov.in");
		
		// start selenium session
		selenium.start();
		
		try 
		{
			// open home page
			selenium.open("/pages/city_weather_main_mausam.php");
			
			// maximize window
			selenium.windowMaximize();

			// click on search box
			selenium.click("name=id");
			
			// type in text question
			selenium.type("css=#menu1 input=[type=\"text\"]", "42793rourkela");
			
			// click Go
			selenium.click("css=#menu1 input[type=\"submit\"]");
			
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