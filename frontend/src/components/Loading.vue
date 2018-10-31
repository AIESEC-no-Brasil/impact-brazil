<template>
    <div :class="[dark ? 'dark' : '', 'spinner', center ? 'center' : '', small ? 'small' : '']">
        <div class="bounce1"></div>
        <div class="bounce2"></div>
        <div class="bounce3"></div>
    </div>
</template>

<script>
	export default {
		name:  "Loading",
		props: {
			center: Boolean,
			dark:   Boolean,
			small:  Boolean
		}
	};
</script>

<style scoped>
    .spinner
    {
        /*margin: auto auto 0;*/
        margin-top: 40px;
        width: 100px;
        text-align: center;
    }

    .center
    {
        margin-left: auto;
        margin-right: auto;
    }

    .spinner > div
    {
        width: 18px;
        height: 18px;
        margin-right: 10px;
        background-color: #fff;

        border-radius: 100%;
        display: inline-block;
        -webkit-animation: sk-bouncedelay 1.4s infinite ease-in-out both;
        animation: sk-bouncedelay 1.4s infinite ease-in-out both;
    }

    .dark > div
    {
        background-color: #444;
    }

    .small
    {
        margin-top: 4px;
    }

    .small > div
    {
        width: 8px;
        height: 8px;
    }
    .spinner .bounce1
    {
        -webkit-animation-delay: -0.32s;
        animation-delay: -0.32s;
    }

    .spinner .bounce2
    {
        -webkit-animation-delay: -0.16s;
        animation-delay: -0.16s;
    }

    @-webkit-keyframes sk-bouncedelay
    {
        0%, 80%, 100%
        {
            -webkit-transform: scale(0)
        }
        40%
        {
            -webkit-transform: scale(1.0)
        }
    }

    @keyframes sk-bouncedelay
    {
        0%, 80%, 100%
        {
            -webkit-transform: scale(0);
            transform: scale(0);
        }
        40%
        {
            -webkit-transform: scale(1.0);
            transform: scale(1.0);
        }
    }
</style>