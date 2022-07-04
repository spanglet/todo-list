<template>
  <div class="form">
    <div class="form-input">
      <label for="name">Task Name</label>
      <input
        v-model="name"
        id="name"
        type="text"
      >
      <div class="warning-message" v-show="name.length < 1"> Name must not be empty. </div>
    </div>
    <div class="form-input">
      <label for="description"> Description </label>
      <textarea
        v-model="description"
        id="description"
        class="textarea"
        type="text"
        rows="2"
      />
    </div>
    <div class="form-input form-slider">
      <label for="deadlineRequired"> Is there a due date? </label>
      <Slider id="deadlineRequired" @clicked="deadline = !deadline" width="6em"/>
    </div>
    <Transition name="toggle-input" mode="out-in">
      <div key=1 v-if="deadline" class="form-input">
        <label for="date"> Due Date </label>
        <input
          v-model="dueDate"
          id="date"
          type="date"
        >
      </div>
      <div key=2 class="form-input" v-else>
        <label for="priority"> Priority </label>
        <select
          v-model="priority"
          id="priority"
          class="selector"
        >
          <option disabled value=""> Select the task's priority</option>
          <option>Optional</option>
          <option>Important</option>
          <option>Urgent</option>
        </select>
      </div>
    </Transition>
    <Button :btn-type="buttonIcon" class="submit-button"  :action="submitForm">
      <div>
        Create Task
      </div>
    </Button>
  </div>
</template>

<script>
  import Button from "./Button.vue"
  import Slider from "./Slider.vue"
  import { useTasks } from '../stores/tasks.js'

  export default {
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    components: {
      Button,
      Slider
    },
    emits: ['submitted'],
    data() {
      return {
        name: "",
        description: "",
        priority: [],
        dueDate: new Date().toLocaleDateString(),
        buttonIcon: "check",
        deadline: true,
        priority: ""
      }
    },
    methods: {
      submitForm() {

        // New task request is sent to Flask backend
        if (!this.name) {
          // Use a watcher or something similiar to make form message visible
        }
          
        this.store.addTask( {
            "name": this.name,
            "description": this.description,
            "trueDueDate": this.dueDate,
            "priority": this.priority,
            "listID": this.store.currentListID
          })
        this.$emit('submitted', true)
      }
    }
  }      
</script>

<style>
  .form {
    display: flex;
    flex-flow: column nowrap;
    background: lightgrey;
    opacity: .98;
    gap: 1em;
    border: 1px black solid;
    border-radius: 12px;
    padding: 1em;
    font-weight: bold;
  }
  .form-input {
    display: flex;
    flex-flow: column nowrap;
    gap: .3em;
  }
  .form-input input {
    font-size: 18pt;
  }
  .submit-button {
    flex: 1;
    background: hsl(var(--hue-green), 100%, var(--lgt-4));
    justify-content: space-evenly;
    font-size: 18pt;
    align-self: center;
  }
  .submit-button > * {
    margin: 0 .5em 0 .5em;
  }
  .form-slider {
    width: 50%;
    align-self: center;
  }
  .message {
    font-size: 14pt;
  }
  .textarea {
    border-radius: 3px; 
    font-size: 16pt;
  }
  .warning-message {
    color: darkred;
    font-style: italic;
  }
  .selector {
    font-size: 1.2em;

  }

.toggle-input-enter-active,
.toggle-input-leave-active {
  transition: all .5s ease-in-out;
}

.toggle-input-enter-from {
  transform: translateX(50px);
  opacity: 0;
}

.toggle-input-leave-to {
  transform: translateX(-50px);
  opacity: 0;
}

</style>
