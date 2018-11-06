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
        <o-row title="Fees">{{oppFees}}</o-row>
        <o-row title="Fee Breakdown" fullspan v-if="$session.get('loggedIn')">
            To be paid to AIESEC in your home entity once you are accepted for this opportunity:<br>
            <b>{{opportunity.opportunity_cost.programme_fee}} {{opportunity.opportunity_cost.currency}} </b><br>
            <br>
            To be paid to AIESEC in Brazil once you arrive - in cash, in either US Dollars or
            Brazilian Reais:<br>
            <b>{{opportunity.opportunity_cost.project_fee}}
                {{opportunity.opportunity_cost.currency}}</b><br><br>
            <span v-html="feeCovers"></span><br><br>
            <small><a
                    href="https://help.aiesec.org/opportunities/how-is-the-price-for-an-exchange-opportunity-determined"
                    target="_blank">Learn more</a> about the fees.
            </small>
        </o-row>
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
			},
			oppFees()
			{
				if (this.opportunity.opportunity_cost === null)
					return "Unknown";
				else if (!this.$session.get('loggedIn'))
					return `Please log in to view the fees you will pay for this opportunity in your own currency.`;
				else
					return `${this.opportunity.opportunity_cost.total} ${this.opportunity.opportunity_cost.currency}`;
			},
			feeCovers()
			{
				if (this.opportunity.transparent_fee_details === null || typeof this.opportunity.transparent_fee_details === "undefined")
					return "";
				else
				{
					let covers = [];
					if (this.opportunity.transparent_fee_details.covers_accommodation)
						covers.push("&middot; Covers accommodation");
					if (this.opportunity.transparent_fee_details.covers_administrative_costs)
						covers.push("&middot; Covers administrative costs");
					if (this.opportunity.transparent_fee_details.covers_leadership_spaces)
						covers.push("&middot; Covers leadership spaces");
					if (this.opportunity.transparent_fee_details.covers_pickup)
						covers.push("&middot; Covers pickup from the airport");
					if (this.opportunity.transparent_fee_details.sponsored_by)
						covers.push(`<br>Opportunity sponsored by ${this.opportunity.transparent_fee_details.sponsored_by}`);

					return covers.join("<br>");
				}
			}
		}
	}
	;
</script>

<style scoped>

</style>