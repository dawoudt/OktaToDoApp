<template>
  <div id="nav">
    <router-link to="/">Home</router-link>
    <router-link
        v-if="!authState && !authState.isAuthenticated"
        to="/login">Login</router-link>
    <span
        v-if='authState && authState.isAuthenticated'
        class="logout-button"
        @click="logout"
    >Logout</span>
  </div>
  <router-view />
</template>

<script lang="ts">
import { Vue } from 'vue-class-component';

export default class App extends Vue {
  async logout() {
    await this.$auth.signOut()
  }
}
</script>

<style>
body {
  background: #111827;
  color: white;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.logout-button {
  cursor: pointer;
}
</style>
