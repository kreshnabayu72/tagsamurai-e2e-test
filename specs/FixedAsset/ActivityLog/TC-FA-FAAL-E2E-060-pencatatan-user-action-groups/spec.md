---
id: TC-FA-FAAL-E2E-060-pencatatan-user-action-groups
title: "Pencatatan User Action: Edit dan Delete Group serta Snapshot Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-235
  - TC-FA-FAAL-236
  - TC-FA-FAAL-252
  - TC-FA-FAAL-254
  - TC-FA-FAAL-285
coverage:
  web: automated
---

# Pencatatan User Action: Edit dan Delete Group serta Snapshot Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor dan observer: Total Control (Pre-setup #1, Admin Alpha), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log). Pengecualian: tiap TC membuka Settings > Groups untuk aksinya lalu Activity Log > User Action.
- Data Dinamis group (Data Dinamis #1, #2, #6; Pre-setup #20), identitas dari `Fixture.activity-log.<kunci>` (fixture belum ada, disediakan tim FE), seluruhnya milik spec ini:
  - Group `Lantai 3` di bawah `Gedung A` (TC-FA-FAAL-235 dan 252).
  - Group `Gedung E1`, `Gedung E2`, dan `Gedung E3` tanpa dependensi (TC-FA-FAAL-236).
  - Group `Gedung F` dengan Group Manager, Group Role, dan Transaction Role yang ter-assign (TC-FA-FAAL-254).
  - Group `Gedung I` tanpa dependensi (Pre-setup #20, TC-FA-FAAL-285).
- Data Tab User Action UA-01 sampai UA-15 (Pre-setup #12) tidak diubah spec ini.
- Baseline (S-12): total baris Tab User Action dibaca dari teks pagination `Showing x–y of N entries` pada awal tiap blok (langkah 1, 8, 15, 23, 31); tiap blok memverifikasi selisih terhadap total itu sebelum memverifikasi baris (eksak, kecuali TC-FA-FAAL-254 yang sedikitnya).
- State yang diubah dan pemulihannya: nama group `Lantai 3` dikembalikan ke `Lantai 3` pada langkah 7 dan di hook `after`; group yang dihapus (`Gedung E1`, `E2`, `E3`, `F`, `I1`) dibuat ulang oleh tim FE/BE di hook `before`.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun aktor.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Activity Log > User Action dan catat total baris dari teks pagination (N0)

### TC-FA-FAAL-235: Edit nama Group tercatat dengan path hierarki di Name

2. Ubah nama group `Lantai 3` menjadi `Lantai 3 - Renovasi` di Settings > Groups
3. Tunggu aksi selesai
4. Buka Activity Log > User Action
5. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): teks pagination menjadi total N0 + 1
6. Verifikasi baris baru di Tab User Action paling atas: Action `Edit`, Object `Groups`, Name `Gedung A > Lantai 3 - Renovasi`, Field `Group Name`, Old Value `Lantai 3`, New Value `Lantai 3 - Renovasi`, Modified By `Admin A`
7. Pulihkan nama group `Lantai 3 - Renovasi` menjadi `Lantai 3` lewat seed API

### TC-FA-FAAL-252: Baris lama tidak berubah setelah entitas diganti nama lagi

8. Catat total baris Tab User Action dari teks pagination (N1)
9. Ubah nama `Lantai 3` menjadi `Lantai 3 - Renovasi` di Settings > Groups
10. Ubah nama lagi menjadi `Lantai 3 - Final`
11. Tunggu aksi selesai
12. Buka Activity Log > User Action
13. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): teks pagination menjadi total N1 + 2
14. Verifikasi dua baris teratas Tab User Action memuat, tanpa urutan: baris Name `Gedung A > Lantai 3 - Final`, Old Value `Lantai 3 - Renovasi`, New Value `Lantai 3 - Final`; dan baris Name `Gedung A > Lantai 3 - Renovasi`, Old Value `Lantai 3`, New Value `Lantai 3 - Renovasi` (baris ini tidak berubah)

### TC-FA-FAAL-236: Bulk Delete Group menulis satu baris Delete per group

15. Catat total baris Tab User Action dari teks pagination (N2)
16. Pilih ketiga group `Gedung E1`, `Gedung E2`, dan `Gedung E3` di Settings > Groups dan lakukan Bulk Delete
17. Tunggu aksi selesai
18. Buka Activity Log > User Action
19. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): teks pagination menjadi total N2 + 3
20. Verifikasi baris baru dengan Action `Delete`, Object `Groups`, Name `Gedung E1`, Field `Group Name`, New Value `—`
21. Verifikasi baris baru dengan Action `Delete`, Object `Groups`, Name `Gedung E2`, Field `Group Name`, New Value `—`
22. Verifikasi baris baru dengan Action `Delete`, Object `Groups`, Name `Gedung E3`, Field `Group Name`, New Value `—`

### TC-FA-FAAL-254: Delete Group menulis tiga jenis entri pencabutan

