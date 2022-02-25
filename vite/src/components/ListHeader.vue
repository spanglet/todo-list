<template>
 <div class="list-header">
   <div class="col-header">
     Name
   </div>
   <div class="col-header">
     Description
   </div>
   <Button :color="blue" :action="showForm"></Button>     
  <Form v-if="formVisible"> </Form>
 </div>

</template>


<script>

  import Button from "./Button.vue"
  import Form from "./Form.vue"
  export default { 

    components: {
      Button,
      Form
    },
    data() {
      return {
        name: "",
        description: "",
        tasks: {},
        formVisible: false 
      }
    },
    methods: {
      showForm() {
        this.formVisible = true
      }
    }
  }

</script>


<style>

  .list-header {
 
    display: flex;
    list-style: none;
    gap: 10px;
  }
  .col-header {

    display: flex;
    justify-content: center;
    background: tomato;
    height: 50px;
    width: 150px;
    text-align: center;
    border-radius: 25px;
  }

</style>
