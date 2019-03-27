<template>
    <div class="board-area">
        <el-row>
            <Draggable
                    v-model="wrappedPipeLineList"
                    class="board-container"
                    :options="draggable_options"
            >
                <PipeLine
                        v-for="pipeLine in wrappedPipeLineList"
                        :pipeLine="pipeLine"
                        class="pipe-line-item"
                        :key="pipeLine.id"
                />
                <AddPipeLine class="add-pipe-line-item"/>
            </Draggable>
        </el-row>

        <router-view/>
    </div>
</template>

<script>

    import Draggable from 'vuedraggable';
    import {createNamespacedHelpers} from 'vuex';

    import PipeLine from './BoardArea/PipeLine.vue';
    import AddPipeLine from './BoardArea/AddPipeLine.vue';

    const {mapGetters, mapState, mapActions} = createNamespacedHelpers('board');

    export default {
        name: 'BoardArea',
        components: {
            AddPipeLine,
            Draggable,
            PipeLine,
        },
        computed: {
            ...mapGetters([
                'getFilteredPipeLineList',
            ]),
            ...mapState([
                'boardData',
            ]),
            wrappedPipeLineList: {
                get() {
                    return this.getFilteredPipeLineList;
                },
                set(value) {
                    console.log(value, this.boardData);
                    this.updatePipeLineOrder({
                        boardId: this.boardData.boardId,
                        pipeLineList: value,
                    });
                },
            },
        },
        methods: {
            ...mapActions([
                'updatePipeLineOrder',
            ]),
        },
        data() {
            return {
                draggable_options: {
                    animation: 300,
                    draggable: '.pipe-line-item',
                },
            };
        },
    };



</script>

<style scoped>
    .board-area {
        width: 100%;
        margin: 2rem 0;
    }

    .board-container {
        display: block;
    }


    .pipe-line-item,
    .add-pipe-line-item{
        margin-bottom: 1rem ;
    }

</style>
