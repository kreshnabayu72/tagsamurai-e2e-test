---
id: TC-AC-DS-E2E-138-usage-setup-column-geser-urutan-dan-pin
title: "Setup Column Usage: Geser Urutan Kolom serta Pin dan Unpin"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-457
  - TC-AC-DS-458
coverage:
  web: automated
---

# Setup Column Usage: Geser Urutan Kolom serta Pin dan Unpin

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): SKU inti `HHR-ARC-100` serta seed (#29, #30); data Usage `HHR-ARC-100` lima baris (#32, #24). Nilai dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).
- Urutan bawaan kolom: `Company, Entity Type, Total Stock`.
- Pemindahan kolom (parameter langkah 6 dan 7; kumulatif dari urutan bawaan; posisi tujuan dipilih spec karena TC hanya menyebut "posisi lain"):

  | # | Kolom | Posisi tujuan | Urutan preview sesudahnya |
  |---|---|---|---|
  | 1 | `Company` | 3 | `Entity Type, Total Stock, Company` |
  | 2 | `Entity Type` | 3 | `Total Stock, Company, Entity Type` |
  | 3 | `Total Stock` | 2 | `Company, Total Stock, Entity Type` |

- Kolom yang di-pin (parameter langkah 11 sampai 15): `Company`, `Entity Type`, `Total Stock`.
- Data Dinamis: tidak ada. Spec menyimpan konfigurasi kolom (urutan pada langkah 8 dan status pin sementara pada langkah 11 dan 14).
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Setup Column popup Usage di browser (hook `before` agar kolom pada konfigurasi bawaan, dan hook `after`), bukan lewat [Reset to Default]. Drag and drop kolom pada Popup Setup Column; tabel Usage dapat digulir horizontal pada viewport uji.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).
- Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar disediakan tim FE (lihat Temuan untuk QA).

## Test Steps

1. Klik SKU `HHR-ARC-100`
2. Verifikasi Popup `Device SKU Detail` tampil

### TC-AC-DS-457: Geser urutan kolom Setup Column Usage by Company

3. Klik header kolom Actions (⋯) pada popup, klik `Setup Column...`
4. Verifikasi Popup Setup Column tampil
5. Untuk setiap baris tabel "Pemindahan kolom" lakukan langkah 6 dan 7
6. Seret kolom ke posisi tujuan
7. Verifikasi urutan preview berubah menjadi "Urutan preview sesudahnya"
8. Klik `[Save]`
9. Verifikasi urutan kolom pada tabel Usage mengikuti hasil drag: `Company, Total Stock, Entity Type`

### TC-AC-DS-458: Pin dan unpin kolom Setup Column Usage by Company

10. Untuk setiap baris tabel "Kolom yang di-pin" lakukan langkah 11 sampai 15
11. Klik header kolom Actions (⋯) pada popup, klik `Setup Column...`, klik ikon Pin pada kolom, klik `[Save]`
12. Gulir tabel Usage secara horizontal
13. Verifikasi kolom tersebut membeku di kiri ketika tabel digulir
14. Klik header kolom Actions (⋯) pada popup, klik `Setup Column...`, klik ikon Pin pada kolom tersebut (unpin), klik `[Save]`, gulir tabel Usage secara horizontal
15. Verifikasi kolom tersebut kembali bergerak setelah unpin
16. Klik header kolom Actions (⋯) pada popup, klik `Setup Column...`, seret kolom `Total Stock` ke posisi tepat di bawah `Entity Type`, lalu klik `[Save]`

### Pemulihan state akhir

17. Tutup popup `Device SKU Detail` dengan ikon close `[✕]`

## Notes

- Langkah 6 dan 7 diulang per baris tabel "Pemindahan kolom" (3 iterasi, ekspansi 6 langkah) dan langkah 11 sampai 15 per baris tabel "Kolom yang di-pin" (3 iterasi, ekspansi 15 langkah); total ekspansi spec sekitar 35 langkah. Semua langkah satu kelas (Setup Column popup Usage) dan tiap iterasi berdiri sendiri.
- Langkah penghubung tanpa `Verifikasi`: langkah 16 mengembalikan urutan kolom bawaan `Company, Entity Type, Total Stock` yang disimpan pada langkah 8, dan langkah 17 menutup popup (S-03, S-09); hook `after` tetap menghapus preferensi kolom sebagai cadangan.
- Temuan untuk QA:
  - S-15: TC 457 hanya menyebut "posisi lain" tanpa posisi tujuan; spec memilih posisi deterministik. Expected 457 menyebut urutan "pada preview dan tabel" dengan satu `[Save]` di akhir; preview per kolom (langkah 7), tabel setelah Save (langkah 9).
  - S-14: Expected 458 mensyaratkan tabel Usage yang dapat digulir horizontal; tiga kolom bisa muat tanpa gulir. TC tidak menyebut viewport; kemampuan dicatat di Prerequisites.
  - TC 458 tidak punya Expected "status pin tersimpan" (berbeda dengan TC 416 Changelog); tidak ditambahkan.
  - S-14: TC tidak menyebut Search untuk menemukan baris `HHR-ARC-100`; spec mengandalkan baris itu tampil di halaman pertama List.
  - Fixture rancangan Pre-setup #32 dan #24 belum terverifikasi ada di environment; fixture `settingsDeviceSku` dan 23 env var `AC_DS_*` (termasuk `AC_DS_TC_PASSWORD`) belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; flag-nya belum dinyatakan di `suite.md`.
