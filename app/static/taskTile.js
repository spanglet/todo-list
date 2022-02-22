
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
    <div class="row">    
      <div class="column" style="width: 50%;">
        <div>Name is [[name]]</div>
      </div>  
      <div class="column" style="width: 50%;">
        <div>Description is [[description]]</div>
      </div>  
    </div>
  `
})
