import { Component } from '@angular/core'
import { Subscription } from 'rxjs'
import { CommonModule } from '@angular/common'
import { MenuModule } from 'primeng/menu'

@Component({
  selector: 'navbar',
  standalone: true,
  imports: [CommonModule, MenuModule],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss',
})
export class NavbarComponent {
  subscriptions = new Subscription()

  constructor() {}

  ngOnDestroy() {
    this.subscriptions.unsubscribe()
  }
}
