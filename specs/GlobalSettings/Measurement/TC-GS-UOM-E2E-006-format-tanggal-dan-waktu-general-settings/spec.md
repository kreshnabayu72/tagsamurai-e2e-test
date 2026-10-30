---
id: TC-GS-UOM-E2E-006-format-tanggal-dan-waktu-general-settings
title: "Format Tanggal dan Waktu General Settings pada Tabel, Filter Date, dan Changelog"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-7
  - TC-GS-UOM-234
  - TC-GS-UOM-328
  - TC-GS-UOM-327
  - TC-GS-UOM-329
coverage:
  web: automated
---

# Format Tanggal dan Waktu General Settings pada Tabel, Filter Date, dan Changelog

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`; password dari `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Nama env didaftarkan di `executionConfig.environmentVariables`.
- Data Pre-setup dan Population (hanya dibaca): Pre-setup Client A (termasuk Meter di halaman 1 dan Pieces di halaman 2) dan Population D-01, di-seed idempotent oleh hook `before` sesuai "Data bersama" di `suite.md`. Modal Changelog Client A memiliki entri.
- Data Dinamis milik spec: unit `Drum {runId}-006` / simbol `drm` (D-27, nama bersuffix menggantikan `Drum` di TC sumber) dibuat lewat UI di langkah 25 sampai 27 (TC-GS-UOM-329) dan dihapus lewat API di hook `after` (pembersihan tidak berasumsi pembuatan berhasil).
- State global yang diubah: Date Format, Time Format, dan Time Zone General Settings. Nilai awal ketiganya dibaca lewat API di hook `before` dan dipulihkan lewat API di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`), sehingga tidak ada spec lain yang membaca format selama spec ini berjalan.
- Kemampuan teknis: membaca dan mengubah General Settings (Date Format, Time Format, Time Zone) lewat jalur API yang disediakan tim FE (tanpa endpoint karangan, S-13); memilih rentang tanggal di date picker; jam server dan jam browser sinkron serta membaca waktu saat ini menurut Time Zone entitas (TC-GS-UOM-329, toleransi satu menit karena kolom Date dan Last Updated berketelitian menit, S-12).
- Guided Tooltip: flag halaman Measurement mengikuti pernyataan hook suite di `suite.md`.
- Layar awal (Global Settings > Master Reference > Measurement) dibuka hook `beforeEach` suite; format hasil perubahan General Settings dimuat lewat muat ulang halaman.

## Test Steps

### Pengaturan format awal

1. Atur General Settings: Date Format `dd MMM yy` dan Time Format `HH:mm`
2. Muat ulang halaman Global Settings > Master Reference > Measurement

### TC-GS-UOM-7: Format Last Updated mengikuti General Settings

3. Perhatikan sel Last Updated baris Meter
4. Verifikasi Last Updated Meter tampil dengan pola `dd MMM yy HH:mm` (tanggal 2 digit, nama bulan singkat, tahun 2 digit, diikuti jam 24 jam)
5. Verifikasi tidak ada sel Last Updated bernilai `—` pada baris yang tampil di halaman 1

### TC-GS-UOM-234: Date Format dan Time Format General Settings berlaku di tabel dan Modal Changelog

6. Atur General Settings: Date Format `M/d/yy` dan Time Format `hh:mm a`
7. Muat ulang halaman Global Settings > Master Reference > Measurement
8. Ketik Search `Pieces`, tekan Enter
9. Perhatikan sel Last Updated baris Pieces
10. Verifikasi Last Updated Pieces memakai tanggal tanpa angka nol di depan dengan tahun 2 digit dan jam 12 jam dengan penanda AM atau PM (pola `M/d/yy hh:mm a`)
11. Klik `(←)` pada kotak Search
12. Klik icon Changelog
13. Perhatikan kolom Date baris pertama
14. Verifikasi kolom Date baris pertama Modal Changelog memakai pola tanggal dan jam yang sama (`M/d/yy hh:mm a`)

### TC-GS-UOM-328: Isian input Date Picker Filter Panel Modal Changelog mengikuti Date Format

15. Klik Filter pada Modal Changelog
16. Pilih rentang Date 01 Jun 2026 – 15 Jun 2026 pada date picker
17. Verifikasi kotak input Date menampilkan tanggal awal `6/1/26` dan tanggal akhir `6/15/26` (pola `M/d/yy`)
18. Tutup Modal Changelog lewat `✕` di header

### TC-GS-UOM-327: Isian input Date Picker Filter Panel tabel utama mengikuti Date Format

19. Klik Filter
20. Pilih rentang Last Updated 01 Jun 2026 – 15 Jun 2026 pada date picker
21. Perhatikan teks di kotak input Last Updated
22. Verifikasi kotak input Last Updated menampilkan tanggal awal `6/1/26` dan tanggal akhir `6/15/26` (pola `M/d/yy`)

### TC-GS-UOM-329: Time Format 12 jam dan Time Zone entitas berlaku pada Last Updated dan kolom Date Changelog

23. Atur General Settings: Time Format `hh:mm a` dan Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`
24. Muat ulang halaman Global Settings > Master Reference > Measurement
25. Klik [+ Unit]
26. Isi Unit Name `Drum {runId}-006` dan Symbol `drm`
27. Klik [Submit]
28. Catat waktu saat ini menurut Time Zone entitas dalam format 12 jam (dicatat sesudah [Submit])
29. Ketik Search `Drum {runId}-006`, tekan Enter
30. Perhatikan sel Last Updated baris Drum
31. Verifikasi Last Updated baris Drum memakai jam 12 jam dengan penanda AM atau PM
32. Verifikasi Last Updated baris Drum menunjukkan waktu yang sama dengan waktu yang dicatat pada langkah 28 (selisih maksimal 1 menit) menurut Time Zone entitas
33. Klik icon Changelog
34. Ketik Search `Drum {runId}-006` pada Modal Changelog, tekan Enter
35. Perhatikan kolom Date baris Create Drum
36. Verifikasi kolom Date baris Create Drum memakai format jam 12 jam dan Time Zone yang sama
37. Tutup Modal Changelog lewat `✕` di header

