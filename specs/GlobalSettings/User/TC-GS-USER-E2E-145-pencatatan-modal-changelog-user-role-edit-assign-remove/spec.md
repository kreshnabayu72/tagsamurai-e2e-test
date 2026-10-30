---
id: TC-GS-USER-E2E-145-pencatatan-modal-changelog-user-role-edit-assign-remove
title: "Pencatatan Modal Changelog User > Role: Edit Permission, Assign Role, dan Remove Role pada Satu User"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-926
  - TC-GS-USER-927
  - TC-GS-USER-928
coverage:
  web: automated
---

# Pencatatan Modal Changelog User > Role: Edit Permission, Assign Role, dan Remove Role pada Satu User

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor pertama: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca, tidak diubah): akun aktor Siti Nurhaliza (No. 2) sebagai pelaku (Modified By `Siti N`); role sistem `Manage TAG` dan `Manage files` (definisi role tetap, hanya penugasannya ke user seed yang berubah). User Pre-setup Ahmad Fauzi (No. 13) tidak dipakai karena aksi tulis memakai user seed milik spec (S-06).
- Data Dinamis milik spec, di-seed lewat API di hook `before` (HK1) dan dihapus di hook `after`: `Ahmad Fauzi {runId}-145`, Email `ahmadfauzi+{runId}-145@qwertysystem.net`, Activated, Division `Finance`, Access `Global Settings`, tanpa tier akses, role `Manage files` sudah Assigned, role `Manage TAG` belum di-assign. Penugasan role sistem adalah data milik spec; definisi role sistem bukan.
- Kemampuan teknis, disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut endpoint): seeding user dan penugasan role individual `Manage files` lewat API sebelum penanda baseline.
- State global: tidak ada. Suite berjalan serial (`suite.md`).
- Baseline log: penanda waktu dicatat pada langkah 2, sesudah hook `before` selesai dan sebelum aksi pemicu pertama (TC-GS-USER-927).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API user `Ahmad Fauzi {runId}-145` (penugasan role ikut hilang). Hook `before` menghapus sisa user bersuffix `-145` dari run lama. Entri log bersifat immutable dan tidak dihapus.

## Test Steps

### Pembukaan layar dan baseline

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Catat penanda waktu baseline (waktu saat ini) untuk Modal Changelog User > Role; baris yang diasersi adalah baris di atas penanda ini

### TC-GS-USER-927: Modal Changelog User > Role mencatat Assign

3. Buka Global Settings > Role & Permission, buka Tab System, klik Role Name `Manage TAG`, klik [+ Assign]
4. Isi Search Popup Table User Picker dengan `Ahmad Fauzi {runId}-145`, tekan Enter, centang barisnya, klik [Assign]
5. Tunggu aksi selesai (Popup tertutup)
6. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-145`, tekan Enter, klik Name `Ahmad Fauzi {runId}-145`, buka Tab Role, klik icon Changelog di Tab Role (Modal Changelog: User > Role)
7. Verifikasi Modal Changelog User > Role `Ahmad Fauzi {runId}-145`: baris di atas penanda baseline dengan Action `Assign`, Role `Manage TAG`, Field `Access`, Old Value `—`, New Value `Assigned`, Modified By `Siti N`
8. Tutup Modal Changelog User > Role

### TC-GS-USER-926: Modal Changelog User > Role mencatat Edit

9. Pada Tab Role, centang Update pada baris `Manage TAG`
10. Tunggu aksi selesai (checkbox tersimpan)
11. Klik icon Changelog di Tab Role (Modal Changelog: User > Role)
12. Verifikasi Modal Changelog User > Role `Ahmad Fauzi {runId}-145`: baris di atas penanda baseline dengan Action `Edit`, Role `Manage TAG`, Field `Update`, Old Value `Inactive`, New Value `Active`, Modified By `Siti N`
13. Tutup Modal Changelog User > Role

### TC-GS-USER-928: Modal Changelog User > Role mencatat Remove

14. Buka Global Settings > Role & Permission, buka Tab System, klik Role Name `Manage files`
15. Klik icon Search, ketik `Ahmad Fauzi {runId}-145`, tekan Enter, klik `⋯` pada baris `Ahmad Fauzi {runId}-145` > Remove
16. Klik [Remove] pada dialog Remove Access
17. Tunggu aksi selesai (dialog tertutup)
18. Buka Global Settings > User > User List, klik icon Search, ketik `Ahmad Fauzi {runId}-145`, tekan Enter, klik Name `Ahmad Fauzi {runId}-145`, buka Tab Role, klik icon Changelog di Tab Role (Modal Changelog: User > Role)
19. Verifikasi Modal Changelog User > Role `Ahmad Fauzi {runId}-145`: baris di atas penanda baseline dengan Action `Remove`, Role `Manage files`, Field `Access`, Old Value `Assigned`, New Value `—`, Modified By `Siti N`
20. Tutup Modal Changelog User > Role

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Urutan TC di spec: 927, 926, 928. 927 sebelum 926 karena baris `Manage TAG` baru ada di Tab Role Ahmad setelah di-assign (926 mencentang Update pada baris itu); 928 (Remove) paling akhir karena menghilangkan penugasan.
- Pembagian TC lintas spec: TC-GS-USER-903, 902, 904, dan 1052 (Assign, Edit, Remove role individual pada Changelog, System Log, dan Activity Log, termasuk Modal Changelog User > Role pada 1052) diverifikasi di spec `TC-GS-USER-E2E-144-pencatatan-tier-role-permission-dan-auto-revert`. TC-GS-USER-929 sampai 932 (tanpa entry per-role pada Assign dan Remove tier) diverifikasi di spec `TC-GS-USER-E2E-147-absence-log-no-op-lintas-user-pair-create-product-selector-dan-per-role`.
- Langkah penghubung (aksi tanpa `Verifikasi`): pencatatan penanda baseline (langkah 2), pembukaan Role & Permission dan pemilihan user di Popup Table User Picker, "Tunggu aksi selesai" (8b butir 8), pembukaan Modal Changelog User > Role lewat Detail user, dan penutupan modal.
- Modal Changelog User > Role milik satu user tidak diberi Search; baris dikenali lewat Action dan Role. Baris yang diasersi per TC adalah baris di atas penanda baseline.
- Temuan untuk QA:
  - TC-GS-USER-926: precondition tidak menyebut bahwa role `Manage TAG` harus sudah di-assign ke Ahmad Fauzi sebelum Update dicentang, sedangkan 927 men-assign role yang sama. Spec menjalankan 927 lebih dulu dan memakai user seed milik spec, bukan Ahmad Fauzi Pre-setup (No. 13).
  - TC-GS-USER-926 Langkah 1 ("Centang Update Manage TAG di Tab Role") tidak menyebut user target; spec memakai `Ahmad Fauzi {runId}-145` sesuai Langkah 2.
  - TC-GS-USER-927 dan 928 menyebut "dari Role & Permission" tanpa menyebut tab; spec memakai Tab System > Detail role karena penugasan role individual ada di Detail role (`role/PRD/role.md` §4.2).
  - TC slice ini tidak punya Post Condition.
