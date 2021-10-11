<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <div>Hello I am Mr {{ givenName }} {{ familyName }}</div>
    <HelloWorld msg="Welcome to Your Vue.js + TypeScript App"/>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src

@Options({
  components: {
    HelloWorld,
  },
})
export default class Home extends Vue {
  givenName?: string = ''
  familyName?: string = ''

  async mounted() {
    const loggedInUser = await this.$auth.getUser()
    console.log(await this.$auth.getAccessToken())
    this.givenName = loggedInUser.given_name
    this.familyName = loggedInUser.family_name
  }

}
</script>
