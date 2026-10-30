---
id: TC-GS-USER-E2E-150-sinkron-position-dan-division-ke-form-dan-list-user
title: "Sinkron Position dan Division (Create, Edit, Delete) ke Form dan List User"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-944
  - TC-GS-USER-945
  - TC-GS-USER-946
  - TC-GS-USER-947
  - TC-GS-USER-948
  - TC-GS-USER-949
coverage:
  web: automated
---

# Sinkron Position dan Division (Create, Edit, Delete) ke Form dan List User

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2), kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User). Tab Position, Division, dan User List berada di modul User yang sama sehingga seluruh spec memakai satu akun tanpa ganti akun. Akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`.
- Data Pre-setup (Tabel Data Uji Pre-setup No. 22 dan 23) dibaca saja dan tidak diubah: Position `Staff` dan Division `Logistics` tidak menjadi target Edit; spec memakai Position dan Division milik sendiri (S-06).
- Data Dinamis (suffix per run dan nomor spec), di-seed lewat API di hook `before` oleh akun Total Control (kemampuan seeding Position, Division, dan Login User lewat API; nilai field wajib lain user mengikuti fixture `fixtures/user.json` yang belum ada, disediakan tim FE):
  - Position `Staff {runId}-150` (setara `Staff` pada TC-GS-USER-945), di-rename lewat UI menjadi `Senior Staff {runId}-150`.
  - Division `Logistics {runId}-150` (setara `Logistics` pada TC-GS-USER-948), di-rename lewat UI menjadi `Supply Chain {runId}-150`.
  - Login User `Gilang Prakoso {runId}-150`, email `gilangprakoso+{runId}-150@qwertysystem.net`, Position `Staff {runId}-150`, Division `Logistics {runId}-150`, Access `Fixed Asset`: user yang memakai Position dan Division di atas.
- Data Dinamis yang dibuat spec lewat UI: Position `Procurement Officer {runId}-150` (TC-GS-USER-944, dihapus pada TC-GS-USER-946) dan Division `Procurement {runId}-150` (TC-GS-USER-947, dihapus pada TC-GS-USER-949); tidak ada user yang memakainya. Code Division di-generate otomatis.
- Cleanup (hook `after`, tidak berasumsi seeding atau langkah berhasil penuh): hapus lewat API Login User `gilangprakoso+{runId}-150@qwertysystem.net`, lalu Position `Staff {runId}-150`, `Senior Staff {runId}-150`, `Procurement Officer {runId}-150`, dan Division `Logistics {runId}-150`, `Supply Chain {runId}-150`, `Procurement {runId}-150` bila masih ada.
- Tidak ada state global yang diubah.

## Test Steps

### Aksi pada master data (TC-GS-USER-944, 945, 947, 948)

1. Buka Global Settings > User > Tab Position
2. Klik `[+ Position]`, isi Position Name `Procurement Officer {runId}-150`, klik `[Submit]`
3. Tunggu aksi selesai
4. Klik icon Search, ketik `Staff {runId}-150`, tekan Enter pada tabel Position
5. Klik `⋯` pada baris `Staff {runId}-150` > Edit, ubah Position Name menjadi `Senior Staff {runId}-150`, klik `[Save]`
6. Tunggu aksi selesai
7. Buka Tab Division
8. Klik `[+ Division]`, isi Division Name `Procurement {runId}-150`, klik `[Submit]`
9. Tunggu aksi selesai
10. Klik icon Search, ketik `Logistics {runId}-150`, tekan Enter pada tabel Division
11. Klik `⋯` pada baris `Logistics {runId}-150` > Edit, ubah Division Name menjadi `Supply Chain {runId}-150`, klik `[Save]`
12. Tunggu aksi selesai

### Refleksi di List dan form Create User (TC-GS-USER-945, 948, 944, 947)

13. Buka Tab User List, klik icon Search, ketik `Gilang Prakoso {runId}-150`, tekan Enter
14. Verifikasi kolom Position baris `Gilang Prakoso {runId}-150` menampilkan `Senior Staff {runId}-150`
15. Verifikasi kolom Division baris `Gilang Prakoso {runId}-150` menampilkan `Supply Chain {runId}-150`
16. Klik `[+ User]`
17. Buka dropdown Position, gulir daftar opsi hingga opsi `Procurement Officer {runId}-150` terlihat
18. Verifikasi opsi `Procurement Officer {runId}-150` tampil pada dropdown Position
19. Gulir daftar opsi hingga opsi `Senior Staff {runId}-150` terlihat
20. Verifikasi opsi `Senior Staff {runId}-150` tampil pada dropdown Position
21. Buka dropdown Division, gulir daftar opsi hingga opsi `Procurement {runId}-150` terlihat
22. Verifikasi opsi `Procurement {runId}-150` tampil pada dropdown Division
23. Klik `✕` di header form Create User
24. Kosongkan Search

### Hapus master data (TC-GS-USER-946, 949)

25. Buka Tab Position, klik icon Search, ketik `Procurement Officer {runId}-150`, tekan Enter
26. Klik `⋯` pada baris `Procurement Officer {runId}-150` > Delete, klik `[Delete]` pada dialog `Delete Position`
27. Tunggu aksi selesai
28. Buka Tab Division, klik icon Search, ketik `Procurement {runId}-150`, tekan Enter
29. Klik `⋯` pada baris `Procurement {runId}-150` > Delete, klik `[Delete]` pada dialog `Delete Division`
30. Tunggu aksi selesai

### Refleksi setelah hapus (TC-GS-USER-946, 949)

31. Buka Tab User List, klik `[+ User]`
32. Buka dropdown Position, gulir daftar opsi hingga opsi `Senior Staff {runId}-150` terlihat
33. Verifikasi opsi `Senior Staff {runId}-150` tampil pada dropdown Position form Create
34. Verifikasi opsi `Procurement Officer {runId}-150` tidak ada pada daftar opsi dropdown Position form Create
35. Buka dropdown Division, gulir daftar opsi hingga opsi `Supply Chain {runId}-150` terlihat
36. Verifikasi opsi `Supply Chain {runId}-150` tampil pada dropdown Division
37. Verifikasi opsi `Procurement {runId}-150` tidak ada pada daftar opsi dropdown Division
38. Klik `✕` di header form Create User
39. Klik icon Search, ketik `Gilang Prakoso {runId}-150`, tekan Enter
40. Klik `⋯` pada baris `Gilang Prakoso {runId}-150` > Edit
41. Buka dropdown Position, gulir daftar opsi hingga opsi `Senior Staff {runId}-150` terlihat
42. Verifikasi opsi `Senior Staff {runId}-150` tampil pada dropdown Position form Edit
43. Verifikasi opsi `Procurement Officer {runId}-150` tidak ada pada daftar opsi dropdown Position form Edit
44. Klik `✕` di header form Edit User
45. Kosongkan Search

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Sinkron master data Position dan Division ke modul User; tidak ada TC kelas harness.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: seluruh aksi Create dan Rename (TC-GS-USER-944, 945, 947, 948) dijalankan lebih dulu pada Tab Position dan Division, lalu satu pembukaan form Create User dan satu pengamatan List memeriksa keempat refleksinya sekaligus; aksi Delete (TC-GS-USER-946, 949) paling akhir (bagian 3 prinsip 5), karena Position dan Division yang dihapus adalah hasil Create TC-GS-USER-944 dan 947 yang harus sudah teramati lebih dulu.
- Spec melewati sekitar 35 langkah (45 langkah). Alasan: enam TC memakai dataset yang sama (Gilang Prakoso dengan Position dan Division milik spec) dan satu tema (sinkron master data ke List dan form User); pembukaan form digabung (dua kali Create User, satu kali Edit User) dan sisa langkah adalah aksi pada master data, Search, serta Verifikasi per klausa (S-01) yang tidak dapat digabung.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 7, 13, 25, 28, 31 (membuka tab); langkah 3, 6, 9, 12, 27, 30 (menunggu aksi selesai); langkah 4, 10, 25, 28, 39 (Search target); langkah 17, 19, 21, 32, 35, 41 (membuka dropdown dan menggulir daftar opsi, karena TC tidak menyebut cara mencari opsi); langkah 23, 38, 44 (menutup form tanpa isian: dropdown dibuka tanpa memilih opsi sehingga form tidak dirty dan tidak memunculkan dialog `Unsaved Changes`); langkah 24 dan 45 (mengosongkan Search).
- Asersi absence (langkah 34, 37, 43) didahului `Verifikasi` opsi pembanding pada dropdown yang sama (langkah 33, 36, 42; bagian 8b butir 2).
- Rename pada TC-GS-USER-945 dan 948 memakai Position dan Division seed milik spec (S-06); nama `Staff` dan `Logistics` pada TC ditulis `Staff {runId}-150` dan `Logistics {runId}-150`.
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-USER-944 sampai 949: langkah "Buka `[+ User]` atau amati tabel" memuat kata "atau"; spec mengamati keduanya sesuai Expected (dropdown Create dan sel List).
  - TC-GS-USER-945 dan 948: TC tidak menyebut user mana yang memakai `Staff` dan `Logistics`; spec memakai Login User hasil seeding.
  - TC-GS-USER-946: Expected menyebut "Popup Create/Edit", sedangkan Langkah Uji hanya menyebut `[+ User]`; spec membuka Popup Edit juga (langkah 40 sampai 44).
  - TC-GS-USER-944 sampai 949: TC tidak menyebut cara mencari opsi di dropdown; PRD User mendefinisikan field Position dan Division form Create hanya sebagai pilihan sehingga spec menggulir daftar opsi.
  - TC-GS-USER-944 dan 947: TC tidak menyebut Code Division maupun field lain Position; spec mengisi Name saja dan Code Division di-generate otomatis.
  - TC sumber tidak menyebut apakah Search dipertahankan saat berpindah tab; spec membuka Search ulang tiap kunjungan tab.
