---
id: TC-AC-ACC-E2E-270-pencatatan-log-generate-enrollment-qr-deactivate-station-dan-revoke-tablet-di-tiga-surface
title: "Pencatatan Log Generate Enrollment QR, Deactivate Station, dan Revoke Tablet di Changelog Asset Control, System Log, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-427
  - TC-AC-ACC-910
  - TC-AC-ACC-911
coverage:
  web: automated
---

# Pencatatan Log Generate Enrollment QR, Deactivate Station, dan Revoke Tablet di Changelog Asset Control, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Nama tampil A-01 tidak tertulis di Pre-setup TC (disediakan tim FE). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Tiga surface pembaca log: Changelog Asset Control (ikon Changelog di Tab Asset Control; kolom Date, Action, Object, Field, Old Value, New Value, Modified By), System Log akun aktor (Settings > User > Detail akun aktor > Tab System Log; kolom Date, Action, Object, Name, Field, Old Value, New Value, tanpa Modified By), Activity Log Admin Console (Tab User Action; kolom sama dengan System Log ditambah Modified By, disaring Object sesuai tabel).
- Data fixture Tabel A3 (skrip seed, bukan lewat UI; Deactivate dan Revoke permanen sehingga di-seed ulang lewat reset data uji): C-AST-8 "PT Uji Token QR" (SFR "Reader Token 1" bertipe Asset Control tanpa station aktif; tanpa token Enrollment QR Active; TC-AC-ACC-427); C-AST-7 "PT Uji Aksi Asset Control" dengan Station Active "Stasiun Log Deactivate" berisi Tablet "Tablet Log Deactivate 1" Active (TC-AC-ACC-910) dan Station Active "Stasiun Tablet Uji" berisi Tablet Active "Tablet Log Revoke" (TC-AC-ACC-911).
- Kemampuan teknis: jam server uji dapat dimajukan (token Active hasil TC-AC-ACC-427 dikembalikan ke Expired dengan memajukan jam server 15 menit di langkah 34 dan di hook `after`; jam dipulihkan).
- Sesi UI dan sesi API aktor tetap valid selama jam digeser (suite.md > Kemampuan teknis > Sesi tetap valid saat jam digeser)
- Baseline (S-12): jumlah baris log pada tiap surface dicatat dengan Search dan Action sebelum aksi, ukuran halaman 100; asersi "baris baru" memakai selisih terhadap baseline. Kolom Date tidak diasersi (Expected TC tidak menyebutnya).
- Parameter blok TC-AC-ACC-427 dan 911 (langkah 1 sampai 13):

| TC | Client | Aksi | Action | Object (Changelog Asset Control) | Object (System Log dan Activity Log) | Name (System Log dan Activity Log) | Old Value | New Value |
|---|---|---|---|---|---|---|---|---|
| TC-AC-ACC-427 | PT Uji Token QR | Klik Tab Asset Control, klik `[Generate Enrollment QR]`, pastikan SFR "Reader Token 1" otomatis terpilih dan QR tampil, klik `[Close]` | `Generate Enrollment QR` | `Enrollment Token` | `Enrollment Token` | `PT Uji Token QR / Reader Token 1` | `—` | `Active` |
| TC-AC-ACC-911 | PT Uji Aksi Asset Control | Klik Tab Asset Control, expand "Stasiun Tablet Uji", buka ⋯ "Tablet Log Revoke" dan pilih Revoke, klik `[Revoke]` pada dialog | `Revoke Tablet` | `Tablet Log Revoke` | `Tablet` | `Tablet Log Revoke` | `Active` | `Revoked` |

- State global: jam server dimajukan lalu dipulihkan; log baru ditambahkan pada audit trail permanen; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List dan Detail diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-427 dan TC-AC-ACC-911: Log Generate Enrollment QR dan Revoke Tablet

1. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-427 dan 911" (langkah 1 sampai 13): klik menu Client di sidebar, ketik Search nama Client, tekan Enter, klik Company Name hasilnya, klik Tab Asset Control, lalu klik ikon Changelog di Tab Asset Control
2. Ketik Search Action sesuai tabel di modal, tekan Enter, ubah ukuran halaman menjadi 100, dan catat jumlah baris Action itu (C0)
3. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search Name sesuai tabel, tekan Enter, dan catat jumlah baris Action itu (S0)
4. Buka Activity Log Admin Console (Tab User Action), saring Object sesuai kolom "Object (System Log dan Activity Log)", ubah ukuran halaman menjadi 100, ketik Search Name sesuai tabel, tekan Enter, dan catat jumlah baris Action itu (V0)
5. Buka Detail Client lagi lewat menu Client di sidebar dan Search nama Client, lalu lakukan aksi sesuai kolom "Aksi"
6. Klik ikon Changelog di Tab Asset Control, ketik Search Action sesuai tabel di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
7. Verifikasi Changelog Asset Control memuat tepat 1 baris baru (jumlah = C0 + 1) dengan Action, Object (kolom "Object (Changelog Asset Control)"), Field `Status`, Old Value, dan New Value sesuai tabel
8. Verifikasi Modified By baris baru itu adalah nama aktor A-01
9. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search Name sesuai tabel, tekan Enter
10. Verifikasi System Log memuat baris baru (jumlah = S0 + 1) dengan Action, Object (kolom "Object (System Log dan Activity Log)"), Name, Field `Status`, Old Value, dan New Value sesuai tabel
11. Buka Activity Log Admin Console (Tab User Action), saring Object sesuai kolom "Object (System Log dan Activity Log)", ubah ukuran halaman menjadi 100, ketik Search Name sesuai tabel, tekan Enter
12. Verifikasi Activity Log memuat baris baru (jumlah = V0 + 1) dengan Action, Object, Name, Field `Status`, Old Value, dan New Value sesuai tabel
13. Verifikasi Modified By baris Activity Log itu adalah nama aktor A-01
14. (rujukan nomor langkah berakhir di langkah 13; blok diulang untuk baris tabel berikutnya)

