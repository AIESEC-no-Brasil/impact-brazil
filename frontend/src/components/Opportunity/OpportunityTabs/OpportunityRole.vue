<template>
    <div id="role">
        <div class="title">
            Role
        </div>

        <span v-if="parseInt(this.opportunity.programme.id) === 1">
            <o-row title="Project" fullspan>
                <table border="0">
                    <tr>
                        <td>
                            <img :src="`${getLogoDirectory(opportunity.programme.id)}${project.logo}`"
                                 v-if="project.logo"
                                 class="project-logo">
                        </td>
                        <td>
                            <div style='font-size: 1.2em'>{{project.name}}</div>
                            {{project.description}}<br>
                            <Loading v-if="!project.name" dark small/>
                        </td>
                    </tr>
                </table>
            </o-row>
            <o-row title="Sustainable Development Goal" fullspan>
                <table border="0">
                    <tr>
                        <td>
                            <img :src="`${getLogoDirectory(opportunity.programme.id)}${extra.field.logo}`"
                                 v-if="extra.field.logo"
                                 class="project-logo">
                        </td>
                        <td>
                            <span v-if="extra.field.name" style='font-size: 1.2em'>{{extra.field.name}}</span>
                            <Loading v-else dark small/>
                            <br>
                            {{opportunity.sdg_info.sdg_target.description}}
                        </td>
                    </tr>
                </table>
            </o-row>
        </span>
        <span v-else>
            <o-row title="Organization" fullspan>
                <span style='font-size: 1.2em'>{{opportunity.branch.company.name}}</span><br>
                {{opportunity.branch.address_detail.city}}, {{opportunity.branch.address_detail.country}}
            </o-row>
            <o-row title="Field" fullspan>
                <table border="0">
                    <tr>
                        <td>
                            <img :src="`${getLogoDirectory(opportunity.programme.id)}${extra.field.logo}`"
                                 v-if="extra.field.logo"
                                 class="project-logo">
                        </td>
                        <td>
                            <span v-if="extra.field.name" style='font-size: 1.2em'>{{extra.field.name}}</span>
                            <Loading v-else dark small/>
                            <span v-if="extra.field.description">{{extra.field.description}}</span>
                        </td>
                    </tr>
                </table>
            </o-row>
        </span>
        <o-row title="Role description" fullspan>
            <div v-html="markdown(opportunity.description)"></div>
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
	import {config} from '../../../config';


	export default {
		name:       "OpportunityRole",
		components: {
			oRow: OpportunityDetailRow,
			Loading
		},
		props:      {
			opportunity: Object,
			extra:       Object,
			project:     Object,
		},
		methods:    {
			markdown(text)
			{
				let md = new MarkdownIt();
				return md.render(text);
			},
			getLogoDirectory(product)
			{
				switch (parseInt(product))
				{
					case 1:
						return config.logos.sdgs;

					case 2:
						return config.logos.subproductsGT;

					case 5:
						return config.logos.subproductsGE;
				}
			},
		}
	};
</script>

<style scoped>
    #role >>> .project-logo
    {
        margin-right: 12px;
    }
</style>