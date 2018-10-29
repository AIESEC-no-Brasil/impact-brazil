<template>
    <div v-if="entityName !== ''"
         id="invite"
         @mousedown="$emit('show-video', entityVideo)">
        Inviting <span>{{entityName}}</span> to Impact Brazil
        <div v-if="entityVideo !== null" id="ey-banner" :style="entityThumb">
            <div></div>
        </div>
    </div>
    <div v-else id="invite">
        <Loading center dark/>
    </div>
</template>

<script>
	import Loading from '../Loading';
	import axios from 'axios';
	import {config} from '../../config';

	export default {
		name:       "OpportunityInvite",
		components: {
			Loading
		},
		data()
		{
			return {
				entityName:  "",
				entityVideo: false,
				entityThumb: {backgroundImage: "url('')"}
			};
		},
		async mounted()
		{
			let entityPartnerID = this.$route.query['entity']; // TODO: handle error
			let entityPartner = await axios.get(config.api + config.endpoints.entityPartner(entityPartnerID));

			if (entityPartner.data.gis_id === 1606)
			{
                this.$emit('i-am-from-brazil');
                this.$emit('no-visa');
            }

			if (entityPartner.data.no_visa)
				this.$emit('no-visa');

			this.entityName = entityPartner.data['name'];
			this.entityVideo = entityPartner.data['video'];
			this.entityThumb = {
				backgroundImage: "url('" + config.videos.entiyPartnerThumbDir + (entityPartner.data['thumbnail'] === "" ? config.videos.defaultEntityPartnerThumb : entityPartner.data['thumbnail']) + "')",
			};
		}
	};
</script>

<style lang="scss" scoped>
    #invite
    {
        padding-top: 12px;
        text-align: center;
        font-size: 18px;

        span
        {
            font-size: 2.5em;
            padding: 0 4px;
            font-family: PierSansBold, sans-serif;
        }
    }

    #ey-banner
    {
        width: calc(100% + 48px);
        height: 300px;
        margin: 12px 0 24px -24px;
        padding: 0;

        cursor: pointer;

        background: no-repeat fixed center;
        background-size: cover;

        div
        {
            background-image: url('../../assets/play-button.png');
            width: 150px;
            height: 150px;
            background-size: 100%;
            position: relative;
            top: 75px;
            margin: auto;
        }
    }


</style>