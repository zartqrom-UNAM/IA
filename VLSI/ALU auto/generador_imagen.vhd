library IEEE;
use IEEE.std_logic_1164.all;

entity generador_imagen is
port (
    display_ena             : in std_logic;
    row                     : in integer;
    column                  : in integer;
    pix_in_y                : in integer;
    pix_in_x                : in integer;
    red                     : out std_logic_vector(3 downto 0);
    green                   : out std_logic_vector(3 downto 0);
    blue                    : out std_logic_vector(3 downto 0);
    led_DH, led_DM, led_DS  : in std_logic_vector(6 DOWNTO 0);
    led_UH, led_UM, led_US  : in std_logic_vector(6 DOWNTO 0)
);
end entity generador_imagen;

architecture arqgenerador_imagen of generador_imagen is
begin
    generador_imagen: process(display_ena, row, column, led_DH, led_DM, led_DS, led_UH, led_UM, led_US)
	begin
        if(display_ena = '1') then
            --Decena Hora
            --barra de arriba
            if ((row > pix_in_y and row < pix_in_y+20) and (column > pix_in_x and column < pix_in_x+40) and led_DH(0) ='1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de arriba derecha
            elsif ((row > pix_in_y+20 and row < pix_in_y+60) and (column > pix_in_x+40 and column < pix_in_x+55) and led_DH(1) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de abajo derecha
            elsif ((row > pix_in_y+80 and row < pix_in_y+120) and (column > pix_in_x+40 and column < pix_in_x+55) and led_DH(2) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --barra de abajo
            elsif ((row > pix_in_y+120 and row < pix_in_y+140) and (column > pix_in_x and column < pix_in_x+40) and led_DH(3) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1'); 
            --Laterales de abajo izquierda
            elsif ((row > pix_in_y+80 and row < pix_in_y+120) and (column > pix_in_x-15 and column < pix_in_x) and led_DH(4) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de arriba izquierda                
            elsif ((row > pix_in_y+20 and row < pix_in_y+60) and (column > pix_in_x-15 and column < pix_in_x) and led_DH(5) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --barra de en medio
            elsif ((row > pix_in_y+60 and row < pix_in_y+80) and (column > pix_in_x and column < pix_in_x+40) and led_DH(6) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');   
            --Unidad Hora
            --barra de arriba
            elsif ((row > pix_in_y and row < pix_in_y+20) and (column > pix_in_x+90 and column < pix_in_x+40+90) and led_UH(0) ='1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de arriba derecha
            elsif ((row > pix_in_y+20 and row < pix_in_y+60) and (column > pix_in_x+40+90 and column < pix_in_x+55+90) and led_UH(1) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de abajo derecha
            elsif ((row > pix_in_y+80 and row < pix_in_y+120) and (column > pix_in_x+40+90 and column < pix_in_x+55+90) and led_UH(2) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --barra de abajo
            elsif ((row > pix_in_y+120 and row < pix_in_y+140) and (column > pix_in_x+90 and column < pix_in_x+40+90) and led_UH(3) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1'); 
            --Laterales de abajo izquierda
            elsif ((row > pix_in_y+80 and row < pix_in_y+120) and (column > pix_in_x-15+90 and column < pix_in_x+90) and led_UH(4) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de arriba izquierda                
            elsif ((row > pix_in_y+20 and row < pix_in_y+60) and (column > pix_in_x-15+90 and column < pix_in_x+90) and led_UH(5) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --barra de en medio
            elsif ((row > pix_in_y+60 and row < pix_in_y+80) and (column > pix_in_x+90 and column < pix_in_x+40+90) and led_UH(6) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');

            --Decena Minuto
            --barra de arriba
            elsif ((row > pix_in_y and row < pix_in_y+20) and (column > pix_in_x+180 and column < pix_in_x+40+180) and led_DM(0) ='1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de arriba derecha
            elsif ((row > pix_in_y+20 and row < pix_in_y+60) and (column > pix_in_x+40+180 and column < pix_in_x+55+180) and led_DM(1) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de abajo derecha
            elsif ((row > pix_in_y+80 and row < pix_in_y+120) and (column > pix_in_x+40+180 and column < pix_in_x+55+180) and led_DM(2) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --barra de abajo
            elsif ((row > pix_in_y+120 and row < pix_in_y+140) and (column > pix_in_x+180 and column < pix_in_x+40+180) and led_DM(3) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1'); 
            --Laterales de abajo izquierda
            elsif ((row > pix_in_y+80 and row < pix_in_y+120) and (column > pix_in_x-15+180 and column < pix_in_x+180) and led_DM(4) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de arriba izquierda                
            elsif ((row > pix_in_y+20 and row < pix_in_y+60) and (column > pix_in_x-15+180 and column < pix_in_x+180) and led_DM(5) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --barra de en medio
            elsif ((row > pix_in_y+60 and row < pix_in_y+80) and (column > pix_in_x+180 and column < pix_in_x+40+180) and led_DM(6) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Unidad Minuto
            --barra de arriba
            elsif ((row > pix_in_y and row < pix_in_y+20) and (column > pix_in_x+270 and column < pix_in_x+40+270) and led_UM(0) ='1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de arriba derecha
            elsif ((row > pix_in_y+20 and row < pix_in_y+60) and (column > pix_in_x+40+270 and column < pix_in_x+55+270) and led_UM(1) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de abajo derecha
            elsif ((row > pix_in_y+80 and row < pix_in_y+120) and (column > pix_in_x+40+270 and column < pix_in_x+55+270) and led_UM(2) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --barra de abajo
            elsif ((row > pix_in_y+120 and row < pix_in_y+140) and (column > pix_in_x+270 and column < pix_in_x+40+270) and led_UM(3) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1'); 
            --Laterales de abajo izquierda
            elsif ((row > pix_in_y+80 and row < pix_in_y+120) and (column > pix_in_x-15+270 and column < pix_in_x+270) and led_UM(4) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de arriba izquierda                
            elsif ((row > pix_in_y+20 and row < pix_in_y+60) and (column > pix_in_x-15+270 and column < pix_in_x+270) and led_UM(5) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --barra de en medio
            elsif ((row > pix_in_y+60 and row < pix_in_y+80) and (column > pix_in_x+270 and column < pix_in_x+40+270) and led_UM(6) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            
            --Decena Segundo
            --barra de arriba
            elsif ((row > pix_in_y and row < pix_in_y+20) and (column > pix_in_x+360 and column < pix_in_x+40+360) and led_DS(0) ='1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de arriba derecha
            elsif ((row > pix_in_y+20 and row < pix_in_y+60) and (column > pix_in_x+40+360 and column < pix_in_x+55+360) and led_DS(1) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de abajo derecha
            elsif ((row > pix_in_y+80 and row < pix_in_y+120) and (column > pix_in_x+40+360 and column < pix_in_x+55+360) and led_DS(2) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --barra de abajo
            elsif ((row > pix_in_y+120 and row < pix_in_y+140) and (column > pix_in_x+360 and column < pix_in_x+40+360) and led_DS(3) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1'); 
            --Laterales de abajo izquierda
            elsif ((row > pix_in_y+80 and row < pix_in_y+120) and (column > pix_in_x-15+360 and column < pix_in_x+360) and led_DS(4) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de arriba izquierda                
            elsif ((row > pix_in_y+20 and row < pix_in_y+60) and (column > pix_in_x-15+360 and column < pix_in_x+360) and led_DS(5) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --barra de en medio
            elsif ((row > pix_in_y+60 and row < pix_in_y+80) and (column > pix_in_x+360 and column < pix_in_x+40+360) and led_DS(6) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Unidad Segundo
            --barra de arriba
            elsif ((row > pix_in_y and row < pix_in_y+20) and (column > pix_in_x+450 and column < pix_in_x+40+450) and led_US(0) ='1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de arriba derecha
            elsif ((row > pix_in_y+20 and row < pix_in_y+60) and (column > pix_in_x+40+450 and column < pix_in_x+55+450) and led_US(1) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de abajo derecha
            elsif ((row > pix_in_y+80 and row < pix_in_y+120) and (column > pix_in_x+40+450 and column < pix_in_x+55+450) and led_US(2) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --barra de abajo
            elsif ((row > pix_in_y+120 and row < pix_in_y+140) and (column > pix_in_x+450 and column < pix_in_x+40+450) and led_US(3) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1'); 
            --Laterales de abajo izquierda
            elsif ((row > pix_in_y+80 and row < pix_in_y+120) and (column > pix_in_x-15+450 and column < pix_in_x+450) and led_US(4) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --Laterales de arriba izquierda                
            elsif ((row > pix_in_y+20 and row < pix_in_y+60) and (column > pix_in_x-15+450 and column < pix_in_x+450) and led_US(5) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            --barra de en medio
            elsif ((row > pix_in_y+60 and row < pix_in_y+80) and (column > pix_in_x+450 and column < pix_in_x+40+450) and led_US(6) = '1') THEN --b  verde
                red <= (OTHERS => '1');
                green<=(OTHERS => '1');
                blue<=(OTHERS => '1');
            else
                red <= (OTHERS => '0');
                green<=(OTHERS => '0');
                blue<=(OTHERS => '0');
            end if;
        end if;
	end process generador_imagen;
end architecture arqgenerador_imagen;
