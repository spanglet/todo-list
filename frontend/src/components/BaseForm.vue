<template>
  <div class="form-wrapper" @click.stop=''>

    <div class="base-form-header">
      <SymbolButton @click="closeForm" :icons="['xmark']" class="del-button"/>
    </div>

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
    
      <div class="form-input form-slider" v-if="!fixedDate">
        <label for="deadlineRequired"> Is there a due date? </label>
        <Slider id="deadlineRequired" @clicked="deadline = !deadline" width="6em"/>
      </div>
      <Transition name="toggle-input" mode="out-in" v-if="!fixedDate">
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
      <SymbolButton
        :icons="buttonIcon"
        @click="submitForm"
        class="submit-button"
      >
        <div>
          Create Task
        </div>
      </SymbolButton>
    </div>
  </div>
</template>

<script>
  import SymbolButton from "./SymbolButton.vue"
  import Slider from "./Slider.vue"
  import { useTasks } from '../stores/tasks.js'
  import { format } from 'date-fns'

  export default {
    setup() {
      const store = useTasks()
      return {
        store,
      }
    },
    components: {
      SymbolButton,
      Slider
    },
    props: {
      fixedDueDate: {
        type: Boolean,
        default: false
      },
      defaultDueDate: {
        type: String,
        default: format(new Date(), 'yyyy-MM-dd')
      },
    },
    beforeUnmount() {
      this.closeForm() 
    },
    emits: ['submitted','closed'],
    data() {
      return {
        name: "",
        description: "",
        dueDate: this.defaultDueDate,
        buttonIcon: ["check"],
        deadline: true,
        priority: "",
        fixedDate: this.fixedDueDate,
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
        this.$emit('closed')
      },
      closeForm() {
        this.$emit('closed')
      }
    }
  }      
</script>

<style>
  .form-wrapper {
    border: 1px black solid;
    border-radius: 12px;
    background: lightgrey;
  }
  .form {
    display: flex;
    flex-flow: column nowrap;
    gap: 1em;
    margin: 1em;
    font-weight: bold;
  }
  .base-form-header {
    position: absolute;
    display: flex;
    justify-content: flex-end;
    width: 100%;
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
