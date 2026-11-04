---
id: TC-FA-LIC-E2E-029-role-matrix-tombol-edit-show-disabled-hidden-per-role
title: "Role Matrix: Tombol Edit Show dan Hidden per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-97
  - TC-FA-LIC-98
  - TC-FA-LIC-620
coverage:
  web: automated
---

# Role Matrix: Tombol Edit Show dan Hidden per Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun lain pada tabel "Role yang diuji" lewat langkah Ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; seluruh nama env pada tabel adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Role yang diuji (Tabel Data Uji Pre-setup #1, #2, #3, #7):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-FA-LIC-97 | Total Control (Pre-setup #1) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| TC-FA-LIC-97 | Manage global license (Pre-setup #3) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |
| TC-FA-LIC-97 | Default User (Pre-setup #7) | `defaultUser_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_DU_PASSWORD` |
| TC-FA-LIC-98, TC-FA-LIC-620 | Read Only (Pre-setup #2) | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |

- Data Pre-setup #12 (`Fixture.fixedAssetLicense.kuotaHierarki`): hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT (beralokasi 100 tanpa subgroup), Divisi Keuangan), Cabang Surabaya, Cabang Medan dengan alokasi, Used, dan Reserved sesuai Example Data PRD §4.1.3; disediakan tim FE/BE.
- Spec hanya mengamati tombol dan tooltip; tidak ada data yang diubah.
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.
- Suite serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### TC-FA-LIC-97: Tombol Edit Show pada semua grup untuk Total Control, Manage global license, dan Default User

1. Buka Tab `Allocation Quota`
2. Verifikasi tombol ikon `[Edit]` tampil di samping Allocated Quota semua grup level 1 pada node `All Groups` (Total Control)
3. Klik node `Kantor Pusat`
4. Verifikasi `[Edit]` tampil di samping Total pada Group Quota Summary Kantor Pusat (Total Control)
5. Klik node `Divisi Logistik`
6. Verifikasi `[Edit]` tampil di samping Total pada Group Quota Summary Divisi Logistik (Total Control)
7. Ganti akun: logout, lalu login sebagai Manage global license dengan `Spectra.env.FA_MGL_PASSWORD`
8. Buka Tab `Allocation Quota`
9. Verifikasi `[Edit]` tampil di samping Allocated Quota semua grup level 1 pada node `All Groups` (Manage global license)
10. Klik node `Kantor Pusat`
11. Verifikasi `[Edit]` tampil di samping Total pada Group Quota Summary Kantor Pusat (Manage global license)
12. Klik node `Divisi Logistik`
13. Verifikasi `[Edit]` tampil di samping Total pada Group Quota Summary Divisi Logistik (Manage global license)
14. Ganti akun: logout, lalu login sebagai Default User dengan `Spectra.env.FA_DU_PASSWORD`
15. Buka Tab `Allocation Quota`
16. Verifikasi `[Edit]` tampil di samping Allocated Quota semua grup level 1 pada node `All Groups` (Default User)
17. Klik node `Kantor Pusat`
18. Verifikasi `[Edit]` tampil di samping Total pada Group Quota Summary Kantor Pusat (Default User)
19. Klik node `Divisi Logistik`
20. Verifikasi `[Edit]` tampil di samping Total pada Group Quota Summary Divisi Logistik (Default User)

### TC-FA-LIC-98: Tombol Edit Hidden untuk Read Only di semua lokasi

21. Ganti akun: logout, lalu login sebagai Read Only dengan `Spectra.env.FA_RO_PASSWORD`
22. Buka Tab `Allocation Quota`
23. Verifikasi Section 2 node `All Groups` memuat baris grup level 1
24. Verifikasi tidak ada tombol `[Edit]` di samping Allocated Quota (modal Edit Allocation tidak dapat dibuka dan field Allocated Quota tidak dapat dikosongkan)
25. Klik node `Kantor Pusat`
26. Verifikasi Group Quota Summary Kantor Pusat tampil
27. Verifikasi tidak ada tombol `[Edit]` di samping Total

### TC-FA-LIC-620: Tombol Edit Hidden pada baris Divisi IT untuk Read Only

28. Verifikasi Section 2 node `Kantor Pusat` memuat baris `Divisi IT`
29. Verifikasi tombol `[Edit]` Hidden pada baris `Divisi IT` (modal Edit Allocation tidak dapat dibuka dan field Allocated Quota tidak dapat dikosongkan)

## Notes

- Spec Role Matrix (bagian 3a konvensi) atas tombol Edit yang memuat dua polaritas (Show dan Hidden); ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung: "Buka Tab `Allocation Quota`" setelah ganti akun; hook `beforeEach` suite membuka halaman License saja.
- Asersi `[Edit]` Hidden (TC-FA-LIC-98 dan TC-FA-LIC-620) didahului `Verifikasi` baris grup atau Group Quota Summary tampil sebagai anchor positif. Kesimpulan "modal Edit Allocation tidak dapat dibuka dan field tidak dapat dikosongkan" tidak teramati terpisah dan menjadi bagian dari `Verifikasi` tombol `[Edit]` Hidden. TC-FA-LIC-620 berjalan pada sesi Read Only dan node `Kantor Pusat` yang sama dengan langkah 25; baris `Divisi IT` ada di Section 2 node tersebut, sehingga tidak ada langkah navigasi tambahan.
- Temuan untuk QA:
  - TC-FA-LIC-97 menyebut tombol Edit "di samping Total pada Group Quota Summary tiap node" tetapi langkahnya hanya membuka node Kantor Pusat dan Divisi Logistik; spec mengasersi dua node itu.
