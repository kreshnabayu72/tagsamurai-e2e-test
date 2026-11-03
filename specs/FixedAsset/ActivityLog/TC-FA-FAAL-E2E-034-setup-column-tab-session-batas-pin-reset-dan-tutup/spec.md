---
id: TC-FA-FAAL-E2E-034-setup-column-tab-session-batas-pin-reset-dan-tutup
title: "Setup Column Tab Session: Batas Pin, Overlay Langsung, Reset to Default, Tutup tanpa Save, dan Independensi Antar Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-112
  - TC-FA-FAAL-113
  - TC-FA-FAAL-114
  - TC-FA-FAAL-116
  - TC-FA-FAAL-117
coverage:
  web: automated
---

# Setup Column Tab Session: Batas Pin, Overlay Langsung, Reset to Default, Tutup tanpa Save, dan Independensi Antar Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, Tab Session). Tidak ada ganti akun di tengah spec.
- Data Pre-setup #11 (Tab Session SS-01 sampai SS-11) dan #12 (Tab User Action UA-01 sampai UA-15), hanya dibaca dan tidak diubah. Spec ini mengasersi kolom, bukan isi baris tertentu. Fixture `fixtures/activity-log.json` disediakan tim FE (nama kunci ditetapkan tim FE).
- Daftar 10 kolom Tab Session berurutan: Date, User, Employee ID, Position, Division, Activity, Status, Note, IP Address, Device/Browser. Tab User Action memiliki 8 kolom (termasuk kolom Field).
- Kemampuan teknis: drag and drop pada overlay Column Visibility dan popup Setup Column, hover tooltip, dan tombol `Esc`.
- State yang diubah spec: konfigurasi kolom Tab Session (disimpan lewat `[Save]` atau diterapkan langsung oleh overlay) dan visibilitas kolom Note (Tab Session) serta Field (Tab User Action). Langkah 21 sampai 24 mengembalikan konfigurasi Tab Session ke bawaan, dan langkah 44 serta 46 mengembalikan kolom Note dan Field; hook `after` memulihkannya dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Flag Guided Tooltip halaman Activity Log di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-112: Batas pin maksimal tiga kolom Tab Session

1. Klik header kolom Actions (⋯) > `Setup Column...`
2. Klik icon Pin pada kolom Date, User, dan Employee ID
3. Arahkan kursor ke icon Pin kolom Position
4. Verifikasi icon Pin kolom Position disabled dengan tooltip `Maximum 3 columns can be pinned at once. Unpin another column first.`
5. Unpin kolom Date
6. Verifikasi icon Pin kolom Position aktif kembali
7. Klik `(X)` pada popup

### TC-FA-FAAL-116: Overlay Column Visibility menerapkan perubahan langsung

8. Klik header kolom Actions (⋯)
9. Hilangkan centang Employee ID di overlay
10. Tarik Position ke posisi pertama di overlay
11. Verifikasi perubahan langsung tampil di tabel tanpa tombol Save
12. Tekan F5
13. Verifikasi kolom tersisa pertama tampil: Position tetap kolom pertama setelah muat ulang
14. Verifikasi Employee ID tetap hilang setelah muat ulang

### TC-FA-FAAL-113: Reset to Default pada Popup Setup Column Tab Session

15. Klik header kolom Actions (⋯) > `Setup Column...`
16. Sembunyikan kolom Division
17. Drag kolom Note ke posisi pertama
18. Pin kolom Date
19. Klik `[Save]`
20. Klik header kolom Actions (⋯) > `Setup Column...`
21. Klik `[Reset to Default]`
22. Verifikasi Live Preview menampilkan 10 kolom default urutan awal
23. Verifikasi Live Preview tanpa kolom beku
24. Klik `[Save]`
25. Verifikasi tabel menampilkan susunan default
26. Tekan F5
27. Verifikasi susunan default tetap setelah muat ulang

### TC-FA-FAAL-114: Tutup Popup Setup Column tanpa Save membatalkan perubahan

