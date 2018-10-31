<template>
    <div id="overview">
        <div class="title">
            Overview
        </div>

        <o-row title="Opportunity">{{opportunity.title}}</o-row>
        <o-row v-if="extra.name" :title="projectOrField">
            {{extra.name}}
        </o-row>
        <o-row v-else :title="projectOrField">
            <Loading dark small/>
        </o-row>
        <o-row title="Location">{{opportunity.location}}</o-row>
        <o-row title="Host">{{opportunity.home_lc.full_name}}</o-row>
        <o-row separator/>
        <o-row title="Languages">
            {{opportunity.languages.reduce((accumulator, current) => accumulator =
            accumulator + `, ${current.constant_name}`, "").substr(2)}}
        </o-row>
        <o-row separator/>
        <o-row title="Earliest Start Date">
            {{dateFormat(opportunity.earliest_start_date, "d mmm, yyyy")}}
        </o-row>
        <o-row title="Latest End Date">
            {{dateFormat(opportunity.latest_end_date, "d mmm, yyyy")}}
        </o-row>
        <o-row title="Duration">{{opportunity.duration}} weeks</o-row>
        <o-row separator/>
        <o-row title="Salary">
            {{opportunity.specifics_info.salary === 0 || opportunity.specifics_info.salary === null
            ? "Unpaid"
            : `${opportunity.specifics_info.salary}
            ${opportunity.specifics_info.salary_currency === null
            ? ''
            : opportunity.specifics_info.salary_currency.alphabetic_code}`}}
        </o-row>
        <o-row title="Positions">{{opportunity.available_openings}}</o-row>
        <o-row separator/>
        <o-row title="Fees">Unknown <!-- FIXME --></o-row>
    </div>
</template>

<script>
	import OpportunityDetailRow from '../OpportunityDetailRow.vue';
	import Loading from '../../Loading.vue';

	import dateFormat from 'dateformat';


	export default {
		name:       "OpportunityOverview",
		components: {
			oRow: OpportunityDetailRow,
			Loading
		},
		props:      {
			opportunity: Object,
			extra:       Object
		},
		data()
		{
			return {
				dateFormat,
			};
		},
		computed:   {
			projectOrField()
			{
				return parseInt(this.opportunity.programme.id) === 1 ? 'Project' : 'Field';
			}
		}
	};
</script>

<style scoped>

</style>