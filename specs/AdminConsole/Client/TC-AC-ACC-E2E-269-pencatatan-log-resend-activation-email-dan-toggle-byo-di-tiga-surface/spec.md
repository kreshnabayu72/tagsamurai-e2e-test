---
id: TC-AC-ACC-E2E-269-pencatatan-log-resend-activation-email-dan-toggle-byo-di-tiga-surface
title: "Pencatatan Log Resend Activation Email dan Toggle BYO Enabled dan Disabled di Changelog Client, System Log, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-426
  - TC-AC-ACC-428
  - TC-AC-ACC-912
coverage:
  web: automated
---

# Pencatatan Log Resend Activation Email dan Toggle BYO Enabled dan Disabled di Changelog Client, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Nama tampil A-01 tidak tertulis di Pre-setup TC (disediakan tim FE). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Tiga surface pembaca log: Changelog: Client (ikon Changelog di toolbar List; kolom Date, Action, Client Name, Field, Old Value, New Value, Modified By), System Log akun aktor (Settings > User > Detail akun aktor > Tab System Log; kolom Date, Action, Object, Name, Field, Old Value, New Value, tanpa Modified By), Activity Log Admin Console (Tab User Action, disaring Object `Client`; kolom sama dengan System Log ditambah Modified By).
- Data Pre-setup yang diubah efeknya (TC-AC-ACC-426): C-02 "PT Teknologi Maju" (Active; Default User Not Yet Activated dengan email `dewi.lestari@ptteknologimaju.test`; term FAMS Grace). Aksi Resend mengirim email dan tidak mengubah data Client lain.
- Data fixture Tabel A3 (skrip seed; dipulihkan lewat langkah dan reset data uji): C-AST-12 "PT Uji BYO" (Active; toggle "Allow Self-Purchased Device Activation" Disabled; satu device Jalur B "Handheld BYO Uji" sudah teraktivasi di Global Settings > Hardware) untuk TC-AC-ACC-428 dan 912.
- Baseline (S-12): jumlah baris log pada tiap surface dicatat dengan Search nama Client dan Action sebelum aksi, ukuran halaman 100; asersi "baris baru" memakai selisih terhadap baseline. Kolom Date tidak diasersi (Expected TC tidak menyebutnya).
- Parameter blok TC-AC-ACC-426 dan 428 (langkah 1 sampai 12):

| TC | Client | Aksi | Action | Field | Old Value | New Value |
|---|---|---|---|---|---|---|
| TC-AC-ACC-426 | PT Teknologi Maju | Search, klik Company Name "PT Teknologi Maju", klik `[Resend Activation Email]`, klik breadcrumb Client | `Resend Activation Email` | `Email` | `—` | `dewi.lestari@ptteknologimaju.test` |
| TC-AC-ACC-428 | PT Uji BYO | Search, klik Company Name "PT Uji BYO", geser toggle "Allow Self-Purchased Device Activation" ke Enabled, klik `[Enable]` pada dialog, klik breadcrumb Client | `Edit` | `Allow Self-Purchased Device Activation` | `Disabled` | `Enabled` |

- State global: log baru ditambahkan pada audit trail permanen; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-426 dan TC-AC-ACC-428: Log Resend Activation Email dan toggle BYO ke Enabled

1. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-426 dan 428" (langkah 1 sampai 12): klik menu Client di sidebar, klik ikon Changelog di toolbar List, ketik Search nama Client di modal, tekan Enter, ubah ukuran halaman menjadi 100, dan catat jumlah baris Action sesuai tabel (C0)
2. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search nama Client, tekan Enter, dan catat jumlah baris Action sesuai tabel (S0)
3. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search nama Client, tekan Enter, dan catat jumlah baris Action sesuai tabel (V0)
4. Klik menu Client di sidebar, lalu lakukan aksi sesuai kolom "Aksi"
5. Klik ikon Changelog di toolbar List, ketik Search nama Client di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
6. Verifikasi Changelog: Client memuat tepat 1 baris baru (jumlah = C0 + 1) dengan Action, Field, Old Value, dan New Value sesuai tabel serta Client Name sesuai kolom "Client"
7. Verifikasi Modified By baris baru itu adalah nama aktor A-01
8. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search nama Client, tekan Enter
9. Verifikasi System Log memuat baris baru (jumlah = S0 + 1) dengan Action, Object `Client`, Name sesuai kolom "Client", Field, Old Value, dan New Value sesuai tabel
10. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search nama Client, tekan Enter
11. Verifikasi Activity Log memuat baris baru (jumlah = V0 + 1) dengan Action, Object `Client`, Name sesuai kolom "Client", Field, Old Value, dan New Value sesuai tabel
12. Verifikasi Modified By baris Activity Log itu adalah nama aktor A-01
13. Pulihkan Client ke keadaan awal (geser toggle "Allow Self-Purchased Device Activation" "PT Uji BYO" kembali ke Disabled untuk TC-AC-ACC-428; TC-AC-ACC-426 tidak punya pemulihan)

