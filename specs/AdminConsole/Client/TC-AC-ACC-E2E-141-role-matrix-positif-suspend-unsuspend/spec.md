---
id: TC-AC-ACC-E2E-141-role-matrix-positif-suspend-unsuspend
title: "Role Matrix Positif: Suspend, Unsuspend, dan Bulk Suspend oleh Pemegang Update Manage Active Client dan Group Manager"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-602
  - TC-AC-ACC-603
  - TC-AC-ACC-604
  - TC-AC-ACC-605
coverage:
  web: automated
---

# Role Matrix Positif: Suspend, Unsuspend, dan Bulk Suspend oleh Pemegang Update Manage Active Client dan Group Manager

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (langkah tiap role berbeda target dan aksi, sehingga spec ditulis per blok role dengan Step ganti akun eksplisit; akun pertama login di hook `before`):

| Blok | Role | Akun | Env password | Client target | Aksi |
|---|---|---|---|---|---|
| 1 | Active-Update-Only A-06 (Manage active client: Update + Read, exact-match Area Jakarta) | `activeUpdateJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_ACTIVE_UPDATE_PASSWORD` | `PT Ubah Mitra 11` (Active), `PT Ubah Mitra 12` (Suspended), `PT Ubah Mitra 13` dan `PT Ubah Mitra 14` (Active) | Suspend; Unsuspend; Bulk Suspend |
| 2 | Group Manager A-03 (scope Area Jakarta + seluruh descendant) | `groupManagerJakarta_automated_qaTeam1@qwertysystem.net` | `AC_CLIENT_GM_PASSWORD` | `PT Menteng Jeda` (Direct, Cabang Menteng, Active) | Suspend |

- Login akun blok 1 di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Data Pre-setup yang diubah lalu dipulihkan lewat UI (S-06): C-ROL-8 `PT Ubah Mitra 11`, `12`, `13`, `14` (tanpa subscription; `12` awalnya Suspended) dan C-ROL-17 `PT Menteng Jeda` (Residen yang dipulihkan). Efek: baris Changelog `Suspend`/`Unsuspend` dan Last Updated bertambah.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel hook suite (rujukan `suite.md`).

## Test Steps

### Blok 1: Active-Update-Only

#### TC-AC-ACC-602: Suspend Client oleh pemegang Update pada Manage active client sampai sukses

1. Ketik Search `PT Ubah Mitra 11`, tekan Enter
2. Klik `[⋯]` pada baris `PT Ubah Mitra 11` → klik `Suspend`
3. Verifikasi header dialog berjudul "Suspend Client"
4. Verifikasi body dialog memuat bullet `• PT Ubah Mitra 11`
5. Verifikasi body dialog memuat "Suspending this client will make access to all subscribed products read-only. Subscription lifecycle will continue running in the background. Are you sure you want to suspend it?"
6. Verifikasi footer memuat `[Cancel]` dan `[Suspend]`
7. Klik `[Suspend]` pada dialog
8. Verifikasi toast sukses "Success, client has been suspended."
9. Klik sub-tab Suspended
10. Verifikasi baris `PT Ubah Mitra 11` tampil di sub-tab Suspended
11. Klik `[⋯]` pada baris `PT Ubah Mitra 11` → pilih `Unsuspend`, lalu klik `[Unsuspend]` pada dialog

#### TC-AC-ACC-603: Unsuspend Client oleh pemegang Update pada Manage active client sampai sukses

12. Ketik Search `PT Ubah Mitra 12`, tekan Enter
13. Klik `[⋯]` pada baris `PT Ubah Mitra 12` → klik `Unsuspend`
14. Verifikasi header dialog berjudul "Unsuspend Client"
15. Verifikasi body dialog memuat bullet `• PT Ubah Mitra 12`
16. Verifikasi body dialog memuat "Unsuspending this client will restore access to all subscribed products. Are you sure you want to unsuspend it?"
17. Verifikasi footer memuat `[Cancel]` dan `[Unsuspend]`
18. Klik `[Unsuspend]` pada dialog
19. Verifikasi toast sukses "Success, client has been unsuspended."
20. Klik sub-tab Active
21. Verifikasi baris `PT Ubah Mitra 12` tampil di sub-tab Active
22. Klik `[⋯]` pada baris `PT Ubah Mitra 12` → pilih `Suspend`, lalu klik `[Suspend]` pada dialog

