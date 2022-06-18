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
        visibleTasks: [],
        drag: false
        
      }
    },
    mounted() {
      this.loadTasks()
    },
    beforeUnmount() {
      this.saveTaskOrder()

    },
    methods: {

      loadTasks() {
        // Tasks fetched from Flask backend
        this.axios.get("tasks/")
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
      deleteTask(task_id, index) {
        var targetPath = "tasks/" + task_id
        this.axios.delete(targetPath)
          .then((res) => {
            if (res.status == 200) {
              this.loadTasks()
            }
          })
      },
      saveTaskOrder() {
        taskOrder = this.visibleTasks.map(({taskID}) => taskID)
        this.axios.put("tasks/",{
            'task_order': taskOrder
          })
      }
    },
    computed: {
      updateCurrentTasks() {
        this.visibleTasks = this.tasks.filter(task => task["listID"] == this.currentListID)
      }
    }
  }
</script>

<template>
  <div class='task-list'>
    <ListHeader class="item" @view-changed='loadTasks' />
    <draggable 
      :list="visibleTasks" 
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
          @remove-item='deleteTask(element.id, index)'
        />
      </template>

    </draggable>
  </div>

</template>

<style>

  .list-group {
    display: flex;
    flex-flow: column nowrap;
    gap: 3px;
  }
  .ghost {
    opacity: 0.5;
    background: lightblue; 
  }
  .item  {
    flex-grow: 1;
  }

</style>
