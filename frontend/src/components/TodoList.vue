<template>

  <div class="todo-main">
    <ListHeader />
    <div class="main-todo-area">
      <TaskList :listID="id" />
      <TaskForm
        @submitted="setFormVisibility(false)"
        class="task-form"
      />
    </div>
  </div>

</template>

<script setup>

  import { watch } from 'vue'

  import ListHeader from './ListHeader.vue'
  import TaskList from './TaskList.vue'
  import TaskForm from './TaskForm.vue'
  import { useTasks } from '../stores/tasks.js'
  import { useLists } from '../stores/lists.js'

  const store = useTasks()
  const listStore = useLists()

  const props = defineProps(['id'])

  watch(() => props.id, (id) => {
     if (id === "completed") {
       store.filter = "completed"
     }
     else {
       store.filter = "currentList"
       listStore.currentListID = parseInt(id)
     }
  })

  function setFormVisibility(visible) {
     this.store.taskFormActive = visible
  }


</script>

<style>

  .main-todo-area {
    position: relative;
    margin: 10px;
  }
  .task-form {
    height: auto;
    box-shadow: 0px 0px 50px 2px black;
    position: absolute;
    z-index: 3;
    top: 0;
    right: 0;
    margin: 5px;
  }

</style>
