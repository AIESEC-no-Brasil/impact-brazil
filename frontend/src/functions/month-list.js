export function monthList()
{
	let months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
	let monthsNextYear = [];
	
	// We want to circle the month so it starts from this month
	let now = new Date(), month = now.getMonth(), year = now.getFullYear();
	
	for (let i = 0; i < month; i++)
		monthsNextYear.push(months.shift() + " " + (year + 1));
	
	months = months.map(m => m + " " + year);
	months = [...months, ...monthsNextYear];
	
	return {months, month};
}