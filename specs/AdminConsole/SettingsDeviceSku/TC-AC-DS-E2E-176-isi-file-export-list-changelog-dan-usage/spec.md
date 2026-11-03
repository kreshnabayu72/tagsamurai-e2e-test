---
id: TC-AC-DS-E2E-176-isi-file-export-list-changelog-dan-usage
title: "Isi File Export: Nilai Sel List, Changelog, dan Usage by Company"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-374
  - TC-AC-DS-423
  - TC-AC-DS-464
coverage:
  web: automated
---

# Isi File Export: Nilai Sel List, Changelog, dan Usage by Company

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Jane Setiawan, Modified By `Jane S`): `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): SKU inti dan seed (#29, #30), Usage by Company (#32), riwayat Changelog Principal (#33), General Settings (#35).
- Data Dinamis: tidak ada.
- Kemampuan teknis (disediakan tim FE/BE): membaca berkas XLSX unduhan (tipe sel, nilai sel, header).
- State global: pilihan kolom List (Hardware Type, Range Type, TAG Type) disimpan sebagai preferensi kolom di browser; preferensi dihapus di hook `after` (bukan `[Reset to Default]`, kemampuan disediakan tim FE, bagian 4). Suite berjalan serial (`parallel: false`).
- Nilai data dibaca dari fixture `settingsDeviceSku` (berkas fixture belum ada; disediakan tim FE).

## Test Steps

### TC-AC-DS-374: Isi sel file export List sesuai tipe kolom

1. Klik header kolom Actions (⋯) lalu centang `Hardware Type` pada Overlay Column Visibility
2. Klik header kolom Actions (⋯) lalu centang `Range Type` pada Overlay Column Visibility
3. Klik header kolom Actions (⋯) lalu centang `TAG Type` pada Overlay Column Visibility
4. Klik ikon Download
5. Klik `Download as XLSX`
6. Buka file dan periksa baris `HHR-BIG-01` dan `TAG-ARC-USR`
7. Verifikasi kolom Photo tidak ikut di file
8. Verifikasi Category baris `HHR-BIG-01` berisi hierarki penuh dari root `Hardware > Handheld Reader > Perangkat Pemindai Kode Batang Industri`
9. Verifikasi Brand baris `HHR-BIG-01` berisi nama penuh `International Scanner Solutions` tanpa pemotongan
10. Verifikasi Model/Type baris `HHR-BIG-01` berisi nama penuh `Industrial Handheld Reader Series Alpha` tanpa pemotongan
11. Verifikasi Current Stock baris `HHR-BIG-01` adalah sel angka bernilai 12500 (bukan teks) tanpa pemisah ribuan
12. Verifikasi Last Modified baris `HHR-BIG-01` bernilai `30/09/26 18:00` mengikuti Date Format dan Time Format General Settings
13. Verifikasi nilai kosong ditulis `-` (hyphen tunggal) bukan `—`: Hardware Type dan Range Type pada baris `TAG-ARC-USR` serta TAG Type pada baris `HHR-BIG-01`

### TC-AC-DS-423: Isi file export Changelog: kolom, format tanggal, dan nilai kosong

14. Klik ikon Changelog
15. Klik ikon Download lalu `Download as XLSX`
16. Buka file dan periksa baris Create `BLE-KIN-GW1` dan Delete `HHR-ARC-300`
17. Verifikasi header kolom sesuai kolom modal yang tampil
18. Verifikasi kolom Date baris Create `BLE-KIN-GW1` mengikuti General Settings (`12/09/26 16:20`)
19. Verifikasi kolom SKU baris Create berisi `BLE Gateway (BLE-KIN-GW1)`
20. Verifikasi Old Value Create ditulis `-` (hyphen) dan New Value Delete ditulis `-` bukan `—`
21. Tutup modal Changelog

### TC-AC-DS-464: Isi file export Usage: dua badge dipisah koma dan Total Stock berupa angka

22. Ketik Search `HHR-ARC-100`, tekan Enter, lalu klik SKU `HHR-ARC-100`
23. Klik ikon Download pada popup lalu `Download as XLSX`
24. Buka file dan periksa baris `PT Mitra Lintas Nusa`
25. Verifikasi Entity Type baris `PT Mitra Lintas Nusa` ditulis `Distributor, Client`
26. Verifikasi Total Stock baris `PT Mitra Lintas Nusa` ditulis sebagai sel angka 20 tanpa pemisah ribuan
27. Tutup Popup Device SKU Detail lalu klik `(←)` pada kotak Search

## Notes

- Langkah penghubung tanpa `Verifikasi`: Search `HHR-ARC-100` pada langkah 22 (menemukan baris target, R-16) dan penutupan modal serta popup.
- Expected 374 butir c dipecah per field (Brand dan Model/Type), butir f satu `Verifikasi` karena nilai kosong lintas kolom disebut utuh dalam satu butir TC; Expected 423 butir c dipecah menjadi kolom SKU dan nilai kosong.
- Temuan untuk QA:
  - TC 423 butir a ("Header kolom sesuai kolom modal yang tampil") tidak merinci nama kolom; spec mengasersi kesesuaian dengan kolom modal.
  - S-12/S-06: TC memakai nama literal Pre-setup (mis. `HHR-ARC-200`) dan kode SKU Data Dinamis literal sebagai target aksi tulis; konvensi meminta data bersuffix dan data milik spec. Lampiran A tidak memuat butir modul ini; spec mengikuti TC dengan pembersihan kode literal di hook `before` (R-13) dan membutuhkan keputusan pengecualian (seeding idempotent, suite serial).
  - S-11/S-13: fixture `settingsDeviceSku`, 23 env var `AC_DS_*` (termasuk yang dipakai spec ini), dan fixture rancangan Pre-setup yang dirujuk belum terverifikasi ada di environment atau belum terdaftar di `spectra.config.ts` dan `.env.example` (disediakan tim FE).
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag agar tidak menutupi layar belum dinyatakan di `suite.md` (disediakan tim FE).
