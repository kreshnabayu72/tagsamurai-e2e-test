---
id: TC-FA-RP-E2E-337-assign-total-control-ke-user-standard-pemegang-peran-tangga-lama
title: "Assign Total Control ke user Standard pemegang peran tangga lama: peran lama diganti baris pola tanpa duplikat"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-1147
coverage:
  web: automated
---

# Assign Total Control ke user Standard pemegang peran tangga lama: peran lama diganti baris pola tanpa duplikat

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #15 (kolam pengguna Standard; Budi Santoso sebagai target), #18 (pohon group Company Alpha), #19 (seed Role Transaksi dan baris pola Transaction Role).
- Precondition TC (dipakai sebagai precondition, tidak diasersi): Budi Santoso memegang Staff pada `Transfer` di `IT Infrastructure` dan Approver pada `Disposal` di `Data Center`, dibuat lewat seeding API di hook `before`.
- Seeding dan pemulihan: Budi Santoso dipulihkan ke state Pre-setup (Standard dengan peran tangga lama yang dibuat seeding) di hook `after` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Kemampuan baca Changelog (baseline jumlah entri) memakai modal Changelog sub-tab `Transfer`; Changelog adalah audit trail permanen sehingga jumlah entri dicatat sebagai baseline sebelum aksi dan tidak diasersi sebagai angka absolut (S-12).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor"). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1147: Assign Total Control ke user Standard pemegang peran tangga lama: peran lama diganti baris pola tanpa duplikat

1. Klik Tab `Transaction Role`
2. Klik sub-tab `Transfer`
3. Klik node `IT Infrastructure` di Sidebar Group Tree
4. Klik ikon `[Changelog]` di baris sub-tab
5. Catat jumlah entri Changelog sub-tab `Transfer` sebagai baseline
6. Tutup modal Changelog dengan `[×]`
7. Klik Tab `Total Control`
8. Klik `[+ Assign]` di Tab Total Control
9. Centang Budi Santoso
10. Klik `[Assign]`
11. Verifikasi tidak ada dialog tambahan
12. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.`
13. Klik Tab `Transaction Role`
14. Klik sub-tab `Transfer`
15. Klik node `IT Infrastructure` di Sidebar Group Tree
16. Verifikasi section Asset Admin memuat Budi Santoso
17. Verifikasi section Approver memuat Budi Santoso
18. Verifikasi section Staff tidak memuat Budi Santoso
19. Klik sub-tab `Disposal`
20. Klik node `Data Center` di Sidebar Group Tree
21. Ketik Search `Budi Santoso` pada section Approver, tekan Enter
22. Verifikasi section Approver memuat tepat satu baris Budi Santoso (tidak ada duplikat)
23. Klik `(←)` pada kotak Search section Approver
24. Klik sub-tab `Transfer`
25. Klik ikon `[Changelog]` di baris sub-tab
26. Verifikasi jumlah entri Changelog bertambah dari baseline langkah 5
27. Verifikasi Changelog memuat entri `Remove` Staff disusul entri `Assign` Asset Admin untuk Budi Santoso (dua entri berurutan)
28. Tutup modal Changelog dengan `[×]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 28 langkah.
- Langkah penghubung (S-03): langkah 1 sampai 6 (pencatatan baseline Changelog), 7, 13 sampai 15, 19, 20, 23, 24, 25 dan 28 (pindah tab, sub-tab, node; menutup modal; membersihkan Search). Akun aktor pertama sudah login di hook `before` (S-07).
- Search untuk menemukan baris target (R-16): langkah 21.
- Urutan Expected b TC disusun mengikuti anchor absence (8b.2): `Verifikasi` section Asset Admin dan Approver memuat Budi Santoso (langkah 16 dan 17) ditulis sebelum `Verifikasi` section Staff tidak memuat (langkah 18). Langkah 11 (tidak ada dialog tambahan) ditulis segera setelah pemicu `[Assign]` dan sebelum toast sukses yang menjadi anchor positifnya (8b.11).
- Langkah 26 dan 27 membaca Changelog: baris entri dibaca sebagai himpunan entri teratas sesudah selisih dari baseline dibuktikan, tanpa mengandalkan urutan di antara entri se-menit (S-14); entri `Remove` Staff dan `Assign` Asset Admin untuk Budi Santoso dicari di antara entri baru itu.
- Post Condition TC-FA-RP-1147 ("peran tangga lama tidak tersisa pada user baru bertingkat Total Control") diasersi oleh Expected b, c, dan d; tidak ada asersi tambahan.
- Temuan untuk QA:
  - TC-FA-RP-1147 Expected d menyebut "dua entri berurutan" tanpa jumlah entri Changelog keseluruhan. Assign Total Control menulis entri `Assign` per baris pola (lihat TC-FA-RP-1163), sehingga selisih jumlah entri jauh lebih dari dua; spec hanya mengasersi bahwa jumlah bertambah dan kedua entri ada.
  - TC-FA-RP-1147 langkah 5 menyebut "Changelog sub-tab `Transfer`" tanpa menyebut node; spec membuka Changelog dari baris sub-tab dan mengasumsikan modal itu mencakup semua node sub-tab itu.
  - TC-FA-RP-1147 Precondition d menyebut Staff `Transfer` di `IT Infrastructure` dan Approver `Disposal` di `Data Center`, sedangkan Pre-setup #19 menyebut `Data Center` tanpa penugasan manual; kedua penugasan itu dibuat lewat seeding sebagai precondition TC.
  - TC-FA-RP-1147 tidak menyatakan client; spec memakai Company Alpha (akun default suite) karena hanya memakai sub-tab `Transfer` dan `Disposal`.
