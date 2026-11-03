---
id: TC-AC-ACC-E2E-267-pencatatan-log-suspend-unsuspend-dan-bulk-suspend-di-tiga-surface
title: "Pencatatan Log Suspend, Unsuspend, dan Bulk Suspend di Changelog Client, System Log, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-421
  - TC-AC-ACC-422
  - TC-AC-ACC-915
coverage:
  web: automated
---

# Pencatatan Log Suspend, Unsuspend, dan Bulk Suspend di Changelog Client, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Nama tampil A-01 tidak tertulis di Pre-setup TC (disediakan tim FE). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Tiga surface pembaca log: Changelog: Client (ikon Changelog di toolbar List; kolom Date, Action, Client Name, Field, Old Value, New Value, Modified By), System Log akun aktor (Settings > User > Detail akun aktor > Tab System Log; kolom Date, Action, Object, Name, Field, Old Value, New Value, tanpa Modified By), Activity Log Admin Console (Tab User Action, disaring Object `Client`; kolom sama dengan System Log ditambah Modified By).
- Data seed milik spec (replika bersuffix `{runId}-267` dengan atribut setara fixture asal TC; di-seed lewat Fixture BE di hook `before`, dihapus di hook `after`; kemampuan disediakan tim FE/BE, endpoint tidak dikarang; S-06): `PT Sinar Distributor {runId}-267` (setara C-11: Active, Distributor langsung PT Distribusi Nusantara tanpa Partner, Group Area Jakarta, FAMS Active; TC-AC-ACC-421 dan 915); `PT Ganti Mitra {runId}-267` (setara C-13: Active, Partner CV Mitra Sejati saja, Group Area Jakarta, FAMS Active; TC-AC-ACC-915); `PT Suspend Uji Satu {runId}-267` (setara C-AST-14: Suspended, Partner CV Mitra Sejati, Group Area Jakarta, FAMS Active; TC-AC-ACC-422). Data Pre-setup C-07 "PT Cahaya Baru" (Active, tidak dipilih, pembanding TC-AC-ACC-915) hanya dibaca. Nama Client replika unik sehingga baseline log bernilai nol, tetap dicatat (S-12). Pemulihan Post Condition TC dilakukan pada replika; replika dihapus di hook `after`.
- Baseline (S-12): jumlah baris log pada tiap surface dicatat dengan Search nama Client dan Action sebelum aksi, ukuran halaman 100; asersi "baris baru" memakai selisih terhadap baseline. Kolom Date tidak diasersi (Expected TC tidak menyebutnya).
- Parameter blok TC-AC-ACC-421 dan 422 (langkah 1 sampai 12):

| TC | Client | Aksi | Action | Field | Old Value | New Value |
|---|---|---|---|---|---|---|
| TC-AC-ACC-421 | PT Sinar Distributor {runId}-267 | Pada sub-tab Active: Search, buka ⋯ baris, klik Suspend, klik `[Suspend]` pada dialog | `Suspend` | `Status` | `Active` | `Suspended` |
| TC-AC-ACC-422 | PT Suspend Uji Satu {runId}-267 | Klik sub-tab Suspended: Search, buka ⋯ baris, klik Unsuspend, klik `[Unsuspend]` pada dialog | `Unsuspend` | `Status` | `Suspended` | `Active` |

- Parameter blok TC-AC-ACC-915 (langkah 15 sampai 16, 18 sampai 19, 21 sampai 22, 27 sampai 28, 30 sampai 31, dan 33 sampai 34; tiga Client):

| Client | Dipilih untuk Bulk Suspend | Jumlah baris Action `Suspend` sesudah aksi |
|---|---|---|
| PT Sinar Distributor {runId}-267 | Ya | baseline + 1 |
| PT Ganti Mitra {runId}-267 | Ya | baseline + 1 |
| PT Cahaya Baru | Tidak | baseline (tetap) |

- State global: log baru ditambahkan pada audit trail permanen; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-421 dan TC-AC-ACC-422: Log Suspend dan Unsuspend

1. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-421 dan 422" (langkah 1 sampai 12): klik menu Client di sidebar, lalu klik ikon Changelog di toolbar List
2. Ketik Search nama Client di modal, tekan Enter, ubah ukuran halaman menjadi 100, dan catat jumlah baris Action sesuai tabel (C0)
3. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search nama Client, tekan Enter, dan catat jumlah baris Action sesuai tabel (S0)
4. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search nama Client, tekan Enter, dan catat jumlah baris Action sesuai tabel (V0)
5. Klik menu Client di sidebar, lalu lakukan aksi sesuai kolom "Aksi"
6. Klik ikon Changelog di toolbar List, ketik Search nama Client di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
7. Verifikasi Changelog: Client memuat tepat 1 baris baru (jumlah = C0 + 1) dengan Action, Client Name sesuai kolom "Client", Field, Old Value, dan New Value sesuai tabel
8. Verifikasi Modified By baris baru itu adalah nama aktor A-01
9. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search nama Client, tekan Enter
10. Verifikasi System Log memuat baris baru (jumlah = S0 + 1) dengan Action, Object `Client`, Name sesuai kolom "Client", Field, Old Value, dan New Value sesuai tabel
11. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search nama Client, tekan Enter
12. Verifikasi Activity Log memuat baris baru (jumlah = V0 + 1) dengan Action, Object `Client`, Name sesuai kolom "Client", Field, Old Value, New Value sesuai tabel, dan Modified By nama aktor A-01
13. Pulihkan Client ke keadaan awal (Unsuspend "PT Sinar Distributor {runId}-267" untuk TC-AC-ACC-421, Suspend kembali "PT Suspend Uji Satu {runId}-267" untuk TC-AC-ACC-422)