### Pemulihan

38. Pulihkan Date Format, Time Format, dan Time Zone General Settings ke nilai awal yang dibaca di hook `before`

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Kelas harness: state global General Settings; seluruh lima TC berada di kelas yang sama, dan spec ini sendiri adalah spec kelas itu (tidak memakai pengecualian P-5).
- Urutan TC: TC-GS-UOM-7 lebih dulu (format `dd MMM yy` / `HH:mm`), lalu satu kali ganti ke `M/d/yy` / `hh:mm a` untuk TC-GS-UOM-234, TC-GS-UOM-328, dan TC-GS-UOM-327 yang memakai format tanggal yang sama, lalu TC-GS-UOM-329 (Time Zone, membuat satu unit) paling akhir. TC-GS-UOM-328 dijalankan sebelum TC-GS-UOM-327 supaya Modal Changelog yang sudah terbuka di TC-GS-UOM-234 dipakai ulang tanpa membuka ulang; urutan TC sumber (327 sebelum 328) diubah karena alasan itu.
- TC-GS-UOM-329 pada TC sumber meminta waktu dicatat sebelum aksi; spec mencatat waktu sesudah [Submit] (langkah 28) sesuai S-12 (waktu aksi dicatat sesudah aksi, toleransi satu menit).
- TC-GS-UOM-329 membuat satu unit sebagai pemicu Last Updated dan Date (nama bersuffix, dihapus di hook `after`); tidak ada TC lain di spec ini yang membuat data.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1, 6, dan 23 (mengatur General Settings), 2, 7, dan 24 (muat ulang agar format baru dimuat), 8 dan 11 (Search `Pieces` untuk menemukan baris di halaman 2 dan mengosongkannya), 18 dan 37 (menutup Modal Changelog), 29 dan 34 (Search untuk menemukan baris Drum dan entri Create Drum), serta 38 (memulihkan General Settings; hook `after` sebagai cadangan).
- Langkah 19 sampai 22 meninggalkan Filter Panel terbuka tanpa [Apply]; muat ulang di langkah 24 menutupnya.
- Spec ini mengubah state global (General Settings) sehingga tidak boleh paralel dengan spec lain; suite memang `parallel: false`.
- Spec ini di atas batas 35 langkah (38): seluruhnya satu kelas harness (state global General Settings) dengan satu akun; format diubah satu kali untuk tiga TC yang memakai format sama, dan Time Zone paling akhir; memecahnya hanya menambah pengubahan dan pemulihan General Settings.
- Temuan untuk QA:
  - TC-GS-UOM-7 dan TC-GS-UOM-234 menetapkan format di precondition, sedangkan default General Settings adalah `dd/MM/yy` + `HH:mm`; spec mengubah dan memulihkan General Settings. Akun atau jalur API pengubah General Settings tidak disebut TC dan disediakan tim FE.
  - TC-GS-UOM-234 Expected b tidak menyebut cara menemukan baris Changelog "pertama"; spec mengikuti TC (baris pertama pada urutan default).
  - TC-GS-UOM-329 langkah uji 4 menyebut "baris Create Drum" tanpa menyebut cara menemukannya di Changelog; spec memakai Search Changelog dengan nama unit bersuffix (asumsi Search Changelog mencocokkan nama unit).
