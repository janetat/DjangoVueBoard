<template>

    <el-col :xs="12" :sm="12" :md="8" :lg="6" :xl="4">
        <div class="pipe-line">
            <el-card class="box-card">
                <div slot="header">
                     <span v-show="!isEditingPipeLineName">
                        <span class="pipe-line-name"
                              @dblclick="startPipeLineNameEdit">
                            {{ pipeLineName }}
                        </span>
                        <span class="delete-pipe-line" title="delete pipeline" @click="delPipeLineAction">
                          <i class="el-icon-delete"></i>
                        </span>

                        <span class="add-card" @click="addCardAction">
                            <i class="el-icon-circle-plus-outline"></i>
                        </span>
                     </span>

                    <span v-show="isEditingPipeLineName">
                        <el-input class="edit-pipeline" type="text" v-model="editPipeLineName" @blur="away"
                                  @keyup.enter.native="savePipeLineName"></el-input>
                        <!--如果用vuedraggable 性能损耗严重： 如果有n个Pipeline, 则每次会触发n次这个函数。如果这个函数里面有密集计算（例如加个循环加法），导致非常卡。-->
                        <!--<input class="edit-pipeline" type="text" v-model="editPipeLineName" v-on-clickaway="away">-->

                        <el-button class="save-pipeline-btn" @click="savePipeLineName">save</el-button>
                    </span>
                </div>

                <div class="card-container">
                    <!--TODO 这里Draggable的options虽然是deprecated，但是直接:draggable='.item'无法生效-->
                    <!-- TODO el-scrollbar在这里就算overflow:hidden了 水平滚动条还会显示-->
                    <!--<el-scrollbar style="height: 100%;">-->
                    <Draggable
                            v-model="wrappedCardList"
                            :options="draggable_options"
                    >
                        <Card v-for="card in wrappedCardList"
                              class="item"
                              v-show="card.isShown"
                              :card="card"
                              :key="card.cardId"
                        />
                    </Draggable>
                    <!--</el-scrollbar>-->
                </div>

            </el-card>


        </div>
    </el-col>
</template>

<script>
    import Card from './Card.vue';

    import {createNamespacedHelpers} from 'vuex';
    import Draggable from 'vuedraggable';

    const {mapActions, mapGetters} = createNamespacedHelpers('board');


    export default {
        name: 'PipeLine',
        components: {
            Draggable,
            Card,
        },
        props: {
            pipeLine: {
                type: Object,
                default: () => {
                },
            },
        },
        data() {
            return {
                isEditingPipeLineName: false,
                editPipeLineName: '',
                draggable_options: {
                    group: 'Cards',
                    animation: 300,
                    draggable: '.item',
                    emptyInsertThreshold: '20',
                },
            };
        },
        computed: {
            wrappedCardList: {
                get() {
                    return this.pipeLine.cardList;
                },
                set(value) {
                    console.log(value);
                    this.updateCardOrder({
                        pipeLineId: this.pipeLine.pipeLineId,
                        cardList: value,
                    });
                },
            },
            pipeLineName() {
                return this.pipeLine.name;
            },
        },
        watch: {
            pipeLine(newPipeLine, oldPipeLine) {
                if (newPipeLine.name !== oldPipeLine.name) {
                    this.isWaitingRename = false;
                }
            },
        },
        methods: {
            ...mapActions([
                'updateCardOrder',
                'addCard',
                'renamePipeLine',
                'deletePipeLine',
            ]),
            ...mapGetters([
                'getBoardId',
            ]),

            away() {
                console.log('clicked away');
                setTimeout(() => {
                    this.isEditingPipeLineName = false;
                }, 100)
            },

            addCardAction() {
                const cardTitle = window.prompt('CardTitle?');
                if (cardTitle) {
                    this.addCard({
                        pipeLineId: this.pipeLine.pipeLineId,
                        cardTitle,
                    });
                }
            },
            delPipeLineAction() {
                if (!window.confirm(`DELETE [${this.pipeLineName}] ? Are you sure?`)) return;
                this.deletePipeLine({
                    boardId: this.getBoardId(),
                    pipeLineId: this.pipeLine.pipeLineId,
                });
            },
            startPipeLineNameEdit() {
                this.isEditingPipeLineName = true;
                console.log('startPipeLineNameEdit', this);
                this.editPipeLineName = this.pipeLine.name;

                // TODO 这里实现自动聚焦手动操作了DOM，其实不符合Vue数据驱动的思想
                this.$nextTick(() => {
                    let edit_pipelines = document.querySelectorAll('.edit-pipeline input');
                    console.log(edit_pipelines);
                    edit_pipelines.forEach((element) => {
                        element.focus();
                    })
                });

            },
            async savePipeLineName() {
                this.isEditingPipeLineName = false;
                if (this.editPipeLineName === this.pipeLine.name) return;
                await this.renamePipeLine({
                    pipeLineId: this.pipeLine.pipeLineId,
                    pipeLineName: this.editPipeLineName,
                });
                this.isWaitingRename = true;
            },


        },
    };
</script>

<style scoped>
    .pipe-line {
        width: 15rem;
    }

    .pipe-line-name {
        font-size: 1.5rem;
        cursor: pointer;
    }

    .card-container {
        overflow-x: hidden;
        height: 300px;
    }

    .delete-pipe-line,
    .add-card {
        cursor: pointer;
        float: right;
    }

    .edit-pipeline {
        width: 150px;
    }

    .save-pipeline-btn {
    }


</style>
