<script>

  import TaskTile from './TaskTile.vue'
  import ListHeader from './ListHeader.vue'
  import draggable from 'vuedraggable/src/vuedraggable.js'
  import { computed } from 'vue'

  export default { 

    components: {
      TaskTile,
      ListHeader,
      draggable
    },
    inject: ['currentListID'],
    data() {
      return {
        tasks: [],
        drag: false
      }
    },
    mounted() {
      this.loadTasks()
    },
    beforeUnmount() {
      this.saveTaskOrder()

    },
    watch: {
      currentListID: 'loadTasks'
    },
    methods: {

      loadTasks() {
        // Tasks fetched from Flask backend
        this.axios.get("lists/" + this.currentListID)
          .then((res) => {
            if (res.status == 200) {
              this.tasks = res.data
            } else {
              router.push("/login")
            }
          })
      },
      /** 
       * Sends delete request to remove selected task from backend.
       * Requests tasks again after OK response. TO CHANGE AS ITS INEFFICIENT
       */
      deleteTask(task_id) {
        this.axios.delete("tasks/" + task_id.toString())
          .then((res) => {
            if (res.status == 200) {
              this.loadTasks()
            }
          })
      },
      sendTaskCompletion(task_id) {
        this.axios.put("tasks/" + task_id, {
            'completed': true
          })
          .then((res) => {
            this.loadTasks()
          })
      },
      saveTaskOrder() {
        taskOrder = this.currentTasks.map(({taskID}) => taskID)
        this.axios.put("tasks/",{
            'task_order': taskOrder
          })
      }
    },
    computed: {
      currentTasks() {
        return this.tasks.filter(task => task["listID"] == this.currentListID)
      }
    }
  }
</script>

<template>
  <div class='task-list'>
    <ListHeader class="item" @view-changed='loadTasks' />
    <draggable 
      :list="tasks" 
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
    margin-top: .5em;
  }
  .ghost {
    opacity: 0.5;
    background: lightblue; 
  }
  .item  {
    flex-grow: 1;
  }

</style>
