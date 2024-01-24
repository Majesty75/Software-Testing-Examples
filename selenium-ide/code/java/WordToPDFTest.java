// Generated by Selenium IDE
import org.junit.Test;
import org.junit.Before;
import org.junit.After;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.is;
import static org.hamcrest.core.IsNot.not;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.Dimension;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.Alert;
import org.openqa.selenium.Keys;
import java.util.*;
import java.net.MalformedURLException;
import java.net.URL;
public class WordtoPDFTest {
  private WebDriver driver;
  private Map<String, Object> vars;
  JavascriptExecutor js;
  @Before
  public void setUp() {
    driver = new ChromeDriver();
    js = (JavascriptExecutor) driver;
    vars = new HashMap<String, Object>();
  }
  @After
  public void tearDown() {
    driver.quit();
  }
  @Test
  public void wordtoPDF() {
    // Test name: Word to PDF
    // Step # | name | target | value
    // 1 | open | /pdf-to-word | 
    driver.get("https://smallpdf.com/pdf-to-word");
    // 2 | setWindowSize | 850x864 | 
    driver.manage().window().setSize(new Dimension(850, 864));
    // 3 | click | id=__picker-input | 
    driver.findElement(By.id("__picker-input")).click();
    // 4 | type | id=__picker-input | C:\Users\Yash\Downloads\Assignment 1 Equivalence Classes.docx
    driver.findElement(By.id("__picker-input")).sendKeys("C:\\Users\\Yash\\Downloads\\Assignment 1 Equivalence Classes.docx");
    // 5 | click | css=.kHOHNI .r5zwp6-3:nth-child(2) | 
    driver.findElement(By.cssSelector(".kHOHNI .r5zwp6-3:nth-child(2)")).click();
    // 6 | close |  | 
    driver.close();
  }
}