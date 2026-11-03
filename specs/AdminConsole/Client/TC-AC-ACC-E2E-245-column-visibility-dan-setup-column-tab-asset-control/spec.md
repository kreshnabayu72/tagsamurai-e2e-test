---
id: TC-AC-ACC-E2E-245-column-visibility-dan-setup-column-tab-asset-control
title: "Column Visibility Tiga Tabel dan Setup Column Station List pada Tab Asset Control"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-821
  - TC-AC-ACC-825
coverage:
  web: automated
---

# Column Visibility Tiga Tabel dan Setup Column Station List pada Tab Asset Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca): Client C-01 "PT Sejahtera Abadi" dengan Station "Gerbang Gudang A" (berisi Tablet).
- Kemampuan teknis: penghapusan preferensi kolom di browser (Setup Column Station List) di hook `after` (bagian 4 konvensi), disediakan tim FE; konfigurasi kolom yang disimpan spec ini didaftarkan di `suite.md`.
- State global: preferensi kolom Station List disimpan lalu dihapus di hook `after`; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

1. Ketik Search "PT Sejahtera Abadi" di List Client, tekan Enter, klik Company Name "PT Sejahtera Abadi", lalu klik Tab Asset Control

### TC-AC-ACC-821: Column Visibility pada tabel Station Quota, Station List, dan Tablet List

2. Klik ⋯ pada header tabel Station Quota
3. Verifikasi panel Column Visibility memuat Total, Used, Available
4. Verifikasi item "Setup Column..." di bagian bawah panel Station Quota
5. Hapus centang kolom Available
6. Verifikasi kolom Available hilang dari tabel Station Quota
7. Klik ⋯ pada header tabel Station List
8. Verifikasi panel Column Visibility memuat Reader Name, Reader Group (Fixed Asset), Reader Group (Supply), Reader ID, Reader Model, Ports, Tablets, Last Active, Status
9. Verifikasi item "Setup Column..." di bagian bawah panel Station List
10. Hapus centang kolom Reader ID
11. Verifikasi kolom Reader ID hilang dari tabel Station List
12. Klik baris "Gerbang Gudang A" untuk membuka Tablet List
13. Klik ⋯ pada header tabel Tablet List
14. Verifikasi panel Column Visibility memuat Device Name, Brand, Device ID, App Version, Enrolled Date, Last Active, Status
15. Verifikasi item "Setup Column..." di bagian bawah panel Tablet List
16. Hapus centang kolom Brand
17. Verifikasi kolom Brand hilang dari tabel Tablet List
18. Centang kembali kolom Brand pada panel Tablet List
19. Klik ⋯ pada header tabel Station List dan centang kembali kolom Reader ID
20. Klik ⋯ pada header tabel Station Quota dan centang kembali kolom Available

### TC-AC-ACC-825: Setup Column Station List: preview, tutup tanpa Save, dan Save

21. Klik ⋯ pada header tabel Station List lalu klik "Setup Column..."
22. Verifikasi modal berjudul "Setup Column"
23. Verifikasi deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
24. Verifikasi footer memuat [Reset to Default] dan [Save] tanpa [Cancel]
25. Hapus centang kolom Reader ID
26. Verifikasi kolom Reader ID masih tampil pada tabel Station List di balik modal sebelum [Save] (perubahan baru berlaku setelah [Save], D-008)
27. Tutup modal dengan tombol ✕
28. Verifikasi kolom Reader ID tetap tampil pada tabel Station List setelah modal ditutup tanpa Save (perubahan dibuang, D-008)
29. Klik ⋯ pada header tabel Station List lalu klik "Setup Column..."
30. Hapus centang kolom Reader ID lalu klik [Save]
31. Muat ulang halaman Detail (F5) lalu klik Tab Asset Control
32. Verifikasi kolom Reader ID tidak tampil pada tabel Station List
33. Klik ⋯ pada header tabel Station List lalu klik "Setup Column...", klik [Reset to Default], lalu klik [Save]

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-09): langkah 1 (Search dan buka Detail Client; hook suite hanya membuka List Client); langkah 12 (membuka Tablet List agar panel Tablet List teramati); langkah 18 sampai 20 (mencentang kembali kolom, Post Condition TC-AC-ACC-821); langkah 33 (pemulihan Post Condition TC-AC-ACC-825); preferensi kolom dihapus di hook `after`.
- Temuan untuk QA:
  - TC-AC-ACC-825 Expected b meminta kolom Reader ID sudah hilang dari tabel Station List di balik modal sebelum [Save], dan Expected c meminta kolom "tampil kembali" setelah ✕. Keputusan user 2026-11-02: spec mengikuti `docs/spec-decisions.md` D-008 (tabel di balik popup tidak berubah sampai [Save]; menutup popup tanpa Save membuang perubahan): langkah 26 mengasersi kolom masih tampil dan langkah 28 kolom tetap tampil. TC tidak diubah. TC tidak menyebut Preview Table di popup, sehingga spec tidak mengasersi preview. Perubahan diasersi sesudah [Save] (langkah 32). TC-AC-ACC-821 memakai panel Column Visibility (bukan popup) yang berlaku langsung dan tidak terdampak.
  - TC-AC-ACC-821 mengikuti PRD §4.1.5: tabel Station Quota, Station List, dan Tablet List punya Column Visibility masing-masing; TC tidak menyebut kolom yang tidak boleh disembunyikan (bukan temuan).
