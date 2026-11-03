---
id: TC-GS-USER-E2E-163-tab-role-user-type-dan-auto-revert-tier-lewat-switch-off
title: "User Detail Tab Role: User Type Mengikuti Role Active, Cancel Dialog Auto-revert, dan Switch OFF pada User Total Control dan Read Only Memunculkan Dialog Auto-revert dan Tier Lepas"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-1098
  - TC-GS-USER-1096
  - TC-GS-USER-1094
  - TC-GS-USER-1095
coverage:
  web: automated
---

# User Detail Tab Role: User Type Mengikuti Role Active, Cancel Dialog Auto-revert, dan Switch OFF pada User Total Control dan Read Only Memunculkan Dialog Auto-revert dan Tier Lepas

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login di hook `before` spec ini (akun default suite); halaman dibuka hook `beforeEach` suite; tidak ada ganti akun. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Dinamis, di-seed lewat API di hook `before` dan dihapus di hook `after` (padanan Tabel Pre-setup):
  - `Dewi Lestari {runId}-163`, email `dewilestari+{runId}-163@qwertysystem.net`: Basic, tanpa assignment role (TC-GS-USER-1098).
  - `Andi Wijaya {runId}-163`, email `andiwijaya+{runId}-163@qwertysystem.net`: tier Total Control, keenam role Active (switch ON) dengan nilai CRUD tertentu (TC-GS-USER-1096 dan 1094).
  - `Doni Pratama {runId}-163`, email `donipratama+{runId}-163@qwertysystem.net`: tier Read Only, keenam role Active (TC-GS-USER-1095).
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD): seeding user dengan tier Total Control atau Read Only dan assignment role lewat API (mekanisme pembentukan tier tidak disebut TC); membaca jumlah entri Tab Changelog Detail `Andi Wijaya {runId}-163` lewat BE tepat sebelum aksi TC-GS-USER-1096 (8b butir 10).
- State global yang diubah: tidak ada; yang berubah hanya assignment dan tier tiga user seed milik spec. Cleanup di hook `after` (tetap berjalan walau spec gagal di tengah): hapus tiga user seed. Tier dilepas pada blok terakhir (data destruktif di akhir, S-10).

## Test Steps

### TC-GS-USER-1098: User Type badge mengikuti jumlah role Active

1. Klik icon Search, ketik `Dewi Lestari {runId}-163`, tekan Enter
2. Klik Name `Dewi Lestari {runId}-163` di User List
3. Verifikasi User Type di General Information `Basic`
4. Klik Tab `Role`
5. Nyalakan switch Active baris `Manage files`
6. Verifikasi User Type di General Information `Admin`
7. Matikan switch Active baris `Manage files`
8. Verifikasi User Type di General Information `Basic`

### TC-GS-USER-1096: Cancel dialog auto-revert mengembalikan switch ke ON

9. Klik menu User di sidebar Global Settings
10. Klik icon Search, ketik `Andi Wijaya {runId}-163`, tekan Enter
11. Klik Name `Andi Wijaya {runId}-163` di User List
12. Klik Tab `Role`
13. Catat jumlah entri Tab Changelog `Andi Wijaya {runId}-163` sebagai J0 (lewat kemampuan baca BE)
14. Matikan switch Active baris `Manage files`
15. Klik `[Cancel]`
16. Verifikasi dialog tertutup
17. Verifikasi tidak ada toast
18. Verifikasi switch Active baris `Manage files` kembali ON
19. Verifikasi banner `This user has Total Control access.` tetap tampil
20. Tekan F5
21. Verifikasi switch Active baris `Manage files` tetap ON setelah muat ulang
22. Klik Tab `Changelog`
23. Verifikasi Tab `Changelog` memuat entri
24. Verifikasi jumlah entri Tab `Changelog` sama dengan J0 (lewat kemampuan baca BE)
25. Klik Tab `Role`

### TC-GS-USER-1094: Switch OFF pada user Total Control memunculkan dialog auto-revert dan tier lepas

26. Verifikasi User Type di General Information `Total Control`
27. Catat nilai checkbox CRUD keenam baris Tab Role sebagai C0
28. Matikan switch Active baris `Manage files`
29. Verifikasi dialog Title `Remove Total Control`
30. Verifikasi body dialog `• Andi Wijaya {runId}-163`
31. Verifikasi body dialog `This edit will remove this user's Total Control access level. Their individual role permissions will remain as edited. Are you sure you want to remove it?`
32. Verifikasi tombol dialog `[Cancel]` dan `[Remove]`
33. Klik `[Remove]`
34. Verifikasi toast sukses `Success, permissions have been updated. Andi Wijaya {runId}-163 is no longer Total Control.`
35. Verifikasi baris `Manage files` tampil di tabel Tab Role
36. Verifikasi banner `This user has Total Control access.` hilang
37. Verifikasi switch Active baris `Manage files` OFF
38. Verifikasi seluruh checkbox baris `Manage files` disabled
39. Verifikasi switch Active kelima baris lain tetap ON
40. Verifikasi nilai CRUD kelima baris lain sama dengan C0 (tidak berubah)
41. Verifikasi User Type di General Information `Admin`

