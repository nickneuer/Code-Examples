/*This is an old homework assignment from a friends database managment class that I completed to practice SQL queries. Comments above describe the queries made below them.*/ 

/*Returns the statecode, county name and 2010 population of all counties who had a population of over 2,000,000 in 2010 in descending order from most populated to least*/

SELECT statecode, name, population_2010 FROM counties WHERE population_2010 > 2000000 ORDER BY population_2010 DESC;

/*Returns a list of statecodes and the number of counties in that state, ordered from the least number of counties to the most
*/

SELECT statecode, COUNT(*) FROM counties GROUP BY statecode; 

/*Returns average number of counties per state*/ 

SELECT AVG(c) FROM (SELECT statecode, COUNT(*) c FROM counties GROUP BY statecode);

/*returns a count of how many states have more than the average number of counties*/

SELECT COUNT(*) FROM (SELECT statecode, COUNT(*) C FROM counties GROUP BY statecode) AS T WHERE T.C > (SELECT AVG(T.C) FROM (SELECT statecode, COUNT(*) AS C FROM counties GROUP BY statecode) AS T);
				
/*returns the statecodes of states whose 2010 population does not equal the sum of the 2010 populations of their counties*/

SELECT statecode FROM states, (SELECT statecode c, SUM(population_2010) p FROM counties GROUP BY statecode) T WHERE states.statecode = T.c AND states.population_2010 != T.p;

/*Gives number of states that have at least one senator whose first name is John, Johnny, or Jon*/

SELECT COUNT(DISTINCT statecode) FROM senators WHERE name LIKE 'John %' OR name LIKE 'Johnny %' OR name LIKE 'Jon %';

/*Outputs the statecode, year the state was admitted to the union, senator name, and year the senator was born for all the senators who were born in a year before the year their state was admitted to the union*/

SELECT statecode, admitted_to_union, name, born FROM senators x, states y WHERE x.statecode = y.statecode AND x.born < cast(strftime('%Y',y.admitted_to_union) as integer);  

/*Returns the name of the county and the number of people who left between 1950 and 2010 (as a positive number) for all the counties of West Virginia whose population shrunk between 1950 and 2010.*/

SELECT name, ABS(population_1950 - population_2010) FROM counties WHERE statecode = 'WV' AND population_2010 < population_1950;

/*Returns the statecode of the state(s) that is (are) home to the most committee chairmen*/

SELECT statecode FROM (SELECT statecode, COUNT(chairman) n  FROM committees c, senators s WHERE c.chairman = s.name  GROUP BY statecode)WHERE n = (SELECT MAX(n) FROM (SELECT statecode, COUNT(chairman) n FROM committees c, senators s WHERE c.chairman = s.name GROUP BY statecode));

/*Returns the statecode of the state(s) that are not the home of any committee chairmen*/

SELECT DISTINCT senators.statecode FROM senators WHERE senators.statecode NOT IN (SELECT DISTINCT senators.statecode FROM senators, committees WHERE senators.name = committees.chairman); 

/* Returns the id of the parent committee, the name of the parent committee's chairman, the id of the subcommittee, and name of that subcommittee's chairman for all subcommittes whose chairman is the same as the chairman of its parent committee*/

SELECT par.id, par.chairman, sub.id, sub.chairman FROM committees sub, committees par WHERE sub.parent_committee = par.id AND sub.chairman = par.chairman;

/*Returns the id of the parent committee,  its chairman, the year the chairman was born, the id of the submcommittee, it’s chairman and the year the subcommittee chairman was born for each subcommittee where the subcommittee’s chairman was born in an earlier year than the chairman of its parent committee*/

SELECT par.id, par.chairman, par_sen.born, sub.id, sub.chairman, sub_sen.born FROM committees sub, committees par, senators sub_sen, senators par_sen WHERE sub.parent_committee = par.id AND sub.chairman = sub_sen.name AND par.chairman = par_sen.name AND sub_sen.born < par_sen.born;


