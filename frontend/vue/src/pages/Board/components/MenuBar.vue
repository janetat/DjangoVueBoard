<template>
    <div class="board-menu-bar">
        <el-col :span="12">
            <div v-show="!isEditingBoardName" @dblclick="startBoardNameEdit">
                <h3 class="board-name">Current Board: {{ boardName }}</h3>
                <form id="search-form">
                    <el-input name="query" class="search-bar" v-model="wrappedSearchWord"
                              placeholder="Search"></el-input>
                </form>
            </div>


            <div v-show="isEditingBoardName">
                <el-input class="edit-board-name" v-model="editBoardName" @blur="away"
                          @keyup.enter.native="saveBoardName"></el-input>
                <el-button class="save-board-button" size="medium" @click="saveBoardName" plain>save</el-button>
            </div>
        </el-col>

        <el-col :offset="8" :span="4">
            <el-button type="danger" class="delete-board-btn" @click.prevent="deleteBoardAction">Delete this Board
            </el-button>

        </el-col>
    </div>
</template>

<script>
    import {createNamespacedHelpers} from 'vuex';

    const {mapActions, mapState} = createNamespacedHelpers('board');


    export default {
        name: 'MenuBar',
        data() {
            return {
                isEditingBoardName: false,
                editBoardName: '',
            };
        },
        computed: {
            wrappedSearchWord: {
                get() {
                    return this.searchWord;
                },
                set(val) {
                    this.setSearchWord(val);
                },
            },
            boardName() {
                return this.boardData.name;
            },
            ...mapState([
                'searchWord',
                'boardData',
            ]),
        },
        methods: {
            startBoardNameEdit() {
                this.isEditingBoardName = true;
                this.editBoardName = this.boardName;
                console.log('start', this.isEditingBoardName);

                this.$nextTick(() => {
                    let edit_boardname = document.querySelector('.edit-board-name input');
                    console.log("edit_boardname", edit_boardname);
                    edit_boardname.focus();
                });
            },
            saveBoardName() {
                this.isEditingBoardName = false;
                if (this.editBoardName === this.boardName) return;
                this.renameBoard({
                    boardId: this.boardData.boardId,
                    boardName: this.editBoardName,
                });
            },
            deleteBoardAction() {
                if (!window.confirm('Are you sure?')) return;
                this.deleteBoard({
                    boardId: this.boardData.boardId,
                });
            },

            away() {
                console.log('clicked away');
                setTimeout(() => {
                    this.isEditingBoardName = false;
                }, 100);
            },
            ...mapActions([
                'setSearchWord',
                'renameBoard',
                'deleteBoard',
            ]),
        },
    };
</script>

<style scoped>
    .board-menu-bar {
        margin: 2rem 0;
    }

    .board-name {
        color: #D9230F;
        cursor: pointer;
        float: left;
        margin-right: 2rem;
    }

    .search-bar {
        width: 200px;
        float: left;
    }

    .edit-board-name {
        width: 200px;
        margin-right: 1rem;
        float: left;
    }

    .delete-board-btn {
        float: right;
    }

</style>
