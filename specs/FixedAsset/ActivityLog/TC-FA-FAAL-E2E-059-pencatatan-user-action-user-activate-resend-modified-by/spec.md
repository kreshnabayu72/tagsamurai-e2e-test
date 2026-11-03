---
id: TC-FA-FAAL-E2E-059-pencatatan-user-action-user-activate-resend-modified-by
title: "Pencatatan User Action: Activate, Deactivate, Resend, Home Group, dan Modified By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-231
  - TC-FA-FAAL-232
  - TC-FA-FAAL-233
  - TC-FA-FAAL-234
  - TC-FA-FAAL-253
  - TC-FA-FAAL-279
coverage:
  web: automated
---

# Pencatatan User Action: Activate, Deactivate, Resend, Home Group, dan Modified By

## Prerequisites

- Mode: FE+BE.
- Akun aktor dan observer: Total Control (Pre-setup #1, Admin Alpha), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log). Pengecualian: tiap TC membuka Settings > User untuk aksinya lalu Activity Log > User Action.
- Data target, identitas dari `Fixture.activity-log.<kunci>` (fixture belum ada, disediakan tim FE):
  - Citra Lestari (Pre-setup #16): berstatus Inactive di awal spec (TC-FA-FAAL-231); Home Group `Gedung A` (TC-FA-FAAL-234); email `citralestari@qwertysystem.net` saat berstatus Pending (TC-FA-FAAL-233).
  - Indra Wijaya (Pre-setup #21): berstatus Active dengan email baru pending konfirmasi `indra.wijaya.baru@qwertysystem.net` (TC-FA-FAAL-279).
  - Hendra Pratama #1 (Pre-setup #16): pelaku baris UA-13 (Modified By `Hendra P`) pada Tab User Action UA-01 sampai UA-15 (Pre-setup #12); disediakan tim FE/BE sebagai data milik spec ini karena dihapus pada langkah 29.
  - Group `Gedung A` dan `Gedung B` ada.
- Cooldown Resend untuk Citra Lestari dan Indra Wijaya sudah berakhir karena belum ada Resend sebelumnya (disediakan tim FE/BE di hook `before`). Email Resend yang terkirim tidak diasersi.
- Kemampuan teknis disediakan tim FE/BE: sesi API aktor (butir "Sesi API aktor" di `suite.md`) untuk Admin Alpha pada langkah 28 dan 29.
- Baseline (S-12): total baris Tab User Action dibaca dari teks pagination `Showing x–y of N entries` pada langkah 1; tiap Verifikasi baris baru juga memastikan total bertambah dari total terakhir yang dibaca.
- State yang diubah dan pemulihannya: status Citra Lestari dipulihkan pada langkah 15 dan di hook `after`; Home Group Citra Lestari dikembalikan ke `Gedung A` di hook `after`; Hendra Pratama #1 dihapus pada langkah 29 dan disediakan ulang di hook `before` run berikutnya.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun aktor.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Activity Log > User Action dan catat total baris dari teks pagination (N0)

### TC-FA-FAAL-231: Activate user tercatat dengan Object User

2. Aktifkan Citra Lestari di Settings > User
3. Tunggu aksi selesai
4. Buka Activity Log > User Action
5. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Activate`, Object `User`, Name `Citra Lestari`, Field `Status`, Old Value `Inactive`, New Value `Active`, Modified By `Admin A`

### TC-FA-FAAL-232: Deactivate user tercatat dengan Object User

6. Nonaktifkan Citra Lestari di Settings > User
7. Tunggu aksi selesai
8. Buka Activity Log > User Action
9. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Deactivate`, Object `User`, Name `Citra Lestari`, Field `Status`, Old Value `Active`, New Value `Inactive`, Modified By `Admin A`

### TC-FA-FAAL-233: Resend Activation Email tercatat dengan Old Value strip

10. Pulihkan Citra Lestari ke status Pending dengan email `citralestari@qwertysystem.net` lewat seed API
11. Klik Resend Activation Email untuk Citra Lestari
12. Tunggu aksi selesai
13. Buka Activity Log > User Action
14. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Resend Activation Email`, Object `User`, Name `Citra Lestari`, Field `Activation Email`, Old Value `—`, New Value `citralestari@qwertysystem.net`, Modified By `Admin A`
15. Pulihkan Citra Lestari ke status Active lewat seed API

### TC-FA-FAAL-234: Edit Home Group tercatat dengan Object User

16. Ubah Home Group Citra Lestari menjadi Gedung B
17. Tunggu aksi selesai
18. Buka Activity Log > User Action
19. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Edit Home Group`, Object `User`, Name `Citra Lestari`, Field `Home Group`, Old Value `Gedung A`, New Value `Gedung B`, Modified By `Admin A`

### TC-FA-FAAL-279: Resend Confirmation Email tercatat dengan Old Value strip

20. Klik Resend Confirmation Email untuk Indra Wijaya di Settings > User
21. Tunggu aksi selesai
22. Buka Activity Log > User Action
23. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Resend Confirmation Email`, Object `User`, Name `Indra Wijaya`, Field `Confirmation Email`, Old Value `—`, New Value `indra.wijaya.baru@qwertysystem.net`, Modified By `Admin A`

### TC-FA-FAAL-253: Modified By tidak berubah saat pelaku diganti nama, dinonaktifkan, atau dihapus

24. Buka Activity Log > User Action
25. Ketik Search `Hendra`, tekan Enter
26. Verifikasi baris UA-13 tampil dengan Modified By `Hendra P`
27. Klik `(←)` pada kotak Search
28. Admin Total Control (sesi API aktor, Admin Alpha) mengganti nama Hendra Pratama #1 menjadi `Hendra Wijaya` di Global Settings > User hingga tersimpan
29. Admin Total Control (sesi API aktor, Admin Alpha) menonaktifkan lalu menghapus pengguna tersebut hingga tersimpan
30. Tunggu aksi selesai
31. Buka Activity Log > User Action
32. Ketik Search `Hendra`, tekan Enter
33. Verifikasi baris UA-13 tetap tampil dengan Modified By `Hendra P`
34. Arahkan kursor ke Modified By pada baris UA-13
35. Verifikasi hover Modified By menampilkan `Hendra Pratama`
36. Klik `(←)` pada kotak Search
37. Klik icon Filter dan buka dropdown Modified By
38. Verifikasi dropdown Modified By memuat `Hendra Pratama`
39. Verifikasi dropdown Modified By tidak memuat `Hendra Wijaya`

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung "Tunggu aksi selesai" (S-03, 8b.8, tanpa Verifikasi): langkah 3, 7, 12, 17, 21, 30; ditulis sebelum tiap pembukaan Activity Log > User Action yang mengikuti aksi tulis tanpa asersi di antaranya. Verifikasi polling tetap menunggu commit log.
- Spec di atas 35 langkah karena 6 langkah penghubung "Tunggu aksi selesai"; spec memuat enam TC (39 langkah, 33 tanpa langkah penghubung tunggu); status Citra Lestari pada TC-FA-FAAL-231 sampai 234 berurutan (hasil tiap TC menjadi keadaan awal TC berikutnya sampai dipulihkan seed API), sedangkan TC-FA-FAAL-279 (Indra Wijaya) dan TC-FA-FAAL-253 (Hendra Pratama #1) independen dari TC lain, sehingga dipertahankan dalam satu spec.
- Urutan TC: 231, 232, 233, 234, 279, 253. TC-FA-FAAL-253 diletakkan terakhir karena menghapus pelaku Hendra Pratama #1.
- Langkah penghubung (S-03): langkah 1, 4, 8, 13, 18, 22, 24, 31 (membuka Tab User Action), langkah 10 dan 15 (pemulihan status Citra Lestari lewat seed API), langkah 25, 27, 32, 36 (Search untuk menemukan baris target, R-16), langkah 26 (membuktikan UA-13 tampil sebelum langkah 33, anchor sebelum aksi).
- Langkah 5, 9, 14, 19, 23 memakai idiom polling (bagian 6): muat ulang Tab User Action tiap 5 detik, batas 2 menit, sebagai pengganti langkah tunggu tersendiri; TC-FA-FAAL-231, 232, 233 menuliskannya di Langkah 2 TC sumber dan spec memakainya juga untuk langkah 19.
- Baseline S-12: langkah 1 mencatat N0. Tiap Verifikasi baris baru juga memeriksa total pagination lebih besar dari total pada Verifikasi sebelumnya.
- Langkah 26 dan 33 mengidentifikasi UA-13 lewat Search `Hendra` karena Tab User Action tumbuh dan UA-13 belum tentu di halaman pertama (S-14). Anchor absence langkah 39 adalah Verifikasi langkah 38 pada dropdown yang sama.
- R-14: Modified By diasersi `Admin A` dan `Hendra P` (First Name dan Last Initial); nama lengkap hanya pada hover.
- Email Resend (TC-FA-FAAL-233 dan 279) terkirim sebagai efek aksi dan tidak diasersi; TC tidak memuat Expected email.
- Temuan untuk QA:
  - TC-FA-FAAL-253 menyebut "Hendra Pratama #1" tanpa menjelaskan arti `#1` dan Pre-setup yang memuat user itu; spec memakai Pre-setup #16 sebagai data milik spec.
  - TC-FA-FAAL-233 mengharuskan Citra Lestari berstatus Pending sedangkan TC-FA-FAAL-231 dan 232 mengubah statusnya; spec memulihkannya lewat seed API pada langkah 10.
  - TC-FA-FAAL-253 langkah 4 tidak menyebut kapan baris UA-13 berada di halaman teramati; spec memakai Search `Hendra`.
