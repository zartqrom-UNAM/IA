library IEEE;
use IEEE.std_logic_1164.all;

entity UL is
port (
    a,b     : in std_logic_vector(2 downto 0);
    selUL   : in std_logic_vector(1 downto 0);
    salUL   : out std_logic_vector(2 downto 0)
);
end entity UL;

architecture arqUL of UL is
    signal sand, sor, sxor, snot : std_logic_vector(2 downto 0);
begin
    sand    <= a and b;
    sor     <= a or b;
    sxor    <= a xor b;
    snot    <= not a;

    with selUL select
    salUL   <=  (sand) when "00",
                (sor) when "01",
                (sxor) when "10",
                (snot) when "11";
end architecture arqUL;