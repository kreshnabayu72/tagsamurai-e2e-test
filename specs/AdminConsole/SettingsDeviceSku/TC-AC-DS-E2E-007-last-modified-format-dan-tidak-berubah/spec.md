---
id: TC-AC-DS-E2E-007-last-modified-format-dan-tidak-berubah
title: "Last Modified: Format Date dan Time Format General Settings, Edit Tanpa Perubahan, dan Perubahan Stok"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-26
  - TC-AC-DS-27
  - TC-AC-DS-28
coverage:
  web: automated
---

# Last Modified: Format Date dan Time Format General Settings, Edit Tanpa Perubahan, dan Perubahan Stok

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima `totalControlSku_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1, nama tampil `Jane Setiawan`), password `Spectra.env.AC_DS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (dibaca saja, tidak diubah): SKU inti #29 (`HHR-ARC-100` Last Modified `01/10/26 09:15`, `HHR-ARC-200` Last Modified `28/09/26 14:40`) dan seed #30. `HHR-ARC-200` hanya menjadi target Edit tanpa perubahan (aksi no-op); data dan Last Modified-nya tidak berubah.
- Data milik spec (hook `before`, lewat sesi API aktor dan fixture BE yang disediakan tim BE/FE): SKU `LMS-{runId}-007` (Device Name `UHF Handheld Reader`, Category `UHF Handheld`, Brand `Arcturus`, Model/Type `LM-{runId}`, Range Type `Short Range`, stok 0, 1 foto) untuk perubahan stok pada TC-28. Hook `after` menghapus unit stok dan SKU itu lewat fixture BE yang disediakan tim BE (SKU berstok lebih dari 0 tidak dapat dihapus lewat UI).
- Modul stok: Hardware Stock > Add Stock pada Principal PT Arunika Prima (Pre-setup #39); menambah 1 unit untuk SKU milik spec lewat Add Stock atau fixture BE.
- State global: General Settings #35 (Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta). TC-26 mengubah Date Format menjadi `dd MMM yy`; spec memulihkannya ke `dd/MM/yy` pada langkah terakhir TC-26 dan hook `after` memulihkannya bila spec gagal di tengah. Kemampuan mengubah General Settings disediakan tim FE/BE. Suite berjalan serial (`parallel: false`).
- Env var `AC_DS_TC_PASSWORD` belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; pendaftarannya disediakan tim FE.
- Dirujuk lewat fixture `fixtures/settings-device-sku.json` (disediakan tim FE, belum ada).

## Test Steps

### TC-AC-DS-27: Last Modified tidak berubah oleh Edit tanpa perubahan

1. Ketik Search `HHR-ARC-200`, tekan Enter
2. Catat nilai sel Last Modified baris `HHR-ARC-200` (`28/09/26 14:40`)
3. Klik ⋯ baris `HHR-ARC-200` lalu pilih `Edit`
4. Klik `[Save]` tanpa mengubah field apa pun
5. Verifikasi toast info: "No changes to save."
6. Verifikasi sel Last Modified baris `HHR-ARC-200` tetap sama dengan nilai yang dicatat pada langkah 2

### TC-AC-DS-28: Last Modified tidak berubah oleh perubahan stok dari modul stok

7. Ganti isi kotak search dengan `LMS-{runId}-007`, tekan Enter
8. Catat nilai sel Last Modified baris `LMS-{runId}-007`
9. Tambahkan 1 unit untuk SKU `LMS-{runId}-007` di Hardware Stock lewat Add Stock hingga unit tersimpan
10. Kembali ke Settings > Device > Device SKU lalu muat ulang halaman
11. Ketik Search `LMS-{runId}-007`, tekan Enter
12. Verifikasi Current Stock baris `LMS-{runId}-007` menjadi `1`
13. Verifikasi Last Modified baris `LMS-{runId}-007` tetap sama dengan nilai yang dicatat pada langkah 8

### TC-AC-DS-26: Last Modified mengikuti Date Format dan Time Format General Settings

14. Ganti isi kotak search dengan `HHR-ARC-100`, tekan Enter
15. Verifikasi sel Last Modified baris `HHR-ARC-100` menampilkan `01/10/26 09:15`
16. Ubah Date Format General Settings menjadi `dd MMM yy` dengan Time Format 24 jam tetap
17. Muat ulang halaman Settings > Device > Device SKU
18. Ketik Search `HHR-ARC-100`, tekan Enter
19. Verifikasi sel Last Modified baris `HHR-ARC-100` menampilkan `01 Oct 26 09:15`
20. Pulihkan Date Format General Settings menjadi `dd/MM/yy`

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Urutan TC dalam spec: TC-27, TC-28, TC-26. TC-26 diletakkan terakhir karena mengubah state global Date Format (S-10); TC-27 dan TC-28 mengasersi Last Modified dalam format awal `dd/MM/yy`.
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 7, 11, 14, 18 (Search untuk menemukan baris target, R-16), 2 dan 8 (mencatat nilai pembanding), 3 dan 4 (membuka Edit dan menyimpan; hasilnya diasersi pada langkah 5 dan 6), 9 sampai 10, 16 sampai 17, 20 (pemulihan Date Format, S-09).
- TC-28 memakai SKU milik spec `LMS-{runId}-007` (bukan `HHR-ARC-200` Pre-setup) karena Add Stock mengubah Current Stock dan tidak dapat dipulihkan lewat UI (S-06); Expected b diasersi sebagai "sama dengan nilai yang dicatat sebelum aksi" (langkah 8), bukan nilai literal `28/09/26 14:40`.
- Temuan untuk QA:
  - S-12: asersi TC-26 dan TC-27 memakai nama literal dan nilai Pre-setup #29 karena TC menetapkannya; Lampiran A tidak memuat pengecualian nama literal untuk modul ini (menunggu keputusan).
  - Fixture rancangan: ketersediaan Pre-setup #29, #35, dan #39 di environment belum diverifikasi.
  - TC-26 langkah 3 tidak menyebut menu atau halaman tempat Date Format General Settings diubah; spec menuliskannya sebagai aksi ubah General Settings dan kemampuannya disediakan tim FE/BE.
  - TC-27 tidak menyebut apakah popup Edit SKU tertutup sendiri setelah `[Save]` tanpa perubahan; langkah 4 mengikuti TC ("popup tutup") dan tidak diasersi.
  - TC-28 (Post Condition kosong): cara menghapus SKU berstok lebih dari 0 pada cleanup tidak dirinci TC; disediakan tim BE.
  - Env var `AC_DS_*` (akun #1 sampai #23) belum terdaftar; email akun berbeda dari akun Admin Console yang sudah ada.
