<template>
    <div class="board-card">
        <el-col :xs="12" :sm="8" :md="8" :lg="6" :xl="6">
            <router-link :to="boardUrl">
                <el-card class="card-body" shadow="never">
                    <h5 class="card-title">{{ title }}</h5>
                </el-card>
            </router-link>
        </el-col>
    </div>
</template>

<script>
    export default {
        name: 'BoardCard',
        props: {
            title: {
                type: String,
                default: '',
            },
            boardId: {
                type: Number,
                default: null,
            },
        },
        computed: {
            boardUrl() {
                if (this.boardId !== null) {
                    return `/boards/${this.boardId}`;
                }
                return '#';
            },
        },
    };
</script>

<style scoped>

    .card-body {
        /*color: #D9230F;*/
        margin: 0.5rem;

    }

    .card-body:hover {
        background-color: lightcoral;
    }

    .card-title {
        white-space: nowrap;
        text-overflow: ellipsis;
        overflow: hidden;
    }
</style>
