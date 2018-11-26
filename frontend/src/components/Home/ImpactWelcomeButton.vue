<template>
    <div :id="id"
         class="header-button"
         role="button">
        <slot />
    </div>
</template>

<script>
	export default {
		name:  "ImpactWelcomeButton",
		props: {
			id: String
		}
	};
</script>

<style lang="scss" scoped>
    .header-button
    {
        font-family: PierSans, sans-serif;
        display: table-cell;
        vertical-align: middle;
        text-align: center;
        padding: 20px 30px;
        line-height: 0.9;
        font-size: 18pt;
        color: #fff;
        box-shadow: 0 8px 4px 0 rgba(0, 0, 0, 0.4);
        transition: background-color 0.5s ease-in-out,
        top 0.2s linear;
        position: relative;
        top: 0;
        cursor: pointer;

        b
        {
            font-size: 48pt;
            font-weight: normal;
            text-shadow: 0 2px rgba(0, 0, 0, 0.4);
        }
    }

    .header-button:hover
    {
        top: -10px;
    }
</style>