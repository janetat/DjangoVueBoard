<template>
    <div class="card" @click="openCard">
        <div class="card-body">
            <h5 class="card-title">{{ title }}</h5>
        </div>
    </div>
</template>

<script>

    import {createNamespacedHelpers} from 'vuex';

    const {mapGetters} = createNamespacedHelpers('board');
    export default {
        name: 'Card',
        props: {
            card: {
                type: Object,
                default: () => {
                },
            },
        },
        computed: {
            ...mapGetters(['getBoardId']),
            title() {
                return this.card.title;
            },
            content() {
                return this.card.content;
            },
        },
        methods: {
            openCard() {
                console.log('OPEN');
                this.$router.push({
                    path: `/boards/${this.getBoardId}/cards/${this.card.cardId}`,
                    query: this.$route.query,
                });
            },
        },

    };
</script>

<style scoped>
    .card {
        cursor: pointer;
        overflow: hidden;
    }

    .card-body:hover {
        background-color: lightcoral;
        text-decoration: none;

    }
</style>
