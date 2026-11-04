---
id: TC-AC-SU-E2E-167-tab-system-log-aktor-objek-tier-group-manager-dan-cascade
title: "Tab System Log Aktor Menampilkan Entri Object Total Control, Read Only, Group Manager, dan Cascade Tier dengan Name Target dan Isi Identik Popup Changelog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-568
  - TC-AC-SU-569
  - TC-AC-SU-570
coverage:
  web: automated
---

# Tab System Log Aktor Menampilkan Entri Object Total Control, Read Only, Group Manager, dan Cascade Tier dengan Name Target dan Isi Identik Popup Changelog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per kebutuhan state (nama berprefix `Mike Tan {runId}-167` agar satu Search menemukan seluruh target). Pelaku seluruh pemicu adalah Default User lewat sesi API aktor (login API password `Spectra.env.AC_DU_PASSWORD`, token tidak dihitung sebagai sesi web). Region A dari Group Tree Pre-setup hanya menjadi target Group Manager dan tidak diubah; group `Region C {runId}-167` milik spec dihapus oleh pemicu K.

| Kode | Name | State awal | Pemicu (sesi API Default User) |
|---|---|---|---|
| A | `Mike Tan {runId}-167A` | tanpa tier | Assign Total Control |
| B | `Mike Tan {runId}-167B` | bertier Total Control | Remove Total Control |
| C | `Mike Tan {runId}-167C` | bertier Total Control | edit role hingga menyimpang dan konfirmasi Remove (Auto-Revert Total Control) |
| D | `Mike Tan {runId}-167D` | tanpa tier | Assign Read Only |
| E | `Mike Tan {runId}-167E` | bertier Read Only | Remove Read Only |
| F | `Mike Tan {runId}-167F` | bertier Read Only | edit role hingga menyimpang dan konfirmasi Remove (Auto-Revert Read Only) |
| G | `Mike Tan {runId}-167G` | tanpa tier | Assign Group Manager Region A |
| H | `Mike Tan {runId}-167H` | Group Manager di Region A | Remove Group Manager Region A |
| I | `Mike Tan {runId}-167I` | Group Manager di Region A | edit CRUD hingga menyimpang dan konfirmasi Remove (Auto-Revert Group Manager) |
| K | `Mike Tan {runId}-167K` | Group Manager di `Region C {runId}-167` | hapus group `Region C {runId}-167` |
| L1 | `Mike Tan {runId}-167L1` | tanpa tier, "Manage group" dan "Manage partner" (Region A) aktif | Assign Total Control |
| L2 | `Mike Tan {runId}-167L2` | tanpa tier, "Manage group" dan "Manage partner" (Region A) aktif | Assign Read Only |
| L3 | `Mike Tan {runId}-167L3` | bertier Total Control, "Manage group" dan "Manage partner" (Region A) aktif | Remove Total Control |
| L4 | `Mike Tan {runId}-167L4` | bertier Read Only, "Manage group" dan "Manage partner" (Region A) aktif | Remove Read Only |

