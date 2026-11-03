---
id: TC-AC-CS-E2E-105-changelog-search
title: "Changelog: Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-406
  - TC-AC-CS-407
  - TC-AC-CS-408
  - TC-AC-CS-409
coverage:
  web: automated
---

# Changelog: Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT ABC (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Data seed Pre-setup #84 (Changelog Client Subscription berisi 24 entri contoh PRD §4.1.2 dengan Action Edit, Activate, Cancel, Renew, Add Subscription, Resubmit, Timeout Auto-Cancel, Cancel Request, Scheduled Flip Auto-Cancel, Convert, dan Schedule Renewal, Modified By `Fajar N`, `Dewi A`, `Rina P`, `Hendra W`, `Maya T`, `Budi S`, dan `System`) bersifat baca-saja; spec tidak menulis entri Changelog. Changelog adalah audit trail permanen: asersi posisi atau urutan memakai entri seed #84 pada keadaan yang dipulihkan baseline automation sebelum tiap spec (Catatan TC; S-14).
- Changelog, Activity Log, dan System Log adalah audit trail permanen: spec ini tidak menulis entri dan tidak mengasersi total entri sebagai angka absolut (S-12).

## Test Steps

1. Klik ikon Changelog di toolbar

### TC-AC-CS-406: Search Changelog kelas teks: Action, Client — Product, Field, Modified By

2. Ketik Search `resubmit`, tekan Enter
3. Verifikasi entri Action `Resubmit` (`Optik Cahaya — FAMS`) tampil
4. Ganti isi kotak search dengan `percetakan`, tekan Enter
5. Verifikasi entri `Percetakan Mega — FAMS` tampil
6. Ganti isi kotak search dengan `quota`, tekan Enter
7. Verifikasi entri Field `Asset Quota`, `Concurrent User Quota`, dan `Log Source Quota` tampil
8. Ganti isi kotak search dengan `rina`, tekan Enter
9. Verifikasi entri Modified By `Rina P` tampil (tanpa membedakan huruf besar kecil dan substring)

### TC-AC-CS-407: Search Changelog kolom Old Value dan New Value

10. Ganti isi kotak search dengan `Waiting for Approval`, tekan Enter
11. Verifikasi entri yang Old Value atau New Value-nya memuat teks `Waiting for Approval` tampil
12. Ganti isi kotak search dengan `30 days`, tekan Enter
13. Verifikasi entri Edit Trial Duration yang Old Value-nya `30 days` tampil
14. Verifikasi entri Activate yang New Value-nya `Trial — [Plan Name], 30 days` tampil

### TC-AC-CS-408: Search Changelog tidak mencocokkan kolom Date

15. Ganti isi kotak search dengan `13/08/26`, tekan Enter
16. Verifikasi empty state "No results found" tampil karena tidak ada kolom Searchable lain yang memuat `13/08/26`
17. Verifikasi entri Resubmit `13/08/26 09:05` tidak tampil
18. Klik ikon Filter pada toolbar modal
19. Verifikasi Filter Panel menyediakan field Date untuk menyaring tanggal
20. Klik ikon Filter lagi untuk menutup Filter Panel

### TC-AC-CS-409: Search Changelog menjalankan trim dan Enter

21. Klik `(←)` pada kotak Search lalu catat isi tabel
22. Ketik Search ` reject ` (dengan spasi di kedua sisi) tanpa menekan Enter
23. Verifikasi tabel belum tersaring (isi tabel sama dengan isi yang dicatat)
24. Tekan Enter lalu catat hasil tabel
25. Ganti isi kotak search dengan `reject`, tekan Enter
26. Verifikasi hasil identik dengan hasil ` reject ` yang dicatat

## Notes

- Langkah penghubung (S-03): langkah mencatat isi tabel dan hasil sebelum asersi "belum tersaring" dan "identik" (baseline), langkah klik ikon Filter untuk membuka dan menutup Filter Panel pada blok TC-AC-CS-408, dan langkah `(←)` pada kotak Search.
- Asersi absence entri `13/08/26 09:05` (TC-AC-CS-408) didahului `Verifikasi` empty state "No results found" sebagai anchor positif hasil Search (bagian 8b butir 2); urutan kedua Verifikasi dibalik terhadap Expected TC untuk itu (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-AC-CS-408 Expected c ("Penyaringan tanggal lewat Filter Panel") tidak punya langkah di Langkah Uji; spec menambah langkah membuka Filter Panel dan `Verifikasi` field Date.
  - TC-AC-CS-409 Expected b ("hasil identik dengan keyword `reject`") membutuhkan hasil pembanding; spec mencatat hasil tabel kedua keyword sebagai baseline.
