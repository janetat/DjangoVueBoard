<template>
    <div class="home">
        <el-row>
            <BoardCard v-for="board in boardList"
                       :title="board.name"
                       :boardId="board.id"
                       :key="board.id"/>
            <AddBoardCard/>
        </el-row>
    </div>
</template>

<script>
    import {createNamespacedHelpers} from 'vuex';
    import BoardCard from './components/BoardCard.vue';
    import AddBoardCard from './components/AddBoardCard.vue';

    const {mapState, mapActions} = createNamespacedHelpers('home');


    export default {
        name: 'home',
        components: {
            BoardCard,
            AddBoardCard,
        },
        computed: {
            ...mapState([
                'boardList',
            ]),
        },
        methods: {
            ...mapActions([
                'fetchBoardList',
            ]),
        },
        async created() {
            this.fetchBoardList();
        },

    };
</script>


<style lang="scss" scoped>

    .home {
        /*text-align: center;*/
    }


</style>
