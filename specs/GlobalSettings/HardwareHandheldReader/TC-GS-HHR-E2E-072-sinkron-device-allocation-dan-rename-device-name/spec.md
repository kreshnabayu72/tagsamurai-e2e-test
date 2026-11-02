---
id: TC-GS-HHR-E2E-072-sinkron-device-allocation-dan-rename-device-name
title: "Sinkron Admin Console: Alokasi Device Allocation pada Kartu Kuota dan Rename Device Name pada Nama Dasar Reader Jalur B"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-HHR-397
  - TC-GS-HHR-398
  - TC-GS-HHR-488
coverage:
  web: automated
---

# Sinkron Admin Console: Alokasi Device Allocation pada Kartu Kuota dan Rename Device Name pada Nama Dasar Reader Jalur B

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (kelas c, perubahan di Admin Console oleh Principal lalu dibaca di Client A). Suite `parallel: false` karena spec mengubah state global (alokasi Client A dan nama Device Name).
- Flag Guided Tooltip halaman Handheld Reader: diatur hook suite untuk akun aktor spec ini (lihat `suite.md`, Hook suite).
- Akun:

| Sesi | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| A | Total Control (Client A) | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| P | Principal (Admin Console) | Bambang Hartono | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_PRINCIPAL_TC_PASSWORD` |

- Login Sesi A dilakukan di hook `before`; hook `beforeEach` membuka Global Settings > Hardware > Handheld Reader. Sesi P dibuka dengan langkah ganti akun eksplisit (langkah 20) untuk blok TC-GS-HHR-488, karena TC memberi langkah UI Principal. Hook `after` menutup Sesi P dan mengembalikan sesi ke akun default suite (Sesi A).
- Data (Client A, plan Growth, Seed Reader A dari fixture BE, alokasi awal `Short Range` 8 dan `Long Range` 6; terpakai `Short Range` 5 dan `Long Range` 5): DD-07 (`Honeywell CK65 - 1`, Jalur B, menyimpan ID Device Name DN-02 `Honeywell CK65`, `SKU` `—`); lima reader Short Range: DD-02 (`Gudang Reader - 1`), DD-04 (`Gudang Reader - 2`), DD-06 (`Zebra RFID Reader - 1`), DD-08 (`Unitech EA520 - 1`), DD-10 (`Gudang Reader - 4`). Seed Changelog Client A memuat entri Activate 22/06/26 10:00 untuk DD-07.
- Kemampuan teknis (disediakan tim FE/BE):
  - Sesi API Principal untuk mengubah alokasi Client A di Admin Console > Device Allocation (menambah `Long Range` dari 6 menjadi 8 dan mengurangi `Short Range` dari 8 menjadi 4). Pelaku hanya memicu perubahan state; endpoint tidak didefinisikan di TC, PRD, atau LLD dan tidak ditulis di spec ini.
  - Konteks browser kedua untuk Sesi P (blok TC-GS-HHR-488).
  - Pemulihan alokasi Client A (`Short Range` 8, `Long Range` 6) dan nama Device Name `Honeywell CK65` (Post Condition TC-GS-HHR-488: dipulihkan automation baseline).
- Baseline: nilai kartu `Short Range` (`5 of 8`, `3 remaining`) dicatat dari keadaan awal sebelum perubahan alokasi.
- State global yang diubah: alokasi Device Allocation Client A dan Device Name `Honeywell CK65`. Pemulihan: langkah pemulihan eksplisit dan hook `after` sebagai cadangan.

## Test Steps

### Alokasi bertambah: TC-GS-HHR-397

1. Catat nilai kartu `Short Range` (`5 of 8`, `3 remaining`) sebagai nilai awal
2. Tambah alokasi `Long Range` Client A dari 6 menjadi 8 lewat sesi API Principal hingga tersimpan
3. Tunggu aksi selesai
4. Muat ulang Global Settings > Hardware > Handheld Reader
5. Amati License Counter Cards
6. Verifikasi kartu `Long Range` menampilkan `5 of 8` dan `3 remaining`
7. Verifikasi kartu `Short Range` tidak berubah dari nilai awal

### Alokasi dikurangi di bawah jumlah terpakai: TC-GS-HHR-398

8. Pulihkan alokasi `Long Range` Client A menjadi 6 lewat sesi API Principal hingga tersimpan
9. Kurangi alokasi `Short Range` Client A dari 8 menjadi 4 (terpakai 5) lewat sesi API Principal hingga tersimpan
10. Tunggu aksi selesai
11. Muat ulang Handheld Reader
12. Verifikasi kelima reader Short Range tetap tampil: `Gudang Reader - 1`, `Gudang Reader - 2`, `Zebra RFID Reader - 1`, `Unitech EA520 - 1`, dan `Gudang Reader - 4`
13. Klik `[+ Activate Reader]`
14. Klik `Short Range` pada Overlay `Select Range Type`
15. Verifikasi dialog `Insufficient License Quota` dengan body `License quota reached for selected range type.` dan tombol `[OK]`
16. Klik `[OK]`
17. Verifikasi kartu `Short Range` menampilkan `5 of 4`
18. Verifikasi kartu `Short Range` menampilkan `0 remaining`
19. Pulihkan alokasi `Short Range` Client A menjadi 8 lewat sesi API Principal hingga tersimpan

### Rename Device Name: TC-GS-HHR-488

20. Ganti akun: buka konteks browser kedua (Sesi P) dan login sebagai Principal Bambang Hartono
21. Sesi P: buka `Settings > Device > Device Name`, ketik Search `Honeywell CK65`, tekan Enter
22. Sesi P: buka Overlay row action baris `Honeywell CK65`, klik `Edit`
23. Sesi P: ubah Device Name menjadi `Honeywell CK65 Plus`, klik `[Save]`
24. Tunggu aksi selesai
25. Sesi A: muat ulang Global Settings > Hardware > Handheld Reader
26. Verifikasi baris DD-07 menampilkan `Device Name` `Honeywell CK65 Plus - 1` (`N` tetap 1)
27. Verifikasi baris DD-07 menampilkan `SKU` `—`
28. Sesi A: klik ikon Changelog
29. Verifikasi Modal Changelog baris `22/06/26 10:00` tetap menampilkan `Honeywell CK65 - 1` (snapshot saat entri dicatat)
30. Sesi A: tutup Modal Changelog
31. Sesi P: ubah kembali Device Name `Honeywell CK65 Plus` menjadi `Honeywell CK65` di `Settings > Device > Device Name`, klik `[Save]`

## Notes

- Sumber: `global-settings/hardware-handheld-reader/TestCases/tc-hardware-handheld-reader.md` (Section 7d dan 7f). Semua TC berlabel Automatable.
- Urutan: penambahan alokasi (TC-GS-HHR-397) sebelum pengurangan (TC-GS-HHR-398), rename Device Name paling akhir (prinsip 3 butir 4). Langkah 8 memulihkan alokasi `Long Range` sebelum TC-GS-HHR-398 supaya tiap TC dimulai dari alokasi Tabel Pre-setup (Catatan TC: tabel dipulihkan antar TC).
- Langkah penghubung tanpa `Verifikasi` (S-03): mencatat nilai awal, mengubah dan memulihkan alokasi lewat sesi API, muat ulang, membuka dan menutup Overlay `Select Range Type`, dialog, dan Modal Changelog, mencari Device Name, memulihkan nama. Langkah "Tunggu aksi selesai" dipakai karena langkah berikut berpindah surface atau sesi.
- TC-GS-HHR-398 memakai Client A sesuai TC; Client lain tidak dipakai.
- Temuan untuk QA:
  - TC-GS-HHR-397 dan TC-GS-HHR-398 menyatakan perubahan alokasi di Admin Console > Device Allocation sebagai precondition oleh Principal tanpa langkah UI; spec memakai sesi API yang disediakan tim FE tanpa mengarang endpoint.
  - TC-GS-HHR-398 butir a ("Kelima reader Short Range tetap tampil") tidak menyebut nama kelima reader; spec memakai nama dari Seed Reader A (DD-02, DD-04, DD-06, DD-08, DD-10).
  - TC-GS-HHR-398 butir b tidak menyebut tombol dialog; spec memakai `[OK]` sesuai langkah TC.
  - TC-GS-HHR-488 precondition a menyebut "akun fixture modul Device Name" untuk Principal; spec memakai akun Principal Pre-setup TC (`totalControlPrincipal_automated_qaTeam1@qwertysystem.net`).
  - TC-GS-HHR-488 Post Condition ("Device Name dipulihkan automation baseline") tidak punya langkah observasi dan tidak diasersi; spec memulihkan nama pada langkah 31 dan di hook `after`.
