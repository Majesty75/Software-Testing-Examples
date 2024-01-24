import com.thoughtworks.selenium.Selenium;
import com.thoughtworks.selenium.DefaultSelenium;

@SuppressWarnings("deprecation")
public class NITRKLTest {

	public static void main(String[] args) throws Exception {
		// creating instance of selenium client
		Selenium selenium = new DefaultSelenium("localhost", 4444, "*firefox D:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe", "https://www.nitrkl.ac.in/");
		
		// start selenium session
		selenium.start();
		
		try 
		{
			// open home page
			selenium.open("/");
				
			// maximize window
			selenium.windowMaximize();

			// click academics menu
			selenium.mouseOver("link=Academics");
			
			// click engineering sub menu
			selenium.click("id=submenu-engineering");
			
			// wait for page to load
			selenium.waitForPageToLoad("3000");
			
			// click computer science and engineering
			selenium.click("css=.department .item:nth-child(5) a");
			
			// wait for page to load
			selenium.waitForPageToLoad("3000");
			
			// click academics menu
			selenium.mouseOver("css=#tmenu-academic .submenu-indicator-chevron");
			
			// click curriculum & syllabus
			selenium.click("id=submenu-curiculum");
			
			// wait for page to load
			selenium.waitForPageToLoad("3000");
			
			// click software engineering
			selenium.click("css=tr:nth-child(4) a");
			
			// wait for page to load
			selenium.waitForPageToLoad("3000");
			
			// click syllabus
			selenium.click("css=#flush-2 tbody tr:nth-child(3) a");
			
			// wait for page to load
			selenium.waitForPageToLoad("3000");
			
			// get course name
			String courseName = selenium.getText("css=.item-left .row:nth-child(2) .col-md-12 > p:nth-child(1)").trim();
			
			// assert course name
			assert courseName.equals("Subject {L-T-P / C} : CS6404 : Software Testing { 3-0-0 / 3}") : "Invalid course name";
			
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
