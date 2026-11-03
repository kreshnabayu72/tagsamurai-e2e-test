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
  - Citra Lestari: tersedia sebagai target user, tanpa Access Level, Group Role, atau Transaction Role di awal spec; satu-satunya Global Role adalah `Manage Open API` dengan izin Update `Inactive` (TC-FA-FAAL-228) dan satu-satunya Group Manager adalah untuk group `Gedung D` tanpa subgroup (TC-FA-FAAL-224).
  - Group `Gedung A` ada; group `Gedung D` ada dan milik spec ini.
  - Dewi Lestari: berstatus Total Control (TC-FA-FAAL-230); di-seed lewat seed API di hook `before` spec ini dan dipulihkan di hook `after`, tanpa bergantung pada spec 075 yang menghapus user Dewi Lestari miliknya sendiri; email tidak tertulis di Pre-setup TC (disediakan tim FE).
  - Baris Tab User Action UA-01 sampai UA-15 (Pre-setup #12) tidak diubah spec ini.
- Hasil Assign berurutan dipakai sebagai precondition TC berikutnya: Group Role `Manage asset & TAG` pada `Gedung A` hasil TC-FA-FAAL-226 menjadi precondition TC-FA-FAAL-229.
- Baseline (S-12): total baris Tab User Action dibaca dari teks pagination `Showing x–y of N entries` pada langkah 1; tiap Verifikasi baris baru juga memastikan total bertambah dari total terakhir yang dibaca. Untuk TC-FA-FAAL-224 dan 230 Z0 adalah total terakhir yang dibaca sebelum aksi, dan Expected relatif terhadap Z0.
- Penantian pencatatan: tiap Verifikasi baris baru memakai idiom polling (muat ulang Tab User Action tiap 5 detik, batas 2 menit) sebagai pengganti langkah tunggu tersendiri.
- State yang diubah dan pemulihannya: Access Level Citra Lestari dipulihkan pada langkah 6 dan 11 lewat seed API; seluruh Access Level, role, dan group target dipulihkan ke keadaan awal Pre-setup #16 oleh tim FE/BE lewat seed dan pemulihan API di hook `after`; group `Gedung D` dibuat ulang di hook `before`.
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
11. Pulihkan Citra Lestari ke keadaan tanpa Access Level lewat seed API

### TC-FA-FAAL-223: Assign Group Manager tercatat dengan Field Group Manager dan nama group

12. Assign Group Manager untuk group Gedung A kepada Citra Lestari
13. Tunggu aksi selesai
14. Buka Activity Log > User Action
15. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Assign`, Object `Group Manager`, Name `Citra Lestari`, Field `Group Manager — Gedung A`, Old Value `—`, New Value `Assigned`, Modified By `Admin A`

### TC-FA-FAAL-224: Remove Group Manager (Group Deleted) saat group dihapus

16. Catat Z0 dari total baris pada Verifikasi langkah 15, lalu hapus group Gedung D di Settings > Groups dan konfirmasi dialog
17. Tunggu aksi selesai
18. Buka Activity Log > User Action
19. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): total baris bertambah dari Z0
20. Ketik Search `Citra Lestari`, tekan Enter
21. Verifikasi di antara baris hasil Search terdapat baris baru: Action `Remove`, Object `Group Manager (Group Deleted)`, Name `Citra Lestari`, Field `Group Manager — Gedung D`, Old Value `Assigned`, New Value `—`, Modified By `Admin A`

### TC-FA-FAAL-225: Assign Global Role tercatat dengan Object Global Role

22. Assign Global Role `Import data` kepada Citra Lestari
23. Tunggu aksi selesai
24. Buka Activity Log > User Action
25. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Assign`, Object `Global Role`, Name `Citra Lestari`, Field `Import data`, Old Value `—`, New Value `Assigned`, Modified By `Admin A`

### TC-FA-FAAL-226: Assign Group Role tercatat dengan Object Group Role

26. Assign Group Role `Manage asset & TAG` pada group Gedung A kepada Citra Lestari
27. Tunggu aksi selesai
28. Buka Activity Log > User Action
29. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Assign`, Object `Group Role`, Name `Citra Lestari`, Field `Manage asset & TAG — Gedung A`, Old Value `—`, New Value `Assigned`, Modified By `Admin A`

### TC-FA-FAAL-227: Assign Transaction Role tercatat dengan Object Transaction Role

30. Assign Transaction Role `Approver` pada sub-tab Disposal group Gedung A kepada Citra Lestari
31. Tunggu aksi selesai
32. Buka Activity Log > User Action
33. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Assign`, Object `Transaction Role`, Name `Citra Lestari`, Field `Disposal — Gedung A — Approver`, Old Value `—`, New Value `Assigned`, Modified By `Admin A`

### TC-FA-FAAL-228: Edit izin Global Role tercatat dengan Old dan New Inactive dan Active

34. Aktifkan izin Update pada Global Role `Manage Open API` milik Citra Lestari
35. Tunggu aksi selesai
36. Buka Activity Log > User Action
37. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Edit`, Object `Global Role`, Name `Citra Lestari`, Field `Manage Open API — Update`, Old Value `Inactive`, New Value `Active`, Modified By `Admin A`

### TC-FA-FAAL-229: Remove Group Role tercatat dengan New Value strip

38. Remove Group Role `Manage asset & TAG` pada group Gedung A dari Citra Lestari
39. Tunggu aksi selesai
40. Buka Activity Log > User Action
41. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): baris baru di Tab User Action paling atas, total baris bertambah: Action `Remove`, Object `Group Role`, Name `Citra Lestari`, Field `Manage asset & TAG — Gedung A`, Old Value `Assigned`, New Value `—`, Modified By `Admin A`

### TC-FA-FAAL-230: Auto-Revert tercatat dengan Modified By admin pemicu

42. Catat Z0 dari total baris pada Verifikasi langkah 41, lalu sebagai Admin Alpha edit CRUD individual peran Dewi Lestari hingga menyimpang dari pola Total Control dan konfirmasi dialog Auto-Revert
43. Tunggu aksi selesai
44. Buka Activity Log > User Action
45. Verifikasi (polling, batas tunggu 2 menit, tab dimuat ulang secara berkala): total baris bertambah dari Z0
46. Ketik Search `Dewi Lestari`, tekan Enter
47. Verifikasi di antara baris hasil Search terdapat baris baru: Action `Auto-Revert`, Object `Total Control`, Name `Dewi Lestari`, Field `Access Level`, Old Value `Total Control`, New Value `—`, Modified By `Admin A`
48. Verifikasi Modified By pada baris langkah 47 tampil `Admin A`, bukan `System`
49. Arahkan kursor ke Modified By pada baris langkah 47
50. Verifikasi hover Modified By menampilkan `Admin Alpha`

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung "Tunggu aksi selesai" (S-03, 8b.8, tanpa Verifikasi): langkah 3, 8, 13, 17, 23, 27, 31, 35, 39, 43; ditulis sebelum tiap pembukaan Activity Log > User Action yang mengikuti aksi tulis tanpa asersi di antaranya. Verifikasi polling tetap menunggu commit log.
- Spec di atas 35 langkah (50 langkah; 40 tanpa 10 langkah penghubung "Tunggu aksi selesai", dan sisanya langkah penghubung S-03 serta pemisahan Verifikasi total dan Search); spec memuat 10 TC berurutan: TC-FA-FAAL-229 memakai Group Role hasil TC-FA-FAAL-226, TC-FA-FAAL-221 sampai 228 menargetkan Citra Lestari, dan TC-FA-FAAL-230 menargetkan Dewi Lestari dengan Z0 dari Verifikasi TC-FA-FAAL-229, sehingga dipertahankan dalam satu spec.
- Langkah penghubung (S-03): langkah 1 (membuka tab dan mencatat baseline); langkah 6 (memulihkan Access Level Citra Lestari agar Old Value `—` pada langkah 10 berlaku); langkah 11 (memulihkan Access Level Citra Lestari sesudah TC-FA-FAAL-222 agar langkah 12 sampai 50 berjalan dari keadaan awal Pre-setup #16, S-09); langkah 20 dan 46 (Search untuk menemukan baris target, R-16); langkah 4, 9, 14, 18, 24, 28, 32, 36, 40, 44 (membuka Tab User Action sebagai bagian dari langkah 2 TC sumber).
- Baseline S-12: langkah 1 mencatat N0. Tiap Verifikasi baris baru juga memeriksa total pagination lebih besar dari total pada Verifikasi sebelumnya; jumlah baris per aksi tidak dipakai sebagai angka absolut karena Delete Group dan Auto-Revert dapat menulis lebih dari satu baris; untuk keduanya baris yang dicari dibaca di antara baris yang bertambah dari Z0 (langkah 21 dan 47). Pada TC-FA-FAAL-224 dan 230 Verifikasi total (langkah 19 dan 45) mendahului Search (langkah 20 dan 46) karena total pagination setelah Search hanya menghitung baris hasil Search; Search dan Verifikasi baris yang mengikutinya (langkah 21 dan 47) adalah asersi dan langkah tambahan spec (S-03) agar baris target dibaca dari hasil Search, bukan dari halaman 1 saja.
- Langkah 48 dan 50 memecah Expected butir b TC-FA-FAAL-230 per klausa (S-01); butir a memakai kolom satu baris yang diamati dari satu entri.
- R-14: Modified By diasersi `Admin A` (First Name dan Last Initial); nama lengkap `Admin Alpha` hanya pada hover.
- Temuan untuk QA:
  - TC-FA-FAAL-221 dan 222 mengubah Access Level yang sama pada Citra Lestari secara berurutan dan tidak menyebut pemulihan di antaranya; langkah 6 memulihkannya lewat seed API. Access Level Read Only dari TC-FA-FAAL-222 juga tidak dipulihkan oleh TC; langkah 11 memulihkannya lewat seed API sebelum TC-FA-FAAL-223.
  - TC-FA-FAAL-229 membutuhkan Group Role dari TC-FA-FAAL-226 (precondition c); spec memakai hasil langkah 26 berurutan.
  - Dewi Lestari (TC-FA-FAAL-230) dan Citra Lestari memakai data Pre-setup #16 yang sama dengan spec Tab Session (075 menghapus Dewi Lestari); tiap spec menyediakan dan memulihkan datanya sendiri.
  - TC-FA-FAAL-224 tidak menyebut baris `Delete` untuk group Gedung D; spec hanya mengasersi baris Remove.
