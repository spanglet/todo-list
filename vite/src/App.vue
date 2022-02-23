<script>

  import TaskTile from './components/TaskTile.vue'

  
  var url = "https://127.0.0.1:5000/tasks/list"


  export default { 

    data() {
      return {
        name: "",
        description: ""
      }
    },
    mounted() {
      axios.get(url, {
	headers: {
          'Access-Control-Allow-Origin': '*'
        }})
        .then((res) => {
          this.task = res.data['name'].
          this.description = res.data['description']
      })
    }
  }

</script>

<template>
  <div id='app'>
    <div>
      <TaskTile id="task" :name="task" :description="description">
      </TaskTile>
    </div>
  </div>
</template>

<style>
</style>

