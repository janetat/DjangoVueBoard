<template>
    <el-dialog :visible=dialogVisible :before-close="close">
        <!--title部分-->
        <div slot="title">
            <div v-show="!isTitleEditing" @dblclick="startTitleEdit">
                <h3>Title</h3>
                <p class="card-title">{{ focusedCard.title }}</p>
            </div>
            <div v-show="isTitleEditing">
                <h3>Title</h3>
                <el-input type="text" class="edit-title" v-model="editTitle"/>
                <el-button type="button" @click="saveTitle">Save</el-button>
            </div>
        </div>

        <!--content部分-->
        <div v-show="!isContentEditing">
            <h3>Description</h3>
            <p v-if="focusedCard.content" @dblclick="startContentEdit" class="card-content">{{ focusedCard.content
                }}</p>
            <p v-else @click="startContentEdit" class="empty-content">description.</p>
        </div>
        <div v-show="isContentEditing">
            <h3>Description</h3>
            <el-input class="edit-area" v-model="editContent" type="textarea" rows="4"></el-input>
            <el-button @click="saveContent">Save</el-button>
        </div>

        <!--footer部分-->
        <div slot="footer">
          <el-button type="danger" @click="deleteCardAction">delete</el-button>
          <el-button @click="close">Close</el-button>
        </div>
    </el-dialog>
</template>

<script>
    import {createNamespacedHelpers} from 'vuex';

    const {mapState, mapActions} = createNamespacedHelpers('board');


    export default {
        props: {
            cardId: {
                type: Number,
                default: null,
            },
            boardId: {
                type: Number,
                default: null,
            },
        },
        name: 'CardShow',
        computed: {
            ...mapState(['focusedCard']),
        },
        data() {
            return {
                dialogVisible: true,
                isContentEditing: false,
                editContent: '',
                isTitleEditing: false,
                editTitle: '',
            };
        },
        methods: {
            close() {
                this.$router.push({
                    path: `/boards/${this.boardId}`,
                    query: this.$route.query,
                });
            },
            async deleteCardAction() {
                if (!window.confirm('Are you sure?')) return;
                await this.deleteCard({
                    cardId: this.cardId,
                });
                this.close();
            },
            startContentEdit() {
                this.isContentEditing = true;
                this.editContent = this.focusedCard.content;
            },
            startTitleEdit() {
                this.isTitleEditing = true;
                this.editTitle = this.focusedCard.title;
            },
            async saveContent() {
                this.isContentEditing = false;
                if (this.editContent === this.focusedCard.content) return;
                await this.updateCardContent({
                    cardId: this.cardId,
                    content: this.editContent,
                });
            },
            async saveTitle() {
                this.isTitleEditing = false;
                if (this.editTitle === this.focusedCard.title) return;
                await this.updateCardTitle({
                    cardId: this.cardId,
                    title: this.editTitle,
                });
            },
            ...mapActions([
                'fetchFocusedCard',
                'updateCardContent',
                'updateCardTitle',
                'deleteCard',
            ]),
        },
        watch: {
            cardId: {
                immediate: true,
                handler(cardId) {
                    console.log(cardId);
                    this.fetchFocusedCard({
                        cardId,
                    });
                },
            },
        },
    };
</script>

<style lang='scss' scoped>
    .edit-title {
        width: 200px;
    }

    .card-title {
        cursor: pointer;
    }

    .card-content {
        cursor: pointer;
    }
</style>
