---
id: TC-GS-HHR-E2E-077-sinkron-hardware-stock-aktivasi-dan-current-power-reader-usb
title: "Sinkron Admin Console Hardware Stock: Efek Aktivasi Reader USB pada Unit dan Current Power Dibaca saat Aktivasi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-373
  - TC-GS-HHR-374
  - TC-GS-HHR-375
  - TC-GS-HHR-384
coverage:
  web: automated
---

# Sinkron Admin Console Hardware Stock: Efek Aktivasi Reader USB pada Unit dan Current Power Dibaca saat Aktivasi

## Prerequisites

- Mode: FE+BE. Kelas harness: harness eksternal (kelas d, simulator reader USB) bersama konteks kedua Principal di Admin Console (kelas c) sesuai pengecualian `P-7` (lihat Notes). Suite `parallel: false`.
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini (lihat `suite.md`, Hook suite).
- Akun:

| Sesi | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| A | Total Control (Client A) | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| P | Principal (Admin Console) | Bambang Hartono | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_PRINCIPAL_TC_PASSWORD` |

- Login Sesi A dilakukan di hook `before`; Sesi P dibuka dengan langkah ganti akun eksplisit (langkah 1) karena hasilnya diasersi di Hardware Stock. Hook `after` menutup Sesi P, memulihkan Current Power unit `SN-HHR-00201` ke 22 dBm, dan mengembalikan sesi ke akun default suite (Sesi A).
- Data Dinamis (Seed Reader A, dipulihkan fixture backend; Client A, plan Growth, DD-01 s.d. DD-10): stok Principal HS-01 `SN-HHR-00201` (Long Range, Current Power 22 dBm, `Available`), HS-04 `SN-HHR-00204` (aktif di Client C), serial Jalur B `SN-HHR-00302` (tidak ada di stok Principal). Katalog Device Name DN-01 s.d. DN-07 (dibaca Client read-only). Nama Seed Reader A bernilai literal tanpa suffix (pengecualian S-12 Population Seed Reader A HHR).
- Kemampuan teknis (disediakan tim FE/BE):
  - Konteks browser kedua untuk Sesi P.
  - Pemulihan Seed Reader A dan stok Hardware Stock ke keadaan Tabel Data Uji TC antar blok (fixture BE; Catatan TC: tabel dipulihkan antar TC).
  - Simulator reader USB/driver lokal untuk Sync `SN-HHR-00201`, `SN-HHR-00204`, dan `SN-HHR-00302` (mekanisme simulasi tidak didefinisikan di TC, PRD, atau LLD; lihat Temuan untuk QA).
  - Perubahan Current Power unit `SN-HHR-00201` dari 22 dBm menjadi 18 dBm di Hardware Stock oleh Principal (blok TC-GS-HHR-384; hasilnya dipakai sebagai precondition dan tidak diasersi).
- Baseline: `Status` unit dan total unit Hardware Stock dicatat sebelum aksi tiap blok.
- State global yang diubah: Seed Reader A, status unit di Hardware Stock, Current Power unit `SN-HHR-00201`. Pemulihan: langkah pemulihan eksplisit tiap blok dan hook `after` sebagai cadangan.

## Test Steps

### Persiapan sesi

1. Ganti akun: buka konteks browser kedua (Sesi P) dan login sebagai Principal Bambang Hartono

### Blok 1 - Aktivasi Jalur A tanpa collision: TC-GS-HHR-373

2. Pulihkan Seed Reader A dan stok Hardware Stock
3. Sesi P: buka Admin Console > Hardware Stock, buka Tab Available, ketik Search `SN-HHR-00201`, tekan Enter, catat `Status` unit sebagai Status awal (`Available`)
4. Sesi A: muat ulang Handheld Reader, klik `[+ Activate Reader]`
5. Sesi A: klik `Long Range` pada Overlay `Select Range Type`
6. Sesi A: klik `[Sync]` (reader USB HS-01 `SN-HHR-00201` tersambung)
7. Sesi A: klik `[Submit]`
8. Tunggu aksi selesai
9. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00201`, tekan Enter
10. Verifikasi `Status` unit `SN-HHR-00201` berubah dari `Available` menjadi `In Use`
11. Klik Tab In Use, ketik Search `SN-HHR-00201`, tekan Enter
12. Verifikasi unit `SN-HHR-00201` tampil di Tab In Use
13. Verifikasi pemakai unit `SN-HHR-00201` adalah Client A
14. Klik Tab Available, ketik Search `SN-HHR-00201`, tekan Enter
15. Verifikasi unit `SN-HHR-00201` tidak ada di Tab Available (empty state `No results found`)

### Blok 2 - Aktivasi yang berakhir Waiting for Approval: TC-GS-HHR-374

