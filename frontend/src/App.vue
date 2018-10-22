<template>
    <div id="app">
        <transition name="fade">
            <router-view/>
        </transition>
    </div>
</template>

<style lang="scss">
    #app
    {
        /*font-family: 'Avenir', Helvetica, Arial, sans-serif;*/
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        /*text-align: center;*/
        /*color: #2c3e50;*/
    }

    /*#nav {*/
    /*padding: 30px;*/
    /*a {*/
    /*font-weight: bold;*/
    /*color: #2c3e50;*/
    /*&.router-link-exact-active {*/
    /*color: #42b983;*/
    /*}*/
    /*}*/
    /*}*/

    body, html
    {
        margin: 0;
        padding: 0;
    }

    .section
    {
        padding: 24px;
    }

    .fade-enter-active, .fade-leave-active
    {
        transition: opacity .2s;
    }

    .fade-leave-active
    {
        /*transition-delay: 1s;*/
    }

    .fade-enter, .fade-leave-to
    {
        opacity: 0;
    }
</style>
