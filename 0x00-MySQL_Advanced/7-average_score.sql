-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
-- Computes the average score of a student
drop procedure IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$ ;
CREATE PROCEDURE ComputeAverageScoreForUser (user_id INTEGER)
 BEGIN
       UPDATE users
          SET average_score=(SELECT (SUM(score) / COUNT(score))
                               FROM corrections
                              WHERE corrections.user_id=user_id)
        WHERE id=user_id;
   END;$$
DELIMITER ;
