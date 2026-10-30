---
id: TC-GS-ROLE-E2E-004-badge-kondisional-pending-activation-lintas-surface
title: "Badge Kondisional Pending Activation di Sebelah Name pada Tab Total Control, Detail, dan Popup Assign Role"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-12
  - TC-GS-ROLE-13
coverage:
  web: automated
---

# Badge Kondisional Pending Activation di Sebelah Name pada Tab Total Control, Detail, dan Popup Assign Role

## Prerequisites

- Mode: FE+BE.
- Aktor: Ahmad Fauzi (Total Control, Pre-setup #1), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `after` mengembalikan sesi ke akun default suite (akun yang sama). Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Role & Permission dengan Tab Total Control aktif.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti hook suite (lihat `suite.md`).
- Data Pre-setup:
  - Rudi Hartono (Pending Activation, Pre-setup #11): di hook `before`, Ahmad Fauzi (lewat API, kemampuan disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD) meng-assign access level Total Control kepada Rudi Hartono sehingga Rudi Hartono menjadi Total Control dan punya baris role Manage TAG (Given TC-GS-ROLE-12 dan TC-GS-ROLE-13, keadaan hasil Assign TC-GS-ROLE-59). Hook `after` memulihkan Rudi Hartono ke kondisi Pre-setup #11 (tanpa access level Total Control dan tanpa baris role hasil Assign) lewat API yang sama.
  - Yoga Pratama (Pending Activation, Active Access Global Settings, tanpa baris role; Pre-setup #18, kandidat fixture sekali pakai). Spec hanya mengamati Yoga Pratama di popup dan tidak mengubahnya.
- Kemampuan teknis: pembacaan atribut tampilan badge (tipe warning).

## Test Steps

### TC-GS-ROLE-12: Badge Pending Activation di sebelah Name pada Tab Total Control

1. Ketik Search `Rudi Hartono`, tekan Enter
2. Verifikasi badge "Pending Activation" tampil di sebelah Name pada baris `Rudi Hartono`
3. Verifikasi badge "Pending Activation" bertipe warning
4. Verifikasi kolom Status baris `Rudi Hartono` menampilkan status user (Active atau Inactive), bukan "Pending Activation"
5. Klik `(←)` pada kotak Search

### TC-GS-ROLE-13: Badge Pending Activation di sebelah Name pada Detail dan Table User Picker

6. Klik Tab System
7. Klik Role Name `Manage TAG`
8. Ketik Search `Rudi Hartono`, tekan Enter
9. Verifikasi badge "Pending Activation" tampil di sebelah Name pada baris `Rudi Hartono` di Detail "Manage TAG"
10. Verifikasi badge "Pending Activation" bertipe warning
11. Klik `(←)` pada kotak Search
12. Klik `[+ Assign]`
13. Ketik Search `Yoga Pratama`, tekan Enter
14. Verifikasi badge "Pending Activation" tampil di sebelah Name pada baris `Yoga Pratama` di popup Assign Role
15. Verifikasi badge "Pending Activation" bertipe warning
16. Klik `✕` pada header popup Assign Role

## Notes

- Mode: FE+BE. Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa `Verifikasi`): mencari nama dengan Search dan mengosongkannya (langkah 1, 5, 8, 11, 13) karena posisi baris di halaman 1 tidak dapat dipastikan; pindah ke Tab System dan membuka Detail (langkah 6 dan 7) sebagai pembuka TC-GS-ROLE-13 langkah 1; menutup popup (langkah 16). Popup Assign Role tidak diubah sehingga `✕` tidak memunculkan dialog `Unsaved Changes`.
- Expected "badge (warning)" dipecah menjadi dua `Verifikasi` (badge tampil di sebelah Name; badge bertipe warning) mengikuti S-01.
- TC-GS-ROLE-12 Expected b ("Status menampilkan Active/Inactive sesuai status user") diasersi sebagai nilai status user, bukan "Pending Activation" (langkah 4); nilai pasti (Active atau Inactive) tidak disebut TC.
- Temuan untuk QA:
  - TC-GS-ROLE-12 Expected b tidak menyebut status user Rudi Hartono (Active atau Inactive); Pre-setup #11 hanya menyebut "Pending Activation" sehingga nilai pasti tidak diasersi.
  - TC-GS-ROLE-13 memakai pencarian Rudi Hartono di Detail tanpa menyebut halamannya; spec memakai Search.
  - TC-GS-ROLE-12 dan TC-GS-ROLE-13 bergantung pada TC-GS-ROLE-59 (Dependensi); spec menyiapkan keadaan Given itu sendiri di hook `before` tanpa menjalankan TC-GS-ROLE-59.
