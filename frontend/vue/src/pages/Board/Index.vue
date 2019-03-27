<template>
    <div class="board">
        <el-row>
            <MenuBar></MenuBar>
        </el-row>
        <el-row>
            <BoardArea></BoardArea>
        </el-row>
    </div>
</template>

<script>
    import MenuBar from './components/MenuBar.vue';
    import BoardArea from './components/BoardArea.vue';


    export default {
        name: 'Board',
        components: {
            MenuBar,
            BoardArea,
        },
    };
</script>
<style lang="scss" scoped>
</style>
