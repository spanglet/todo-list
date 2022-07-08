<template>

  <div class="cal-tile">
    <div class="cal-tile-header">
      {{ date.getDate() }}
      <SymbolButton @click.stop="toggleForm(true)" :icons="['plus']" />
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
    gap: 2px;
  }
  .cal-tile-header {
    display: flex;
    justify-content: space-between;
  }
  .cal-tile-form {
    position: absolute;
    font-size: .8em;
    z-index: 1;
  }
  .cal-task {
    display: flex;
    flex-flow: column;
    border: 1px solid black;
    border-radius: 5px;
    background-color: lightpink;
    margin: 0 5px 0 5px;
    font-size: .8em;
  }

</style>
