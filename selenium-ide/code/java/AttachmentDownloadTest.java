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
public class AttachmentDownloadTest {
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
  public void attachmentDownload() {
    // Test name: Attachment Download
    // Step # | name | target | value
    // 1 | open | /nitris/Student/Home/Home.aspx | 
    driver.get("https://eapplication.nitrkl.ac.in/nitris/Student/Home/Home.aspx");
    // 2 | setWindowSize | 850x864 | 
    driver.manage().window().setSize(new Dimension(850, 864));
    // 3 | click | css=.mdi-comment-processing | 
    driver.findElement(By.cssSelector(".mdi-comment-processing")).click();
    // 4 | click | css=.message-item:nth-child(2) > .mail-contnet | 
    driver.findElement(By.cssSelector(".message-item:nth-child(2) > .mail-contnet")).click();
    // 5 | click | id=ContentPlaceHolder2_hypPreview | 
    driver.findElement(By.id("ContentPlaceHolder2_hypPreview")).click();
    // 6 | close |  | 
    driver.close();
  }
}
