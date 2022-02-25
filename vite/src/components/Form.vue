<template>
  <div>
    <label> Name </label>
    <input type="text" v-model="name">
    <label> Description </label>
    <input type="text" v-model="description">
  </div>
  <Button :color="green" :action="newTask" @click="$emit('taskSent')">
  </Button>
</template>

<script>
  import Button from "./Button.vue"
  export default {
    components: {
      Button
    },
    data() {
      return {
        name: "",
        description: ""
      }
    },
    methods: {
      newTask() {

        var url = "127.0.0.1:5000/tasks/new_task"
        
        // Name field must be filled out
        if (name === "") {
          alert("Name cannot be empty")
          return
        }
         
        // New task request is sent to Flask backend
        axios.post(url, data, {
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          }
        })
      }
    }
  }
      
</script>
