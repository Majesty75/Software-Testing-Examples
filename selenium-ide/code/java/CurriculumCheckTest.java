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
public class CurriculumCheckTest {
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
  public void curriculumCheck() {
    // Test name: Curriculum Check
    // Step # | name | target | value
    // 1 | open | / | 
    driver.get("https://www.nitrkl.ac.in/");
    // 2 | setWindowSize | 1552x880 | 
    driver.manage().window().setSize(new Dimension(1552, 880));
    // 3 | click | linkText=Academics | 
    driver.findElement(By.linkText("Academics")).click();
    // 4 | click | id=submenu-engineering | 
    driver.findElement(By.id("submenu-engineering")).click();
    // 5 | runScript | window.scrollTo(0,696) | 
    js.executeScript("window.scrollTo(0,696)");
    // 6 | click | css=.item:nth-child(5) h5 | 
    driver.findElement(By.cssSelector(".item:nth-child(5) h5")).click();
    // 7 | click | css=#tmenu-academic .submenu-indicator-chevron | 
    driver.findElement(By.cssSelector("#tmenu-academic .submenu-indicator-chevron")).click();
    // 8 | click | id=submenu-curiculum | 
    driver.findElement(By.id("submenu-curiculum")).click();
    // 9 | click | css=tr:nth-child(4) a | 
    driver.findElement(By.cssSelector("tr:nth-child(4) a")).click();
    // 10 | click | css=#flush-heading-2 > .accordion-button | 
    driver.findElement(By.cssSelector("#flush-heading-2 > .accordion-button")).click();
    // 11 | click | css=#flush-2 tr:nth-child(3) a | 
    driver.findElement(By.cssSelector("#flush-2 tr:nth-child(3) a")).click();
    // 12 | close |  | 
    driver.close();
  }
}
