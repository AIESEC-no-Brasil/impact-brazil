<template>
    <div id="role">
        <div class="title">
            Role
        </div>

        <o-row title="Project" fullspan v-if="parseInt(this.opportunity.programme.id) === 1">
            <span v-if="extra.name" style='font-size: 1.2em'>{{extra.name}}</span>
            <Loading v-else small/>
            <br>
            {{opportunity.sdg_info.sdg_target.description}}
        </o-row>
        <o-row title="Organization" fullspan v-else>
            <span style='font-size: 1.2em'>{{opportunity.branch.company.name}}</span><br>
            {{opportunity.branch.address_detail.city}}, {{opportunity.branch.address_detail.country}}
        </o-row>
        <o-row title="Role description" fullspan>
            {{markdown(opportunity.description)}}
        </o-row>
        <o-row title="Main activities" fullspan>
            <ul style="margin-left: 24px;">
                <li v-for="activity in opportunity.role_info.learning_points_list" :key="activity">{{activity}}</li>
            </ul>
        </o-row>
    </div>

</template>

<script>
	import OpportunityDetailRow from '../OpportunityDetailRow.vue';
	import Loading from '../../Loading.vue';
	import MarkdownIt from 'markdown-it';


	export default {
		name:       "OpportunityRole",
		components: {
			oRow: OpportunityDetailRow,
			Loading
		},
		props:      {
			opportunity: Object,
			extra:       Object
		},
		methods:    {
			markdown(text)
			{
				let md = new MarkdownIt();
				return md.render(text);
			},
		}
	};
</script>

<style scoped>

</style>