---
id: TC-AC-DS-E2E-035-register-duplikat-kode-sku-dan-daftar-ulang
title: "Register SKU: Kode Duplikat Principal, Helper Text Kembali, Case-insensitive, dan Daftar Ulang Kode Terhapus"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DS-116
  - TC-AC-DS-117
  - TC-AC-DS-118
  - TC-AC-DS-122
coverage:
  web: automated
---

# Register SKU: Kode Duplikat Principal, Helper Text Kembali, Case-insensitive, dan Daftar Ulang Kode Terhapus

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): SKU inti #29 `HHR-ARC-100` dan `HHR-ARC-200` (kode yang sudah ada, hanya dibaca); pohon Category #25 (`TAG > NFC > Asset TAG`); Device Name #26 (`Asset TAG`); Brand Principal #27 (`Arcturus`); file foto uji #37 (`foto-a.jpg`, 200 KB). Kode `HHR-ARC-101` tidak ada di Pre-setup dan tidak pernah disimpan.
- Data Dinamis: SKU `DEL-OBJ-{runId}-035` (Category `Asset TAG`, Device Name `Asset TAG`, Brand `Arcturus`, Model/Type `T-OBJ`, stok 0, satu foto) di-seed lewat API di hook `before` sebagai SKU milik spec yang dihapus oleh TC-AC-DS-122 lalu didaftarkan ulang dengan Model/Type `T-OBJ2`. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-035`.
- Kemampuan teknis (disediakan tim FE/BE): seeding SKU lewat API di hook `before` (tidak menyebut endpoint karena tidak tercantum di TC). Jeda nyata 1 detik pada langkah 4, 9, 11, 17, dan 31 memenuhi debounce pemeriksaan keunikan SKU (sekitar 500 ms) dan disebut eksplisit.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

1. Klik tombol `[+ SKU]` pada toolbar

### TC-AC-DS-116: SKU yang sudah ada pada Principal ditolak setelah debounce sekitar 500 ms tanpa menunggu blur

2. Klik field SKU lalu ketik `HHR-ARC-100`
3. Verifikasi area bawah field SKU menampilkan "Checking availability..." menggantikan helper text
4. Tunggu 1 detik tanpa memindahkan fokus dari field SKU
5. Verifikasi pesan error "SKU already exists" tampil tanpa menunggu blur
6. Verifikasi helper text tidak tampil selama pesan error aktif

### TC-AC-DS-117: Helper text kembali setelah pesan duplikat diperbaiki

7. Kosongkan isi field SKU
8. Ketik `HHR-ARC-100` pada field SKU
9. Tunggu 1 detik sampai pesan "SKU already exists" tampil
10. Ubah teks menjadi `HHR-ARC-101`
11. Tunggu 1 detik
12. Verifikasi area bawah field SKU menampilkan kembali helper text "Letters, numbers, hyphens, and dots only (e.g. SKU-RFID-V2)"
13. Verifikasi pesan "SKU already exists" hilang setelah kode diubah

### TC-AC-DS-118: Kode SKU yang diketik huruf kecil tetap terdeteksi duplikat karena dibandingkan tanpa membedakan huruf besar-kecil

14. Kosongkan isi field SKU
15. Ketik `hhr-arc-200` pada field SKU
16. Verifikasi teks pada field SKU tampil `HHR-ARC-200`
17. Tunggu 1 detik
18. Verifikasi pesan error "SKU already exists" tampil karena kode yang sama sudah ada pada SKU Principal

### TC-AC-DS-122: Kode SKU yang sudah dihapus dapat didaftarkan lagi sebagai SKU baru

19. Klik ikon close `[✕]`
20. Verifikasi dialog "You have unsaved changes. Are you sure you want to leave?" dengan tombol `[Cancel]` dan `[Leave]` tampil
21. Klik `[Leave]`
22. Ketik Search `DEL-OBJ-{runId}-035`, tekan Enter
23. Klik ⋯ pada baris `DEL-OBJ-{runId}-035` lalu pilih `Delete`
24. Klik `[Delete]` pada dialog konfirmasi
25. Klik tombol `[+ SKU]` pada toolbar
26. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
27. Klik field Device Name lalu pilih `Asset TAG`
28. Klik field Brand lalu pilih `Arcturus`
29. Ketik `T-OBJ2` pada field Model/Type
30. Ketik `DEL-OBJ-{runId}-035` pada field SKU
31. Tunggu 1 detik
32. Verifikasi field SKU berisi `DEL-OBJ-{runId}-035`
33. Verifikasi tidak ada pesan duplikat pada field SKU setelah SKU lama terhapus
34. Unggah `foto-a.jpg` pada field Photo
35. Klik `[Submit]`
36. Verifikasi toast sukses "Success, device SKU has been registered." tampil
37. Verifikasi baris `DEL-OBJ-{runId}-035` tampil sebagai SKU baru dengan badge Model/Type `T-OBJ2`
38. Verifikasi Current Stock baris `DEL-OBJ-{runId}-035` bernilai `0`
39. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 7 dan 14 mengosongkan field SKU agar TC berikutnya mengetik pada field kosong (S-09); langkah 9 menunggu pesan duplikat sebagai precondition langkah 3 TC-AC-DS-117; langkah 19 sampai 21 menutup form dirty secara deterministik (S-08) sebelum TC-AC-DS-122; langkah 22 dan 39 (Search untuk menemukan baris target lalu menutup Search, R-16).
- Urutan state sementara (bagian 8b butir 5): pada TC-AC-DS-116 teks "Checking availability..." diasersi segera sesudah mengetik dan sebelum jeda 1 detik; TC menaruh jeda 1 detik sebelum seluruh Expected.
- Verifikasi langkah 32 (field SKU berisi `DEL-OBJ-{runId}-035`) ditambahkan sebagai anchor positif bagi asersi absence pesan duplikat (bagian 8b butir 2, S-03); asersi tersebut tidak ada di Expected TC.
- Ukuran spec (sedikit di atas sekitar 35 langkah): semua blok adalah kelas fungsional yang sama (validasi keunikan kode SKU pada popup Register) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan aksi yang menghapus data ada di akhir spec (S-10).
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-035` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - TC-AC-DS-122 menghapus SKU Pre-setup `TAG-ARC-OBJ` lalu mendaftarkannya ulang; spec memakai SKU milik spec `DEL-OBJ-{runId}-035` agar SKU Pre-setup bersama (total 129 SKU) tidak berubah (S-06). Asersi Model/Type `T-OBJ2` dan Current Stock `0` tetap sama; kode literal pada Expected TC tidak dipakai.
  - TC-AC-DS-116 tidak menyebut cara membuktikan "sekitar 500 ms" selain jeda 1 detik; asersi hanya pada keadaan sebelum dan sesudah jeda.
