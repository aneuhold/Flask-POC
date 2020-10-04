<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="This is a Vue.js app"/>
    <TextEntry/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
import TextEntry from './components/TextEntry';

export default {
  name: 'App',
  components: {
    HelloWorld,
    TextEntry
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
