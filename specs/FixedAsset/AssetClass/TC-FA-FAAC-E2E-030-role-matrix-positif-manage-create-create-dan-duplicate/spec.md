---
id: TC-FA-FAAC-E2E-030-role-matrix-positif-manage-create-create-dan-duplicate
title: "Role Matrix Positif: Manage Accounting (Read, Create) Create dan Duplicate Asset Class Berhasil"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-75
  - TC-FA-FAAC-76
coverage:
  web: automated
---

# Role Matrix Positif: Manage Accounting (Read, Create) Create dan Duplicate Asset Class Berhasil

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Manage accounting (Read, Create)) dilakukan di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Role yang diuji (tiap role memakai akunnya sendiri):

| Role | Akun | Env var password | TC |
|---|---|---|---|
| Manage accounting (Read, Create) | `manageAccountingReadCreate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_AC_MA_RC_PASSWORD` | TC-FA-FAAC-75, TC-FA-FAAC-76 |

- Env var: `FA_AC_MA_RC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`).
- Rujukan suite: seed dan pemulihan data lewat API/fixture BE, flag Guided Tooltip, dan sesi akun mengikuti `suite.md` (butir Hook suite). Suite berjalan serial (`parallel: false`).
- Data Pre-setup: sembilan Asset Class contoh (Tabel Data Uji Pre-setup; nilai mengikuti Example Data PRD §4.1.1): HEAVY-EQ, VEHICLES, IT-EQ, MACHINERY, BLDG, STORAGE, OFFICE-NEW, LAND (Active) dan OFFICE-OLD (Inactive). Identitasnya dirujuk lewat `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada; nama kunci ditetapkan tim FE); langkah memakai nama seed literal sesuai TC. VEHICLES dipakai sebagai sumber Duplicate (dibaca, tidak diubah).
- Tabel Asset Class memuat baris lain di luar sembilan Asset Class contoh (seed B-*, TEMP-EQ, dan sejenisnya); baris yang dipakai langkah dicari lewat Search kode Class Code karena tidak dijamin berada di halaman 1.
- Data Dinamis: Asset Class CRT-EQ (Class Name Create Only Equipment) dan VEH-CPY dibuat spec dengan kode literal sesuai TC (pengecualian beralasan atas S-12 untuk modul ini). Kode itu belum dipakai di awal spec; fixture BE (disediakan tim FE/BE) menghapus CRT-EQ dan VEH-CPY di hook `before` (R-13) dan `after`, termasuk bila spec gagal di tengah.
- State global yang diubah: tidak ada selain flag Guided Tooltip (dipulihkan hook suite).
- Kemampuan teknis: pengisian form Create (Select dan input), fixture BE untuk pembersihan kode literal.

## Test Steps

### TC-FA-FAAC-75

1. Klik [+ Asset Class]
2. Isi tab General: Class Code CRT-EQ, Class Name Create Only Equipment
3. Isi tab Depreciation: Method Straight Line, Useful Life 48, Tax Depreciation Class Bukan bangunan – Kelompok 1, Tax Method Straight Line
4. Klik [Submit]
5. Verifikasi toast "Success, asset class has been created." tampil
6. Verifikasi halaman Detail tetap terbuka dalam mode Edit dengan tab Asset Names aktif
7. Kembali ke tabel Asset Class lewat Breadcrumb Asset Class (form tersimpan, tidak ada perubahan belum tersimpan)

### TC-FA-FAAC-76

8. Ketik Search `VEHICLES`, tekan Enter
9. Klik tombol ⋯ pada baris VEHICLES lalu klik Duplicate
10. Verifikasi halaman Detail mode Create terbuka dengan Class Code kosong
11. Verifikasi Class Name "Vehicles"
12. Isi Class Code VEH-CPY
13. Klik [Submit]
14. Verifikasi toast "Success, asset class has been created." tampil setelah Submit

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix positif (bagian 3a): aksi tulis Create dan Duplicate berhasil bagi role dengan huruf Create; satu role, tanpa ganti akun.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 (kembali ke tabel dari Detail Asset Class yang baru dibuat, S-09).
- Post Condition TC-FA-FAAC-75 dan TC-FA-FAAC-76 (Asset Class berstatus Active tersimpan) tidak punya langkah observasi di TC dan tidak diasersi.
- Temuan untuk QA:
  - TC-FA-FAAC-75 tidak menyebut field akun pada tab Accounts; spec mengikuti TC tanpa mengisi akun, dan apakah akun wajib saat Submit tidak dijelaskan.
  - Class Code CRT-EQ dan VEH-CPY ditulis literal di TC (tanpa suffix per run); spec memakai literal itu dan fixture BE membersihkannya di hook `before` dan `after`.
