---
id: TC-GS-USER-E2E-046-sinkron-admin-console
title: Status Active Global user tercermin di Settings User Admin Console
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-170
coverage:
  web: automated
---

# Status Active Global user tercermin di Settings User Admin Console

## Prerequisites

- Login sebagai Role: Total Control di Global Settings, dengan akses ke Admin Console > Settings User
- User "Dina Kusuma" Active Global di Global Settings dan muncul di Admin Console > Settings User, dengan switch `admin_console` ON
- Spec ini mematikan lalu menyalakan kembali Toggle Active Global "Dina Kusuma", jadi datanya kembali seperti awal

## Test Steps

1. Di Global Settings > User, klik Toggle Active [Global] pada baris "Dina Kusuma" untuk mematikannya, lalu klik `[Deactivate]` pada dialog
2. Buka Admin Console > Settings User dan cari "Dina Kusuma"
3. Verifikasi switch `admin_console` pada baris itu Disabled dengan tooltip "This user is inactive in Global Settings. Contact a Global Settings admin to reactivate." dan posisi switch terakhir dipertahankan
4. Pilih baris "Dina Kusuma" bersama satu baris user Active Global lain, lalu klik bulk action `Activate`
5. Verifikasi baris "Dina Kusuma" dilewati, sedangkan baris user lain diproses
6. Kembali ke Global Settings > User, klik Toggle Active [Global] pada baris "Dina Kusuma" untuk menyalakannya, lalu klik `[Activate]` pada dialog
7. Buka Admin Console > Settings User lagi
8. Verifikasi switch `admin_console` pada baris "Dina Kusuma" aktif kembali dengan posisi yang sama seperti sebelum dimatikan, dan perubahan tampil langsung tanpa cache lama

## Notes

- Yang diuji adalah sisi Global Settings sebagai sumber status. Perilaku switch dan bulk activate di Admin Console dimiliki modul Settings User Admin Console (`TC-AC-SU-33`, `34`, `249`).
- Spec ini butuh akses ke dua aplikasi (Global Settings dan Admin Console). Kebutuhan itu ditulis di Prerequisites untuk tim FE.
