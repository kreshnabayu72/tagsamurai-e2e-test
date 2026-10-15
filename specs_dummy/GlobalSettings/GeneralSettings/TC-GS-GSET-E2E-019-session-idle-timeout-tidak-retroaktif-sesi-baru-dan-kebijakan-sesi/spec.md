---
id: TC-GS-GSET-E2E-019-session-idle-timeout-tidak-retroaktif-sesi-baru-dan-kebijakan-sesi
title: "Session Idle Timeout: tidak retroaktif pada sesi berjalan, berlaku pada sesi baru, dan tidak mengubah kebijakan concurrency Auth"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-GSET-57
  - TC-GS-GSET-58
  - TC-GS-GSET-59
coverage:
  web: automated
---

# Session Idle Timeout: tidak retroaktif pada sesi berjalan, berlaku pada sesi baru, dan tidak mengubah kebijakan concurrency Auth

## Prerequisites

- Akun Total Control Budi Santoso dengan sesi A aktif
- Admin B (Total Control) pada sesi terpisah
- Record General Settings entitas tersimpan: Currency Code `IDR`, Date Format `dd/MM/yy`, Time Format `HH:mm`, Time Zone `Asia/Jakarta`, Session Idle Timeout `30 minutes`
- Harness eksternal waktu untuk memicu idle melewati batas (dikendalikan dari sisi server/aplikasi, bukan jam browser)

## Test Steps

### Tidak Retroaktif pada Sesi Berjalan

1. Admin B memilih Session Idle Timeout `1 hour` lalu klik `[Save]`
2. Pada sesi A, biarkan idle melewati 30 menit
3. Pada sesi A, lakukan aksi apa pun setelah 31 menit idle
4. Verifikasi sesi A tidak diputus dan tidak di-reset setelah Save oleh Admin B
5. Verifikasi sesi A tetap memakai batas 30 menit: setelah 31 menit idle sesi A berakhir (Dialog Session Expired sesuai Auth)

### Berlaku pada Sesi Baru

6. Logout lalu login kembali sebagai Budi Santoso (sesi baru)
7. Biarkan idle 31 menit lalu lakukan aksi apa pun
8. Verifikasi pada 31 menit idle sesi baru tetap aktif
9. Biarkan idle hingga 61 menit lalu lakukan aksi
10. Verifikasi setelah melewati 60 menit idle sesi berakhir (Dialog Session Expired sesuai Auth)

### Tidak Mengubah Kebijakan Concurrency Auth

11. Login Budi Santoso di browser 1 (sesi web 1)
12. Login Budi Santoso di browser 2 (sesi web 2)
13. Kembali ke browser 1 dan lakukan aksi
14. Verifikasi kebijakan concurrency Auth tetap berlaku (maks. 1 sesi web aktif): sesi web 1 diakhiri sesuai perilaku Auth; nilai Session Idle Timeout tidak mengubah jumlah sesi yang diizinkan

## Notes

- Menggabungkan TC-GS-GSET-57, 58, 59 (Manual Only; butuh harness waktu). Idle lintas menit dikendalikan dari sisi server/aplikasi, bukan penungguan jam browser nyata.
