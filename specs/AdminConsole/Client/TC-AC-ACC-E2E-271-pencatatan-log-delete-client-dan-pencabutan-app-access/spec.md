---
id: TC-AC-ACC-E2E-271-pencatatan-log-delete-client-dan-pencabutan-app-access
title: "Pencatatan Log Delete Client di Tiga Surface dan Pencabutan App Access Tercatat Terpisah di System Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-425
  - TC-AC-ACC-429
coverage:
  web: automated
---

# Pencatatan Log Delete Client di Tiga Surface dan Pencabutan App Access Tercatat Terpisah di System Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Nama tampil A-01 tidak tertulis di Pre-setup TC (disediakan tim FE). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Tiga surface pembaca log: Changelog: Client (ikon Changelog di toolbar List; kolom Date, Action, Client Name, Field, Old Value, New Value, Modified By), System Log akun aktor (Settings > User > Detail akun aktor > Tab System Log; kolom Date, Action, Object, Name, Field, Old Value, New Value, tanpa Modified By), Activity Log Admin Console (Tab User Action, disaring Object `Client`; kolom sama dengan System Log ditambah Modified By).
- Data seed milik spec (replika bersuffix `{runId}-271` dengan atribut setara fixture A3 asal TC; di-seed lewat skrip seed atau Fixture BE di hook `before`, bukan lewat UI, dan dihapus di hook `after` bila masih ada; kemampuan disediakan tim FE/BE; S-06; Delete adalah soft-delete permanen dari UI sehingga tiap run memakai replika baru): `PT Hapus Uji Log {runId}-271` (setara C-AST-10: Active; Direct; Group Area Jakarta; tanpa riwayat subscription; Default User tanpa App Access; TC-AC-ACC-425); `PT App Access Hapus {runId}-271` (setara C-ISO-13: Archived; FAMS Archive; satu user ber-App Access FAMS (Default User) tanpa peran di entitas lain; Partner CV Mitra Sejati; Group Area Jakarta; TC-AC-ACC-429). Nama Client unik sehingga baseline log bernilai nol, tetap dicatat (S-12).
- Baseline (S-12): jumlah baris log pada tiap surface dicatat dengan Search nama Client dan Action sebelum aksi, ukuran halaman 100; asersi "baris baru" memakai selisih terhadap baseline. Kolom Date tidak diasersi (Expected TC tidak menyebutnya).
- State global: log baru ditambahkan pada audit trail permanen; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-425: Log Delete tercatat di tiga surface

1. Klik ikon Changelog di toolbar List, ketik Search "PT Hapus Uji Log {runId}-271" di modal, tekan Enter, ubah ukuran halaman menjadi 100, catat jumlah baris Action `Delete` (C0), lalu tutup modal
2. Buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search "PT Hapus Uji Log {runId}-271", tekan Enter, dan catat jumlah baris Action `Delete` (S0)
3. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search "PT Hapus Uji Log {runId}-271", tekan Enter, dan catat jumlah baris Action `Delete` (V0)
4. Klik menu Client di sidebar, ketik Search "PT Hapus Uji Log {runId}-271", tekan Enter
5. Buka ⋯ baris "PT Hapus Uji Log {runId}-271" lalu pilih Delete
6. Ketik "PT Hapus Uji Log {runId}-271" pada input "Type the client name to confirm" dan centang "I understand this action cannot be undone"
7. Klik `[Delete]`
8. Klik ikon Changelog di toolbar List, ketik Search "PT Hapus Uji Log {runId}-271" di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
9. Verifikasi Changelog: Client memuat tepat 1 baris baru (jumlah = C0 + 1): Action `Delete`, Client Name `PT Hapus Uji Log {runId}-271`, Field `Company Name`, Old Value `PT Hapus Uji Log {runId}-271`, New Value `—`
10. Verifikasi Modified By baris baru itu adalah nama aktor A-01
11. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search "PT Hapus Uji Log {runId}-271", tekan Enter
12. Verifikasi System Log memuat baris baru (jumlah = S0 + 1): Action `Delete`, Object `Client`, Name `PT Hapus Uji Log {runId}-271`, Field `Company Name`, Old Value `PT Hapus Uji Log {runId}-271`, New Value `—`
13. Verifikasi System Log tidak memiliki kolom Modified By
14. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search "PT Hapus Uji Log {runId}-271", tekan Enter
15. Verifikasi Activity Log memuat baris baru (jumlah = V0 + 1): Action `Delete`, Object `Client`, Name `PT Hapus Uji Log {runId}-271`, Field `Company Name`, Old Value `PT Hapus Uji Log {runId}-271`, New Value `—`
16. Verifikasi Modified By baris Activity Log itu adalah nama aktor A-01

### TC-AC-ACC-429: Delete mencabut App Access dicatat terpisah di System Log Settings > User

17. Buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search `App Access — FAMS`, tekan Enter, dan catat jumlah baris Object `User`, Field `App Access — FAMS`, Old Value `Active`, New Value `—` (A0)
18. Klik menu Client di sidebar, klik sub-tab Archived, ketik Search "PT App Access Hapus {runId}-271", tekan Enter
19. Buka ⋯ baris "PT App Access Hapus {runId}-271" lalu pilih Delete
20. Ketik nama Client persis pada input konfirmasi dan centang checkbox "I understand this action cannot be undone"
21. Klik `[Delete]`
22. Tunggu aksi selesai (Delete Client)
23. Buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search `App Access — FAMS`, tekan Enter
24. Verifikasi System Log memuat baris baru (jumlah = A0 + 1): Object `User`, Field `App Access — FAMS`, Old Value `Active`, New Value `—`

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-12): langkah 1 sampai 4, 8, 11, 14, 17, 18, 22 dan 23 (Search nama Client, ukuran halaman 100, dan baseline jumlah baris log pada audit trail permanen, S-14; TC-AC-ACC-425 dan 429 tidak mencatat baseline; Search `App Access — FAMS` membatasi baris System Log).
- Aksi hapus memakai replika bersuffix `{runId}-271` (S-06), bukan fixture A3 C-AST-10 dan C-ISO-13. Baseline A0 pada langkah 17 membaca System Log dengan Search `App Access — FAMS` yang tidak terikat nama Client sehingga tetap dicatat sebagai selisih.
- Urutan TC: kedua TC menghapus Client (aksi yang menghabisi data); tiap TC memakai Client sendiri sehingga tidak ada kasus lain yang butuh baris yang dihapus (prinsip 3 butir 5 terpenuhi).
- Pembagian TC lintas spec: log Create/Edit/Change Partner di spec 266; log Suspend/Unsuspend/Bulk di spec 267; log aksi sistem di spec 268; log Resend dan BYO di spec 269; log Asset Control di spec 270; "tidak ada baris log" di spec 272.
- Temuan untuk QA:
  - TC-AC-ACC-429 menyebut "Type the client name to confirm" tanpa label tombol konfirmasi dan memuat Name pada baris System Log `User`; Name baris itu (nama user ber-App Access) tidak disebut sehingga tidak diasersi. TC-AC-ACC-429 tidak menyebut pelaku Delete di Admin Console (diasumsikan A-01).
  - TC-AC-ACC-425 dan 429 Post Condition ("Fixture ... dipulihkan lewat reset data uji") ditutup lewat replika per run yang di-seed Fixture BE (disediakan tim FE/BE); tidak ada langkah UI pemulihan.
  - Nama tampil A-01 untuk asersi Modified By tidak tertulis di Pre-setup TC.
