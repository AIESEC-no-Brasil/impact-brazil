// This function takes an array of endpoints, loads them simultaneously and returns an object with all the data ready
// In the future, maybe it would be more efficient to have a separate then() for each promise, but the chances of one
// specific holding back the data low are too low to bother with this!
import axios from 'axios';
import {config} from '../config';

export async function dataLoad(vm, endpoints)
{
	let promiseArray = [];
	endpoints.forEach(endpoint => {
		let data;
		let storedList = vm.$store.getters.getList(endpoint);
		
		if (storedList && storedList.length > 0)
			data = {data: storedList};
		else
			data = axios.get(config.api + config.endpoints[endpoint]);
		
		promiseArray.push(data);
	});
	
	let promiseGet;
	try
	{
		promiseGet = await Promise.all(promiseArray);
	}
	catch (err)
	{
		console.error(err);
		vm.$root.$emit('error');
		return false;
	}
	
	let promiseOut = {};
	for (let i = 0; i < endpoints.length; i++)
	{
		if (promiseGet.hasOwnProperty(i) && endpoints.hasOwnProperty(i))
		{
			promiseOut[endpoints[i]] = promiseGet[i].data;
			vm.$store.commit('setList', {list: endpoints[i], arr: promiseGet[i].data});
		}
	}
	
	return promiseOut;
}