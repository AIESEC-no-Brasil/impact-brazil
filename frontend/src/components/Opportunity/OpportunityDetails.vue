<template>
    <div id="details-opportunity">
        <transition-group name="tab-transition">
            <OpportunityOverview v-if="tab === 'overview'"
                                 :opportunity="opportunity"
                                 :extra="extra"
                                 key="overview"/>
            <OpportunityRole v-if="tab === 'role'"
                             :opportunity="opportunity"
                             :extra="extra"
                             key="role"/>
            <OpportunityPrerequisites v-if="tab === 'prerequisites'"
                                      :opportunity="opportunity"
                                      key="prerequisites"/>
            <OpportunityLogistics v-if="tab === 'logistics'"
                                  :opportunity="opportunity"
                                  key="logistics"/>
            <OpportunityVisa v-if="tab === 'visa'"
                             :opportunity="opportunity"
                             key="visa"/>
        </transition-group>
    </div>
</template>

<script>
	import OpportunityDetailRow from './OpportunityDetailRow.vue';
	import OpportunityOverview from './OpportunityTabs/OpportunityOverview.vue';
	import OpportunityRole from './OpportunityTabs/OpportunityRole.vue';
	import OpportunityPrerequisites from './OpportunityTabs/OpportunityPrerequisites.vue';
	import OpportunityLogistics from './OpportunityTabs/OpportunityLogistics.vue';
	import OpportunityVisa from './OpportunityTabs/OpportunityVisa.vue';

	export default {
		name:       "OpportunityDetails",
		components: {
			OpportunityOverview,
			OpportunityRole,
			OpportunityPrerequisites,
			OpportunityLogistics,
			OpportunityVisa,
			oRow: OpportunityDetailRow
		},
		props:      {
			opportunity: Object,
			extra:       Object,
			tab:         {
				type:    String,
				default: 'overview'
			},
		},
	};
</script>

<style scoped>
    #details-opportunity
    {
        color: #353535;
    }

    #details-opportunity >>> .title
    {
        font-family: PierSans, sans-serif;
        font-size: 30px;
    }

    #details-opportunity >>> .badge
    {
        font-weight: normal !important;
        position: relative;
        top: -2px;
    }

    .tab-transition-enter, .tab-transition-leave-to
    {
        opacity: 0;
    }

    .tab-transition-enter-active, .tab-transition-leave-active
    {
        transition: opacity 0.2s;
    }

    .tab-transition-enter-active
    {
        transition-delay: 0.2s;
    }
</style>