<template>
    <div class="section">
        <div class="title">
            {{[null, "GV", "GT", null, null, "GE"][$route.params.prod]}} Opportunities
            &middot; <a href="#" v-if="opps.length > 0" @click="csvExport">Export as Spreadsheet</a>
        </div>
        <table-component :data="opps" id="opps" v-if="opps.length > 0">
            <table-column show="gis_id" label="Opp. ID"></table-column>
            <table-column show="lc.reference_name" label="LC"></table-column>
            <table-column show="title" label="Title"></table-column>
            <table-column show="organization_name" label="Organization"></table-column>
            <table-column label="Duration">
                <template slot-scope="row">{{row.duration}} weeks</template>
            </table-column>
            <table-column show="available_openings" label="Openings"></table-column>
            <table-column show="start_date" label="Start Date" data-type="date:YYYY-MM-DD"></table-column>
            <table-column show="end_date" label="End Date" data-type="date:YYYY-MM-DD"></table-column>
            <table-column show="close_date" label="Close Date" data-type="date:YYYY-MM-DD"></table-column>
        </table-component>
        <div style="padding: 35vh 0; text-align: center;" v-else>
            <Loading dark center/>
            Getting opportunity data, this could take a few minutes...
        </div>
    </div>
</template>

<script>
	import {TableComponent, TableColumn} from 'vue-table-component';
	import Loading from '../components/Loading.vue';
	import axios from 'axios';
	import {config} from "../config";

	export default {
		name:       "Searchtool",
		components: {
			Loading,
			TableComponent,
			TableColumn,
		},
		data()
		{
			return {
				tf:   null,
				opps: [],
			};
		},
		methods:    {
			csvExport()
			{
				if (this.opps.length === 0)
					return false;

				let data = [["Opp. ID", "LC", "Title", "Organization", "Duration", "Openings", "Start Date", "End Date", "Close Date"]];
				let data_csv = [];
				this.opps.forEach(opp => data.push([opp.id, opp.lc.reference_name, opp.title, opp.organization, opp.duration, opp.available_openings, opp.start_date, opp.end_date, opp.close_date]));

				data.forEach(opp => {
					let row = [];
					opp.forEach(str => row.push(str !== undefined ? `"${str.toString().replace('"', '""')}"` : `""`));
					data_csv.push(row);
				});

				let csvContent = "data:text/csv;charset=utf-8,";
				csvContent += "\ufeff"; // This ensures it's UTF-8
				data_csv.forEach(opp => {
					let row = opp.join(",");
					csvContent += row + "\r\n";
				});

				var encodedUri = encodeURI(csvContent);
				var link = document.createElement("a");
				link.setAttribute("href", encodedUri);
				link.setAttribute("download", "opportunities.csv");
				document.body.appendChild(link);

				link.click();
				return true;
			}
		},
		async mounted()
		{
			if (!this.$route.params.prod)
			{
				this.$router.push('/404');
			}
			else
			{
				let product = parseInt(this.$route.params.prod);
				let oppData;
				try
				{
					oppData = await axios.get(config.api + config.endpoints.opportunities + '?all_opps=true&product=' + product);
				}
				catch (err)
				{
					console.error(err);
					this.$root.$emit('error');
					return;
				}

				this.opps = oppData.data;

			}
		}
	};
</script>

<style>
    .title
    {
        margin-top: 10px;
        font-size: 2em;
    }

    *,
    *:after,
    *:before
    {
        position: relative;
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    .table-component
    {
        display: flex;
        flex-direction: column;
        margin: 4em 0;
    }

    .table-component__filter
    {
        align-self: flex-end;
    }

    .table-component__filter__field
    {
        padding: 0 1.25em 0 .75em;
        height: 2.5em;
        border: solid 2px #e0e0e0;
        border-radius: 2em;
        font-size: inherit;
    }

    .table-component__filter__clear
    {
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        width: 2em;
        color: #007593;
        font-weight: bold;
        cursor: pointer;
    }

    .table-component__filter__field:focus
    {
        outline: 0;
        border-color: #007593;
    }

    .table-component__table-wrapper
    {
        overflow-x: auto;
        margin: 1em 0;
        width: 100%;
        border: solid 1px #ddd;
        border-bottom: none;
    }

    .table-component__table
    {
        min-width: 100%;
        border-collapse: collapse;
        border-bottom: solid 1px #ddd;
        table-layout: fixed;
    }

    .table-component__table__caption
    {
        position: absolute;
        top: auto;
        left: -10000px;
        overflow: hidden;
        width: 1px;
        height: 1px;
    }

    .table-component__table th,
    .table-component__table td
    {
        padding: .75em 1.25em;
        vertical-align: top;
        text-align: left;
    }

    .table-component__table th
    {
        background-color: #e0e0e0;
        color: #999;
        text-transform: uppercase;
        white-space: nowrap;
        font-size: .85em;
    }

    .table-component__table tbody tr:nth-child(even)
    {
        background-color: #f0f0f0;
    }

    .table-component__table a
    {
        color: #007593;
    }

    .table-component__message
    {
        color: #999;
        font-style: italic;
    }

    .table-component__th--sort,
    .table-component__th--sort-asc,
    .table-component__th--sort-desc
    {
        text-decoration: underline;
        cursor: pointer;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }

    .table-component__th--sort-asc:after,
    .table-component__th--sort-desc:after
    {
        position: absolute;
        left: .25em;
        display: inline-block;
        color: #bbb;
    }

    .table-component__th--sort-asc:after
    {
        content: '↑';
    }

    .table-component__th--sort-desc:after
    {
        content: '↓';
    }
</style>