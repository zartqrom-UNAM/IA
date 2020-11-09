LIBRARY ieee;
USE ieee.std_logic_1164.all;
ENTITY bcd7seg IS
PORT(	bcd : IN std_logic_vector(2 DOWNTO 0);
		led : OUT std_logic_vector(6 DOWNTO 0)
);
END bcd7seg;
ARCHITECTURE arqbcd7seg OF bcd7seg IS
BEGIN
	WITH bcd SELECT
	led <=	"1000000" WHEN "000",--0
			"1111001" WHEN "001",--1
			"0100100" WHEN "010",--2
			"0110000" WHEN "011",--3
			"0011001" WHEN "100",--4
			"0010010" WHEN "101",--5
			"0000010" WHEN "110",--6
			"1111000" WHEN "111",--7
			"0111111" WHEN OTHERS;
END arqbcd7seg;