### TC-AC-ACC-910: Log Deactivate Station dan cascade tablet

15. Klik menu Client di sidebar, ketik Search "PT Uji Aksi Asset Control", tekan Enter, klik Company Name hasilnya, klik Tab Asset Control, lalu klik ikon Changelog di Tab Asset Control
16. Ketik Search "Stasiun Log Deactivate" di modal, tekan Enter, ubah ukuran halaman menjadi 100, dan catat jumlah baris Action `Deactivate Station` (C1); ganti isi Search dengan "Tablet Log Deactivate 1" dan catat jumlah baris Action `Revoke Tablet` (R1)
17. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search "Stasiun Log Deactivate", tekan Enter, dan catat jumlah baris Action `Deactivate Station` (S1)
18. Buka Activity Log Admin Console (Tab User Action), saring Object `Station`, ubah ukuran halaman menjadi 100, ketik Search "Stasiun Log Deactivate", tekan Enter, dan catat jumlah baris Action `Deactivate Station` (V1)
19. Buka Detail "PT Uji Aksi Asset Control" lewat menu Client di sidebar, klik Tab Asset Control, buka ⋯ pada "Stasiun Log Deactivate" dan pilih Deactivate
20. Klik `[Deactivate]` pada dialog
21. Klik ikon Changelog di Tab Asset Control, ketik Search "Stasiun Log Deactivate" di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
22. Verifikasi Changelog Asset Control memuat tepat 1 baris baru (jumlah = C1 + 1): Action `Deactivate Station`, Object `Stasiun Log Deactivate`, Field `Status`, Old Value `Active`, New Value `Deactivated`
23. Verifikasi Modified By baris baru itu adalah nama aktor A-01
24. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search "Stasiun Log Deactivate", tekan Enter
25. Verifikasi System Log memuat baris baru (jumlah = S1 + 1): Action `Deactivate Station`, Object `Station`, Name `Stasiun Log Deactivate`, Field `Status`, Old Value `Active`, New Value `Deactivated`
26. Buka Activity Log Admin Console (Tab User Action), saring Object `Station`, ubah ukuran halaman menjadi 100, ketik Search "Stasiun Log Deactivate", tekan Enter
27. Verifikasi Activity Log memuat baris baru (jumlah = V1 + 1): Action `Deactivate Station`, Object `Station`, Name `Stasiun Log Deactivate`, Field `Status`, Old Value `Active`, New Value `Deactivated`
28. Verifikasi Modified By baris Activity Log itu adalah nama aktor A-01
29. Kembali ke Tab Asset Control "PT Uji Aksi Asset Control" lewat menu Client di sidebar dan Search nama Client, lalu klik row "Stasiun Log Deactivate" untuk expand Tablet List
30. Verifikasi "Tablet Log Deactivate 1" berbadge `Revoked`
31. Klik ikon Changelog di Tab Asset Control, ketik Search "Tablet Log Deactivate 1" di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
32. Verifikasi jumlah baris Action `Revoke Tablet` tetap R1 (cascade tercakup baris `Deactivate Station`, bagian 8.1b PRD)
33. Tutup modal

### Pemulihan token Active hasil TC-AC-ACC-427

34. Majukan jam server uji 15 menit hingga token Active hasil TC-AC-ACC-427 menjadi Expired, lalu pulihkan jam server dan jam browser

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-12): Search nama Client, ukuran halaman 100, dan baseline jumlah baris log pada audit trail permanen (S-14; ketiga TC tidak mencatat baseline); langkah 34 (memulihkan token Active menjadi Expired mengikuti Post Condition TC-AC-ACC-427); klik menu Client di sidebar (kembali ke List dan mereset Search).
- Langkah 1 sampai 13 diulang 2 kali (26 langkah setelah ekspansi).
- Spec ini melewati sekitar 35 langkah setelah ekspansi. Alasan: semua blok satu topik (pencatatan log aksi Asset Control) dengan akun yang sama dan pola baca tiga surface yang identik; tiap blok memakai Station, Tablet, atau Client sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: Deactivate/Revoke tanpa pembacaan log di spec 238 dan 239; Generate di spec 234; log Create/Edit/Change Partner di spec 266; log Suspend/Unsuspend di spec 267; log aksi sistem di spec 268; log Resend dan BYO di spec 269; log Delete di spec 271.
- Temuan untuk QA:
  - TC-AC-ACC-910 dan 911 Post Condition a ("Global Settings (modul hardware-asset-control-station) mencatat Deactivate Station / Revoke Tablet pada sisinya") tidak punya langkah observasi di TC sehingga tidak diasersi.
  - TC-AC-ACC-427 menyebut System Log Name `PT Uji Token QR / Reader Token 1` tanpa menyebut format pemisah " / "; spec mengasersi teks apa adanya.
  - Nama tampil A-01 untuk asersi Modified By tidak tertulis di Pre-setup TC.
