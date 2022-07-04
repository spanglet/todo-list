<script>

  import TaskTile from './TaskTile.vue'
  import ListHeader from './ListHeader.vue'
  import draggable from 'vuedraggable/src/vuedraggable.js'
  import { computed } from 'vue'

  import { useTasks } from '../stores/tasks.js'

  export default { 
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    components: {
      TaskTile,
      ListHeader,
      draggable
    },
    data() {
      return {
        tasks: [],
        drag: false
      }
    },
    mounted() {
      this.tasks = this.store.filteredTasks
      this.currentListID = this.store.currentListID
    },
    methods: {

      deleteTask(task_id) {
        this.store.deleteTask(task_id)
      },
      sendTaskCompletion(task_id) {
        this.store.completeTask(task_id)
      },
    }
  }
</script>

<template>
  <div class='task-list'>
    <draggable 
      :list="store.filteredTasks" 
      @start="drag=true" 
      @end="drag=false" 
      item-key="id"
      ghost-class="ghost"
      class="list-group">

      <template #item="{element, index}">
        <TaskTile class="list-group-item item"
          :name="element.name"
          :description="element.description"
          :dueDate="element.trueDueDate"
          @remove-item='deleteTask(element.id)'
          @task-completed='sendTaskCompletion(element.id)'
        />
      </template>

    </draggable>
  </div>

</template>

<style>

  .task-list {
    background: hsl(var(--hue-purple), 100%, var(--lgt-6));
    min-width: 0;
  }

  .list-group {
    display: flex;
    flex-flow: column nowrap;
    gap: 3px;
    margin: .5em;
  }
  .ghost {
    opacity: 0.5;
    background: lightblue; 
  }

</style>