### TC-GS-USER-1095: Switch OFF pada user Read Only memunculkan dialog auto-revert dan tier lepas

42. Klik menu User di sidebar Global Settings
43. Klik icon Search, ketik `Doni Pratama {runId}-163`, tekan Enter
44. Klik Name `Doni Pratama {runId}-163` di User List
45. Klik Tab `Role`
46. Matikan switch Active baris `Manage TAG`
47. Verifikasi dialog Title `Remove Read Only`
48. Verifikasi body dialog `• Doni Pratama {runId}-163`
49. Verifikasi body dialog `This edit will remove this user's Read Only access level. Their individual role permissions will remain as edited. Are you sure you want to remove it?`
50. Verifikasi tombol dialog `[Cancel]` dan `[Remove]`
51. Klik `[Remove]`
52. Verifikasi toast sukses `Success, permissions have been updated. Doni Pratama {runId}-163 is no longer Read Only.`
53. Verifikasi baris `Manage TAG` tampil di tabel Tab Role
54. Verifikasi banner `This user has Read Only access.` hilang
55. Verifikasi switch Active baris `Manage TAG` OFF
56. Verifikasi switch Active kelima baris lain tetap ON

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Spec melewati sekitar 35 langkah (56 langkah) karena empat TC berada di satu kelas harness (fungsional, aksi tulis pada user milik spec), satu aktor, dan satu layar (Tab Role User Detail); tiap blok memakai user seed sendiri kecuali TC-GS-USER-1096 dan TC-GS-USER-1094 yang berurutan pada user tier Total Control yang sama, dan banyak langkah berasal dari satu `Verifikasi` per klausa Expected (S-01).
- Urutan TC sumber diubah: TC-GS-USER-1098 (tanpa tier) dahulu; TC-GS-USER-1096 (Cancel, tidak mengubah data) mendahului TC-GS-USER-1094 pada user yang sama karena TC-GS-USER-1094 melepas tier; TC-GS-USER-1095 terakhir (data destruktif tier di akhir, S-10). Langkah 1 sampai 2 TC-GS-USER-1094 dipenuhi langkah 11 sampai 12 dan 25.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 10, dan 43 (Search nama target sebelum Klik Name, R-16), 9 dan 42 (kembali ke User List), 13 dan 27 (mencatat baseline), 20 (muat ulang untuk mengamati penyimpanan), 22 dan 25 (pindah tab).
- Anchor dan asersi tambahan (bagian 8b butir 2; tidak ada di TC, hanya sebagai anchor): langkah 35 dan 53 (baris tabel tampil sebagai pembanding untuk "banner hilang"); langkah 23 (Tab Changelog memuat entri, pembanding sebelum membandingkan jumlah); langkah 16 (dialog tertutup) mendahului langkah 17. Langkah 26 (User Type awal `Total Control`) mendukung klausa "berubah dari `Total Control` ke `Admin`".
- P-1: TC-GS-USER-1096 butir c ("tidak ada entri log baru") diasersi di spec ini lewat perbandingan jumlah entri Tab Changelog terhadap baseline J0 (langkah 13 dan 24), bukan lewat spec absence, karena tidak ada spec absence yang memuat aksi Cancel dialog auto-revert dan state tier Total Control dibangun dalam alur ini (S-05).
- Pembagian TC lintas spec: Tab Role user non-tier tanpa aksi tulis (screening, banner) ada di spec 063; auto-revert tier dengan Remove pada perubahan checkbox ada di spec 064.
- Temuan untuk QA:
  - TC-GS-USER-1096 Expected c ("tidak ada entri log baru") tidak menyebut surface log; spec memakai Tab Changelog Detail. "Tidak ada perubahan tersimpan" diamati lewat muat ulang (langkah 20 sampai 21).
  - TC-GS-USER-1094 Post Condition ("Notifikasi in-app view-only ke Andi Wijaya", "Terdampak: Role & Permission tab Total Control") dan TC-GS-USER-1095 Post Condition ("Notifikasi in-app view-only ke Doni Pratama") tanpa langkah observasi; tidak diasersi.
  - TC-GS-USER-1094 Expected c menyebut "nilai CRUD tidak berubah" tanpa nilai awal; spec membandingkan dengan C0 yang dicatat sebelum aksi (langkah 27).
  - TC-GS-USER-1098 Expected c memuat "baris Manage files inactive-retained tidak dihitung" sebagai penjelasan; spec hanya mengasersi User Type `Basic`.
  - Mekanisme pembentukan tier Total Control dan Read Only pada user tidak disebut TC (Tabel Pre-setup hanya menyebut tier); disediakan tim FE/BE.
  - TC-GS-USER-1098, 1096, 1094, 1095 memakai user Pre-setup (Dewi Lestari, Andi Wijaya, Doni Pratama); spec memakai seed milik spec (S-06).
