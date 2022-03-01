<template>
 <div class="list-header">
   <div class="col-header">
     Name
   </div>
   <div class="col-header">
     Description
   </div>
   <Button class="pos-button" :action="changeFormVisibility" :icon="buttonIcon" />
 </div>
 <Form @submitted='changeFormVisibility' v-if="formVisible"> </Form>

</template>


<script>

  import Button from "./Button.vue"
  import Form from "./Form.vue"
  export default { 

    components: {
      Button,
      Form
    },
    emits: ['viewChanged'],
    data() {
      return {
        name: "",
        description: "",
        tasks: {},
        formVisible: false,
        buttonIcon: "plus"
      }
    },
    methods: { // triggered on successful form submission
      // emits event up to main container for list refresh
      changeFormVisibility() {
        this.formVisible = !this.formVisible
        this.$emit('viewChanged')

        // Also change button icon
        this.buttonIcon = (this.formVisible ? "minus" : "plus")
      }
    }
  }

</script>


<style>

  .list-header {
 
    display: flex;
    list-style: none;
    justify-content:center;
    align-items: stretch;
    height: 46px;
    gap: 5px;
  }
  .col-header {
    display: flex;
    background: hsl(var(--hue-purple), 100%, var(--lgt-4 ));
    width: 100%;
    text-align: center;
    border-radius: 8px;
    align-items: center;
    justify-content: center;
  }
  .pos-button {
    display: flex;
    width: 10%;
    background: hsl(var(--hue-green), 100%, var(--lgt-3));
  }

</style>
