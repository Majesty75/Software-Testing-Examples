import com.thoughtworks.selenium.DefaultSelenium;
import com.thoughtworks.selenium.Selenium;

@SuppressWarnings("deprecation")
public class SmallPDFTest {

	public static void main(String[] args) throws Exception {
		// creating instance of selenium client
		Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", "https://smallpdf.com");
		
		// start selenium session
		selenium.start();
		
		try
		{
			// open /pdf-to-word page
			selenium.open("/pdf-to-word");
			
			// maximize window
			selenium.windowMaximize();

			// type in file location in file picker
			selenium.typeKeys("id=__picker-input", "C:\\Users\\Yash\\Downloads\\Assignment 1 Equivalence Classes.docx");
			
			// click on convert button
			selenium.click("css.kHOHNI .r5zwp6-3:nth-child(2)");
			
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

/* Test Results
 * Test failed as older firefox is not capable to load this page.
 */
