<template>

  <div class="cal-tile">
    <slot />
    <div class="cal-task-container">
      <div
        v-for="task in tasksDue"
        @click=""
        class="cal-task"
      >
        {{ task.name }} 
        {{ task.description }} 
      </div>
    </div>
  </div>

</template>

<script>

  import { useTasks } from "../stores/tasks.js"

  export default {
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
  props: {
    date: Date
  },
  computed: {   
    tasksDue() {
      return this.store.getTasksOnDate(this.date)
    }
  }
  }
  

</script>

<style>

  .cal-tile {
     
  }
  .cal-task-container {
    display: flex;
    flex-flow: column;
    gap: 3px;
  }
  .cal-task {
    display: flex;
    flex-flow: column;
    border: 1px solid black;
    border-radius: 5px;
    background-color: lightpink;
    margin: 5px;
  }

</style>
