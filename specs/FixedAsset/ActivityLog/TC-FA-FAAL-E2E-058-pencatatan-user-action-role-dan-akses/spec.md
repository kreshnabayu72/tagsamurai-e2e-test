---
id: TC-FA-FAAL-E2E-058-pencatatan-user-action-role-dan-akses
title: "Pencatatan User Action: Assign dan Remove Role serta Access Level"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-221
  - TC-FA-FAAL-222
  - TC-FA-FAAL-223
  - TC-FA-FAAL-224
  - TC-FA-FAAL-225
  - TC-FA-FAAL-226
  - TC-FA-FAAL-227
  - TC-FA-FAAL-228
  - TC-FA-FAAL-229
  - TC-FA-FAAL-230
coverage:
  web: automated
---

# Pencatatan User Action: Assign dan Remove Role serta Access Level

## Prerequisites

- Mode: FE+BE.
- Akun aktor dan observer: Total Control (Pre-setup #1, Admin Alpha), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log). Pengecualian: tiap TC membuka Settings (Role & Permission, Groups) untuk aksinya lalu Activity Log > User Action.
- Data target (Pre-setup #16), identitas dari `Fixture.activity-log.<kunci>` (fixture belum ada, disediakan tim FE):
  - Citra Lestari: tersedia sebagai target user, tanpa Access Level, Group Manager, Global Role, Group Role, atau Transaction Role di awal spec; memegang Global Role `Manage Open API` dengan izin Update `Inactive` (TC-FA-FAAL-228); Group Manager untuk group `Gedung D` tanpa subgroup (TC-FA-FAAL-224).
  - Group `Gedung A` ada; group `Gedung D` ada dan milik spec ini.
  - Dewi Lestari: berstatus Total Control (TC-FA-FAAL-230); di-seed lewat seed API di hook `before` spec ini dan dipulihkan di hook `after`, tanpa bergantung pada spec 075 yang menghapus user Dewi Lestari miliknya sendiri; email tidak tertulis di Pre-setup TC (disediakan tim FE).
  - Baris Tab User Action UA-01 sampai UA-15 (Pre-setup #12) tidak diubah spec ini.
- Hasil Assign berurutan dipakai sebagai precondition TC berikutnya: Group Role `Manage asset & TAG` pada `Gedung A` hasil TC-FA-FAAL-226 menjadi precondition TC-FA-FAAL-229.
- Baseline (S-12): total baris Tab User Action dibaca dari teks pagination `Showing x–y of N entries` pada langkah 1; tiap Verifikasi baris baru juga memastikan total bertambah dari total terakhir yang dibaca. Untuk TC-FA-FAAL-224 dan 230 Z0 adalah total terakhir yang dibaca sebelum aksi, dan Expected relatif terhadap Z0.
- Penantian pencatatan: tiap Verifikasi baris baru memakai idiom polling (muat ulang Tab User Action tiap 5 detik, batas 2 menit) sebagai pengganti langkah tunggu tersendiri.
- State yang diubah dan pemulihannya: Access Level Citra Lestari dipulihkan pada langkah 6 lewat seed API; seluruh Access Level, role, dan group target dipulihkan ke keadaan awal Pre-setup #16 oleh tim FE/BE lewat seed dan pemulihan API di hook `after`; group `Gedung D` dibuat ulang di hook `before`.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun aktor.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Buka Activity Log > User Action dan catat total baris dari teks pagination (N0)

### TC-FA-FAAL-221: Assign Total Control tercatat dengan Object Total Control

2. Di Settings > Role & Permission > Total Control assign user Citra Lestari
3. Tunggu aksi selesai
4. Buka Activity Log > User Action
5. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Assign`, Object `Total Control`, Name `Citra Lestari`, Field `Access Level`, Old Value `—`, New Value `Total Control`, Modified By `Admin A`
6. Pulihkan Citra Lestari ke keadaan tanpa Access Level lewat seed API

### TC-FA-FAAL-222: Assign Read Only tercatat dengan Object Read Only

7. Di Settings > Role & Permission > Read Only assign user Citra Lestari
8. Tunggu aksi selesai
9. Buka Activity Log > User Action
10. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Assign`, Object `Read Only`, Name `Citra Lestari`, Field `Access Level`, Old Value `—`, New Value `Read Only`, Modified By `Admin A`

### TC-FA-FAAL-223: Assign Group Manager tercatat dengan Field Group Manager dan nama group

11. Assign Group Manager untuk group Gedung A kepada Citra Lestari
12. Tunggu aksi selesai
13. Buka Activity Log > User Action
14. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Assign`, Object `Group Manager`, Name `Citra Lestari`, Field `Group Manager — Gedung A`, Old Value `—`, New Value `Assigned`, Modified By `Admin A`

### TC-FA-FAAL-224: Remove Group Manager (Group Deleted) saat group dihapus

15. Catat Z0 dari total baris pada Verifikasi langkah 14, lalu hapus group Gedung D di Settings > Groups dan konfirmasi dialog
16. Tunggu aksi selesai
17. Buka Activity Log > User Action
18. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): total baris bertambah dari Z0 dan di antara baris yang bertambah terdapat baris: Action `Remove`, Object `Group Manager (Group Deleted)`, Name `Citra Lestari`, Field `Group Manager — Gedung D`, Old Value `Assigned`, New Value `—`, Modified By `Admin A`

### TC-FA-FAAL-225: Assign Global Role tercatat dengan Object Global Role

19. Assign Global Role `Import data` kepada Citra Lestari
20. Tunggu aksi selesai
21. Buka Activity Log > User Action
22. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Assign`, Object `Global Role`, Name `Citra Lestari`, Field `Import data`, Old Value `—`, New Value `Assigned`, Modified By `Admin A`

### TC-FA-FAAL-226: Assign Group Role tercatat dengan Object Group Role

23. Assign Group Role `Manage asset & TAG` pada group Gedung A kepada Citra Lestari
24. Tunggu aksi selesai
25. Buka Activity Log > User Action
26. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Assign`, Object `Group Role`, Name `Citra Lestari`, Field `Manage asset & TAG — Gedung A`, Old Value `—`, New Value `Assigned`, Modified By `Admin A`

### TC-FA-FAAL-227: Assign Transaction Role tercatat dengan Object Transaction Role

27. Assign Transaction Role `Approver` pada sub-tab Disposal group Gedung A kepada Citra Lestari
28. Tunggu aksi selesai
29. Buka Activity Log > User Action
30. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Assign`, Object `Transaction Role`, Name `Citra Lestari`, Field `Disposal — Gedung A — Approver`, Old Value `—`, New Value `Assigned`, Modified By `Admin A`

### TC-FA-FAAL-228: Edit izin Global Role tercatat dengan Old dan New Inactive dan Active

31. Aktifkan izin Update pada Global Role `Manage Open API` milik Citra Lestari
32. Tunggu aksi selesai
33. Buka Activity Log > User Action
34. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Edit`, Object `Global Role`, Name `Citra Lestari`, Field `Manage Open API — Update`, Old Value `Inactive`, New Value `Active`, Modified By `Admin A`

### TC-FA-FAAL-229: Remove Group Role tercatat dengan New Value strip

35. Remove Group Role `Manage asset & TAG` pada group Gedung A dari Citra Lestari
36. Tunggu aksi selesai
37. Buka Activity Log > User Action
38. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Remove`, Object `Group Role`, Name `Citra Lestari`, Field `Manage asset & TAG — Gedung A`, Old Value `Assigned`, New Value `—`, Modified By `Admin A`

### TC-FA-FAAL-230: Auto-Revert tercatat dengan Modified By admin pemicu

39. Catat Z0 dari total baris pada Verifikasi langkah 38, lalu sebagai Admin Alpha edit CRUD individual peran Dewi Lestari hingga menyimpang dari pola Total Control dan konfirmasi dialog Auto-Revert
40. Tunggu aksi selesai
41. Buka Activity Log > User Action
42. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): total baris bertambah dari Z0 dan di antara baris yang bertambah terdapat baris: Action `Auto-Revert`, Object `Total Control`, Name `Dewi Lestari`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Admin A`
43. Verifikasi Modified By pada baris langkah 42 tampil `Admin A`, bukan `System`
44. Arahkan kursor ke Modified By pada baris langkah 42
45. Verifikasi hover Modified By menampilkan `Admin Alpha`

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung "Tunggu aksi selesai" (S-03, 8b.8, tanpa Verifikasi): langkah 3, 8, 12, 16, 20, 24, 28, 32, 36, 40; ditulis sebelum tiap pembukaan Activity Log > User Action yang mengikuti aksi tulis tanpa asersi di antaranya. Verifikasi polling tetap menunggu commit log.
- Spec di atas 35 langkah karena 10 langkah penghubung "Tunggu aksi selesai"; 10 TC (221 sampai 230) berurutan pada akun dan data Citra Lestari yang sama (TC-FA-FAAL-229 memakai Group Role dari TC-FA-FAAL-226; TC-FA-FAAL-230 memakai total dari Verifikasi TC-FA-FAAL-229), sehingga dipertahankan dalam satu spec.
- Langkah penghubung (S-03): langkah 1 (membuka tab dan mencatat baseline); langkah 6 (memulihkan Access Level Citra Lestari agar Old Value `—` pada langkah 10 berlaku); langkah 4, 9, 13, 17, 21, 25, 29, 33, 37, dan 41 (membuka Tab User Action sebagai bagian dari langkah 2 TC sumber).
- Baseline S-12: langkah 1 mencatat N0. Tiap Verifikasi baris baru juga memeriksa total pagination lebih besar dari total pada Verifikasi sebelumnya; jumlah baris per aksi tidak dipakai sebagai angka absolut karena Delete Group dan Auto-Revert dapat menulis lebih dari satu baris; untuk keduanya baris yang dicari dibaca di antara baris yang bertambah dari Z0 (langkah 18 dan 42).
- Langkah 43 dan 45 memecah Expected butir b TC-FA-FAAL-230 per klausa (S-01); butir a memakai kolom satu baris yang diamati dari satu entri.
- R-14: Modified By diasersi `Admin A` (First Name dan Last Initial); nama lengkap `Admin Alpha` hanya pada hover.
- Temuan untuk QA:
  - TC-FA-FAAL-221 dan 222 mengubah Access Level yang sama pada Citra Lestari secara berurutan dan tidak menyebut pemulihan di antaranya; langkah 6 memulihkannya lewat seed API.
  - TC-FA-FAAL-229 membutuhkan Group Role dari TC-FA-FAAL-226 (precondition c); spec memakai hasil langkah 23 berurutan.
  - Dewi Lestari (TC-FA-FAAL-230) dan Citra Lestari memakai data Pre-setup #16 yang sama dengan spec Tab Session (075 menghapus Dewi Lestari); tiap spec menyediakan dan memulihkan datanya sendiri.
  - TC-FA-FAAL-224 tidak menyebut baris `Delete` untuk group Gedung D; spec hanya mengasersi baris Remove.
