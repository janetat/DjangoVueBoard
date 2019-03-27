<template>
    <el-container class="main-container">


        <el-header>
            <MyHeader></MyHeader>
        </el-header>

        <el-main>
            <router-view></router-view>
        </el-main>

    </el-container>
</template>

<script>
    import MyHeader from './MyHeader.vue';

    export default {
        name: 'DefaultLayout',
        components: {
            MyHeader,
        },
    };
</script>


<style scoped>


</style>
