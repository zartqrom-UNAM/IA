library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.std_logic_unsigned.all;

entity UA is
    port (
        selmux  : in std_logic_vector(1 downto 0);
        a,b     : in std_logic_vector(2 downto 0);
        cin     : in std_logic;
        salsum  : out std_logic_vector(2 downto 0);
        cout    : out std_logic
    );
end entity UA;

architecture arqUA of UA is
    signal cablemux : std_logic_vector(2 downto 0);
begin
    u1 : entity work.mux4x1(arqmux4x1) port map (selmux,b,cablemux);
    u2 : entity work.sum(arqsum) port map (a,cablemux, cin, salsum, cout);
end architecture arqUA;