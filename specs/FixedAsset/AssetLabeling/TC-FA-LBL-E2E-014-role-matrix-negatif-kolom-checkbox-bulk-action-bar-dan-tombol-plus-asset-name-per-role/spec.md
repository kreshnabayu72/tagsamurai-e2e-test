---
id: TC-FA-LBL-E2E-014-role-matrix-negatif-kolom-checkbox-bulk-action-bar-dan-tombol-plus-asset-name-per-role
title: "Role Matrix Negatif: Kolom Checkbox, Bulk Action Bar, dan Tombol [➕] Asset Name per Role"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-205
  - TC-FA-LBL-524
coverage:
  web: automated
---

# Role Matrix Negatif: Kolom Checkbox, Bulk Action Bar, dan Tombol [➕] Asset Name per Role

## Prerequisites

- Mode: FE+BE.
- Hook suite: `before`, `beforeEach`, dan `after` berlaku sesuai `suite.md` (termasuk flag Guided Tooltip `seen`); spec ini tidak menulis ulang isinya.
- Role yang diuji (Create-Only login di hook `before` spec ini menggantikan akun default suite; halaman dibuka hook `beforeEach` suite; role lain lewat langkah Ganti akun; hook `after` mengembalikan sesi ke akun default suite, Total Control Company Alpha, `Spectra.env.FA_LBL_TC_PASSWORD`):

| Role | Pre-setup | Akun (Fixture) | Env | TC | Langkah |
|---|---|---|---|---|---|
| Create-Only | #3 | `Fixture.assetLabeling.akun.createOnly` | `Spectra.env.FA_CREATEONLY_PASSWORD` | TC-FA-LBL-205, TC-FA-LBL-524 | 1 sampai 6 |
| Update-Only | #4 | `Fixture.assetLabeling.akun.updateOnly` | `Spectra.env.FA_UPDATEONLY_PASSWORD` | TC-FA-LBL-205, TC-FA-LBL-524 | 7 sampai 14 |
| Read Only | #2 | `Fixture.assetLabeling.akun.readOnly` | `Spectra.env.FA_RO_PASSWORD` | TC-FA-LBL-205 | 15 sampai 17 |

- Environment variable: `FA_CREATEONLY_PASSWORD`, `FA_UPDATEONLY_PASSWORD`, `FA_RO_PASSWORD`, `FA_LBL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Fixture: `Fixture.assetLabeling.*` (`fixtures/asset-labeling.json`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Data Pre-setup (dibaca saja, tidak diubah spec): #12 (katalog Company Alpha 9 label; Labels List perlu memuat sedikitnya satu baris) dan #14 (Asset Name `Laptop Dell` di tab Asset Name; dibuka pada modal Edit dan form Create tanpa disimpan).
- State global: tidak ada yang diubah selain sesi login. Suite berjalan serial (`parallel: false`, lihat `suite.md`).

## Test Steps

### Create-Only: TC-FA-LBL-205 dan TC-FA-LBL-524

1. Verifikasi kolom Checkbox dan Select All Hidden (tidak dirender) pada tabel Labels List
2. Verifikasi Bulk Action Bar Hidden (tidak dirender)
3. Klik Tab `Asset Name`
4. Klik `[+ Asset Name]`
5. Verifikasi tombol `[➕]` tampil di field Default Label
6. Tutup form Create Asset Name dengan `✕`

### Update-Only: TC-FA-LBL-205 dan TC-FA-LBL-524

7. Ganti akun: Logout, login sebagai Update-Only `Fixture.assetLabeling.akun.updateOnly` (`Spectra.env.FA_UPDATEONLY_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
8. Verifikasi kolom Checkbox dan Select All Hidden (tidak dirender) pada tabel Labels List
9. Verifikasi Bulk Action Bar Hidden (tidak dirender)
10. Klik Tab `Asset Name`
11. Klik `⋯` pada baris `Laptop Dell` lalu `Edit`
12. Verifikasi field Default Label tampil
13. Verifikasi tombol `[➕]` Hidden (tidak dirender)
14. Tutup modal Edit Asset Name dengan `✕`

### Read Only: TC-FA-LBL-205

15. Ganti akun: Logout, login sebagai Read Only `Fixture.assetLabeling.akun.readOnly` (`Spectra.env.FA_RO_PASSWORD`), buka Fixed Asset > Settings > Asset Master > tab `Labels`
16. Verifikasi kolom Checkbox dan Select All Hidden (tidak dirender) pada tabel Labels List
17. Verifikasi Bulk Action Bar Hidden (tidak dirender)

## Notes

- Spec ditulis per blok role dengan langkah Ganti akun eksplisit (langkah 7 dan 15) karena akun pertama login di hook `before` dan langkah tiap role berbeda (bagian 3a, varian A).
- Langkah penghubung (S-03): langkah 6 dan 14 (menutup form atau modal Asset Name yang tidak diubah, bukan form dirty sehingga tidak ada dialog `Unsaved Changes`).
- Urutan TC: TC-FA-LBL-524 untuk Create-Only (langkah 3 sampai 5) ditaruh langsung sesudah TC-FA-LBL-205 Create-Only supaya akun hanya sekali login; TC-FA-LBL-524 untuk Update-Only mengikuti pola yang sama (langkah 10 sampai 13). Tiap TC tetap mengikuti urutan langkahnya sendiri (S-10).
- Asersi `Hidden` pada langkah 1, 2, 8, 9, 13, 16, 17: tabel Labels List yang sudah memuat sedikitnya satu baris (Pre-setup #12) dan field Default Label yang tampil (langkah 12) menjadi anchor permukaan (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-LBL-205 Precondition meminta pengulangan untuk Update-Only dan Read Only selain Create-Only; ketiga role diuji (Read Only pada langkah 15 sampai 17).
  - TC-FA-LBL-524 Judul menyebut tombol `[➕]` pada tab Asset Name; tab itu dimiliki PRD Asset Name, spec hanya mengasersi keberadaan tombol `[➕]` pada field Default Label.
