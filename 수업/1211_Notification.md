## 푸시 알림 

```javascript
// 알림 기능
const btn = document.querySelector('button');
btn.addEventListener('click', notify);

function notify() {
    switch (Notification.permission) {
        case 'default':
            Notification.requestPermission();
            break;
        case 'granted':
            new Notification('안녕하세요');
            break;
        case 'denied':
            alert('알림 Off');
            break;
    }
}
```

