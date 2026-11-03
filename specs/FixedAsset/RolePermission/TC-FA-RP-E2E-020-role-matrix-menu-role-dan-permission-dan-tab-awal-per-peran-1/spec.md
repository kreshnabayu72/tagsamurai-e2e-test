---
id: TC-FA-RP-E2E-020-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-1
title: "Role Matrix: menu Role & Permission dan tab awal per peran (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-3
  - TC-FA-RP-77
  - TC-FA-RP-78
  - TC-FA-RP-79
  - TC-FA-RP-82
coverage:
  web: automated
---

# Role Matrix: menu Role & Permission dan tab awal per peran (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Manage global user & role tanpa Update (Pre-setup #8, role pertama pada tabel); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Role yang diuji (Role Matrix, bagian 3a); urutan baris = urutan pemakaian; spec ditulis per blok role karena ganti akun menuntut Step eksplisit:

| Role | Pre-setup | TC | Email | Env var password |
|---|---|---|---|---|
| Manage global user & role tanpa Update (Bayu Prakoso) | #8 | TC-FA-RP-3, TC-FA-RP-82 | `murReadOnlyGate_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.murGlobalReadOnly.email`) | `Spectra.env.FA_MUR_GLOBAL_RO_PASSWORD` |
| Total Control (Siti Rahmawati) | #2 | TC-FA-RP-77 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |
| Read Only (Dewi Anggraini) | #4 | TC-FA-RP-78 | `readOnly_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.readOnly.email`) | `Spectra.env.FA_RO_PASSWORD` |
| Group Manager (Fajar Nugroho, `IT Infrastructure`) | #5 | TC-FA-RP-79 | `groupManager_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.groupManager.email`) | `Spectra.env.FA_GM_PASSWORD` |

- Data Pre-setup (Company Alpha): #15 (pool pengguna; baris Tab Total Control) dan #17 (Home Group). Spec membaca pool dan hanya mengubah data seed di bullet berikut.
- Data Dinamis dan pemulihan (seed hook `before` lewat sesi API, pola spec 035 sampai 037): Gunawan Halim (Pre-setup #17, Home Group `Data Center`, dalam cakupan `IT Infrastructure`) ditetapkan Total Control. Seed ini menjamin Tab `Total Control` memuat sedikitnya satu baris bagi tiap aktor, termasuk aktor yang hanya melihat user dalam cakupan `IT Infrastructure`. Hook `after` mengembalikan Gunawan Halim ke kondisi Pre-setup #17 (tanpa tingkat akses).
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun ditambahkan tim FE.
- Kemampuan teknis: tidak ada tambahan. State global yang diubah hanya data seed milik spec di atas (dipulihkan atau dihapus hook `after`).

## Test Steps

### TC-FA-RP-82 dan TC-FA-RP-3: Manage global user & role tanpa Update

1. Verifikasi item `Role & Permission` tampil di sidebar Settings (Show)
2. Klik `Role & Permission`
3. Verifikasi Tab `Total Control` aktif
4. Verifikasi data Tab `Total Control` tampil (sedikitnya satu baris)
5. Verifikasi Breadcrumb tampil `Settings > Role & Permission > Total Control`

### TC-FA-RP-77: Total Control

6. Logout dari akun sebelumnya, lalu login sebagai Total Control dengan `Spectra.env.FA_TC_PASSWORD`
7. Verifikasi item `Role & Permission` tampil di sidebar Settings (Show)
8. Klik `Role & Permission`
9. Verifikasi Tab `Total Control` aktif
10. Verifikasi data Tab `Total Control` tampil (sedikitnya satu baris)

### TC-FA-RP-78: Read Only

11. Logout dari akun sebelumnya, lalu login sebagai Read Only dengan `Spectra.env.FA_RO_PASSWORD`
12. Verifikasi item `Role & Permission` tampil di sidebar Settings (Show)
13. Klik `Role & Permission`
14. Verifikasi Tab `Total Control` aktif
15. Verifikasi data Tab `Total Control` tampil (sedikitnya satu baris)

### TC-FA-RP-79: Group Manager

16. Logout dari akun sebelumnya, lalu login sebagai Group Manager dengan `Spectra.env.FA_GM_PASSWORD`
17. Verifikasi item `Role & Permission` tampil di sidebar Settings (Show)
18. Klik `Role & Permission`
19. Verifikasi Tab `Total Control` aktif
20. Verifikasi data Tab `Total Control` tampil (sedikitnya satu baris)

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-3, 77, 78, 79, 82). TC-FA-RP-80, 81, dan 83 ada di spec `TC-FA-RP-E2E-021-role-matrix-menu-role-dan-permission-dan-tab-awal-per-peran-2`.
- Spec Role Matrix ditulis per blok role (bagian 3a, keputusan 2026-10-30): langkah tiap role identik, tetapi ganti akun menuntut Step eksplisit karena akun pertama login di hook `before`.
- TC-FA-RP-3 dan TC-FA-RP-82 memakai role yang sama (Manage global user & role tanpa Update) dan langkah yang sama; keduanya dicakup satu blok. `Verifikasi` Tab `Total Control` aktif dan data tampil memenuhi expected a TC-FA-RP-3 dan expected b TC-FA-RP-82; Breadcrumb memenuhi expected b TC-FA-RP-3.
- Langkah penghubung (tanpa awalan `Verifikasi`): ganti akun (logout dan login role berikutnya) dan klik `Role & Permission`. Halaman Role & Permission sudah dibuka hook `beforeEach` suite untuk akun pertama; klik menu tetap dijalankan karena TC menguji membuka menu dari sidebar.
- Temuan untuk QA:
  - TC-FA-RP-3 dan TC-FA-RP-82 identik (role, langkah, dan expected a dan b); keduanya dipertahankan sebagai dua TC sumber pada satu blok.
  - TC-FA-RP-77 sampai 79 dan 82 menyebut "datanya tampil" tanpa data spesifik; spec memverifikasi sedikitnya satu baris tampil dan menjaminnya lewat seed Total Control ber-Home Group dalam cakupan di hook `before`.
  - Post Condition TC-FA-RP-3, 77, 78, 79, dan 82 tidak memberi langkah observasi tambahan; tidak diasersi.