28. Klik header kolom Actions (⋯) > `Setup Column...`
29. Sembunyikan kolom Note
30. Klik `(X)` pada popup
31. Verifikasi popup tertutup
32. Verifikasi kolom Note tetap tampil di tabel
33. Klik header kolom Actions (⋯) > `Setup Column...`
34. Sembunyikan kolom Note
35. Tekan `Esc`
36. Verifikasi popup tertutup
37. Verifikasi kolom Note tetap tampil di tabel

### TC-FA-FAAL-117: Konfigurasi kolom tiap tab tersimpan independen

38. Klik header kolom Actions (⋯), hilangkan centang kolom Note di overlay Column Visibility
39. Klik tab User Action
40. Verifikasi Tab User Action tetap menampilkan seluruh 8 kolom setelah Note disembunyikan di Tab Session
41. Klik header kolom Actions (⋯), hilangkan centang kolom Field di overlay Column Visibility
42. Klik tab Session
43. Verifikasi Tab Session tetap tanpa kolom Note setelah Field disembunyikan di Tab User Action
44. Klik header kolom Actions (⋯), centang kembali kolom Note di overlay Column Visibility
45. Klik tab User Action
46. Klik header kolom Actions (⋯), centang kembali kolom Field di overlay Column Visibility

## Notes

- Alasan di atas 35 langkah (46 langkah): kelima TC satu halaman, satu kelas fungsional (Setup Column Tab Session), dan dataset yang sama; tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok tidak mengulang langkah per kolom.
- Urutan TC: TC-FA-FAAL-112, 116, 113, 114, 117 (bukan urutan nomor). TC-FA-FAAL-116 menyimpan perubahan langsung dari overlay (Employee ID tersembunyi, Position pertama) dan TC-FA-FAAL-113 mengembalikannya lewat `[Reset to Default]` dan `[Save]` (langkah 21 sampai 24), sehingga TC-FA-FAAL-114 dan TC-FA-FAAL-117 berangkat dari konfigurasi bawaan (S-09, S-10). TC-FA-FAAL-112 tanpa `[Save]` sehingga tidak mengubah konfigurasi tersimpan.
- Langkah penghubung (S-03): langkah 7 (menutup popup tanpa Save sebelum TC berikutnya); langkah 44 sampai 46 (menampilkan kembali kolom Note dan Field, memulihkan state tiap tab).
- Langkah 13 dan 14 mengikuti butir b TC-FA-FAAL-116: `Verifikasi` kolom tersisa pertama tampil (Position, anchor halaman termuat setelah F5) ditulis sebelum `Verifikasi` Employee ID tetap hilang (butir 8b.2).
- Langkah 22 dan 23 memecah butir Expected a TC-FA-FAAL-113 per klausa (kolom default berurutan, tanpa kolom beku; S-01); langkah 25 dan 27 memisahkan "setelah Save" dan "setelah muat ulang" butir b.
- Temuan untuk QA:
  - TC-FA-FAAL-112, 113, 114, 116, 117 mengasumsikan konfigurasi kolom awal adalah bawaan; spec mengandalkan preferensi kolom di browser yang bersih saat spec dimulai (pemulihan oleh hook `after` spec yang menyimpan konfigurasi kolom, kemampuan disediakan tim FE).
  - TC-FA-FAAL-113 menyebut "Sembunyikan Division, drag Note ke posisi pertama, pin Date" dalam satu langkah; spec memecahnya menjadi langkah 16 sampai 18.
  - TC-FA-FAAL-116 menulis "muat ulang halaman" tanpa menyebut cara; spec memakai F5. Expected a ("tanpa tombol Save") tidak menyebut cara mengamati selain overlay yang terbuka.
  - TC-FA-FAAL-114 Expected tidak menyebut apakah dialog `Unsaved Changes` tampil saat popup ditutup dengan perubahan belum disimpan; spec mengasersi hanya popup tertutup dan Note tetap tampil.
