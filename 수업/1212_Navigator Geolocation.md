## Navigator Geolocation

```javascript
// 현재 위치 가져오기
navigator.geolocation.getCurrentPosition(geoSuccess, geoError);

// 가져오기 성공
function geoSuccess(position) {
    // 위도
    const lat = position.coords.latitude;
    // 경도
    const lng = position.coords.longitude;
    const accuracy = Math.floor(postion.coords.accuracy);
}

function geoError() {
    alert('Geolocation Error');
}

```

* 정보 제공 동의하면 구글 지도에 위치를 확인할 수 있습니다.