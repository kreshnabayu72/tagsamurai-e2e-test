---
id: TC-GS-USER-E2E-006-deactivate-force-logout-active-session
title: Menonaktifkan user memaksa logout sesi aktifnya secara real time
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-481
  - TC-GS-USER-251
coverage:
  web: automated
---

# Menonaktifkan user memaksa logout sesi aktifnya secara real time

## Prerequisites

- Login sebagai Role: Total Control, entity Client, di sesi browser A
- User "Rina Wijaya" sedang login dan aktif di sesi browser B yang terpisah, di halaman mana pun dari produk berlisensi mana pun
- Tim FE menyediakan sesi browser kedua yang bisa dikendalikan sendiri untuk spec ini, karena butuh dua akun yang login bersamaan
- Di sesi B, daftar notifikasi "Rina Wijaya" dicatat sebelum langkah 1 dan sekali lagi tepat setelah langkah 4

## Test Steps

1. Di sesi A, klik Toggle Active [Global] pada baris "Rina Wijaya" untuk mematikannya (OFF)
2. Klik `[Deactivate]` pada dialog
3. Verifikasi toast sukses "Success, user has been deactivated." muncul di sesi A
4. Di sesi B, verifikasi pesan real time muncul yang memberi tahu user bahwa sesinya telah diakhiri
5. Di sesi B, lakukan permintaan apa pun atau pindah ke halaman mana pun
6. Verifikasi permintaan di sesi B mengembalikan 401 dan sesi dianggap tidak valid
7. Di sesi B, coba login lagi sebagai "Rina Wijaya"
8. Verifikasi dialog blokir login muncul, sesuai dengan user yang sudah dinonaktifkan

### Tidak ada notifikasi terpisah

9. Di sesi B, bandingkan daftar notifikasi yang dicatat tepat setelah langkah 4 dengan yang dicatat sebelum langkah 1
10. Verifikasi tidak ada entri notifikasi baru untuk "Rina Wijaya" dari penonaktifan ini, dan satu-satunya umpan balik yang ia terima adalah pesan sesi berakhir secara real time serta dialog blokir login "Account Deactivated"

## Notes

- Spec ini butuh dua sesi browser dengan dua akun berbeda, itulah sebabnya dipisah dari TC-GS-USER-E2E-005, mengikuti `docs/e2e-conventions.md` bagian 3 (dipisah untuk akun berbeda).
- "Rina Wijaya" berstatus Active tanpa dependensi lain sebelum spec ini berjalan, dan dibiarkan Inactive sesudahnya. Tidak ada pembersihan lanjutan karena tidak ada data yang dibuat.
- TC-GS-USER-251: Deactivate tidak boleh membuat notifikasi in-app tersendiri. Pesan sesi berakhir dan dialog blokir login sudah mencakupnya.