16. Pulihkan Seed Reader A dan stok Hardware Stock
17. Sesi P: ketik Search `SN-HHR-00204`, tekan Enter, catat `Status` unit sebagai Status awal
18. Sesi A: muat ulang Handheld Reader, klik `[+ Activate Reader]`, klik `Long Range`, klik `[Sync]` (reader USB HS-04 `SN-HHR-00204` tersambung, aktif di Client C), klik `[Submit]` sehingga reader menjadi Waiting for Approval
19. Tunggu aksi selesai
20. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00204`, tekan Enter
21. Verifikasi `Status` unit `SN-HHR-00204` sama dengan Status awal

### Blok 3 - Aktivasi Jalur B: TC-GS-HHR-375

22. Pulihkan Seed Reader A dan stok Hardware Stock
23. Sesi P: buka Hardware Stock, catat total unit
24. Sesi A: muat ulang Handheld Reader, klik `[+ Activate Reader]`, klik `Long Range`, klik `[Sync]` (reader USB `SN-HHR-00302` tersambung)
25. Sesi A: pilih `Chainway C72` pada `Device Name`, isi `Brand` `Chainway`, isi `Model/Type` `C72`, klik `[Submit]`
26. Tunggu aksi selesai
27. Sesi P: muat ulang Hardware Stock, ketik Search `SN-HHR-00302`, tekan Enter
28. Verifikasi `SN-HHR-00302` tidak ditemukan di Hardware Stock (empty state `No results found`)
29. Verifikasi total unit Hardware Stock sama dengan total unit yang dicatat

### Blok 4 - Current Power di Hardware Stock dibaca saat aktivasi: TC-GS-HHR-384

30. Pulihkan Seed Reader A dan stok Hardware Stock
31. Sesi P: ubah Current Power unit `SN-HHR-00201` dari 22 dBm menjadi 18 dBm di Hardware Stock hingga tersimpan
32. Tunggu aksi selesai
33. Sesi A: muat ulang Handheld Reader, klik `[+ Activate Reader]`, pilih `Long Range` pada Overlay `Select Range Type`
34. Sesi A: klik `[Sync]` (reader USB HS-01 `SN-HHR-00201` tersambung)
35. Verifikasi slider `Reader Power` terisi nilai awal `18 dBm`
36. Sesi A: klik `✕` pada popup Activate Reader
37. Verifikasi dialog `Cancel Activation` tampil dengan body `Are you sure you want to cancel this activation? The Sync progress you've made will be lost.` dan tombol `[Go Back]` `[Cancel Activation]`
38. Sesi A: klik `[Cancel Activation]`
39. Sesi P: pulihkan Current Power unit `SN-HHR-00201` menjadi 22 dBm di Hardware Stock hingga tersimpan

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 7a). Keempat TC memakai reader USB lewat driver lokal; kebutuhannya ditulis di Prerequisites.
- `P-7` (simulator USB bersama konteks lain, pengecualian atas pemisahan kelas d). Alasan per TC:
  - TC-GS-HHR-373: membutuhkan simulator USB untuk Sync HS-01 (`SN-HHR-00201`) dan sesi Principal sebagai konteks lain yang mengasersi `Status` unit dan Tab In Use di Hardware Stock.
  - TC-GS-HHR-374: membutuhkan simulator USB untuk Sync HS-04 (`SN-HHR-00204`) dan sesi Principal yang mengasersi `Status` unit tidak berubah.
  - TC-GS-HHR-375: membutuhkan simulator USB untuk Sync `SN-HHR-00302` (Jalur B) dan sesi Principal yang mengasersi `SN-HHR-00302` tidak ada dan total unit tidak berubah.
  - TC-GS-HHR-384: membutuhkan simulator USB untuk Sync HS-01; sesi Principal hanya mengubah Current Power unit sebagai precondition (tanpa asersi di Sesi P). Blok ini memakai sesi Principal yang sama dengan blok lain sehingga tidak dipisah.
- Urutan blok: tiga blok yang mengasersi Hardware Stock lebih dahulu, blok TC-GS-HHR-384 yang mengubah Current Power terakhir. Seed Reader A dan stok dipulihkan di awal tiap blok (langkah 2, 16, 22, 30), sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Spec memuat 39 langkah, sedikit di atas sekitar 35 langkah. Alasan: semua blok satu kelas (aktivasi atau Sync reader USB dengan Sesi P membaca Hardware Stock) dan berdiri sendiri; tidak ada blok yang dapat dipindahkan tanpa memisahkan simulator USB dan sesi Principal yang sama.
- Langkah penghubung tanpa `Verifikasi` (S-03): pemulihan Seed Reader A dan stok, muat ulang, mencatat nilai awal, berpindah sesi, Tab In Use/Available, mencari unit lewat Search, mengubah Current Power (langkah 31, 39). Langkah "Tunggu aksi selesai" dipakai karena langkah berikut berpindah sesi (bagian 8b butir 8). Langkah 36 sampai 38 menutup Popup Activate yang sudah Sync (S-08).
- Pembagian TC lintas spec: Mark as, Bulk, Delete, Bulk Delete, dan Cancel Request yang diasersi di Hardware Stock (TC-GS-HHR-217, 376 sampai 383) ada di spec 068.
- Pengecualian S-12 Population Seed Reader A HHR berlaku untuk Seed Reader A (nama literal tanpa suffix `{runId}`); pemulihannya dijamin fixture backend dan dinyatakan di `suite.md`.
- Temuan untuk QA:
  - Mekanisme simulasi reader USB (Sync `SN-HHR-00201`, `SN-HHR-00204`, `SN-HHR-00302`) tidak didefinisikan di TC, PRD, atau LLD; tidak ada endpoint yang dikarang.
  - TC-GS-HHR-375 tidak menyebut nama kolom untuk "total unit"; spec memakai total unit yang tampil di Hardware Stock.
  - TC-GS-HHR-373 tidak mencatat `Status` awal unit dalam langkahnya; spec mencatatnya sebelum aktivasi sebagai baseline untuk Expected "berubah dari `Available` menjadi `In Use`" (S-12).
  - TC-GS-HHR-384 precondition e menyebut Principal mengubah Current Power di Hardware Stock tanpa langkah UI; spec menaruhnya sebagai langkah Sesi P tanpa `Verifikasi`.
  - TC-GS-HHR-384 Langkah 1 ("Pilih `Long Range`, klik `[Sync]`") tidak menyebut membuka popup lewat `[+ Activate Reader]`; spec menambahkannya sebagai langkah penghubung (langkah 33).
  - TC-GS-HHR-384 tidak menyebut cara menutup popup sesudah Amati slider; spec menutupnya dengan `✕` dan dialog `Cancel Activation` sesuai teks TC-GS-HHR-89 (S-08).
