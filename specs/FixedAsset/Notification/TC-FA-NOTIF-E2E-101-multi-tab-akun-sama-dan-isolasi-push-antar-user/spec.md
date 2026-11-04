---
id: TC-FA-NOTIF-E2E-101-multi-tab-akun-sama-dan-isolasi-push-antar-user
title: "Multi-Konteks: Multi-Tab Akun yang Sama dan Isolasi Push Antar User"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-NOTIF-5
  - TC-FA-NOTIF-79
  - TC-FA-NOTIF-227
  - TC-FA-NOTIF-356
  - TC-FA-NOTIF-366
coverage:
  web: automated
---

# Multi-Konteks: Multi-Tab Akun yang Sama dan Isolasi Push Antar User

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`, `Fixture.fixedAssetNotification.totalControl`. Tab A dan tab B memakai akun yang sama pada browser yang sama. Login di hook `before` spec ini (tab A); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Akun sesi kedua untuk TC-FA-NOTIF-356 (login pada langkah 33 di konteks browser kedua): Staff (Pre-setup #9, Staff Disposal), `staffDisposal_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_STAFFDSP_PASSWORD`, `Fixture.fixedAssetNotification.staffDisposal`. TC tidak menyebut nomor Pre-setup akun Staff (lihat Temuan untuk QA).
- Data Pre-setup: notifikasi N-01 sampai N-07 (Pre-setup #17; N-01 sampai N-05 Unread, N-06 dan N-07 Read, badge `5`; N-03 view-only Unread) dan varian N-01 sampai N-37 (Pre-setup #17 dan #18) untuk TC-FA-NOTIF-227. Varian seed ditukar oleh fixture BE penukar (butir "Fixture BE penukar varian seed #18" di `suite.md`) pada langkah 1; fixture BE pemulih seed (butir "Fixture BE pemulih seed notifikasi dan transaksi" di `suite.md`) dijalankan di hook `before`, pada langkah 7, 12, 20, 32, dan di hook `after`.
- Kemampuan teknis: dua tab browser dengan akun yang sama dan dua sesi UI dengan akun berbeda (tab atau sesi kedua menjadi objek asersi, bagian 3 prinsip 13c); intercept stream SSE pada tab B (`Spectra.intercept()`, butir "Intercept respons HTTP dan SSE pada browser" di `suite.md`) untuk membuat tab B tidak menerima update pada TC-FA-NOTIF-79; fixture BE pemicu event yang menghasilkan notifikasi hanya untuk Staff (butir "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`). Semuanya disediakan tim FE/BE tanpa endpoint karangan (S-13).
- Pengecualian S-06/S-12 butir A-16: notifikasi seed N-01 sampai N-07 dan varian N-01 sampai N-37 (Pre-setup #17 dan #18) dipakai literal tanpa suffix `{runId}-101` sebagai target Mark as Read dan Search, karena notifikasi seed hanya ada untuk akun Pre-setup. Pemulihan ke keadaan awal dijamin fixture BE pemulih (idempotent) di hook `before` dan `after` spec ini serta sebagai langkah penghubung antar blok TC (langkah 7, 12, 20, 32); suite berjalan serial (`parallel: false`).
- Intercept SSE pada tab B (langkah 22) hanya membuat tab B basi sebagai pemicu state pada TC-FA-NOTIF-79 dan ditahan sampai akhir blok itu (dilepas pada langkah 32, sebelum blok TC-FA-NOTIF-356) karena tab B harus tetap belum menerima update selama langkah 25 sampai 31.
- Asersi absence atas notifikasi in-app pada TC-FA-NOTIF-356 memakai baseline per sesi yang dicatat tepat sebelum pemicu, anchor positif (sesi Staff menerima), dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD).
- Env var `FA_TC_PASSWORD` dan `FA_STAFFDSP_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk kedua akun di atas: hook suite `before` menyetelnya dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-227: State Notification Center tidak dibagi antar tab browser

1. Tukar seed notifikasi ke varian N-01 sampai N-37 (Pre-setup #17 dan #18) lewat fixture BE penukar, lalu muat ulang halaman Fixed Asset > Dashboard di tab A
2. Pada tab A, klik Bell icon lalu klik `[Show All]` untuk membuka Notification Center
3. Pada tab A, ketik Search `access`, tekan Enter
4. Buka tab B baru pada Fixed Asset > Dashboard dengan akun yang sama, klik Bell icon, lalu klik `[Show All]`
5. Verifikasi Notification Center pada tab B tampil dari keadaan default
6. Verifikasi Notification Center pada tab B tanpa Search (kotak Search tidak berisi `access`)
7. Tutup tab B, pulihkan seed notifikasi Pre-setup #17 (N-01 sampai N-07) lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard di tab A

### TC-FA-NOTIF-5: Badge Bell icon berkurang real-time saat notifikasi jadi Read dari sesi lain

8. Buka tab B baru pada Fixed Asset > Dashboard dengan akun yang sama, lalu klik Bell icon pada tab B
9. Pada tab B, klik `[Mark as Read]` pada item N-03
10. Pindah ke tab A tanpa memuat ulang halaman
11. Verifikasi badge Bell icon pada tab A berkurang dari `5` menjadi `4` tanpa reload
12. Tutup tab B, pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard di tab A

### TC-FA-NOTIF-366: Konsistensi cross-tab, notifikasi Read di tab lain tersinkron tanpa reload

13. Pada tab A, klik Bell icon lalu klik `[Show All]` untuk membuka Notification Center
14. Buka tab B baru pada Fixed Asset > Dashboard dengan akun yang sama, klik Bell icon, lalu klik `[Show All]`
15. Pada tab B, catat nilai badge Bell icon sebagai baseline
16. Pada tab A, klik `[Mark as Read]` pada item N-03
17. Pindah ke tab B tanpa memuat ulang halaman
18. Verifikasi item N-03 pada tab B berstatus Read
19. Verifikasi badge Bell icon pada tab B berkurang dari baseline langkah 15
20. Tutup tab B, pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard di tab A

### TC-FA-NOTIF-79: Mark as Read pada dua tab menghasilkan No-Op pada tab kedua

21. Buka tab B baru pada Fixed Asset > Dashboard dengan akun yang sama, lalu klik Bell icon pada tab A dan tab B
22. Pada tab B, blokir push SSE lewat intercept
23. Pada tab A, klik `[Mark as Read]` pada item N-03
24. Verifikasi badge Bell icon pada tab A berkurang menjadi `4`
25. Pindah ke tab B
26. Verifikasi tombol `[Mark as Read]` pada item N-03 masih tampil (anchor: tab B belum menerima update)
27. Pada tab B, klik `[Mark as Read]` pada item N-03
28. Verifikasi muncul toast sukses `Success, notification has been marked as read.` pada tab B
29. Verifikasi tidak ada toast error pada tab B
30. Verifikasi item N-03 pada tab B berstatus Read
31. Verifikasi badge Bell icon pada tab B menjadi `4`
32. Lepas intercept SSE pada tab B, tutup tab B, pulihkan seed notifikasi Pre-setup #17 lewat fixture BE pemulih, lalu muat ulang halaman Fixed Asset > Dashboard di tab A

### TC-FA-NOTIF-356: Push SSE tidak mengirim notifikasi ke sesi user lain

33. Buka sesi UI kedua (konteks browser kedua), login sebagai Staff (Pre-setup #9) dengan `Spectra.env.FA_STAFFDSP_PASSWORD`, lalu buka Fixed Asset > Dashboard
34. Pada sesi Total Control, klik Bell icon, lalu catat nilai badge Bell icon sesi Total Control dan item pada Dropdown Panel (baseline); pada sesi Staff catat nilai badge Bell icon (baseline)
35. Picu notifikasi baru hanya untuk Staff lewat fixture BE pemicu event hingga tersimpan
36. Verifikasi badge Bell icon sesi Staff bertambah dari baseline langkah 34 (anchor positif: sesi Staff menerima)
37. Tunggu 5 detik tanpa memuat ulang halaman
38. Verifikasi badge Bell icon sesi Total Control sama dengan baseline langkah 34
39. Verifikasi item pada Dropdown Panel sesi Total Control sama dengan baseline langkah 34 (N-01 sampai N-05)

## Notes

- Spec kelas c (multi-konteks): tab B dan sesi Staff menjadi objek asersi pada seluruh TC.
- `P-2`: intercept SSE pada langkah 22 (kelas b) hanya membentuk keadaan tab B belum menerima update sebagai pemicu state dan bukan objek asersi; ditahan sampai akhir blok TC-FA-NOTIF-79 (alasan di `## Prerequisites`) dan dilepas pada langkah 32 sebelum blok berikutnya.
- Urutan blok: TC-FA-NOTIF-227 lebih dulu karena memerlukan varian seed N-01 sampai N-37 yang dipulihkan sebelum blok lain; TC-FA-NOTIF-5 dan TC-FA-NOTIF-366 (sinkron real-time tanpa intercept) mendahului TC-FA-NOTIF-79 karena TC-FA-NOTIF-79 memakai intercept SSE yang menahan update; TC-FA-NOTIF-356 terakhir karena membuka konteks browser kedua dan akun lain (S-10).
- Seed Pre-setup #17 (N-01 sampai N-07) juga dipakai spec kelas lain (defense-in-depth); pemisahan mengikuti satu spec satu kelas harness (kelas c multi-konteks di sini).
- Langkah penghubung (S-03): langkah 2, 4, 13, dan 14 (membuka Notification Center lewat Bell icon dan `[Show All]` karena TC tidak menyebut jalur lain); langkah 3 (Search, bagian 8b butir 9); langkah 7, 12, 20, dan 32 (pemulihan seed dan penutupan tab B antar TC, S-09); langkah 8 dan 21 (membuka tab B dan Bell icon); langkah 10, 17, dan 25 (pindah tab); langkah 15 dan 34 (baseline, S-12); langkah 33 (login sesi Staff, ganti akun eksplisit); langkah 1 (penukar varian seed N-01 sampai N-37 yang dibutuhkan TC-FA-NOTIF-227, sedangkan TC lain memakai N-01 sampai N-07); langkah 35 (pemicu lewat fixture BE; hasilnya diasersi pada langkah 36).
- Asersi absence dengan anchor positif (bagian 8b butir 2): langkah 6 didahului langkah 5 (Notification Center tab B tampil dari keadaan default); langkah 29 didahului langkah 28 (toast sukses tampil); langkah 38 dan 39 didahului langkah 36 (sesi Staff menerima notifikasi) dan jendela 5 detik langkah 37.
- TC-FA-NOTIF-79: "Buka Dropdown Panel pada keduanya" ditulis sebagai langkah 21; langkah 26 menambah `Verifikasi` bahwa tab B masih menampilkan `[Mark as Read]` sebagai anchor keadaan basi sebelum klik tab B.
- Alasan spec melewati ambang sekitar 35 langkah (39 langkah): seluruh blok satu kelas harness (multi-konteks, akun dan tab sebagai objek asersi) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan tiap blok memulihkan seed sendiri.
- Temuan untuk QA:
  - TC-FA-NOTIF-5 dan 366: Pre-setup #17 tidak menjamin tab B dibuka pada layar yang sama; spec membuka tab B pada Fixed Asset > Dashboard (TC-FA-NOTIF-5) dan pada Notification Center (TC-FA-NOTIF-366). Nilai badge awal tab B pada TC-FA-NOTIF-366 tidak ditulis TC; baseline dicatat pada langkah 15.
  - TC-FA-NOTIF-227: Post Condition dan Data Uji kosong; tidak ada asersi tambahan selain tab B tanpa Search.
  - TC-FA-NOTIF-79: cara membuat tab B "belum menerima update" tidak ditulis TC; spec memakai blokir push SSE lewat intercept (kemampuan tim FE/BE).
  - TC-FA-NOTIF-366: Post Condition "N-03 berstatus Read di kedua tab" tidak punya langkah observasi di tab A; hanya tab B yang diasersi.
  - TC-FA-NOTIF-356: "Picu notifikasi hanya untuk Staff" tidak menyebut event, akun Staff (Pre-setup #9 diambil dari satu-satunya role Staff), maupun cara memicunya; spec memakai fixture BE pemicu event tanpa endpoint karangan. Post Condition kosong.
