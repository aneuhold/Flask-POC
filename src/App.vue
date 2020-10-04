<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png" />
    <HelloWorld msg="This is a Vue.js app" />

    <TextEntry />
    <p>{{ flaskGreeting }}</p>
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import TextEntry from "./components/TextEntry";

export default {
  name: "App",
  components: {
    HelloWorld,
    TextEntry,
  },
  data: () => {
    return {
      flaskGreeting: "testing",
    };
  },
  created: async () => {
    const response = await fetch("http://localhost:5000/hello");
    const responseText = await response.text();
    console.log(responseText);
    flaskGreeting = responseText;
  },
};
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