23. Catat total baris Tab User Action dari teks pagination (N3)
24. Hapus group `Gedung F` di Settings > Groups dan konfirmasi dialog peringatan
25. Tunggu aksi selesai
26. Buka Activity Log > User Action
27. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): teks pagination menjadi total sedikitnya N3 + jumlah assignment seed Gedung F (Group Manager, Group Role, dan Transaction Role)
28. Verifikasi entri baru `Remove` dengan Object `Group Manager (Group Deleted)`, satu baris per assignment, Modified By `Admin A`
29. Verifikasi entri baru `Remove` dengan Object `Group Role`, satu baris per assignment, Modified By `Admin A`
30. Verifikasi entri baru `Remove` dengan Object `Transaction Role`, satu baris per assignment, Modified By `Admin A`

### TC-FA-FAAL-285: Baris Tab User Action lama tidak berubah setelah entitas dihapus

31. Catat total baris Tab User Action dari teks pagination (N4)
32. Ubah nama group `Gedung I` menjadi `Gedung I1` di Settings > Groups
33. Hapus group `Gedung I1` dan konfirmasi dialog
34. Tunggu aksi selesai
35. Buka Activity Log > User Action
36. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): teks pagination menjadi total N4 + 2
37. Verifikasi dua baris teratas Tab User Action memuat, tanpa urutan: baris `Delete` dengan Name `Gedung I1`, Field `Group Name`, New Value `—`; dan baris `Edit` dengan Name `Gedung I1`, Old Value `Gedung I`, New Value `Gedung I1` (tidak berubah setelah entitas dihapus)

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung "Tunggu aksi selesai" (S-03, 8b.8, tanpa Verifikasi): langkah 3, 11, 17, 25, 34; ditulis sebelum tiap pembukaan Activity Log > User Action yang mengikuti aksi tulis tanpa asersi di antaranya. Verifikasi polling tetap menunggu commit log.
- Spec di atas 35 langkah karena 5 langkah penghubung "Tunggu aksi selesai"; spec memuat lima TC berurutan; satu-satunya ketergantungan antar TC adalah TC-FA-FAAL-252 yang bergantung pada pemulihan nama group `Lantai 3` dari TC-FA-FAAL-235 (TC-FA-FAAL-236, 254, dan 285 memakai group masing-masing), sehingga dipertahankan dalam satu spec (37 langkah, 32 tanpa langkah penghubung tunggu).
- Urutan TC: 235, 252, 236, 254, 285. TC-FA-FAAL-252 mengikuti TC-FA-FAAL-235 pada group `Lantai 3` yang sama; langkah 7 memulihkan nama group sebelum TC-FA-FAAL-252 mengandalkannya (S-09).
- Langkah penghubung (S-03): langkah 1, 4, 12, 18, 26, 35 (membuka Tab User Action), langkah 7 (pemulihan nama group), langkah 8, 15, 23, 31 (mencatat total awal blok, N1 sampai N4).
- Baseline S-12: tiap blok mencatat total awal (N0 pada langkah 1, N1 sampai N4 pada langkah 8, 15, 23, 31) dan Verifikasi selisih mendahului Verifikasi baris: +1 untuk TC-FA-FAAL-235, +2 untuk TC-FA-FAAL-252 (dua rename), +3 untuk TC-FA-FAAL-236 (satu baris Delete per group), +2 untuk TC-FA-FAAL-285 (Edit lalu Delete). Untuk TC-FA-FAAL-254 Delete Group menulis baris pencabutan tambahan, sehingga selisih diasersi sedikitnya sejumlah assignment seeding Gedung F (disediakan tim FE/BE). Langkah pemulihan nama group lewat seed API diasumsikan tidak menulis baris log.
- Langkah 28 sampai 30 memecah Expected TC-FA-FAAL-254 per jenis entri; asersi "satu baris per assignment" dibaca dari jumlah assignment seeding Gedung F.
- Cara baca TC-FA-FAAL-252 dan 285 (S-14): dua entri yang ditulis berurutan dapat jatuh dalam menit yang sama pada kolom Date, sehingga urutan di antaranya tidak dijamin. Setelah Verifikasi total N1 + 2 (langkah 13) dan N4 + 2 (langkah 36) membuktikan selisih, spec mengasersi himpunan dua baris teratas tanpa mengandalkan urutan (langkah 14 dan 37), sesuai Expected TC.
- Tiap Verifikasi selisih memakai idiom polling (muat ulang Tab User Action tiap 5 detik, batas 2 menit) sebagai pengganti langkah tunggu tersendiri.
- R-14: Modified By diasersi `Admin A` (First Name dan Last Initial).
- Temuan untuk QA:
  - TC-FA-FAAL-235 dan 252 memakai nama literal group `Lantai 3` tanpa suffix per run; baris log immutable sehingga run berikutnya menambah baris dengan nama yang sama dan asersi baris teratas hanya dipakai sesudah Verifikasi selisih total.
  - TC-FA-FAAL-254 tidak menyebut jumlah assignment per jenis di Gedung F; asersi "satu baris per assignment" membutuhkan jumlah dari seeding.
  - TC-FA-FAAL-236 Expected tidak menyebut Modified By dan Old Value; spec tidak menambah asersi itu.
  - TC-FA-FAAL-285 butir a menyebut baris `Delete` tanpa Old Value; spec mengikuti Expected TC.
