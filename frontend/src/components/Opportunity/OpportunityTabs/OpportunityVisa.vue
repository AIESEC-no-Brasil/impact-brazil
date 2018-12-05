<template>
    <div id="visa">
        <div class="title">
            Visa
        </div>

        <o-row title="Visa type">{{opportunity.legal_info.visa_type}}</o-row>
        <o-row title="Visa duration">{{opportunity.legal_info.visa_duration}}</o-row>
        <o-row title="Visa link">
            <a class="dont-break-out" :href="opportunity.legal_info.visa_link" target="_blank">
                {{opportunity.legal_info.visa_link}}
            </a>
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
    .dont-break-out
    {

        /* These are technically the same, but use both */
        overflow-wrap: break-word;
        word-wrap: break-word;

        -ms-word-break: break-all;
        /* This is the dangerous one in WebKit, as it breaks things wherever */
        word-break: break-all;
        /* Instead use this non-standard one: */
        word-break: break-word;

        /* Adds a hyphen where the word breaks, if supported (No Blink) */
        -ms-hyphens: auto;
        -moz-hyphens: auto;
        -webkit-hyphens: auto;
        hyphens: auto;

    }
</style>