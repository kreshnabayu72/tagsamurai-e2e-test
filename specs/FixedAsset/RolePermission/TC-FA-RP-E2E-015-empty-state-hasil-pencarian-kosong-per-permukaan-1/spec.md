---
id: TC-FA-RP-E2E-015-empty-state-hasil-pencarian-kosong-per-permukaan-1
title: "Empty state hasil pencarian kosong per permukaan (1/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-47
  - TC-FA-RP-55
  - TC-FA-RP-56
  - TC-FA-RP-57
  - TC-FA-RP-58
coverage:
  web: automated
---

# Empty state hasil pencarian kosong per permukaan (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Group Manager (Pre-setup #5, Fajar Nugroho); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Akun aktor (password hanya lewat env); urutan baris = urutan pemakaian:

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Group Manager (Fajar Nugroho, `IT Infrastructure`) | #5 | `groupManager_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.groupManager.email`) | `Spectra.env.FA_GM_PASSWORD` |
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #15 (pool pengguna), #18 (pohon group), #43 (seed Group Manager). Precondition TC-FA-RP-47: tidak ada user Total Control ber-Home Group dalam cakupan `IT Infrastructure` beserta descendant; dijamin fixture backend yang disediakan tim FE/BE.
- Data uji: keyword Search `zzzz` (TC-FA-RP-55 sampai 58); tidak menghasilkan baris pada permukaan mana pun.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun dan keyword ditambahkan tim FE.
- Kemampuan teknis: tidak ada tambahan. Spec tidak mengubah data atau state global.

## Test Steps

### TC-FA-RP-47: Tab Total Control kosong dalam cakupan Group Manager tanpa Home Group user

1. Verifikasi Illustration dengan Title `No users assigned` dan Description `Assign users to grant permissions for this role.` pada Tab `Total Control`
2. Verifikasi baris Default User dan Total Control tanpa Home Group dalam cakupan tidak tampil di tabel

### Ganti akun ke Total Control

3. Logout dari akun Group Manager, lalu login sebagai Total Control dengan `Spectra.env.FA_TC_PASSWORD`
4. Buka menu Settings > Role & Permission dari sidebar

### TC-FA-RP-55: Tab Total Control, empty state hasil pencarian kosong

5. Ketik Search `zzzz`, tekan Enter
6. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
7. Verifikasi tabel tidak menampilkan baris
8. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-FA-RP-57: Tab Group Manager, empty state hasil pencarian kosong

9. Klik Tab `Group Manager`
10. Ketik Search `zzzz`, tekan Enter
11. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
12. Verifikasi tabel tidak menampilkan baris
13. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-FA-RP-58: Tab System, empty state hasil pencarian kosong

14. Klik Tab `System`
15. Ketik Search `zzzz`, tekan Enter
16. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
17. Verifikasi tabel tidak menampilkan baris
18. Verifikasi baris katalog tidak ditampilkan
19. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-FA-RP-56: Detail Role, empty state hasil pencarian kosong

20. Klik Role Name `Manage Open API` pada section Global Role
21. Ketik Search `zzzz`, tekan Enter
22. Verifikasi Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
23. Verifikasi tabel tidak menampilkan baris

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-47, 55, 56, 57, 58). Spec ditulis per blok akun karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`); ganti akun pada langkah 3.
- Urutan TC di spec: TC-FA-RP-47 (Group Manager), lalu TC-FA-RP-55, 57, 58, 56 (Total Control); TC-FA-RP-56 diletakkan terakhir karena Detail Role dibuka dari Tab System sehingga tidak perlu kembali ke tab lain.
- Langkah penghubung (tanpa awalan `Verifikasi`): ganti akun, membuka menu, klik tab dan Role Name, dan klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel sebelum pindah permukaan. Tab `Total Control` TC-FA-RP-47 sudah terbuka oleh hook `beforeEach` suite (padanan langkah 1 TC-FA-RP-47). Search memakai bagian 8b butir 9 (ketik lalu Enter).
- Absence baris pada TC-FA-RP-47 dan "baris katalog tidak ditampilkan" pada TC-FA-RP-58 didahului empty state yang sama sebagai anchor positif permukaan.
- Temuan untuk QA:
  - TC-FA-RP-47 precondition d mensyaratkan tidak ada user ber-Home Group dalam cakupan `IT Infrastructure`, sedangkan Pre-setup #17 memuat Joko Santoso (Home Group `IT Infrastructure`) dan Gunawan Halim (Home Group `Data Center`) sebagai pengguna Standard; spec mengikuti precondition (tidak ada Total Control ber-Home Group dalam cakupan).
  - TC-FA-RP-58 expected menyebut "tabel tidak menampilkan baris" dan "baris katalog tidak ditampilkan" sebagai dua klausa; spec memverifikasi keduanya terpisah.
  - Post Condition TC-FA-RP-47, 55, 56, 57, dan 58 tidak memberi langkah observasi tambahan; tidak diasersi.
