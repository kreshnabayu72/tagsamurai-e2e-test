---
id: TC-AC-ACC-E2E-256-modal-changelog-column-visibility-setup-column-dan-loading-state
title: "Tiga Modal Changelog: Screening Column Visibility dan Setup Column, Tutup tanpa Save, Kolom Terakhir Disabled, dan Loading State"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-741
  - TC-AC-ACC-742
  - TC-AC-ACC-747
  - TC-AC-ACC-748
  - TC-AC-ACC-858
coverage:
  web: automated
---

# Tiga Modal Changelog: Screening Column Visibility dan Setup Column, Tutup tanpa Save, Kolom Terakhir Disabled, dan Loading State

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup (hanya dibaca): Client C-01 "PT Sejahtera Abadi" (Tab Subscription dan Tab Asset Control).
- Tabel "Modal Changelog" (parameter blok semua TC di spec ini; kolom `Cara buka` selalu dimulai dari menu Client di sidebar):

| Modal | Cara buka | Kolom (7, urutan default) |
|---|---|---|
| Changelog: Client | Klik menu Client di sidebar, lalu klik [Changelog] di toolbar List | Date, Action, Client Name, Field, Old Value, New Value, Modified By |
| Changelog: Subscription | Klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Subscription, lalu klik [Changelog] | Date, Action, Subscription, Field, Old Value, New Value, Modified By |
| Changelog: Asset Control | Klik menu Client di sidebar, ketik Search "PT Sejahtera Abadi", tekan Enter, klik Company Name "PT Sejahtera Abadi", klik Tab Asset Control, lalu klik ikon Changelog | Date, Action, Object, Field, Old Value, New Value, Modified By |

- Kemampuan teknis: (1) tahanan respons data Changelog per modal lewat throttling jaringan atau intercept yang menahan respons, dilepas segera sesudah dipakai (S-09), untuk TC-AC-ACC-858 (menahan respons untuk mengamati state UI bukan kelas b); endpoint mengikuti kontrak modul, dipetakan tim FE; (2) penghapusan preferensi kolom di browser untuk ketiga modal Changelog di hook `after` (bagian 4 konvensi), disediakan tim FE; konfigurasi kolom yang disimpan spec ini didaftarkan di `suite.md`.
- State global: preferensi kolom ketiga modal Changelog dihapus di hook `after`; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-741: Screening overlay Column Visibility

1. Untuk setiap baris tabel "Modal Changelog" (langkah 1 sampai 8): buka modal sesuai kolom "Cara buka"
2. Arahkan kursor ke header kolom Actions (⋯) pada tabel modal
3. Verifikasi tooltip "Column Visibility"
4. Klik header kolom Actions (⋯)
5. Verifikasi panel memuat checkbox tercentang dan enabled serta handle drag untuk 7 kolom pada kolom tabel "Kolom"
6. Verifikasi item "Setup Column..." di bagian bawah panel
7. Verifikasi tidak ada kolom Curated dan kolom Actions tidak tercantum sebagai baris panel
8. Tutup panel dengan Esc lalu tutup modal

### TC-AC-ACC-742: Screening modal Setup Column

9. Untuk setiap baris tabel "Modal Changelog" (langkah 9 sampai 14): buka modal sesuai kolom "Cara buka"
10. Klik header kolom Actions (⋯) pada tabel modal lalu klik "Setup Column..."
11. Verifikasi Title "Setup Column", deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.", dan ikon close [✕]
12. Verifikasi 7 baris kolom pada kolom tabel "Kolom" tercentang dengan handle drag dan ikon Pin
13. Verifikasi footer [Reset to Default] dan [Save] tanpa [Cancel]
14. Tutup modal Setup Column dengan tombol ✕, lalu tutup modal Changelog

### TC-AC-ACC-747: Menutup modal Setup Column lewat [✕] atau Esc membuang perubahan

15. Untuk setiap baris tabel "Modal Changelog" (langkah 15 sampai 23): buka modal sesuai kolom "Cara buka"
16. Klik header kolom Actions (⋯) pada tabel modal lalu klik "Setup Column..."
17. Hapus centang Modified By lalu klik [✕]
18. Verifikasi kolom Modified By tetap tampil di tabel
19. Klik header kolom Actions (⋯) pada tabel modal lalu klik "Setup Column..."
20. Hapus centang Modified By
21. Tekan Esc
22. Verifikasi kolom Modified By tetap tampil di tabel
23. Tutup modal Changelog

### TC-AC-ACC-748: Checkbox kolom terakhir yang tampil disabled

24. Untuk setiap baris tabel "Modal Changelog" (langkah 24 sampai 31): buka modal sesuai kolom "Cara buka"
25. Klik header kolom Actions (⋯) pada tabel modal lalu klik "Setup Column..."
26. Hapus centang enam kolom pertama pada daftar sehingga hanya Modified By yang tercentang
27. Arahkan kursor ke checkbox Modified By
28. Verifikasi checkbox Modified By tetap tampil namun disabled dengan tooltip "At least one column must remain visible."
29. Klik checkbox Modified By
30. Verifikasi klik tidak mengubah apa pun (Modified By tetap tercentang)
31. Klik [✕] untuk menutup modal tanpa menyimpan, lalu tutup modal Changelog

### TC-AC-ACC-858: Loading state saat data modal Changelog diambil

32. Untuk setiap baris tabel "Modal Changelog" (langkah 32 sampai 35): tahan respons data modal (throttle jaringan), lalu buka modal sesuai kolom "Cara buka"
33. Verifikasi Loading component tampil selama data diambil
34. Lepaskan tahanan respons
35. Verifikasi baris tabel tampil setelah respons, lalu tutup modal

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16): "Cara buka" tiap modal (menu Client di sidebar, Search dan buka Detail Client; hook suite hanya membuka List Client dan klik sidebar mereset Search), langkah 8, 14, 23, 31, 35 (menutup panel, modal Setup Column, dan modal Changelog).
- Langkah 1 sampai 8 diulang 3 kali (24 langkah setelah ekspansi), 9 sampai 14 diulang 3 kali (18), 15 sampai 23 diulang 3 kali (27), 24 sampai 31 diulang 3 kali (24), 32 sampai 35 diulang 3 kali (12); total ekspansi sekitar 108 langkah.
- Spec ini melewati sekitar 35 langkah. Alasan: semua blok satu kelas harness (UI Only: Column Visibility, Setup Column, dan loading state pada tiga modal Changelog dengan akun yang sama); tiap iterasi membuka modal dari awal sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: Setup Column yang disimpan (hide/show, drag, pin, reset) ada di spec 257, 258, 259, dan 260; error state modal Changelog ada di spec 240.
- Temuan untuk QA:
  - Keputusan user 2026-11-02: spec mengikuti `docs/spec-decisions.md` D-008 (tabel di balik popup tidak berubah sampai [Save]; menutup popup tanpa Save membuang perubahan) untuk Setup Column. TC-AC-ACC-747 dan 748 di spec ini tidak mengasersi perubahan tabel sebelum [Save] sehingga tidak terdampak; selisih TC-AC-ACC-743 sampai 746 dicatat di spec 257, 258, dan 260.
  - TC-AC-ACC-858 tidak menyebut durasi tahanan respons; spec menahan respons sampai Loading component teramati.
