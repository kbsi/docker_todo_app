import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Task } from '../models'

const URL = 'http://localhost/api/v1'

@Injectable({
  providedIn: 'root',
})
export class TasksService {
  constructor(private http: HttpClient) {}
  
  getTasks() {
    return this.http.get<Task[]>(`${URL}/tasks`)
  }

  addTask(task: Task) {
    return this.http.post<Task>(`${URL}/tasks`, task)
  }
}
