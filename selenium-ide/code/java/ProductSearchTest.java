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
public class ProductSearchTest {
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
  public String waitForWindow(int timeout) {
    try {
      Thread.sleep(timeout);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
    Set<String> whNow = driver.getWindowHandles();
    Set<String> whThen = (Set<String>) vars.get("window_handles");
    if (whNow.size() > whThen.size()) {
      whNow.removeAll(whThen);
    }
    return whNow.iterator().next();
  }
  @Test
  public void productSearch() {
    // Test name: Product Search
    // Step # | name | target | value
    // 1 | open | / | 
    driver.get("https://www.amazon.in/");
    // 2 | setWindowSize | 1552x880 | 
    driver.manage().window().setSize(new Dimension(1552, 880));
    // 3 | click | id=twotabsearchtextbox | 
    driver.findElement(By.id("twotabsearchtextbox")).click();
    // 4 | type | id=twotabsearchtextbox | macbook pro m3
    driver.findElement(By.id("twotabsearchtextbox")).sendKeys("macbook pro m3");
    // 5 | click | id=nav-search-submit-button | 
    driver.findElement(By.id("nav-search-submit-button")).click();
    // 6 | click | xpath=//a/span[text()="2023 MacBook Air laptop with M2 chip: 38.91cm (15.3 inch) Liquid Retina display, 8GB RAM 256GB SSD storage, backlit keyboard, 1080p FaceTime HD camera,Touch ID. Works with iPhone/iPad; Starlight"] | 
    vars.put("window_handles", driver.getWindowHandles());
    // 7 | storeWindowHandle | root | 
    driver.findElement(By.xpath("//a/span[text()=\"2023 MacBook Air laptop with M2 chip: 38.91cm (15.3 inch) Liquid Retina display, 8GB RAM 256GB SSD storage, backlit keyboard, 1080p FaceTime HD camera,Touch ID. Works with iPhone/iPad; Starlight\"]")).click();
    // 8 | selectWindow | handle=${productPage} | 
    vars.put("productPage", waitForWindow(2000));
    // 9 | assertElementPresent | xpath=//h1/span[text()="        Apple 2023 MacBook Air laptop with M2 chip: 38.91cm (15.3 inch) Liquid Retina display, 8GB RAM 256GB SSD storage, backlit keyboard, 1080p FaceTime HD camera,Touch ID. Works with iPhone/iPad; Starlight       "] | 
    vars.put("root", driver.getWindowHandle());
    // 10 | close |  | 
    driver.switchTo().window(vars.get("productPage").toString());
    // 11 | selectWindow | handle=${root} | 
    {
      List<WebElement> elements = driver.findElements(By.xpath("//h1/span[text()=\"        Apple 2023 MacBook Air laptop with M2 chip: 38.91cm (15.3 inch) Liquid Retina display, 8GB RAM 256GB SSD storage, backlit keyboard, 1080p FaceTime HD camera,Touch ID. Works with iPhone/iPad; Starlight       \"]"));
      assert(elements.size() > 0);
    }
    // 12 | close |  | 
    driver.close();
    driver.switchTo().window(vars.get("root").toString());
    driver.close();
  }
}
