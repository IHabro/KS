package KvalitySoftware.CV_01;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.params.provider.NullSource;
import org.junit.jupiter.params.provider.ValueSource;

/**
 * Unit test for simple App.
 */
class AppTest 
{
    /**
     * Rigorous Test :-)
     */
	/*
	@Test
    void shouldAnswerWithTrue()
    {
    	assertTrue( true );
    }
    */
	
	private App app;
	private static String text;
	
	@BeforeAll
	static void initAll()
	{
		text = "Test cases.";
	}
	
	@BeforeEach
	void init()
	{
		app = new App();
	}
	
	@AfterEach
	void end()
	{
		//Uklid
	}
    
    @ParameterizedTest
    @ValueSource(strings = { "739 32"})
    void ValidatePSC(String input)
    {
    	assertTrue(app.validatePSC(input));
    }
    
    @ParameterizedTest(name = "invalid psc {index}: {0}")
    @NullSource
    @ValueSource(strings = { "708-00", "abc de", "654321", "" })
    void ValidatePSCInvalid(String input)
    {
    	assertFalse(app.validatePSC(input));
    }
    
    @ParameterizedTest(name = "invalid psc {index}: \"{0}\" valid {1}")
    @CsvSource({ 
    	"708-00, true, normalni psc",
		"abc de, false, text do psc",
		"12345, true, psc bez mezery",
		"654321, false, psc moc dlouhe",
		"00000, false, prazne psc",
		"12345, true, normalni psc",
		"654321, false, dlouhe psc",
		", false, prazdny string"
		})
    void testValidatePSC(String psc, boolean expectedValue, String comment)
    {
    	assertEquals(expectedValue, app.validatePSC(psc));
    }
}
