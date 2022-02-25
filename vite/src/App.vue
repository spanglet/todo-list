<script>

  import TaskTile from './components/TaskTile.vue'
  import ListHeader from './components/ListHeader.vue'

  
  var url = "http://127.0.0.1:5000/tasks/list"


  export default { 

    components: {
      TaskTile,
      ListHeader
    },
    data() {
      return {
        name: "",
        description: "",
        tasks: {}
      }
    },
    mounted() {
      axios.get(url, {
	headers: {
          'Access-Control-Allow-Origin': '*'
        }})
        .then((res) => {
          this.tasks = res.data
      })
    },
    methods: {
      action() { alert("The Button Was Clicked.")}
    }
  }
</script>

<template>
  <div id='app'>
    <ListHeader></ListHeader>
    <div v-for='task in tasks'>
      <TaskTile :name="task.name" :description="task.description">
      </TaskTile>
    </div>
  </div>
</template>

<style>
</style>

