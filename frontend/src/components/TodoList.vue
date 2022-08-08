<template>

  <div class="todo-main">
    <ListHeader class="todo-header" />
    <div class="main-todo-area">
      <TaskList :listID="id" />
      <TaskForm
        @submitted="setFormVisibility(false)"
        class="task-form"
      />
    </div>
  </div>

</template>

<script>

  import ListHeader from './ListHeader.vue'
  import TaskList from './TaskList.vue'
  import TaskForm from './TaskForm.vue'
  import { useTasks } from '../stores/tasks.js'

  export default {
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    components: {
      TaskList,
      TaskForm,
      ListHeader,
    },
    props: ["id"],
    data() {
      return {
    
      }
    },
    watch: {
      id: 'setListID'
    },
    methods: {
      setFormVisibility(visible) {
        this.store.taskFormActive = visible
      },
      setListID() {
        this.store.currentListID = parseInt(this.id)
      },
    },
  }

</script>

<style>

  .todo-header {
    align-self: stretch;
  }
  .main-todo-area {
    position: relative;
    margin: 5px;
  }
  .task-form {
    height: auto;
    box-shadow: 0px 0px 50px 2px black;
    position: absolute;
    top: 0;
    right: 0;
    margin: 5px;
  }

</style>
