<template>
    <div id="options-menu">
        <div id="options-left">
            Showing <b>IT</b> opportunities for <b>Global Talent</b>
        </div>
        <div id="options-right">
            <b-dropdown id="timespan" variant="transparent" right size="sm" text="January 2019">
                <b-dropdown-item>Global Volunteer</b-dropdown-item>
                <b-dropdown-item>Global Talent</b-dropdown-item>
                <b-dropdown-item>Global Entrepreneur</b-dropdown-item>
            </b-dropdown>
            <b-dropdown id="prog" variant="transparent" right size="sm" text="Global Talent">
                <b-dropdown-item>Global Volunteer</b-dropdown-item>
                <b-dropdown-item>Global Talent</b-dropdown-item>
                <b-dropdown-item>Global Entrepreneur</b-dropdown-item>
            </b-dropdown>
            <b-dropdown id="subproductOrSdg" variant="transparent" right size="sm" text="IT">
                <b-dropdown-item>Global Volunteer</b-dropdown-item>
                <b-dropdown-item>Global Talent</b-dropdown-item>
                <b-dropdown-item>Global Entrepreneur</b-dropdown-item>
            </b-dropdown>
        </div>
    </div>
    {{ route.$query }}
</template>

<script>
	import bDropdown from 'bootstrap-vue/es/components/dropdown/dropdown';
	import bDropdownItem from 'bootstrap-vue/es/components/dropdown/dropdown-item';

	export default {
		name:       "OpportunityOptions",
		components: {
			bDropdown,
			bDropdownItem,
		},
	};
</script>

<style lang="scss" scoped>
    #options-left
        {
            float: left;
        }

        #options-right
        {
            float: right;
        }

        #options-right /deep/
        {
            button
            {
                margin-left: 8px;
            }
        }

        #options-menu:after
        {
            content: "";
            clear: both;
            display: block;
        }
</style>