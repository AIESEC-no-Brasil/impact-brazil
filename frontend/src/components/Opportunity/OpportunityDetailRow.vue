<template>
    <b-row v-if="separator">
        <b-col cols="12">
            <hr>
        </b-col>
    </b-row>
    <b-row v-else-if="fullspan">
        <b-col cols="12" class="heading nospace">
            {{title}}
        </b-col>
        <b-col cols="12" class="bigspace">
            <slot></slot>
        </b-col>
    </b-row>
    <b-row v-else>
        <b-col cols="4" class="text-right">
            {{title}}
        </b-col>
        <b-col cols="8"  :class="bigspace ? 'bigspace' : ''">
            <slot></slot>
        </b-col>
    </b-row>
</template>

<script>
	import bCol from 'bootstrap-vue/es/components/layout/col';
	import bRow from 'bootstrap-vue/es/components/layout/row';

	export default {
		name:       "OpportunityDetailRow",
		components: {
			bCol,
			bRow,
		},
		props:      {
			title:     String,
			separator: Boolean,
			fullspan:  Boolean,
			bigspace:  Boolean
		}
	};
</script>

<style scoped>
    .row:not(.nospace)
    {
        margin-bottom: 4px;
    }

    .bigspace
    {
        margin-bottom: 16px;
    }

    .text-right, .heading
    {
        font-family: PierSans, sans-serif;
    }
</style>