<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <div class="user-profile">
      Hello I am Mr {{ givenName }} {{ familyName }}
    </div>

    <div class="new-todo-box">
      <div class="new-todo-box-inner">
        <input class="new-todo-input" v-model="newTodoTitle" />
        <button @click="createNewTodo">Make new TODO</button>
      </div>
    </div>

    <div class="todo-list">
      <div class="todo-item" v-for="todo of todoList" v-bind:key="todo.id">
        <input
          class="todo-item-checkbox"
          type="checkbox"
          v-model="todo['done']"
          @change="updateTodo($event)"
        />
        <span hidden>{{ todo.id }}</span>

        <div class="todo-item-title">{{ todo.title }}</div>
        <div class="todo-item-time">{{ todo.date }}</div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";
import axios from "axios";

interface Todo {
  id: number;
  title: string;
  done: boolean;
}

export default class Home extends Vue {
  givenName?: string = "";
  familyName?: string = "";
  todoList?: Todo[] = [];
  newTodoTitle = "";
  access_token?: string = "";

  async getTodos() {
    let access_token = await this.$auth.getAccessToken();

    axios
      .get<Todo[]>("http://127.0.0.1:8000/todos/", {
        headers: {
          Authorization: `${access_token}`,
        },
      })
      .then((res) => {
        this.todoList = res.data;
        this.todoList.reverse();
      })
      .catch((error) => {
        console.error(error);
      });
  }

  async mounted() {
    let loggedInUser = await this.$auth.getUser();
    this.givenName = loggedInUser.given_name;
    this.familyName = loggedInUser.family_name;
    await this.getTodos();
  }

  async updateTodo(e: any) {
    let updatedDone = e.target.checked;
    let todoId = e.srcElement.nextElementSibling.innerText;
    let patchEndpoint = `http://127.0.0.1:8000/todos/${todoId}/`;
    let access_token = await this.$auth.getAccessToken();

    await axios
      .patch(
        patchEndpoint,
        {
          done: updatedDone,
        },
        {
          headers: {
            Authorization: `${access_token}`,
          },
        }
      )
      .catch((error) => {
        console.error(error);
      });
  }

  // events
  async createNewTodo() {
    let access_token = await this.$auth.getAccessToken();

    axios
      .post(
        "http://127.0.0.1:8000/todos/",
        {
          title: this.newTodoTitle,
          done: false,
        },
        {
          headers: {
            Authorization: `${access_token}`,
          },
        }
      )
      .then((res) => {
        this.getTodos();
      })
      .catch((error) => {
        console.error(error);
      });
    this.newTodoTitle = "";
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
