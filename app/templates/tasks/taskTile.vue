<script>
export default {
  data() {
    return {
      name: "",
      taskName "{{ }}" 
      
    }
  },
  props: {
    name: String,
    description: String
  }
}
</script>

<template>

  <b-container fluid="lg" class="border">    
    <b-row>
      <b-col>Name is [[name]]</b-col>
      <b-col>Description is [[description]]</b-col>
    </b-row>  
  </b-container>

</template>

