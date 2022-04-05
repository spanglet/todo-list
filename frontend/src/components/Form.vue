<template>
  <div class="form">
    <input class="task-input" type="text" placeholder="Name" v-model="name">
    <input class="task-input" type="text" placeholder="Description" v-model="description">
    <input class="task-input" type="date" placeholder="07/03/2027" v-model="dueDate">
    <Button :btn-type="buttonIcon" id="submitButton"  :action="submitForm"> Submit </Button>
    <p class="message" v-if="warning">Name must not be empty</p> 
  </div>
</template>

<script>
  import Button from "./Button.vue"
  export default {
    components: {
      Button
    },
    emits: ['submitted'],
    inject: ['currentListID'],
    data() {
      return {
        name: "",
        description: "",
        warning: false,
        buttonIcon: "check",
        dueDate: new Date().toLocaleDateString(),
        listID: this.currentListID
      }
    },
    methods: {
      submitForm() {

        var url = "http://127.0.0.1:5000/tasks/"
         
        // New task request is sent to Flask backend
        axios.post(url, {
            "name": this.name,
            "description": this.description,
            "trueDueDate": this.dueDate,
            "listID": this.listID
          },  {
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
          }
        }).then((res) => { 
          // Emit to parent container so list is updated
          if (res.status == 200) {
            this.$emit('submitted', true)
            this.warning = false
          }       
          // Bad request will occur if required fields are empty
          if (res.status == 400) {
            this.warning = true
          }
        })
      }
    }
  }      
</script>

<style>
  .form {
    display: flex;
    gap: 1em;
    height: 40px;
    
  }
  .task-input {
    flex: 5;
  }
  #submitButton {
    flex: 1;
    background: hsl(var(--hue-green), 100%, var(--lgt-4))
  }
  .message {
    font-size: 14pt;
  }

</style>
