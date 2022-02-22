
Vue.component('task-tile', {
  delimiters:['[[',']]'],
  data() {
    return {
      name: "",
      taskName: "{{ }}" 
      
    }
  },
  props: {
    name: String,
    description: String
  },
  template: `
  <div>
    <p1> Hopes this shows up </p1>
    <b-container fluid="lg" class="border">    
      <b-row>
        <b-col>Name is [[name]]</b-col>
        <b-col>Description is [[description]]</b-col>
      </b-row>  
    </b-container>
  </div>
  `
})
