---
id: TC-FA-RP-E2E-004-screening-tab-transaction-role-dan-panel-sub-tab-2
title: "Screening Tab Transaction Role dan panel sub-tab (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-10
  - TC-FA-RP-11
  - TC-FA-RP-63
coverage:
  web: automated
---

# Screening Tab Transaction Role dan panel sub-tab (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #18 (pohon group), #20 (sub-tab Transfer pada `IT Infrastructure`: Require Approval ON, Approver Pandu Wijaya, aturan OR, Approval Scope `Both`; `Data Center`: Require Approval OFF), #21 (pemegang Update Manage asset & TAG, dipakai TC-FA-RP-63).
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan nama group ditambahkan tim FE.
- Kemampuan teknis: tidak ada tambahan. Spec tidak mengubah data dan tidak mengubah state global.

## Test Steps

### TC-FA-RP-10: Approval Scope hanya ada di sub-tab Transfer

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` di Sidebar Group Tree
3. Klik sub-tab `Transfer`
4. Verifikasi pada sub-tab `Transfer` toggle Require Approval tampil ON
5. Verifikasi pada sub-tab `Transfer` radio aturan tampil
6. Verifikasi pada sub-tab `Transfer` RadioGroup berlabel `Approval scope` tampil dengan tiga opsi `Origin only`, `Destination only`, `Both`
7. Verifikasi opsi `Both` terpilih
8. Klik sub-tab `Damaged`
9. Verifikasi pada sub-tab `Damaged` field Approval scope tidak tampil
10. Klik node `Data Center` di Sidebar Group Tree
11. Klik sub-tab `Transfer`
12. Verifikasi pada node `Data Center` sub-tab `Transfer` (toggle OFF) radio aturan tidak tampil
13. Verifikasi RadioGroup `Approval scope` tetap tampil dengan `Both` terpilih

### TC-FA-RP-11: Breadcrumb Tab Transaction Role tidak berubah saat sub-tab berganti

14. Verifikasi Breadcrumb tampil `Settings > Role & Permission > Transaction Role`
15. Klik sub-tab `Disposal`
16. Verifikasi Breadcrumb tetap `Settings > Role & Permission > Transaction Role`
17. Verifikasi sub-tab `Disposal` tidak menjadi segmen Breadcrumb

### TC-FA-RP-63: Panel Registration belum ada node group, card prompt menggantikan panel

18. Klik Tab `System`
19. Klik Role Name `Manage asset & TAG` pada section Group Role
20. Klik node `All Groups` di Sidebar Group Tree
21. Verifikasi panel diganti card prompt `Select a group from the sidebar to view and manage its approval settings.`
22. Verifikasi toggle `Require Approval for Registration` beserta ikon info `ⓘ` tidak tampil (Hidden)
23. Verifikasi tabel user assignments di bawah panel tetap tampil sebagai gabungan lintas group

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-10, 11, 63).
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, node, dan sub-tab; klik node `All Groups` pada Detail Role untuk memastikan Sidebar Group Tree pada `All Groups` (langkah 2 TC-FA-RP-63).
- Temuan untuk QA:
  - TC-FA-RP-10 expected c menyebut "RadioGroup `Approval scope` tetap tampil dengan `Both` terpilih" pada `Data Center` (toggle OFF); Pre-setup #20 tidak menyebut nilai Approval Scope `Data Center`. Spec mengasersi sesuai TC.
  - TC-FA-RP-63 memuat salinan bertanda `copy usulan, PRD 12 #1` (NC-02); asersi literal bergantung pada persetujuan PM.
  - Post Condition TC-FA-RP-10, 11, dan 63 tidak memberi langkah observasi tambahan; tidak diasersi.
