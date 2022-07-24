<template>

  <div class="cal-tile" :style="{ 'current-day': isToday }">
    <div class="cal-tile-header">
      {{ date.getDate() }}
      <SymbolButton class="cal-tile-button" @click.stop="toggleForm(true)" :icons="['plus']" />
    </div>
    <div v-if="formActive">
      <BaseForm
        @closed="toggleForm(false)"
        :defaultDueDate="formattedDate"
        :fixedDueDate="true"
        class="cal-tile-form"
      />
    </div>
    <div v-else class="cal-task-container">
      <div
        v-for="task in tasksDue"
        class="cal-task"
      >
        {{ task.name }} 
      </div>
    </div>
  </div>

</template>

<script>

  import { format } from 'date-fns'

  import { useTasks } from "../stores/tasks.js"
  import SymbolButton from "./SymbolButton.vue"
  import BaseForm from "./BaseForm.vue"

  export default {
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    data() {
      return {
        formVisible: false,
      }
    },
    components: {
      SymbolButton,
      BaseForm,
    },
    props: {
      date: Date
    },
    methods: {
      toggleForm(visibility) {
        this.formVisible = visibility
        this.store.taskFormActive = true
      }
    },
    computed: {   
      tasksDue() {
        return this.store.getTasksOnDate(this.formattedDate)
      },
      formattedDate() {
        return format(this.date, "yyyy-MM-dd")
      },
      formActive() {
        return this.formVisible && this.store.taskFormActive
      },
      isToday() {
        return this.date === new Date()
      },
    }
  }

</script>

<style>

  .cal-tile {
    background-color: #9f63b5;
    height: 100%;
    overflow: scroll;
  }
  .cal-tile-header {
    display: flex;
    flex-flow: row nowrap;
    justify-content: space-between;
  }
  .cal-task-container {
    display: flex;
    flex-flow: column;
    gap: 2px;
  }
  .cal-tile-group {
    display: flex;
    justify-content: space-between;
    height: 1em;
    gap: 1em;
  }
  .cal-tile-form {
    position: absolute;
    font-size: .8em;
    z-index: 1;
  }
  .cal-tile-button {
    border-radius: 3px 2px 3px 10px;
  }
  .cal-task {
    display: flex;
    flex-flow: column;
    border: 1px solid black;
    border-radius: 5px;
    background-color: darkslateblue;
    margin: 1px 3px 1px 3px;
    padding: 2px;
    font-size: .8em;
    color: white;
    
  }
  .current-day {
    border: 8px solid black;
  }

</style>
