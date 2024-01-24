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
public class CheckWeatherTest {
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
  public void checkWeather() {
    // Test name: Check Weather
    // Step # | name | target | value
    // 1 | open | /pages/city_weather_main_mausam.php | 
    driver.get("https://internal.imd.gov.in/pages/city_weather_main_mausam.php");
    // 2 | setWindowSize | 845x864 | 
    driver.manage().window().setSize(new Dimension(845, 864));
    // 3 | click | name=id | 
    driver.findElement(By.name("id")).click();
    // 4 | type | name=id | 42793rourkela
    driver.findElement(By.name("id")).sendKeys("42793rourkela");
    // 5 | click | css=input:nth-child(3) | 
    vars.put("window_handles", driver.getWindowHandles());
    // 6 | storeWindowHandle | root | 
    driver.findElement(By.cssSelector("input:nth-child(3)")).click();
    // 7 | selectWindow | handle=${win2622} | 
    vars.put("win2622", waitForWindow(2000));
    // 8 | assertText | xpath=//font[@color="blue"] | Rourkela
    vars.put("root", driver.getWindowHandle());
    // 9 | close |  | 
    driver.switchTo().window(vars.get("win2622").toString());
    // 10 | selectWindow | handle=${root} | 
    assertThat(driver.findElement(By.xpath("//font[@color=\"blue\"]")).getText(), is("Rourkela"));
    // 11 | close |  | 
    driver.close();
    driver.switchTo().window(vars.get("root").toString());
    driver.close();
  }
}