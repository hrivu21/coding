library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity jk1 is 
    port(
        j : in STD_LOGIC;
        k : in STD_LOGIC;
        rst : in STD_LOGIC;
        clk : in STD_LOGIC;
        q : out STD_LOGIC);
end jk1;

architecture behavioral of jk1 is
begin
    process(clk, rst)
    begin
        if (rst='1') then
            q <= '0';
        elsif (rising_edge(clk)) then
            if (j='0' and k='0') then
                q <= q;
            elsif (j='0' and k='1') then
                q <= 0;
            elsif (j='1' and k='0') then
                q <= 1;
            elsif (j='1'and k='1') then
                q <= not q;
            end if;
        end if;
    end process;
end behavioral ; -- behavioral





library IEEE;
use IEEE.STD_LOGIC_1164.all;

entity jk2 is 
    port(
        j : in STD_LOGIC;
        k : in STD_LOGIC;
        rst : in STD_LOGIC;
        clk : in STD_LOGIC;
        q : out STD_LOGIC);
end jk2;

architecture behavioral2 of jk1 is
signal jk : STD_LOGIC_VECTOR(1 downto 0);
begin
    process(clk, rst)
    begin
    jk <= j & k; --concatenation
        if (rst='1') then
            q <= '0';
        elsif (rising_edge(clk)) then
            case (jk) is
                when "00" => q <= q;
                when "01" => q <= '0';
                when "10" => q <= '1';
                when "11" => q <= not q;
            end case;
        end if;
    end process;
end behavioral2 ;




library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
 
entity fa is
    port(
        a : in STD_LOGIC;
        b : in STD_LOGIC;
        cin : in STD_LOGIC;
        s : out STD_LOGIC;
        cout : out STD_LOGIC);
end fa;
 
architecture gate_level of full_adder is
begin
    s <= a xor b xor cin ;
    cout <= (a and b) or (cin and a) or (cin and b) ;
end gate_level;






library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
 
entity rca is
    port(
        A : in STD_LOGIC_VECTOR (3 downto 0);
        B : in STD_LOGIC_VECTOR (3 downto 0);
        Cin : in STD_LOGIC;
        Sum : out STD_LOGIC_VECTOR (3 downto 0);
        Cout : out STD_LOGIC);
end rca;
 
architecture structural of rca is 
component full_adder
    port(
        a : in STD_LOGIC;
        b: in STD_LOGIC;
        cin : in STD_LOGIC;
        s : out STD_LOGIC;
        cout : out STD_LOGIC);
end component;
 
signal c1,c2,c3: STD_LOGIC;
 
begin
 
FA1: fa port map( A(0), B(0), Cin, S(0), c1);
FA2: fa port map( A(1), B(1), c1, S(1), c2);
FA3: fa port map( A(2), B(2), c2, S(2), c3);
FA4: fa port map( A(3), B(3), c3, S(3), Cout);
 
end structural;





library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity comparator is
    Port(
        a: in std_logic_vector(7 to 0);
        b: in std_logic_vector(7 to 0);
        g: out std_logic;
        e: out std_logic;
        l: out std_logic);
end comparator;

architecture concurrent of comparator is
begin
    g <= '1' when (a>b) else '0';
    e <= '1' when (a=b) else '0';
    l <= '1' when (a<b) else '0';
end concurrent;




library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
entity generic_comparator is
    generic(
        n: natural:= 8);
    Port(
        a: in std_logic_vector(n-1 to 0);
        b: in std_logic_vector(n-1 to 0);
        g: out std_logic;
        s: out std_logic;
        e: out std_logic);
end generic_comparator;
architecture sequential of generic_comparator is
begin
    process(a, b)
        if (a > b) then
            g <= '1';
        else
            g <= '0';
        end if;

        if (a = b) then
            e <= '1';
        else
            e <= '0';
        end if;

        if (a < b) then
            l <= '1';
        else
            l <= '0';
        end if;        
end concurrent;