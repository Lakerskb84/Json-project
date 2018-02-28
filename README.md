# Json project

Used the world_data_projects.json and loaded it using pandas. Normalized the columns 'mjtheme_namecode' and 'countryname' I then changed the values for the code, name and countryname column to correspond with length using applymap(len). Any length that was not blank would have a value of 1 or greater so I changed all values less than 1 to NaN using np.nan. grouped project name together sorting the values in ascending order to obtain the greatest number of projects and printing out the top ten using .head(10). I did the same thing for top 10 countries.
