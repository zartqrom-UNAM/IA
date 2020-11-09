library IEEE;
use IEEE.std_logic_1164.all;

entity mux4x1 is
    port (
        a : in std_logic_vector(1 downto 0);
        b : in std_logic_vector(2 downto 0);
        sal : out std_logic_vector(2 downto 0)
    );
end entity mux4x1;

architecture arqmux4x1 of mux4x1 is
begin
    with a select
        sal <=  (others => '0') when "00",
                not b           when "01",
                b               when "10",
                (others => '1') when "11",
                (others => '0') when others;
end architecture arqmux4x1;