#### TC-AC-ACC-604: Bulk Suspend oleh pemegang Update pada Manage active client sampai sukses

23. Ketik Search `PT Ubah Mitra 13`, tekan Enter, lalu centang barisnya
24. Ganti isi Search dengan `PT Ubah Mitra 14`, tekan Enter, lalu centang barisnya
25. Klik Bulk Action lalu pilih `Suspend`
26. Verifikasi header dialog berjudul "Suspend Clients"
27. Verifikasi body dialog memuat bullet `• PT Ubah Mitra 13` dan `• PT Ubah Mitra 14`
28. Verifikasi body dialog memuat "Suspending these clients will make access to all subscribed products read-only. Subscription lifecycle will continue running in the background. Are you sure you want to suspend them?"
29. Verifikasi footer memuat `[Cancel]` dan `[Suspend]`
30. Klik `[Suspend]` pada dialog
31. Verifikasi toast sukses "Success, client has been suspended."
32. Klik sub-tab Suspended
33. Ketik Search `PT Ubah Mitra 13`, tekan Enter
34. Verifikasi baris `PT Ubah Mitra 13` tampil di sub-tab Suspended
35. Ganti isi Search dengan `PT Ubah Mitra 14`, tekan Enter
36. Verifikasi baris `PT Ubah Mitra 14` tampil di sub-tab Suspended
37. Ketik Search `PT Ubah Mitra 13`, tekan Enter, lalu centang barisnya
38. Ganti isi Search dengan `PT Ubah Mitra 14`, tekan Enter, lalu centang barisnya
39. Klik Bulk Action → pilih `Unsuspend`, lalu klik `[Unsuspend]` pada dialog
40. Tunggu aksi selesai (dialog Unsuspend tertutup)

### Blok 2: Group Manager

41. Ganti akun: logout lalu login sebagai Group Manager A-03

#### TC-AC-ACC-605: Suspend Client oleh Group Manager di node descendant sampai sukses

42. Ketik Search `PT Menteng Jeda`, tekan Enter
43. Klik `[⋯]` pada baris `PT Menteng Jeda` → klik `Suspend`
44. Verifikasi header dialog berjudul "Suspend Client"
45. Verifikasi body dialog memuat bullet `• PT Menteng Jeda`
46. Verifikasi body dialog memuat "Suspending this client will make access to all subscribed products read-only. Subscription lifecycle will continue running in the background. Are you sure you want to suspend it?"
47. Verifikasi footer memuat `[Cancel]` dan `[Suspend]`
48. Klik `[Suspend]` pada dialog
49. Verifikasi toast sukses "Success, client has been suspended."
50. Klik sub-tab Suspended
51. Verifikasi baris `PT Menteng Jeda` tampil di sub-tab Suspended
52. Klik `[⋯]` pada baris `PT Menteng Jeda` → pilih `Unsuspend`, lalu klik `[Unsuspend]` pada dialog

## Notes

- Mode: FE+BE. Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` dan `####` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif ditulis per blok role (bagian 3a): langkah berbeda per role (target dan aksi) dan ganti akun memakai Step eksplisit; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal. Kombinasi role × aksi hanya yang punya TC sumber.
- Spec ini melewati sekitar 35 langkah: satu `Verifikasi` per klausa Expected (S-01) atas empat TC satu topik (aksi Suspend/Unsuspend oleh role terbatas); tiap blok memakai Client sendiri dan memulihkannya sehingga tetap bermakna walau blok sebelumnya gagal.
- Langkah penghubung (tanpa awalan Verifikasi): pemulihan status di akhir tiap blok TC (langkah 11, 22, 39, 52; Post Condition TC), "Tunggu aksi selesai" sebelum ganti akun (langkah 40; butir 8 bagian 8b), ganti akun (langkah 41), dan Search yang menemukan baris target (R-16).
- Post Condition TC-AC-ACC-602, 603, 604, 605 butir b (log Changelog `Suspend`/`Unsuspend` tercatat) tanpa langkah observasi di TC tidak diasersi.
- Temuan untuk QA:
  - TC-AC-ACC-602 dan 603 menyebut pemulihan "Unsuspend/Suspend PT Ubah Mitra 11/12" sebagai Post Condition yang menambah baris Changelog tambahan; spec memulihkan sesuai Post Condition.
