---
id: TC-AC-CS-E2E-107-changelog-filter-panel-2
title: "Changelog: Filter Panel (2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-415
  - TC-AC-CS-416
  - TC-AC-CS-417
  - TC-AC-CS-418
coverage:
  web: automated
---

# Changelog: Filter Panel (2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #84 (Changelog Client Subscription berisi 24 entri contoh PRD §4.1.2 dengan Action Edit, Activate, Cancel, Renew, Add Subscription, Resubmit, Timeout Auto-Cancel, Cancel Request, Scheduled Flip Auto-Cancel, Convert, dan Schedule Renewal, Modified By `Fajar N`, `Dewi A`, `Rina P`, `Hendra W`, `Maya T`, `Budi S`, dan `System`) bersifat baca-saja; spec tidak menulis entri Changelog. Changelog adalah audit trail permanen: asersi posisi atau urutan memakai entri seed #84 pada keadaan yang dipulihkan baseline automation sebelum tiap spec (Catatan TC; S-14).
- Changelog, Activity Log, dan System Log adalah audit trail permanen: spec ini tidak menulis entri dan tidak mengasersi total entri sebagai angka absolut (S-12).
- Client yang tidak punya entri Changelog dan Client yang sudah di-rename tetapi punya entri historis (Expected TC-AC-CS-416 a dan b) tidak tercantum di Pre-setup #84; keduanya disediakan tim FE (S-11) dan tercatat di Temuan untuk QA.
- General Settings Principal PT ABC: Date Format `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00`; tanggal acuan uji `19/08/26` (Pre-setup #28).

## Test Steps

1. Klik ikon Changelog di toolbar

### TC-AC-CS-415: Kombinasi field filter Changelog bersifat AND dan Clear Field melepas

2. Catat jumlah entri tabel Changelog sebelum filter
3. Klik ikon Filter pada toolbar modal, pilih Action `Cancel Request` dan Modified By `Fajar N`, lalu klik `[Apply]`
4. Verifikasi tabel menampilkan sedikitnya satu entri
5. Verifikasi hanya entri Action `Cancel Request` oleh `Fajar N` yang tampil
6. Buka Filter Panel, klik `[Clear Field]`, lalu klik `[Apply]`
7. Verifikasi semua entri tampil kembali (jumlah entri sama dengan yang dicatat)

### TC-AC-CS-416: Opsi filter Changelog di-populate dari entri log saat ini

8. Buka Filter Panel lalu buka dropdown Client
9. Verifikasi dropdown Client memuat Client yang punya entri log (`Optik Cahaya`)
10. Verifikasi Client tanpa entri log tidak ada di dropdown
11. Verifikasi Client yang sudah di-rename tetap muncul sesuai entri historisnya
12. Tutup dropdown Client lalu buka dropdown Field
13. Verifikasi opsi Field memuat tepat nilai `Asset Quota`, `Concurrent User Quota`, `Duration`, `Log Source Quota`, `Pending Renewal`, `Plan`, `Plan/End Date`, `Start Date`, `Status`, dan `Subscription Type`, tanpa nilai lain

### TC-AC-CS-417: Pencarian di dalam dropdown filter Changelog

14. Tutup dropdown Field, buka dropdown Modified By, lalu ketik `hen`
15. Verifikasi opsi menyempit ke `Hendra W`
16. Ganti isi pencarian dropdown dengan `zzzz`
17. Verifikasi dropdown menampilkan teks "No results found"
18. Tutup dropdown Modified By lalu tutup Filter Panel

### TC-AC-CS-418: Default sort Changelog Date Newest First

19. Verifikasi entri `19/08/26 11:50` berada paling atas pada halaman 1
20. Pindah ke halaman terakhir
21. Verifikasi entri `15/08/25 09:40` berada paling bawah pada halaman terakhir
22. Verifikasi pada timestamp yang sama entri yang ditulis lebih akhir berada lebih atas

## Notes

- TC-AC-CS-410 sampai 414 (Filter Panel screening, Date, Action, Client dan Product, Field dan Modified By) dicakup spec lain suite ini; TC-AC-CS-419 sampai 421 (sort) dicakup spec lain suite ini.
- Langkah penghubung (S-03): langkah mencatat jumlah entri sebelum filter (baseline), langkah `[Clear Field]` lalu `[Apply]`, dan langkah membuka dan menutup dropdown dan Filter Panel.
- Asersi absence (Client tanpa entri log) didahului `Verifikasi` Client yang punya entri log pada dropdown yang sama sebagai anchor positif (bagian 8b butir 2). Asersi "hanya entri" didahului `Verifikasi` sedikitnya satu entri.
- Temuan untuk QA:
  - TC-AC-CS-416 Precondition menyebut "Client yang tidak punya entri log" tanpa nomor Pre-setup dan Expected b (Client yang sudah di-rename) tidak punya langkah penyiapan rename; data keduanya disediakan tim FE.
  - TC-AC-CS-418 Expected b (timestamp sama) tidak menyebut pasangan entri bertimestamp sama pada seed #84; spec mengasersinya pada pasangan entri seed yang ada.
  - TC-AC-CS-418 Expected a bergantung pada urutan seed #84 di halaman pertama dan terakhir; karena Changelog adalah audit trail permanen, asersi itu hanya sah pada keadaan yang dipulihkan baseline automation (S-14).
