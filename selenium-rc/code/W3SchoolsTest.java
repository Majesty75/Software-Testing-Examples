import com.thoughtworks.selenium.DefaultSelenium;
import com.thoughtworks.selenium.Selenium;

public class W3SchoolsTest {

	public static void main(String[] args) throws Exception {
		// creating instance of selenium client
		Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", "https://www.w3schools.com");
		
		// start selenium session
		selenium.start();
		
		try 
		{
			// open home page
			selenium.open("/jsref/tryit.asp?filename=tryjsref_alert");
			
			// maximize window
			selenium.windowMaximize();
			
			String test = selenium.getTitle();

			assert selenium.getTitle().equals("W3Schools Tryit Editor") : "Failed to open correct site";
			
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
