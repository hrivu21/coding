library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity decoder1 is
    port(
        a : in STD_LOGIC_VECTOR (2 downto 0);
        b : out STD_LOGIC_VECTOR (7 downto 0));    ;
end decoder1;


architecture concurrent1 of decoder1 is
begin
    
    b <="00000001" when a="000" else
        "00000010" when a="001" else
        "00000100" when a="010" else
        "00001000" when a="011" else
        "00010000" when a="100" else
        "00100000" when a="101" else
        "01000000" when a="110" else
        "10000000" when a="111" else "XXXXXXXX";

end concurrent1;














library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity decoder2 is
    port(
        a : in STD_LOGIC_VECTOR (2 downto 0);
        b : out STD_LOGIC_VECTOR (7 downto 0));
end decoder2;

architecture concurrent2 of decoder2 is
begin

    with a select
    b <="00000001" when "000",
        "00000010" when "001",
        "00000100" when "010",
        "00001000" when "011",
        "00010000" when "100",
        "00100000" when "101",
        "01000000" when "110",
        "10000000" when "111",
        "XXXXXXXX" when others;

end concurrent2;












library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity decoder3 is
    port(
        a : in STD_LOGIC_VECTOR (2 downto 0);
        b : out STD_LOGIC_VECTOR (7 downto 0));
end decoder3;

architecture sequential1 of decoder3 is
begin
    process(a)
        if (a="000") then
            b <= "00000001";
        elsif (a="001") then
            b <= "00000010";
        elsif (a="010") then
            b <= "00000100";
        elsif (a="011") then
            b <= "00001000";
        elsif (a="100") then            
            b <= "00010000";
        elsif (a="101") then
            b <= "00100000";
        elsif (a="110") then
            b <= "01000000";
        elsif (a="111") then
            b <= "10000000";
        else
            b <= "XXXXXXXX";
        end if;
    end process;
end sequential1;











library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity decoder4 is
    port(
        a : in STD_LOGIC_VECTOR (2 downto 0);
        b : out STD_LOGIC_VECTOR (7 downto 0));
end decoder4;


architecture sequential2 of decoder4 is
begin

    process(a)
    begin

        case a is 
            when "000" => b <= "00000001";
            when "000" => b <= "00000010";
            when "000" => b <= "00000100";
            when "000" => b <= "00001000";
            when "000" => b <= "00010000";
            when "000" => b <= "00100000";
            when "000" => b <= "01000000";
            when "000" => b <= "10000000";
            when others => b <= "XXXXXXXX"
        end case;

    end process;
    
end architecture sequential2;


