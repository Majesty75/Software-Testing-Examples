import com.thoughtworks.selenium.DefaultSelenium;
import com.thoughtworks.selenium.Selenium;

public class HouseOfPanchhiTest {

	public static void main(String[] args) throws Exception {
		// creating instance of selenium client
		Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", "https://houseofpanchhi.com");
		
		// start selenium session
		selenium.start();
		
		try 
		{
			// open home page
			selenium.open("/collections/lehenga");
			
			// maximize window
			selenium.windowMaximize();

			assert selenium.getTitle().equals("Lehenga – houseofpanchhi") : "Failed to open correct site";
			
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

/* Test Result
 * Test Failed as firefox is not able to open site with error sec_error_ocsp_invalid_signing_cert
 */