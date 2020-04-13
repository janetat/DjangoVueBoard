<template>
    <div id="app">
        <router-view/>
    </div>
</template>

<style>
    @import 'https://cdnjs.cloudflare.com/ajax/libs/element-ui/2.6.1/theme-chalk/index.css';
    @import 'https://cdnjs.cloudflare.com/ajax/libs/bootswatch/4.3.1/simplex/bootstrap.min.css';
</style>

{#阻止某些浏览器在卡片drop的时候， 打开新的标签页#}
<script>
    document.body.ondrop = function (event) {
        event.preventDefault();
        event.stopPropagation();
    }
</script>