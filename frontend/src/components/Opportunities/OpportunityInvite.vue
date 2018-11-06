<!--suppress XmlDuplicatedId -->
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
		methods:    {
			async loadInvite()
			{
				let entityPartner, entityPartnerID;
				try
				{
					if (this.$route.query.entity)
						entityPartnerID = this.$route.query.entity;
					else if (this.$store.state.options.entity)
						entityPartnerID = this.$store.state.options.entity;
					else
					{
						// Auto detect the entity!
						let entities = await axios.get(config.api + config.endpoints.entities);
						let myEntity = await axios.get(config.api + config.endpoints.ip);

						// TODO: what if the country is not found?
						entityPartnerID = entities.data.find(entity => entity.name === myEntity.data.country).id;

						// Don't forget to route
						this.$router.push({path: 'opportunities', query: {entity: entityPartnerID}});
					}
					entityPartner = await axios.get(config.api + config.endpoints.entityPartner(entityPartnerID));
				}
				catch (err)
				{
					console.error(err);
					this.$root.$emit('error');
					return false;
				}

				if (entityPartner.data.gis_id === 1606)
				{
					this.$store.commit('brazilian', true);
					this.$store.commit('noVisa', true);
				}

				if (entityPartner.data.no_visa)
					this.$store.commit('noVisa', true);

				this.entityName = entityPartner.data['name'];
				this.entityVideo = entityPartner.data['video'];
				this.entityThumb = {
					backgroundImage: "url('" + config.videos.entiyPartnerThumbDir + (entityPartner.data['thumbnail'] === "" ? config.videos.defaultEntityPartnerThumb : entityPartner.data['thumbnail']) + "')",
				};


				// We don't need to reload any more
				this.$store.commit('inviteLoaded');
			}
		},
		async mounted()
		{
			this.loadInvite();
		},
		async activated()
		{
			if (this.$store.state.optReloadQueued.invite)
				this.loadInvite();
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