### TC-AC-ACC-912: Log toggle BYO ke Disabled

14. Klik menu Client di sidebar, klik ikon Changelog di toolbar List, ketik Search "PT Uji BYO" di modal, tekan Enter, ubah ukuran halaman menjadi 100, dan catat jumlah baris Action `Edit` dengan Field `Allow Self-Purchased Device Activation`, Old Value `Enabled`, New Value `Disabled` (N0)
15. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search "PT Uji BYO", tekan Enter, dan catat jumlah baris yang sama (S0)
16. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search "PT Uji BYO", tekan Enter, dan catat jumlah baris yang sama (V0)
17. Klik menu Client di sidebar, ketik Search "PT Uji BYO", tekan Enter, lalu buka Detail "PT Uji BYO"
18. Geser toggle "Allow Self-Purchased Device Activation" ke Enabled lalu klik `[Enable]`
19. Geser toggle ke Disabled
20. Verifikasi tidak ada dialog yang tampil
21. Verifikasi toast sukses: "Success, self-purchased device activation setting has been updated."
22. Klik breadcrumb "Client" untuk kembali ke List
23. Klik ikon Changelog di toolbar List, ketik Search "PT Uji BYO" di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
24. Verifikasi jumlah baris Action `Edit` dengan Field `Allow Self-Purchased Device Activation`, Old Value `Enabled`, New Value `Disabled` = N0 + 1 (tepat 1 baris baru), Client Name `PT Uji BYO`
25. Verifikasi Modified By baris baru itu adalah nama aktor A-01
26. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search "PT Uji BYO", tekan Enter
27. Verifikasi System Log memuat baris baru (jumlah = S0 + 1): Action `Edit`, Object `Client`, Name `PT Uji BYO`, Field `Allow Self-Purchased Device Activation`, Old Value `Enabled`, New Value `Disabled`
28. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search "PT Uji BYO", tekan Enter
29. Verifikasi Activity Log memuat baris baru (jumlah = V0 + 1): Action `Edit`, Object `Client`, Name `PT Uji BYO`, Field `Allow Self-Purchased Device Activation`, Old Value `Enabled`, New Value `Disabled`
30. Verifikasi Modified By baris Activity Log itu adalah nama aktor A-01

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-12): Search nama Client, ukuran halaman 100, dan baseline jumlah baris log pada audit trail permanen (S-14; TC-AC-ACC-426, 428, dan 912 hanya TC-AC-ACC-912 mencatat baseline); langkah 13 (pemulihan Post Condition TC-AC-ACC-428); klik menu Client di sidebar (kembali ke List dan mereset Search).
- Langkah 1 sampai 12 diulang 2 kali (24 langkah setelah ekspansi).
- TC-AC-ACC-912 langkah 3 menggeser toggle ke Enabled sebelum Disabled (menghasilkan baris Enabled tambahan di log); baseline N0 hanya menghitung baris Disabled sehingga tidak terpengaruh. Dialog `[Enable]` dan toast sukses toggle Disabled diasersi sesuai Expected d.
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua blok satu topik (pencatatan log aksi Client) dengan akun yang sama dan pola baca tiga surface yang identik; tiap blok memakai Client sendiri dan memulihkan datanya sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: log Create/Edit/Change Partner di spec 266; log Suspend/Unsuspend/Bulk di spec 267; log aksi sistem di spec 268; log Asset Control di spec 270; log Delete di spec 271.
- Temuan untuk QA:
  - TC-AC-ACC-426 Precondition menyebut Default User "Not Yet Activated" dengan term FAMS Grace tanpa batas jumlah Resend (cooldown atau kuota harian); bila cooldown berlaku di environment, aksi Resend berulang dapat ditolak.
  - Nama tampil A-01 untuk asersi Modified By tidak tertulis di Pre-setup TC.
