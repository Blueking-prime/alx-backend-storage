-- creates a function SafeDiv that divides (and returns) the first by the second number
-- Divides two numbers
DROP FUNCTION IF EXISTS SafeDiv
DELIMITER $$ ;
CREATE FUNCTION SafeDiv (a INT, b INT)
        RETURNS FLOAT
        DETERMINISTIC
                BEGIN
                      IF b=0 THEN
                         RETURN 0;
                      ELSE
                         RETURN ((a * 1.0) / b);
                    END IF;
                  END; $$
DELIMITER ;