- Kemampuan teknis: Fixture BE (seeding user, tier, role, group, dan Group Manager); sesi API aktor Default User (kemampuan disediakan tim BE/FE tanpa endpoint karangan di spec); nama tampil akun Default User dari `Fixture.settingsUser.defaultUserActor.displayName` (disediakan tim FE; tidak tertulis di Pre-setup TC). Tanpa intercept, klien HTTP, dan jam server.
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-568: Object `Total Control` dan `Read Only`
1. Jalankan pemicu A sampai F (tabel Prerequisites) lewat sesi API Default User hingga keenam entri tersimpan
2. Ketik Search nama tampil Default User, tekan Enter, klik Name baris Default User untuk membuka Detail, klik Tab System Log, lalu ketik Search `Mike Tan {runId}-167` pada tab, tekan Enter
3. Verifikasi tepat 1 baris Action `Assign`: Object `Total Control`, Name `Mike Tan {runId}-167A`, Field `Access Level`, Old Value `—`, New Value `Total Control`
4. Verifikasi tepat 1 baris Action `Remove`: Object `Total Control`, Name `Mike Tan {runId}-167B`, Field `Access Level`, Old Value `Total Control`, New Value `—`
5. Verifikasi tepat 1 baris Action `Auto-Revert`: Object `Total Control`, Name `Mike Tan {runId}-167C`, Field `Access Level`, Old Value `Total Control`, New Value `—`
6. Verifikasi tepat 1 baris Action `Assign`: Object `Read Only`, Name `Mike Tan {runId}-167D`, Field `Access Level`, Old Value `—`, New Value `Read Only`
7. Verifikasi tepat 1 baris Action `Remove`: Object `Read Only`, Name `Mike Tan {runId}-167E`, Field `Access Level`, Old Value `Read Only`, New Value `—`
8. Verifikasi tepat 1 baris Action `Auto-Revert`: Object `Read Only`, Name `Mike Tan {runId}-167F`, Field `Access Level`, Old Value `Read Only`, New Value `—`
9. Verifikasi tabel Tab System Log tidak memiliki kolom Modified By
10. Klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-167` pada Popup Changelog: User, tekan Enter
11. Verifikasi Popup Changelog: User memuat baris `Assign` untuk A dengan Field `Access Level` dan Old/New Value yang sama dengan Tab System Log (Total Control)
12. Verifikasi Popup Changelog: User memuat baris `Remove` untuk B dengan Field `Access Level` dan Old/New Value yang sama dengan Tab System Log (Total Control)
13. Verifikasi Popup Changelog: User memuat baris `Auto-Revert` untuk C dengan Field `Access Level` dan Old/New Value yang sama dengan Tab System Log (Total Control)
14. Verifikasi Popup Changelog: User memuat baris `Assign` untuk D dengan Field `Access Level` dan Old/New Value yang sama dengan Tab System Log (Read Only)
15. Verifikasi Popup Changelog: User memuat baris `Remove` untuk E dengan Field `Access Level` dan Old/New Value yang sama dengan Tab System Log (Read Only)
16. Verifikasi Popup Changelog: User memuat baris `Auto-Revert` untuk F dengan Field `Access Level` dan Old/New Value yang sama dengan Tab System Log (Read Only)
### TC-AC-SU-569: Object `Group Manager`
17. Tutup popup, jalankan pemicu G, H, I, dan K (tabel Prerequisites) lewat sesi API Default User hingga keempat entri tersimpan
18. Buka Detail Default User (Search nama tampil Default User, klik Name baris), klik Tab System Log, lalu ketik Search `Mike Tan {runId}-167` pada tab, tekan Enter
19. Ubah page size Tab System Log menjadi 100
20. Verifikasi tepat 1 baris Action `Assign`: Object `Group Manager`, Name `Mike Tan {runId}-167G`, Field `Group Manager — Region A`, Old Value `—`, New Value `Assigned`
21. Verifikasi tepat 1 baris Action `Remove`: Object `Group Manager`, Name `Mike Tan {runId}-167H`, Field `Group Manager — Region A`, Old Value `Assigned`, New Value `—`
22. Verifikasi tepat 1 baris Action `Auto-Revert`: Object `Group Manager`, Name `Mike Tan {runId}-167I`, Field `Group Manager — Region A`, Old Value `Assigned`, New Value `—`
23. Verifikasi tepat 1 baris Action `Remove`: Object `Group Manager (Group Deleted)`, Name `Mike Tan {runId}-167K`, Field `Group Manager — Region C {runId}-167`, Old Value `Assigned`, New Value `—`
24. Verifikasi tabel Tab System Log tidak memiliki kolom Modified By
25. Klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-167` pada Popup Changelog: User, tekan Enter
26. Ubah page size Popup Changelog: User menjadi 100
27. Verifikasi Popup Changelog: User memuat baris `Assign` untuk G dengan Field dan Old/New Value yang sama dengan Tab System Log
28. Verifikasi Popup Changelog: User memuat baris `Remove` untuk H dengan Field dan Old/New Value yang sama dengan Tab System Log
29. Verifikasi Popup Changelog: User memuat baris `Auto-Revert` untuk I dengan Field dan Old/New Value yang sama dengan Tab System Log
30. Verifikasi Popup Changelog: User memuat baris `Remove (Group Deleted)` untuk K dengan Field dan Old/New Value yang sama dengan Tab System Log
### TC-AC-SU-570: Cascade Total Control dan Read Only
31. Tutup popup, jalankan pemicu L1, L2, L3, dan L4 (tabel Prerequisites) lewat sesi API Default User hingga seluruh entri cascade tersimpan
32. Buka Detail Default User (Search nama tampil Default User, klik Name baris), klik Tab System Log, lalu ketik Search `Mike Tan {runId}-167L` pada tab, tekan Enter
33. Ubah page size Tab System Log menjadi 100
34. Verifikasi tepat 1 baris Action `Assign (via Total Control)` untuk L1 dengan Object `Global Role` per Global Role terdampak, Name `Mike Tan {runId}-167L1`
35. Verifikasi tepat 1 baris Action `Assign (via Total Control)` untuk L1 dengan Object `Group Role` per Group Role per group, Name `Mike Tan {runId}-167L1`
36. Verifikasi tepat 1 baris Action `Assign (via Read Only)` untuk L2 dengan Object `Global Role` per Global Role terdampak, Name `Mike Tan {runId}-167L2`
37. Verifikasi tepat 1 baris Action `Assign (via Read Only)` untuk L2 dengan Object `Group Role` per Group Role per group, Name `Mike Tan {runId}-167L2`
38. Verifikasi tepat 1 baris Action `Remove (via Total Control)` untuk L3 dengan Object `Global Role` per Global Role terdampak, Name `Mike Tan {runId}-167L3`
39. Verifikasi tepat 1 baris Action `Remove (via Total Control)` untuk L3 dengan Object `Group Role` per Group Role per group, Name `Mike Tan {runId}-167L3`
40. Verifikasi tepat 1 baris Action `Remove (via Read Only)` untuk L4 dengan Object `Global Role` per Global Role terdampak, Name `Mike Tan {runId}-167L4`
41. Verifikasi tepat 1 baris Action `Remove (via Read Only)` untuk L4 dengan Object `Group Role` per Group Role per group, Name `Mike Tan {runId}-167L4`
42. Verifikasi tabel Tab System Log tidak memiliki kolom Modified By
43. Klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-167L` pada Popup Changelog: User, tekan Enter
44. Ubah page size Popup Changelog: User menjadi 100
45. Verifikasi Popup Changelog: User memuat baris cascade Action `Assign (via Total Control)` untuk L1 dengan Field `[Role] — Access` (Global Role) atau `[Role] — [Group Name] — Access` (Group Role), Old Value `—`, New Value `Assigned`, identik dengan Tab System Log
46. Verifikasi Popup Changelog: User memuat baris cascade Action `Assign (via Read Only)` untuk L2 dengan format Field dan Old/New Value yang sama, identik dengan Tab System Log
47. Verifikasi Popup Changelog: User memuat baris cascade Action `Remove (via Total Control)` untuk L3 dengan Old Value `Assigned`, New Value `—`, identik dengan Tab System Log
48. Verifikasi Popup Changelog: User memuat baris cascade Action `Remove (via Read Only)` untuk L4 dengan Old Value `Assigned`, New Value `—`, identik dengan Tab System Log

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): pemicu lewat sesi API (langkah 1 dan serupa; R-20), pembukaan Detail aktor, Tab System Log, dan Search nama target (langkah 2 dan langkah serupa, R-16), menutup popup, serta Search nama target pada Popup Changelog: User (langkah 10 dan langkah serupa; user bernama unik sehingga baseline entri nol, dan "tepat 1 baris" menjadi asersi jumlah pada hasil Search nama unik), serta mengubah page size Tab System Log dan Popup Changelog: User menjadi 100 sesudah Search berprefix agar seluruh baris (termasuk cascade) tampil dalam satu halaman sebelum asersi (langkah 19, 26, 33, 44; S-14).
- Tiga blok TC berpola sama (pemicu, Tab System Log aktor, padanan Popup Changelog: User) untuk kelas Object berbeda dan berdiri sendiri; 48 langkah (di atas smell 35 langkah) dipertahankan karena kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-570 butir b meminta entri cascade identik dengan baris di Popup Changelog: User, sedangkan TC-541 sampai TC-544 butir b menyatakan Popup Changelog: User tidak memuat baris cascade (cascade hanya di modal Global Role dan Group Role). Spec mengikuti TC-570 apa adanya; asersi Popup untuk cascade akan bertentangan dengan spec 158 dan 159 bila TC-541 benar.
  - TC-568 sampai TC-570 menyebut satu target `Mike Tan` untuk semua Action padahal state awal tiap Action berbeda (tier, Group Manager); spec memakai user terpisah bernama berprefix sama.
  - TC-570 tidak menyebut jumlah Global Role atau Group Role per group yang terdampak; spec mengasersi satu baris per role terdampak tanpa menyebut jumlah (daftar role dari katalog, disediakan tim FE).
  - TC-568 sampai TC-570 menyebut "Dependensi" tanpa mengisinya; spec men-seed pemicu lewat sesi API aktor (S-04). Nilai Field/Old/New TC-568 sampai TC-570 tidak ditulis di TC; spec memakai nilai dari TC-541 sampai TC-550.
  - Nama tampil akun Default User tidak tertulis di Pre-setup TC (hanya email).
