library IEEE;
use IEEE.std_logic_1164.all;

entity mux2x1 is
    port (
        a,b  : in std_logic_vector(2 downto 0);
        sel  : in std_logic;
        sal  : out std_logic_vector(2 downto 0)
    );
end entity mux2x1;

architecture arqmux2x1 of mux2x1 is
begin
    with sel select
        sal <=  a   when '0', --suma
                b   when '1';
end architecture arqmux2x1;