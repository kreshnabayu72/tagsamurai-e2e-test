---
id: TC-AC-SG-E2E-032-popup-create-terisi-reload-dan-navigasi-in-app
title: "Popup Create Terisi: Reload dan Navigasi In-App"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-102
  - TC-AC-SG-103
coverage:
  web: automated
---

# Popup Create Terisi: Reload dan Navigasi In-App

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook `before` suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis: `Region Reload-{runId}-032` (level 1) dibuat pada TC-AC-SG-102 untuk cabang "setelah Submit sukses"; nama ditetapkan spec karena TC tidak menyebut nama. Nilai ketikan lain (`Draft Reload`, `Draft Navigasi`) memakai nilai literal TC karena tidak pernah disimpan.
- Kemampuan teknis: menangani dialog `beforeunload` browser (mengamati kemunculan dan menolak reload dengan tetap di halaman), disediakan tim FE; Fixture BE (penghapusan data milik spec) disediakan tim FE/BE (lihat `suite.md`).
- Pemulihan: hook `after` menghapus group milik spec lewat Fixture BE.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-102: Reload saat popup Create terisi

1. Klik `[+] Group` di Sidebar Group Tree
2. Ketik `Draft Reload` pada Group Name
3. Tekan F5
4. Verifikasi konfirmasi bawaan browser (beforeunload) muncul
5. Batalkan reload dengan memilih tetap berada di halaman pada konfirmasi bawaan browser
6. Klik `[✕]` pada popup
7. Verifikasi dialog Unsaved Changes tampil
8. Klik `[Leave]`
9. Klik `[+] Group` di Sidebar Group Tree
10. Tekan F5 pada popup kosong
11. Verifikasi Sidebar Group Tree dan `[+] Group` tampil kembali
12. Verifikasi konfirmasi bawaan browser (beforeunload) tidak muncul pada popup kosong
13. Klik `[+] Group` di Sidebar Group Tree
14. Ketik `Region Reload-{runId}-032` pada Group Name, klik `[Submit]`
15. Tunggu aksi selesai (popup tertutup)
16. Tekan F5
17. Verifikasi Sidebar Group Tree dan `[+] Group` tampil kembali
18. Verifikasi konfirmasi bawaan browser (beforeunload) tidak muncul setelah Submit sukses

### TC-AC-SG-103: Navigasi in-app saat popup Create terisi

19. Klik `[+] Group` di Sidebar Group Tree
20. Ketik `Draft Navigasi` pada Group Name
21. Klik menu `Settings > User` pada sidebar navigasi
22. Verifikasi perpindahan route dicegat (halaman Settings > Group tetap tampil dengan popup terbuka)
23. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" tampil
24. Klik `[Cancel]`
25. Verifikasi navigasi dibatalkan dan popup tetap terbuka
26. Klik `[✕]` pada popup
27. Verifikasi dialog Unsaved Changes tampil
28. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 5 (menolak reload agar sesi popup dapat ditutup deterministik, S-08), langkah 8 dan 28 (menutup popup yang dirty setelah Verifikasi dialog langkah 7 dan 27), langkah 15 (tunggu aksi selesai sebelum F5, bagian 8b butir 8).
- Langkah 11 dan 17 adalah anchor positif bagi asersi absence langkah 12 dan 18 (R-21).
- Temuan untuk QA: TC-AC-SG-102 Expected butir "pada popup kosong atau setelah Submit sukses konfirmasi tidak muncul" tidak punya langkah dan data di TC; spec menambah langkah 9 sampai 18 dengan nama group `Region Reload-{runId}-032` yang ditetapkan spec.
