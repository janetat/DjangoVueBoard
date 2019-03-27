<template>
    <div class="header">
        <div class="logo">
            <router-link to="/">KANBAN</router-link>
        </div>
        <div class="user-information">
            <div v-if="isLoggedIn">
                <span>Current User: </span>
                <span>{{ accountInfo.name }}</span>
            </div>
        </div>
        <div class="log-out">
            <div v-if="isLoggedIn">
                <a href="/account/logout/">Logout</a>
            </div>
            <ul v-if="!isLoggedIn">
                <li>
                    <a href="#">Register</a>
                </li>
                <li>
                    <a href="#">Login</a>
                </li>
            </ul>
        </div>
    </div>


</template>

<script>
    import {createNamespacedHelpers} from 'vuex';

    const {mapState, mapActions} = createNamespacedHelpers('header');

    export default {
        name: 'MyHeader',
        computed: {
            isLoggedIn() {
                return this.accountInfo !== null;
            },
            ...mapState(['accountInfo']),
        },
        methods: {
            ...mapActions(['fetchAccountInfo']),
        },
        created() {
            this.fetchAccountInfo();
        },
    };
</script>

<style scoped>
    .header {
        font-size: 20px;
        /*text-align: center;*/
        /*line-height: 60px;*/
        color: #D9230F;
        display: flex;
        position: relative;
    }

    .user-information {
        position: absolute;
        left: 50%;
        transform: translate(-50%);
    }

    .log-out {
        position: absolute;
        right: 0;
    }
</style>
