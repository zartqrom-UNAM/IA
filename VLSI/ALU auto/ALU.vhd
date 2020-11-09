library IEEE;
use IEEE.std_logic_1164.all;

entity ALU is
port (
    a,b             : in std_logic_vector(2 downto 0);
    selmux4         : in std_logic_vector(1 downto 0);
    selmux2, cin    : in std_logic;
    led             : out std_logic_vector(6 downto 0);
    cout            : out std_logic  
);
end entity ALU;

architecture arqALU of ALU is
    signal salsum, salmux4x1,bcd : std_logic_vector(2 downto 0);
begin
    u1 : entity work.UA(arqUA) port map (selmux4, a, b, cin, salsum, cout);
    u2 : entity work.UL(arqUL) port map (a, b, selmux4, salmux4x1);
    u3 : entity work.mux2x1(arqmux2x1) port map (salsum, salmux4x1, selmux2, bcd);
    u4 : entity work.bcd7seg(arqbcd7seg) port map (bcd, led);
end architecture arqALU;