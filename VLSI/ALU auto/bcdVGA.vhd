LIBRARY ieee;
USE ieee.std_logic_1164.all;
ENTITY bcdVGA IS
PORT(	bcd : IN std_logic_vector(3 DOWNTO 0);
		led : OUT std_logic_vector(6 DOWNTO 0)
);
END bcdVGA;
ARCHITECTURE arqbcdVGA OF bcdVGA IS
BEGIN
	WITH bcd SELECT
	led <=		"0111111" WHEN "0000",
				"0000110" WHEN "0001",
				"1011011" WHEN "0010",
				"1001111" WHEN "0011",
				"1100110" WHEN "0100",
				"1101101" WHEN "0101",
				"1111101" WHEN "0110",
				"0000111" WHEN "0111",
				"1111111" WHEN "1000",
				"1101111" WHEN "1001",
				"1000000" WHEN OTHERS;
END arqbcdVGA;