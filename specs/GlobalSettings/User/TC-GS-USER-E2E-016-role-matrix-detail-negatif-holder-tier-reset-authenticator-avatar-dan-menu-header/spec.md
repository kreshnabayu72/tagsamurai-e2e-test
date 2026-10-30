---
id: TC-GS-USER-E2E-016-role-matrix-detail-negatif-holder-tier-reset-authenticator-avatar-dan-menu-header
title: "Role Matrix Negatif: Reset Authenticator, Hover Avatar, dan Menu Header User Detail untuk Holder Full CRUD, Delete-Only, dan Create-Only"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-997
  - TC-GS-USER-998
  - TC-GS-USER-999
  - TC-GS-USER-1003
  - TC-GS-USER-1072
coverage:
  web: automated
---

# Role Matrix Negatif: Reset Authenticator, Hover Avatar, dan Menu Header User Detail untuk Holder Full CRUD, Delete-Only, dan Create-Only

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Role yang diuji (tiap role memakai akunnya sendiri; langkah ganti akun ditulis eksplisit di Test Steps):

| Role | Akun (Tabel Data Uji Pre-setup) | Nama user | Env var password | Target dan TC |
|---|---|---|---|---|
| Manage user and role (Full CRUD) | `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (No. 4) | Fajar Nugroho | `Spectra.env.GS_FULLCRUD_PASSWORD` | Andi Wijaya (tier Total Control): TC-GS-USER-997, TC-GS-USER-999 |
| Manage user and role (Delete-Only: R+D) | `manageUserDelete_automated_{namaCompany}@qwertysystem.net` (No. 7) | Citra Melati | `Spectra.env.GS_DELETE_PASSWORD` | Dewi Lestari: TC-GS-USER-998; John Doe: TC-GS-USER-1072 |
| Manage user and role (Create-Only: C+R) | `manageUserCreate_automated_{namaCompany}@qwertysystem.net` (No. 5) | Lestari Ayu | `Spectra.env.GS_CREATE_PASSWORD` | Dewi Lestari: TC-GS-USER-1003 |

- Login akun Full CRUD (aktor pertama spec) dilakukan di hook `before`; Delete-Only dan Create-Only memakai langkah ganti akun eksplisit. Karena spec berakhir di akun Create-Only, hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Env var: `GS_FULLCRUD_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca; spec tidak membuat, mengubah, atau menghapus data): Andi Wijaya (No. 10, tier Total Control), Dewi Lestari (No. 12), John Doe (No. 18, MFA Enrolled, punya foto). State berikut dibutuhkan TC tetapi tidak tercantum di Tabel Pre-setup sehingga disediakan tim FE/BE: Andi Wijaya MFA Enrolled dan punya foto (TC-GS-USER-997, TC-GS-USER-999), Dewi Lestari MFA Enrolled (TC-GS-USER-998).
- Kemampuan teknis: hover elemen termasuk elemen disabled untuk membaca tooltip; membaca state tampil/Hidden dan enabled/disabled.
- State global yang diubah: tidak ada. Cleanup: tidak ada data dibuat; hook `after` hanya memulihkan sesi.

## Test Steps

### TC-GS-USER-997: Reset Authenticator target bertier untuk holder Update, Disabled dengan tooltip tier

1. Buka Global Settings > User > User List (sub-tab Login User)
2. Klik icon Search, ketik `Andi Wijaya`, tekan Enter
3. Klik Name `Andi Wijaya` untuk membuka Detail
4. Hover `Reset Authenticator`
5. Verifikasi `Reset Authenticator` tampil namun disabled
6. Verifikasi tooltip `Reset Authenticator` `"You don't have permission to edit."`

### TC-GS-USER-999: Hover Avatar target bertier untuk holder, [Edit]/[Delete] Disabled dengan tooltip tier

7. Hover Avatar header
8. Verifikasi overlay `[Edit]` dan `[Delete]` tampil namun disabled
9. Hover `[Edit]`
10. Verifikasi tooltip `[Edit]` `"You don't have permission to edit."`
11. Hover `[Delete]`
12. Verifikasi tooltip `[Delete]` `"You don't have permission to edit."`

### TC-GS-USER-998: Reset Authenticator Hidden untuk holder tanpa Update

13. Logout, lalu login sebagai Manage user and role (Delete-Only: R+D)
14. Buka Global Settings > User > User List (sub-tab Login User)
15. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
16. Klik Name `Dewi Lestari` untuk membuka Detail
17. Verifikasi badge `Enrolled` tampil
18. Verifikasi tombol `Reset Authenticator` Hidden

### TC-GS-USER-1072: Hover Avatar tidak menampilkan [Edit]/[Delete] untuk holder tanpa Update

19. Klik menu User di sidebar Global Settings
20. Klik icon Search, ketik `John Doe`, tekan Enter
21. Klik Name `John Doe` untuk membuka Detail
22. Hover Avatar header
23. Verifikasi Avatar header tampil
24. Verifikasi nama `John Doe` tampil
25. Verifikasi overlay `[Edit]` dan `[Delete]` Hidden (tidak dirender)

### TC-GS-USER-1003: Menu [⋯] header Detail Hidden untuk holder tanpa Update dan Delete

26. Logout, lalu login sebagai Manage user and role (Create-Only: C+R)
27. Buka Global Settings > User > User List (sub-tab Login User)
28. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
29. Klik Name `Dewi Lestari` untuk membuka Detail
30. Verifikasi nama `Dewi Lestari` tampil di header Detail
31. Verifikasi menu `[⋯]` header tidak dirender

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber diubah: TC-GS-USER-999 mengikuti TC-GS-USER-997 pada Detail Andi Wijaya yang sama (satu kali membuka Detail untuk dua TC, langkah 1 TC-GS-USER-999 "Klik Name `Andi Wijaya`" dipenuhi oleh langkah 3). TC dikelompokkan per akun (Full CRUD, Delete-Only, Create-Only) supaya ganti akun hanya dua kali.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 2, 15, 20, dan 28 (Search nama target sebelum membuka Detail), 13 dan 26 (ganti akun), 14 dan 27 (membuka User List sesudah ganti akun), 19 (kembali ke User List).
- Asersi absence didahului anchor (bagian 8b butir 2): langkah 17 (badge `Enrolled` tampil) mendahului langkah 18; langkah 23 dan 24 (Avatar dan nama tampil) mendahului langkah 25 (urutan Expected a dan b TC-GS-USER-1072 dibalik karena Expected b menjadi anchor Expected a); langkah 30 (nama target tampil di header Detail) mendahului langkah 31, anchor ini tidak ada di TC dan ditambahkan hanya sebagai anchor.
- Pembagian TC lintas spec: Role Matrix kontrol header dan section Detail untuk aktor Total Control dan Full CRUD ada di spec 015; Role Matrix Detail untuk Read Only dan holder Read-only role ada di spec 009.
- Temuan untuk QA:
  - TC-GS-USER-997, 998, dan 999 mensyaratkan Andi Wijaya MFA Enrolled dan berfoto serta Dewi Lestari MFA Enrolled, tetapi Tabel Data Uji Pre-setup (No. 10 dan 12) tidak menyebut status MFA dan foto kedua user itu; disediakan tim FE/BE.
  - TC-GS-USER-1072 menyebut `[Edit]` dan `[Delete]` Hidden tanpa menyebut anchor pembanding; spec memakai Avatar dan nama sebagai anchor (Expected b).
