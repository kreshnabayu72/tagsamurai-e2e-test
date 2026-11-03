---
id: TC-FA-LIC-E2E-032-role-matrix-remove-allocation-dengan-mengosongkan-field
title: "Role Matrix: Mengosongkan Field Allocated Quota, Total Control dan Manage Global License Dapat, Read Only Tanpa Tombol Edit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-107
coverage:
  web: automated
---

# Role Matrix: Mengosongkan Field Allocated Quota, Total Control dan Manage Global License Dapat, Read Only Tanpa Tombol Edit

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control (Pre-setup #1): `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, kata sandi `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; akun lain pada tabel "Role yang diuji" lewat langkah Ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1). Password tidak ditulis di spec atau fixture; seluruh nama env pada tabel adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Role yang diuji (Tabel Data Uji Pre-setup #1, #2, #3):

| TC | Role | Email | Env var password |
|---|---|---|---|
| TC-FA-LIC-107 | Total Control (Pre-setup #1) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| TC-FA-LIC-107 | Manage global license (Pre-setup #3) | `manageGlobalLicense_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGL_PASSWORD` |
| TC-FA-LIC-107 | Read Only (Pre-setup #2) | `readOnlyFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` |

- Data Pre-setup #12 (`Fixture.fixedAssetLicense.kuotaHierarki`): hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan dengan alokasi, Used, dan Reserved sesuai Example Data PRD §4.1.3; disediakan tim FE/BE. Divisi IT beralokasi 100 tanpa subgroup.
- Spec ini tidak menyimpan perubahan: modal Edit Allocation ditutup lewat `[×]` dan `[Leave]`, sehingga alokasi Pre-setup #12 tidak berubah. Suite serial (`parallel: false`).
- Hook dan kemampuan suite (fixture BE penyetel state, sesi API aktor, flag Guided Tooltip): dinyatakan sekali di `suite.md`.

## Test Steps

### TC-FA-LIC-107: Mengosongkan field Allocated Quota dapat dilakukan Total Control dan Manage global license; Read Only tanpa tombol Edit

1. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
2. Klik `[Edit]` pada Divisi IT
3. Klik `[Clear Field]`
4. Verifikasi field Allocated Quota dapat dikosongkan (Total Control)
5. Tutup modal Edit Allocation dengan `[×]`
6. Verifikasi dialog `Unsaved Changes` tampil
7. Klik `[Leave]`
8. Ganti akun: logout, lalu login sebagai Manage global license dengan `Spectra.env.FA_MGL_PASSWORD`
9. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
10. Klik `[Edit]` pada Divisi IT
11. Klik `[Clear Field]`
12. Verifikasi field Allocated Quota dapat dikosongkan (Manage global license)
13. Tutup modal Edit Allocation dengan `[×]`
14. Verifikasi dialog `Unsaved Changes` tampil
15. Klik `[Leave]`
16. Ganti akun: logout, lalu login sebagai Read Only dengan `Spectra.env.FA_RO_PASSWORD`
17. Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`
18. Verifikasi baris Divisi IT tampil
19. Verifikasi tombol `[Edit]` Hidden untuk Divisi IT sehingga modal Edit Allocation tidak dapat dibuka dan field tidak dapat dikosongkan (Read Only)

## Notes

- Spec Role Matrix positif (bagian 3a konvensi) atas pengosongan field Allocated Quota; ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). TC-FA-LIC-103, 528, dan 529 ada di spec `TC-FA-LIC-E2E-170`.
- Alasan tidak dipisah per polaritas (bagian 3a): TC-FA-LIC-107 adalah satu TC yang memuat eksekusi sukses (Total Control, Manage global license) dan visibilitas tombol `[Edit]` (Read Only). Memecahnya ke dua spec membuat satu TC tercakup di dua spec non-mock (temuan C2), yang tidak diizinkan konvensi; pemisahan menunggu TC-107 dipecah di sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): "Buka Tab `Allocation Quota`, lalu klik node `Kantor Pusat`" setelah ganti akun. Modal dengan field yang dikosongkan ditutup deterministik lewat `[×]`, dialog `Unsaved Changes`, dan `[Leave]` (S-08); TC menulis "tutup tanpa Save".
- Asersi `[Edit]` Hidden pada Read Only didahului `Verifikasi baris Divisi IT tampil` sebagai anchor positif.
- Temuan untuk QA:
  - TC-FA-LIC-107 menyatakan modal dibuka "tutup tanpa Save" tanpa menyebut dialog `Unsaved Changes`; spec mengikuti S-08.
