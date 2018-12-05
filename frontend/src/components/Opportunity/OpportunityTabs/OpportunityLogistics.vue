<template>
    <div id="logistics">
        <div class="title">
            Logistics
        </div>

        <o-row title="Working hours">
            {{opportunity.specifics_info.expected_work_schedule.from}}:00 -
            {{opportunity.specifics_info.expected_work_schedule.to}}:00<br>
            {{opportunity.specifics_info.saturday_work === 'true' ? "Monday-Saturday" : "Monday-Friday"}}
        </o-row>
        <o-row separator/>
        <o-row title="Computer provided">
            <span v-html="checkmark(opportunity.specifics_info.computer === 'true')"></span>
        </o-row>
        <o-row title="Accommodation provided">
            <span v-html="checkmark(opportunity.logistics_info.accommodation_provided === 'Provided')"></span>
        </o-row>
        <o-row title="Accommodation covered">
            <span v-html="checkmark(opportunity.logistics_info.accommodation_covered === 'true')"></span>
        </o-row>
        <o-row title="Food covered">
            <span v-html="checkmark(opportunity.logistics_info.food_covered !== 'Not covered')"></span>
            {{opportunity.logistics_info.food_covered === 'Not covered' ? '' : opportunity.logistics_info.food_covered}}
        </o-row>
        <o-row separator/>
        <o-row title="Host">{{opportunity.home_lc.full_name}}</o-row>
        <o-row title="Location">
            <i class="material-icons" style="vertical-align: middle; position: relative; top: -2px;">location</i>
            <a :href="`https://maps.google.com/?q=${opportunity.location}`"
               rel="noopener"
               target="_blank">{{opportunity.location}}</a>
        </o-row>
    </div>
</template>

<script>
	import OpportunityDetailRow from '../OpportunityDetailRow.vue';

	export default {
		name:       "OpportunityLogistics",
		components: {
			oRow: OpportunityDetailRow
		},
		props:      {
			opportunity: Object
		},
		methods:    {
			checkmark(item)
			{
				return item ? "<span class='badge badge-success'>Yes</span>" : "<span class='badge badge-danger'>No</span>";
			}
		}
	};
</script>

<style scoped>

</style>