---
id: TC-FA-RP-E2E-108-persetujuan-registrasi-aset-aktivasi-toggle-dan-prasyarat-1
title: "Persetujuan registrasi aset: aktivasi toggle dan prasyarat (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-361
  - TC-FA-RP-362
  - TC-FA-RP-363
  - TC-FA-RP-364
  - TC-FA-RP-371
coverage:
  web: automated
---

# Persetujuan registrasi aset: aktivasi toggle dan prasyarat (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Akun aktor kedua (langkah 17, ganti akun eksplisit): Total Control pada `Company Isolated` (Pre-setup #35). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, kredensial `Spectra.env.FA_ISOLATED_TC_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #18 (pohon group), #21 (pemegang Update Manage asset & TAG: Ahmad Fauzi di `Head Office`, Budi Santoso di `IT Infrastructure`, Dimas Pranata di `Data Center`), #43 (Group Manager Fajar Nugroho di `IT Infrastructure`), #35 `Company Isolated` (`Helpdesk` tanpa Approver dan tanpa pemegang Update, tanpa Group Manager).
- Data Dinamis: tidak ada data yang dibuat spec.
- State yang diubah dan pemulihannya: toggle Require Approval for Registration pada `IT Infrastructure`, `Helpdesk`, `Data Center` (Company Alpha). Hook `after` memulihkan Pre-setup #21 dan #35 (toggle registrasi OFF pada node yang diubah) lewat fixture backend yang disediakan tim FE/BE.

## Test Steps

1. Klik Tab `System`
2. Buka Detail Role `Manage asset & TAG`

### TC-FA-RP-361: Aktifkan Require Approval for Registration saat ada pemegang Update pada scope node

3. Klik node `IT Infrastructure` pada Sidebar Group Tree
4. Aktifkan toggle `Require Approval for Registration`
5. Verifikasi toast sukses `Success, permissions have been updated.`
6. Verifikasi toggle `Require Approval for Registration` ON
7. Verifikasi panel tidak menyediakan pilihan OR/AND

### TC-FA-RP-362: Sub-label toggle registrasi

8. Verifikasi sub-label di bawah toggle tampil `New asset registrations in this group must be approved before the asset becomes active. Registrations already pending are not affected.`

### TC-FA-RP-364: Aktifkan registrasi saat hanya ada Group Manager yang menaungi node

9. Klik node `Helpdesk` pada Sidebar Group Tree
10. Aktifkan toggle `Require Approval for Registration`
11. Verifikasi toast sukses `Success, permissions have been updated.`
12. Verifikasi toggle `Require Approval for Registration` ON

### TC-FA-RP-371: Nilai registrasi per node, node anak tidak mewarisi dari induk

13. Klik node `IT Infrastructure` pada Sidebar Group Tree
14. Klik node `Data Center` pada Sidebar Group Tree
15. Verifikasi toggle `Require Approval for Registration` node `Data Center` OFF

### TC-FA-RP-363: Aktifkan registrasi tanpa pemegang Update dan tanpa Group Manager diblok dialog

16. Logout dari akun Total Control Company Alpha
17. Login sebagai Total Control `Company Isolated`
18. Klik Tab `System`
19. Buka Detail Role `Manage asset & TAG`
20. Klik node `Helpdesk` pada Sidebar Group Tree
21. Aktifkan toggle `Require Approval for Registration`
22. Verifikasi dialog blok severity warning dengan Title `Cannot Require Approval`, Body `Grant Update access on Manage asset & TAG to at least one user in this group before enabling approval.`, dan satu tombol `[OK]`
23. Klik `[OK]`
24. Verifikasi toggle `Require Approval for Registration` kembali OFF

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah menjadi 361, 362, 364, 371, 363: TC-FA-RP-363 memakai tenant `Company Isolated` sehingga diletakkan di akhir sesudah ganti akun eksplisit (langkah 16 dan 17); blok akun lain tidak melompat antar tenant.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 23 (menutup dialog blok). Langkah TC-FA-RP-362 yang menyebut node dan toggle terpenuhi oleh langkah 3 sampai 7; langkah 2 TC-FA-RP-371 ("aktifkan toggle") terpenuhi oleh langkah 4.
- Pembagian TC lintas spec: TC-FA-RP-372 (dua sesi UI Total Control yang diasersi, kelas c) ada di spec 296.
- Teks bertanda `copy usulan, PRD 12 #1` (sub-label, dialog `Cannot Require Approval`) diasersi literal sesuai TC dan bergantung pada persetujuan PM.
- Temuan untuk QA:
  - Email akun Total Control `Company Isolated` tidak tertulis di Pre-setup #35 maupun #1 sampai #11; akun disediakan tim FE.
  - TC-FA-RP-364 menulis node `Helpdesk` "tanpa pemegang Update pada scope", sedangkan Pre-setup #21 memberi pemegang Update di ancestor (`IT Infrastructure`: Budi Santoso, `Head Office`: Ahmad Fauzi) dan TC-FA-RP-1032 menyatakan pemegang Update di ancestor dihitung. Precondition itu perlu klarifikasi; spec mengikuti Langkah dan Expected TC.
  - Post Condition TC-FA-RP-361 sampai TC-FA-RP-371 tidak punya langkah observasi; tidak diasersi.
