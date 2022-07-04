import { defineStore } from 'pinia'
import { axios } from "../axios.js"


export const useLists = defineStore('lists', {
  state: () => ({
    lists: [],
    /** @type {'all' | 'completed' | 'incomplete' | 'currentList'} */
    //filter: 'currentList',
    currentListID: 1,
  }),
  getters: {
    completedTasks(state) {
      return state.tasks.filter((task) => task.completed)
    },
    incompleteTasks(state) {
      return state.tasks.filter((task) => !task.completed)
    },
    currentListTasks(state) {
      return state.tasks.filter((task) => task.listID == this.currentListID)
    },
    /**
     * @returns {{ text: string, id: number, isFinished: boolean }[]}
     */
    filteredTasks(state) {
      if (this.filter === 'completed') {
        return this.completedTasks
      }
      else if (this.filter === 'incomplete') {
        return this.incompleteTasks
      }
      else if (this.filter === 'currentList') {
        return this.currentListTasks
      }
      return this.tasks
    },
  },
  actions: {
    async fetchTasks() {
      try {
        var resp = await axios.get("tasks/")
        this.tasks = resp.data
      }
      catch (error) {
        console.log(error)
      }
    },
    async deleteTask(task_id) {
      // DELETE request to remove task from db
      var targetPath = "tasks/" + String(task_id)
      var response = await axios.delete(targetPath)
      this.fetchTasks()
    },
    async addTask(data) {
      var response = await axios.post('tasks/', data)
      this.fetchTasks()
    },
    async completeTask(task_id) {
      await axios.put("tasks/" + task_id, {
         'completed': true
      })
      this.fetchTasks() 
    },
  }
})

