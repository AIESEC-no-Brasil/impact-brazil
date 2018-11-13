<!--suppress XmlDuplicatedId -->
<template>
    <div>
        <div v-if="noVisa" id="invite">
            We have detected that you are from {{entityName}}.<br>
            Is this not where you are from? <a href="#" @click="showEntityDialog">Click here</a> to change.
        </div>
        <div v-else-if="entityName !== ''"
             id="invite">
            <div class="invitation-text">Inviting <span>{{entityName}}</span> to Impact Brazil</div>
            <div class="change-entity-text">Not from {{entityName}}? <a href="#" @click="showEntityDialog">Click
                here</a> to change.
            </div>
            <div v-if="entityVideo !== null"
                 id="ey-banner"
                 :style="entityThumb"
                 @mousedown="$emit('show-video', entityVideo)">
                <div></div>
            </div>
        </div>
        <div v-else id="invite">
            <Loading center dark/>
        </div>
        <SweetModal modal-theme="dark"
                    overlay-theme="dark"
                    ref="changeEntity"
                    id="video-modal"
                    title="Choose your country/territory">
            Where are you from? (Country or territory of citizenship)<br>
            <select title="entity" v-if="entityList.length > 0" v-model="entitySelection">
                <option v-for="entity in entityList"
                        :key="entity.id"
                        :value="entity.id">
                    {{entity.name}}
                </option>
            </select>
            <select title="entity" v-else>
                <option>Loading...</option>
            </select>
            <button v-if="entityList.length > 0" @click="setEntity(entitySelection)">Submit</button>
        </SweetModal>
    </div>
</template>

<script>
	import Loading from '../Loading';
	import {SweetModal} from 'sweet-modal-vue';
	import axios from 'axios';
	import {config} from '../../config';

	export default {
		name:       "OpportunityInvite",
		components: {
			Loading,
			SweetModal
		},
		props:      {
			noVisa: Boolean,
		},
		data()
		{
			return {
				entityName:      "",
				entityVideo:     false,
				entityThumb:     {backgroundImage: "url('')"},
				entityList:      [],
				entitySelection: -1,
			};
		},
		methods:    {
			loadInvite: async function () {
				let entityPartner, entityPartnerID;
				try
				{
					if (this.$session.get('entity'))
						entityPartnerID = this.$session.get('entity');
					else
					{
						// Auto detect the entity!
						let entities = await axios.get(config.api + config.endpoints.entities);
						let myEntity = await axios.get(config.api + config.endpoints.ip);

						// TODO: what if the country is not found?
						entityPartnerID = entities.data.find(entity => entity.name === myEntity.data.country).id;

						// Store the entity in the session
						this.$session.set('entity', entityPartnerID);
					}

					entityPartner = await axios.get(config.api + config.endpoints.entityPartner(entityPartnerID));
				}
				catch (err)
				{
					console.error(err);
					this.$root.$emit('error');
					return false;
				}

				if (entityPartner.data.gis_id === config.gisBrazilID || entityPartner.data.no_visa)
					this.$store.commit('noVisa', true);

				this.entityName = entityPartner.data['name'];
				this.entityVideo = entityPartner.data['video'];
				this.entityThumb = {
					backgroundImage: "url('" + config.videos.entiyPartnerThumbDir + (entityPartner.data['thumbnail'] === "" ? config.videos.defaultEntityPartnerThumb : entityPartner.data['thumbnail']) + "')",
				};


				// We don't need to reload any more
				this.$store.commit('inviteLoaded');
			},
			async showEntityDialog()
			{
				this.$refs.changeEntity.open();

				let storedEntityList = this.$store.getters.getList('entities');
				if (storedEntityList.length > 0)
					this.entityList = storedEntityList;
				else
				{
					let entityList;
					try
					{
						entityList = await axios.get(config.api + config.endpoints.entities);
					}
					catch (err)
					{
						console.error(err);
						this.$root.$emit('error');
						return false;
					}
					this.$store.commit('setList', {list: 'entities', arr: entityList.data});
					this.entityList = entityList.data;
				}
			},
			setEntity(ey)
			{
				this.$session.set('entity', ey);
				window.location.reload();
			}
		},
		async created()
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

    .change-entity-text
    {
        font-size: 10px;
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