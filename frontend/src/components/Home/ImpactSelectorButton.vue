<template>
    <transition name="fade" mode="out-in">
        <img v-if="qno === 0 && dir === 'left'" src="../../assets/logo5.png"
             style="width: 100%; margin-top: -20px;"/>
        <button v-else
                :class="['spin', 'circle', 'accent--'+accent, dir === 'left' ? 'left-button' : 'right-button']">
            <i role="button" class="material-icons md-light">{{ dir === "left" ? "keyboard_arrow_left" :
                "keyboard_arrow_right" }}</i>
        </button>
    </transition>
</template>

<script>
	export default {
		name:  "ImpactSelectorButton",
		props: {
			dir:    String,
			qno:    Number,
			accent: {
				type:    String,
				default: "blue"
			},
		}
	};
</script>

<style lang="scss" scoped>
    @import "../../assets/colors";
    @import url("https://fonts.googleapis.com/icon?family=Material+Icons");

    i
    {
        font-size: 96px;
        position: relative;
    }

    .left-button i
    {
        left: -2px;
    }

    .right-button i
    {
        left: 2px;
    }

    button
    {
        background: none;
        border: 2px solid;
        font: inherit;
        line-height: 1;
        margin: 0.5em;
        width: 100px;
        height: 100px;
        text-align: center;
        border-radius: 100px;
        cursor: pointer;
        position: relative;
        left: 0;
    }

    button
    {
        color: #fff;
        transition: color 0.3s, box-shadow 0.5s, left 0.2s, border-color 0.2s;
        border-color: #fff;

        &:hover,
        &:focus
        {
            /*border-color: #000;*/
            /*color: #fff;*/
        }
    }

    button:hover
    {
        //box-shadow: inset -3.6em -10px 0 0 #fff,
        //inset 3.6em -10px 0 0 #fff;
        color: #000;
    }

    $accentlist: blue yellow green purple pink orange;
    @each $accent in $accentlist
    {
        button.accent--#{$accent}:hover
        {
            box-shadow: inset -3.6em -10px 0 0 #fff,
            inset 3.6em -10px 0 0 #fff;
            color: map_get($ib-colors-list-dk, $accent);
            border-color: transparent;
        }

    }

    .left-button:active
    {
        left: -12px;
    }

    .right-button:active
    {
        left: 12px;
    }

    .fade-enter-active, .fade-leave-active
    {
        transition: opacity .2s;
    }

    .fade-leave-active
    {
        transition-delay: 1s;
    }

    .fade-enter, .fade-leave-to
    {
        opacity: 0;
    }

</style>