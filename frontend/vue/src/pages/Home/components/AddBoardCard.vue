<template>
    <div class="add-board-bard">
        <el-col :xs="12" :sm="8" :md="8" :lg="6" :xl="6">
            <a @click="addBoardAction">
                <el-card class="card-body" shadow="never">
                    <h5 class="card-title"><i class="el-icon-circle-plus"></i></h5>
                </el-card>
            </a>
        </el-col>
    </div>
</template>

<script>
    import {createNamespacedHelpers} from 'vuex';

    const {mapActions} = createNamespacedHelpers('home');


    export default {
        name: 'BoardCard',
        methods: {
            addBoardAction() {
                const boardName = window.prompt('BoardName?');
                if (boardName) {
                    this.addBoard({
                        boardName,
                    });

                }
            },
            ...mapActions(['addBoard']),
        },
    };
</script>

<style scoped>
    .card-body {
        margin: 0.5rem;
        background-color: #E5E9EB;
    }

    .card-body:hover {
        background-color: lightcoral;
    }
</style>
