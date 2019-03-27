<template>
    <el-col :xs="12" :sm="12" :md="8" :lg="6" :xl="4">
        <div class="add-pipe-line">
            <el-card class="box-card">
                <div slot="header" @click="addPipeLineAction">
                    <i class="el-icon-circle-plus"></i>
                </div>

                <div class="card-container">

                </div>
            </el-card>
        </div>
    </el-col>
</template>

<script>

    import {createNamespacedHelpers} from 'vuex';

    const {mapActions, mapState} = createNamespacedHelpers('board');


    export default {
        name: 'AddPipeLine',
        computed: {
            ...mapState([
                'boardData',
            ]),
        },
        methods: {
            addPipeLineAction() {
                const pipeLineName = window.prompt('PipeLineName?');
                if (pipeLineName) {
                    this.addPipeLine({
                        boardId: this.boardData.boardId,
                        pipeLineName,
                    });
                }
            },
            ...mapActions([
                'addPipeLine',
            ]),
        },
    };
</script>

<style scoped>
    .box-card {
        background-color: #E5E9EB;
    }

    .add-pipe-line {
        font-size: 1.5rem;
        width: 15rem;
        float: left;

    }

    .card-container {
        height: 300px;
    }


</style>
