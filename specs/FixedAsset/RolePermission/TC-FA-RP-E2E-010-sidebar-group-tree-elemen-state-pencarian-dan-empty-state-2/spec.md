---
id: TC-FA-RP-E2E-010-sidebar-group-tree-elemen-state-pencarian-dan-empty-state-2
title: "Sidebar Group Tree: elemen, state, pencarian, dan empty state (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-32
  - TC-FA-RP-33
  - TC-FA-RP-34
coverage:
  web: automated
---

# Sidebar Group Tree: elemen, state, pencarian, dan empty state (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control Company Alpha (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control Company Alpha, `FA_TC_PASSWORD`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati), Company Alpha | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |
| Total Control pada `Company Kosong` (company tanpa node group) | #27 | disediakan tim FE (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA) | `Spectra.env.FA_EMPTY_TC_PASSWORD` |

- Data Pre-setup: #18 (pohon group Company Alpha, dipakai TC-FA-RP-32 dan 33), #27 (`Company Kosong`: hanya Default User dan Total Control, tanpa node group; dipakai TC-FA-RP-34).
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan nama group ditambahkan tim FE.
- Kemampuan teknis: akun Total Control `Company Kosong` disediakan tim FE. Spec tidak mengubah data dan tidak mengubah state global.

## Test Steps

### TC-FA-RP-32: Pencarian berjalan saat Enter dan reset saat input dikosongkan lalu Enter

1. Klik Tab `Group Manager`
2. Ketik `Data` pada kolom pencarian tree tanpa menekan Enter
3. Verifikasi pohon belum tersaring (pencarian bukan real-time)
4. Tekan Enter pada kolom pencarian tree
5. Verifikasi pohon tersaring ke node yang cocok `Data Center`
6. Kosongkan isi kotak pencarian tree, tekan Enter
7. Verifikasi pohon kembali tanpa filter

### TC-FA-RP-33: Empty state hasil pencarian kosong

8. Ketik Search tree `zzz`, tekan Enter
9. Verifikasi area pohon menampilkan Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
10. Kosongkan isi kotak pencarian tree, tekan Enter

### TC-FA-RP-34: Empty state saat client belum punya group

11. Logout dari akun Total Control Company Alpha, lalu login sebagai Total Control `Company Kosong` dengan `Spectra.env.FA_EMPTY_TC_PASSWORD`
12. Buka menu Settings > Role & Permission dari sidebar
13. Klik Tab `Group Manager`
14. Verifikasi panel Sidebar Group Tree menampilkan Illustration dengan Title `No group yet` dan Description `Select another item from the tree.`

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-32, 33, 34). TC-FA-RP-29, 30, 31 ada di spec `TC-FA-RP-E2E-009-sidebar-group-tree-elemen-state-pencarian-dan-empty-state-1`.
- Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`); ganti akun hanya satu kali sebelum TC-FA-RP-34.
- Langkah penghubung (tanpa awalan `Verifikasi`): klik tab, mengosongkan kotak pencarian tree sesudah TC-FA-RP-33 (pemulihan state sebelum pindah akun), ganti akun, dan membuka menu.
- Temuan untuk QA:
  - TC-FA-RP-34 hanya menyebut "company tanpa node group" tanpa rujukan Pre-setup; spec memakai `Company Kosong` (Pre-setup #27) dengan asumsi company itu juga belum punya group. Akun Total Control company itu tidak tertulis di Pre-setup TC dan disediakan tim FE.
  - TC-FA-RP-33 precondition d ("pencarian ... disiapkan pada langkah") dan expected tidak menyebut nilai awal kotak pencarian; spec memulai dari kotak kosong.
  - Post Condition TC-FA-RP-32, 33, dan 34 tidak memberi langkah observasi tambahan; tidak diasersi.
