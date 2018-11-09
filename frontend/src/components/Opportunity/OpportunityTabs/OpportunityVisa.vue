<template>
    <div id="visa">
                <div class="title">
                    Visa
                </div>

                <o-row title="Visa type">{{opportunity.legal_info.visa_type}}</o-row>
                <o-row title="Visa duration">{{opportunity.legal_info.visa_duration}}</o-row>
                <o-row title="Visa link">
                    <a :href="opportunity.legal_info.visa_link" target="_blank">{{opportunity.legal_info.visa_link}}</a>
                </o-row>
                <o-row separator/>
                <o-row title="Health insurance" fullspan>{{opportunity.legal_info.health_insurance_info}}</o-row>
            </div>
</template>

<script>
	import OpportunityDetailRow from '../OpportunityDetailRow.vue';

	export default {
		name:       "OpportunityVisa",
		components: {
			oRow: OpportunityDetailRow
		},
		props:      {
			opportunity: Object
		},
	};
</script>

<style scoped>

</style>