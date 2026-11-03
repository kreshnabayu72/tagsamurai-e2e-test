---
id: TC-AC-CS-E2E-106-changelog-filter-panel-1
title: "Changelog: Filter Panel (1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-410
  - TC-AC-CS-411
  - TC-AC-CS-412
  - TC-AC-CS-413
  - TC-AC-CS-414
coverage:
  web: automated
---

# Changelog: Filter Panel (1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #84 (Changelog Client Subscription berisi 24 entri contoh PRD §4.1.2 dengan Action Edit, Activate, Cancel, Renew, Add Subscription, Resubmit, Timeout Auto-Cancel, Cancel Request, Scheduled Flip Auto-Cancel, Convert, dan Schedule Renewal, Modified By `Fajar N`, `Dewi A`, `Rina P`, `Hendra W`, `Maya T`, `Budi S`, dan `System`) bersifat baca-saja; spec tidak menulis entri Changelog. Changelog adalah audit trail permanen: asersi posisi atau urutan memakai entri seed #84 pada keadaan yang dipulihkan baseline automation sebelum tiap spec (Catatan TC; S-14).
- Changelog, Activity Log, dan System Log adalah audit trail permanen: spec ini tidak menulis entri dan tidak mengasersi total entri sebagai angka absolut (S-12).
- General Settings Principal PT ABC: Date Format `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00`; tanggal acuan uji `19/08/26` (Pre-setup #28).

## Test Steps

1. Klik ikon Changelog di toolbar

### TC-AC-CS-410: Screening Filter Panel Modal Changelog

2. Klik ikon Filter pada toolbar modal
3. Verifikasi field Filter Panel: Date (date range picker, placeholder "Select date range"), Action (multi-select searchable, "All actions"), Client ("All clients"), Product ("All products"), Field ("All fields"), Modified By ("All users")
4. Verifikasi Client dan Product berupa dua dropdown terpisah
5. Verifikasi `[Clear Field]` dan `[Apply]` tampil di bawah panel

### TC-AC-CS-411: Filter Date Modal Changelog: placeholder dan rentang inklusif

6. Verifikasi placeholder field Date adalah "Select date range"
7. Pilih rentang `13/08/26` sampai `13/08/26`, lalu klik `[Apply]`
8. Verifikasi rentang satu hari menampilkan entri tanggal `13/08/26` (Resubmit `13/08/26 09:05`)
9. Verifikasi entri di luar rentang `13/08/26` tidak tampil
10. Buka Filter Panel, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-CS-412: Filter Action multi-select

11. Buka Filter Panel, pilih Action `Cancel` dan `Convert`, lalu klik `[Apply]`
12. Verifikasi tabel menampilkan sedikitnya satu entri
13. Verifikasi hanya entri Action `Cancel` dan `Convert` yang tampil (gabungan OR dalam field)
14. Buka Filter Panel lalu buka dropdown Action
15. Verifikasi dropdown Action menampilkan sedikitnya satu opsi Action
16. Verifikasi opsi dropdown Action hanya memuat Action yang ada di tabel log saat ini
17. Tutup dropdown Action, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-CS-413: Filter Client dan Product sebagai dua dropdown terpisah

18. Buka Filter Panel, pilih Client `Optik Cahaya` dan Product `FAMS`, lalu klik `[Apply]`
19. Verifikasi tabel menampilkan sedikitnya satu entri
20. Verifikasi hanya entri Client `Optik Cahaya` Product `FAMS` yang tampil
21. Verifikasi entri Activate Trial yang hanya berisi Client tanpa Product tidak tampil karena tidak cocok dengan filter Product
22. Buka Filter Panel, klik `[Clear Field]`, lalu klik `[Apply]`

### TC-AC-CS-414: Filter Field dan Modified By termasuk System

23. Buka Filter Panel, pilih Field `Status` dan Modified By `System`, lalu klik `[Apply]`
24. Verifikasi tabel menampilkan sedikitnya satu entri
25. Verifikasi hanya entri Field `Status` yang dicatat oleh `System` (Scheduled Flip, Timeout Auto-Cancel) yang tampil
26. Buka Filter Panel lalu buka dropdown Modified By
27. Verifikasi opsi Modified By memuat `System` dan nama user yang tercatat
28. Tutup dropdown Modified By, klik `[Clear Field]`, lalu klik `[Apply]`

## Notes

- TC-AC-CS-415 sampai 418 (kombinasi filter, opsi, pencarian dropdown, dan default sort) dicakup spec lain suite ini.
- Langkah penghubung (S-03): langkah `[Clear Field]` lalu `[Apply]` sesudah tiap blok yang memakai filter, langkah membuka dan menutup dropdown, dan klik ikon Changelog untuk membuka modal.
- Asersi universal ("hanya entri ...") dan absence (entri di luar rentang, entri tanpa Product) didahului `Verifikasi` sedikitnya satu entri atau entri yang cocok pada permukaan yang sama (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-AC-CS-411 Expected a menyebut placeholder "Select date range" sedangkan klausa global menyebut "Select date" (NC-06 digantikan 2026-10-18); spec mengikuti Expected TC.
  - TC-AC-CS-412 Expected b dan TC-AC-CS-414 Expected b tidak punya langkah membuka dropdown; spec menambah langkah membuka dropdown Action dan Modified By.
