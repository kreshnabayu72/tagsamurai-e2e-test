---
id: TC-FA-RP-E2E-021-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-2
title: "Role Matrix: menu Role & Permission dan tab awal per peran (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-80
  - TC-FA-RP-81
  - TC-FA-RP-83
coverage:
  web: automated
---

# Role Matrix: menu Role & Permission dan tab awal per peran (2/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage global user & role (Update) (Pre-setup #6, role pertama pada tabel); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Role yang diuji (Role Matrix, bagian 3a); urutan baris = urutan pemakaian; spec ditulis per blok role karena ganti akun menuntut Step eksplisit:

| Role | Pre-setup | TC | Email | Env var password |
|---|---|---|---|---|
| Manage global user & role (Update) (Hendra Wijaya) | #6 | TC-FA-RP-80 | `murGlobal_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGlobal.email`) | `Spectra.env.FA_MUR_GLOBAL_PASSWORD` |
| Manage user & role (Group, Update, `IT Infrastructure`) (Gita Maharani) | #7 | TC-FA-RP-81 | `murGroup_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGroup.email`) | `Spectra.env.FA_MUR_GROUP_PASSWORD` |
| Manage user & role (Group) tanpa Update (`IT Infrastructure`) (Wulan Sari) | #9 | TC-FA-RP-83 | `murGroupReadOnly_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGroupReadOnly.email`) | `Spectra.env.FA_MUR_GROUP_RO_PASSWORD` |

- Data Pre-setup (Company Alpha): #15 (pool pengguna; baris Tab Total Control) dan #17 (Home Group). Spec membaca pool dan hanya mengubah data seed di bullet berikut.
- Data Dinamis dan pemulihan (seed hook `before` lewat sesi API, pola spec 035 sampai 037): Gunawan Halim (Pre-setup #17, Home Group `Data Center`, dalam cakupan `IT Infrastructure`) ditetapkan Total Control. Seed ini menjamin Tab `Total Control` memuat sedikitnya satu baris bagi tiap aktor, termasuk aktor yang hanya melihat user dalam cakupan `IT Infrastructure`. Hook `after` mengembalikan Gunawan Halim ke kondisi Pre-setup #17 (tanpa tingkat akses).
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun ditambahkan tim FE.
- Kemampuan teknis: tidak ada tambahan. State global yang diubah hanya data seed milik spec di atas (dipulihkan atau dihapus hook `after`).

## Test Steps

### TC-FA-RP-80: Manage global user & role (Update)

1. Verifikasi item `Role & Permission` tampil di sidebar Settings (Show)
2. Klik `Role & Permission`
3. Verifikasi Tab `Total Control` aktif
4. Verifikasi data Tab `Total Control` tampil (sedikitnya satu baris)

### TC-FA-RP-81: Manage user & role (Group, Update, `IT Infrastructure`)

5. Logout dari akun sebelumnya, lalu login sebagai Manage user & role (Group, Update) dengan `Spectra.env.FA_MUR_GROUP_PASSWORD`
6. Verifikasi item `Role & Permission` tampil di sidebar Settings (Show)
7. Klik `Role & Permission`
8. Verifikasi Tab `Total Control` aktif
9. Verifikasi data Tab `Total Control` tampil (sedikitnya satu baris)

### TC-FA-RP-83: Manage user & role tanpa Update (Group, `IT Infrastructure`)

10. Logout dari akun sebelumnya, lalu login sebagai Manage user & role (Group) tanpa Update dengan `Spectra.env.FA_MUR_GROUP_RO_PASSWORD`
11. Verifikasi item `Role & Permission` tampil di sidebar Settings (Show)
12. Klik `Role & Permission`
13. Verifikasi Tab `Total Control` aktif
14. Verifikasi data Tab `Total Control` tampil (sedikitnya satu baris)

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-80, 81, 83). TC-FA-RP-3, 77, 78, 79, dan 82 ada di spec `TC-FA-RP-E2E-020-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-1`.
- Spec Role Matrix ditulis per blok role (bagian 3a, keputusan 2026-10-30): langkah tiap role identik, tetapi ganti akun menuntut Step eksplisit karena akun pertama login di hook `before`.
- Langkah penghubung (tanpa awalan `Verifikasi`): ganti akun (logout dan login role berikutnya) dan klik `Role & Permission`. Halaman Role & Permission sudah dibuka hook `beforeEach` suite untuk akun pertama; klik menu tetap dijalankan karena TC menguji membuka menu dari sidebar.
- Temuan untuk QA:
  - TC-FA-RP-80, 81, dan 83 menyebut "datanya tampil" tanpa data spesifik; spec memverifikasi sedikitnya satu baris tampil dan menjaminnya lewat seed Total Control ber-Home Group dalam cakupan di hook `before`.
  - Post Condition TC-FA-RP-80, 81, dan 83 tidak memberi langkah observasi tambahan; tidak diasersi.