### TC-AC-ACC-915: Bulk Suspend dua Client menulis tepat satu baris log per Client

14. Klik menu Client di sidebar, lalu klik ikon Changelog di toolbar List, dan ubah ukuran halaman modal menjadi 100
15. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-915" (langkah 15 sampai 16): ketik Search nama Client di modal, tekan Enter
16. Catat jumlah baris Action `Suspend` (N1 untuk PT Sinar Distributor {runId}-267, N2 untuk PT Ganti Mitra {runId}-267, N3 untuk PT Cahaya Baru)
17. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100
18. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-915" (langkah 18 sampai 19): ketik Search nama Client, tekan Enter
19. Catat jumlah baris Action `Suspend` (S1, S2, S3)
20. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100
21. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-915" (langkah 21 sampai 22): ketik Search nama Client, tekan Enter
22. Catat jumlah baris Action `Suspend` (V1, V2, V3)
23. Klik menu Client di sidebar, klik sub-tab Active, ketik Search "PT Sinar Distributor {runId}-267", tekan Enter, dan centang barisnya
24. Ganti isi Search dengan "PT Ganti Mitra {runId}-267", tekan Enter, dan centang barisnya
25. Pilih Bulk Action, pilih Suspend, lalu klik `[Suspend]` pada dialog
26. Klik ikon Changelog di toolbar List dan ubah ukuran halaman modal menjadi 100
27. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-915" (langkah 27 sampai 28): ketik Search nama Client di modal, tekan Enter
28. Verifikasi jumlah baris Action `Suspend` sesuai kolom "Jumlah baris Action `Suspend` sesudah aksi" terhadap baseline N1, N2, N3 (baris baru berisi Field `Status`, Old Value `Active`, New Value `Suspended` untuk dua Client terpilih)
29. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100
30. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-915" (langkah 30 sampai 31): ketik Search nama Client, tekan Enter
31. Verifikasi jumlah baris Action `Suspend`, Object `Client` pada System Log sesuai kolom "Jumlah baris Action `Suspend` sesudah aksi" terhadap baseline S1, S2, S3
32. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100
33. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-915" (langkah 33 sampai 34): ketik Search nama Client, tekan Enter
34. Verifikasi jumlah baris Action `Suspend`, Object `Client` pada Activity Log sesuai kolom "Jumlah baris Action `Suspend` sesudah aksi" terhadap baseline V1, V2, V3 (baris baru ber-Modified By nama aktor A-01)
35. Pulihkan "PT Sinar Distributor {runId}-267" dan "PT Ganti Mitra {runId}-267" ke Active lewat Bulk Unsuspend atau Unsuspend satu per satu

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-12): Search nama Client, ukuran halaman 100, dan baseline jumlah baris log (S-14); langkah 13 dan 35 (pemulihan Post Condition TC); klik menu Client di sidebar (kembali ke List dan mereset Search).
- Langkah 1 sampai 12 diulang 2 kali (24 langkah), langkah 15 sampai 16, 18 sampai 19, 21 sampai 22, 27 sampai 28, 30 sampai 31, dan 33 sampai 34 diulang 3 kali (36 langkah setelah ekspansi).
- Target aksi tulis (Suspend, Unsuspend, Bulk Suspend) memakai replika bersuffix `{runId}-267` (S-06); TC menulis Client literal fixture bersama (C-11, C-13, C-AST-14). Langkah pemulihan 13 dan 35 dipertahankan pada replika sebagai penutup alur Post Condition TC.
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua blok satu topik (pencatatan log aksi status Client) dengan akun yang sama dan pola baca tiga surface yang identik; tiap blok memakai Client sendiri dan memulihkan datanya sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- TC-AC-ACC-915 menyebut Client pembanding "PT Cahaya Baru" yang tidak dipilih dan Expected "tetap N3/S3/V3"; asersi jumlah dengan baseline bukan asersi absence kelas g (bagian 3 prinsip 13 butir g).
- Pembagian TC lintas spec: log Create/Edit/Change Partner di spec 266; log aksi sistem di spec 268; log Resend dan BYO di spec 269; log Asset Control di spec 270; log Delete di spec 271; "tidak ada baris log" di spec 272.
- Temuan untuk QA:
  - TC-AC-ACC-421 dan 422 tidak menyebut baseline; spec menambahkannya (S-12).
  - Nama tampil A-01 untuk asersi Modified By tidak tertulis di Pre-setup TC.
