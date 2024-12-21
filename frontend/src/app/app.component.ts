import { Component } from '@angular/core';
import { NavbarComponent } from "./shared/navbar/navbar.component";
import { FooterComponent } from './shared/footer/footer.component'
import { Observable, of, shareReplay, Subscription } from 'rxjs';
import { AsyncPipe } from '@angular/common';
import { DataViewModule } from 'primeng/dataview';
import { TasksService } from './core/services/tasks.service';
import { Task } from './core/models';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [NavbarComponent, FooterComponent, AsyncPipe, DataViewModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  subscriptions = new Subscription()

  tasks$: Observable<Task[]> = of()

  constructor(private tasksService: TasksService) {
    this.tasks$ = this.tasksService.getTasks().pipe(shareReplay())
  }

  ngOnDestroy() {
    this.subscriptions.unsubscribe()
  }
}
