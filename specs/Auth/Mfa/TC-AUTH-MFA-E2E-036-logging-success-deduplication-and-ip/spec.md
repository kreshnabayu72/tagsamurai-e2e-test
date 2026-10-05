---
id: TC-AUTH-MFA-E2E-036-logging-success-deduplication-and-ip
title: Pencatatan login final sukses ke kedua surface tanpa duplikasi dan IP tercatat
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-MFA-74
  - TC-AUTH-MFA-77
  - TC-AUTH-MFA-78
  - TC-AUTH-MFA-83
coverage:
  web: automated
---

# Pencatatan login final sukses ke kedua surface tanpa duplikasi dan IP tercatat

## Prerequisites

- Mode: FE+BE
- Faktor-1 Login with Password sukses dan memicu MFA
- Faktor-2 diselesaikan hingga sukses

## Test Steps

### Pemeriksaan Log Saat MFA Sedang Berlangsung (In-Flight)
1. Setelah Faktor-1 sukses dan layar MFA terbuka, periksa Activity Log Session dan User Log
2. Verifikasi BELUM ada entri login Success yang tercatat (mencegah pencatatan prematur sebelum faktor kedua tuntas)

### Pemeriksaan Log Pasca Faktor Kedua Sukses
3. Selesaikan verifikasi faktor kedua (OTP / Authenticator) hingga mendarat di Portal
4. Buka Global Settings > Activity Log > Session
5. Verifikasi tercatat tepat 1 entri baru dengan Status "Success", Note "Login with password", dan kolom IP Address terisi valid
6. Buka Global Settings > User > Detail > User Log
7. Verifikasi tercatat tepat 1 entri baru yang konsisten dengan Status "Success" dan Note "Login with password"
8. Verifikasi tidak ada entri duplikat (tidak tercatat 2 kali dari Faktor-1 dan Faktor-2)

## Notes

- TC Frontend Ref: `TC-AUTH-MFA-FE-36`
- Merepresentasikan `TC-AUTH-MFA-74`, `77`, `78`, `83` (FE Ref: `TC-AUTH-MFA-FE-36`).
