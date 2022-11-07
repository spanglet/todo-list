import { defineStore } from 'pinia'

import Fetch from "../fetch.js"

// Holds list-related data and functions across project
export const useLists = defineStore('lists', {
  state: () => ({
    _lists: [],
    currentListID: 0,
  }),
  getters: {
    currentList(state) {
      return state.currentListID
    },
    lists(state) {
      return this._lists
    },
  },
  actions: {
    async fetchLists() {
      var json = await Fetch.get("lists/")
      if (json.data) {
        this._lists = json.data
      }
      if (this.currentListID == 0) {
        this.currentListID = this._lists[0].id
      }
    },
    // Sends delete request to backend and removes from store on success
    async deleteList(list) {
      var json = await Fetch.delete("lists/" + String(list.id))
      if (json.data) {
	var idx = this._lists.indexOf(list)
        this._lists.splice(idx, 1)
	if (this.currentListID == list.id) {
	  this.currentListID = this._lists[0].id
          this.router.push("/app/todo/" + String(this.currentListID))
	}
      }
    },
    async addList(list_name, description) {

      var json = {
	  'name': list_name,
      }
      var json = await Fetch.post("lists/", json)
      if (json.data) {
        this._lists.push(json.data)
      }
    },
  }
})

