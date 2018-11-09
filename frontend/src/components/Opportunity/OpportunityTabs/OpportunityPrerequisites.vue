<template>
    <div id="prerequisites">
        <div class="title">
            Prerequisites
        </div>

        <o-row title="Backgrounds" bigspace>
            <span v-html="reqSorter(opportunity.backgrounds)"></span>
        </o-row>
        <o-row title="Skills" bigspace>
            <span v-html="reqSorter(opportunity.skills)"></span>
        </o-row>
        <o-row title="Citizenships" bigspace>
            <span v-html="reqSorter(opportunity.nationalities)"></span>
        </o-row>
        <o-row title="Languages" bigspace>
            <span v-html="reqSorter(opportunity.languages)"></span>
        </o-row>
        <o-row title="Study Levels" bigspace>
            <span v-html="reqSorter(opportunity.study_levels)"></span>
        </o-row>
        <o-row separator/>
        <o-row title="Selection Process" fullspan>{{opportunity.role_info.selection_process}}</o-row>
    </div>
</template>

<script>
	import OpportunityDetailRow from '../OpportunityDetailRow.vue';

	export default {
		name:       "OpportunityPrerequisites",
		components: {
			oRow: OpportunityDetailRow
		},
		props:      {
			opportunity: Object
		},
		methods:    {
			reqSorter(list)
			{
				if (list && list.length > 0)
				{
					// We can technically do this inline with a .sort() and a .reduce() and ternary, but...
					// This way is more readable
					let retList = [];
					let sortedList = JSON.parse(JSON.stringify(list));
					sortedList.sort((a) => a.option === "required" ? -1 : 1);

					sortedList.forEach(item => {
							let thisItem = item.constant_name ? item.constant_name : item.name;
							if (item.option === "required")
								thisItem += " <span class='badge badge-danger'>Required</span>";
							else
								thisItem += " <span class='badge badge-secondary'>Preferred</span>";
							retList.push(thisItem);
						}
					);
					return retList.join("<br>");
				}

				return "No preferences";
			},
		}
	};
</script>

<style scoped>

</style>