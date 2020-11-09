LIBRARY ieee;
use ieee.std_logic_1164.all;

entity VGAreloj is
    port (
        input_clk               : in  std_logic;
        reset                   : in  std_logic;
        red                     : out std_logic_vector(3 DOWNTO 0);
        green                   : out std_logic_vector(3 downto 0);
        blue                    : out std_logic_vector(3 DOWNTO 0);
        h_sync                  : out std_logic;
        v_sync                  : out std_logic;
        led1, led2, led3, led4, led5, led6 :  out std_logic_vector(6 DOWNTO 0);
        sw                      : in std_logic_vector(1 downto 0)
    );
end entity;

architecture archVGAreloj of VGAreloj is
    constant pixels_y               : integer range 0 to 480:= 170;
    constant pixels_x               : integer range 0 to 640:= 40;
    signal pix_clk, disp_ena        : std_logic;
    signal column, row              : integer;
    signal led_DH, led_DM, led_DS   : std_logic_vector(6 DOWNTO 0);
    signal led_UH, led_UM, led_US   : std_logic_vector(6 DOWNTO 0);
begin
    u1 : entity work.gen25MHz(arqgen25MHz) port map (input_clk, pix_clk);
    u2 : entity work.controlador_vga(arqcontrolador_vga) port map (pix_clk, h_sync, v_sync, disp_ena, column, row);
    u3 : entity work.Reloj(arqReloj) port map (input_clk, sw, led1, led2, led3, led4, led5, led6, led_US, led_DS, led_UM, led_DM, led_UH, led_DH, reset);
    u4 : entity work.generador_imagen(arqgenerador_imagen) port map (disp_ena,row,column,pixels_y,pixels_x,red,green,blue,led_DH, led_DM, led_DS,led_UH, led_UM, led_US);
    end architecture;