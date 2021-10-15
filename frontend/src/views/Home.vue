<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <div class="user-profile">Hello I am Mr {{ givenName }} {{ familyName }}</div>

    <div class="new-todo-box">
      <div class="new-todo-box-inner">
        <input class="new-todo-input" v-model="newTodoTitle" />
        <button @click="createNewTodo">Make new TODO</button>
      </div>
    </div>

    <div class="todo-list">
      <div
          class="todo-item"
          v-for="todo of todoList"
          v-bind:key="todo.id"
      >
        <input class="todo-item-checkbox" type="checkbox" v-model="todo['done']">
        <div class="todo-item-title">{{ todo.itemTitle }}</div>
        <div class="todo-item-time">{{ todo.date }}</div>
      </div>
    </div>


  </div>
</template>

<script lang="ts">
import { Vue } from 'vue-class-component';

export default class Home extends Vue {
  givenName?: string = ''
  familyName?: string = ''

  todoList = [
    { id: 1, itemTitle: 'eat KBBQ', done: false },
    { id: 2, itemTitle: 'watch squid game', done: false },
    { id: 3, itemTitle: 'buy groceries', done: false },
    { id: 4, itemTitle: 'buy BTC dip', done: false },
    { id: 5, itemTitle: 'hug girlfriend', done: false },
    { id: 6, itemTitle: 'hug girlfriend hug girlfriend hug girlfriend hug girlfriend hug girlfriend hug girlfriend hug girlfriend hug girlfriendlfriend hug girlfriend hug girlfriend hug girlfriendlfriend hug girlfriend hug girlfriend hug girlfriendlfriend hug girlfriend hug girlfriend hug girlfriendlfriend hug girlfriend hug girlfriend hug girlfriendlfriend hug girlfriend hug girlfriend hug girlfriendlfriend hug girlfriend hug girlfriend hug girlfriend', done: false },
  ].reverse()

  newTodoTitle = ''

  async mounted() {
    const loggedInUser = await this.$auth.getUser()
    console.log(await this.$auth.getAccessToken())
    this.givenName = loggedInUser.given_name
    this.familyName = loggedInUser.family_name
  }

  // events
  createNewTodo() {
    this.todoList.push({ id: this.todoList.length, itemTitle: this.newTodoTitle, done: false })
    this.newTodoTitle = ''
  }
}
</script>

<style scoped>
.user-profile {
  color: white;
  margin-bottom: 30px;
  margin-top: 30px;
}

.new-todo-box {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.new-todo-box-inner {
  border: 3px solid #1e2536;
  width: 300px;
  padding: 10px;
}

.new-todo-input {
  margin-right: 10px;
}

.todo-list {
  color: white;
  margin-left: 400px;
  margin-right: 400px;
  border: 1px solid black;
}

.todo-item {
  display: flex;
  justify-content: left;
  background: #202839;
  margin: 10px 200px;
  padding: 15px;
  border-radius: 20px;
}

.todo-item-checkbox {
  margin-right: 20px;
  outline: 5px solid pink;
}
</style>
