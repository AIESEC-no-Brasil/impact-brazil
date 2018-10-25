<!--suppress XmlDuplicatedId -->
<template>
    <div id="opportunity-list-root">
        <OpportunityOptions/>
        <div v-if="oppList.length > 0" id="opportunities-list">
            <OpportunityCard v-for="opp in oppList"
                             :ref="opp.id"
                             :opp="opp"/>
        </div>
        <div v-else id="opportunities-list">
            <Loading center dark/>
        </div>
    </div>
</template>

<script>
	import OpportunityOptions from './OpportunityOptions.vue';
	import OpportunityCard from './OpportunityCard.vue';
	import Loading from '../Loading';
	import axios from 'axios';
	import {config} from '../../config';

	export default {
		name:       "OpportunityList",
		components: {
			OpportunityOptions,
			OpportunityCard,
			Loading,
		},
		data()
		{
			return {
				oppList: []
			};
		},
		async mounted()
		{
			let opps = await axios.get("http://127.0.0.1:8000/api/opportunities.json?entity=1&start_date=1&end_date=1&product=5&subproduct=15"); // FIXME: temporary!
			// TODO: handle error

            // Ensure we remove extra details like [Venture Brazil] from the title
            opps.data.forEach((opp) => {
            	opp.title = opp.title.replace(/^\[(.*)]( - )?/, '');
            });
			this.oppList = opps.data;
		}
	};
</script>

<style scoped>
    #opportunities-list
    {
        margin-top: 24px;
    }
</style>