---
id: TC-GS-ROLE-E2E-022-role-matrix-gating-seleksi-checkbox-baris-detail
title: "Role Matrix: Gating Seleksi Checkbox Baris Detail dan Select All per Aktor"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-49
  - TC-GS-ROLE-50
coverage:
  web: automated
---

# Role Matrix: Gating Seleksi Checkbox Baris Detail dan Select All per Aktor

## Prerequisites

- Mode: FE+BE. Spec tidak mengubah data; seleksi checkbox dan Select All hanya state layar, tidak ada aksi Remove.
- Langkah kedua blok sama (buka Detail, Select All, periksa tiap baris, periksa angka), tetapi hasil yang diharapkan berbeda per aktor, sehingga spec ditulis sebagai blok per aktor dengan hasil per baris pada tabel di bawah. Login Total Control dilakukan di hook `before`; Hendra Wijaya memakai ganti akun eksplisit. Password tidak ditulis di spec atau fixture.

Role yang diuji (Tabel Data Uji Pre-setup):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-ROLE-49 | Total Control | Ahmad Fauzi | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-ROLE-50 | Manage user and role C/R/U/D | Hendra Wijaya | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` |

- Environment variable: `GS_TC_PASSWORD`; env baru `GS_ROLE_MANAGE_CRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE).
- Data Pre-setup (hanya dibaca): Detail "Manage TAG" memuat tepat 7 baris saat spec mulai (kondisi Pre-setup: Rina Putri masih Read Only, Tabel Data Uji Dinamis #14; Wawan Setiawan dan Nina Kartika belum punya baris Manage TAG).

Baris Detail "Manage TAG" dan hasil Select All per aktor:

| Baris | Access level (Pre-setup) | Hasil untuk Total Control (TC-GS-ROLE-49) | Hasil untuk Hendra Wijaya (TC-GS-ROLE-50) |
|---|---|---|---|
| Ahmad Fauzi | Total Control (aktor) | tidak checked | disabled dan tidak checked |
| Budi Santoso | Total Control (Default User) | tidak checked | disabled dan tidak checked |
| Dewi Lestari | Total Control | checked | disabled dan tidak checked |
| Doni Pratama | tanpa access level | checked | checked |
| Siti Nurhaliza | Read Only | checked | disabled dan tidak checked |
| Rina Putri | Read Only | checked | disabled dan tidak checked |
| Hendra Wijaya | tanpa access level (aktor pada TC-GS-ROLE-50) | checked | disabled dan tidak checked |

- Angka pada button Select All dan counter: 5 untuk Total Control, 1 untuk Hendra Wijaya.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: membuka Global Settings > Role & Permission > Tab Total Control.
- Hook `after`: mengembalikan sesi ke akun default suite (Ahmad Fauzi, `GS_TC_PASSWORD`) karena spec berakhir di akun Hendra Wijaya.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-49: Checkbox seleksi Detail untuk aktor Total Control dan Select All mengecualikan baris disabled

1. Buka Detail "Manage TAG"
2. Klik button Select All di Bulk Action toolbar
3. Untuk setiap baris pada tabel Prerequisites (langkah 3): Verifikasi checkbox seleksi baris tersebut sesuai kolom "Hasil untuk Total Control"
4. Verifikasi angka pada button Select All = 5
5. Verifikasi counter = 5

### TC-GS-ROLE-50: Checkbox seleksi Detail untuk aktor Manage user and role Update

6. Logout, lalu login sebagai Hendra Wijaya
7. Buka Detail "Manage TAG"
8. Klik button Select All
9. Untuk setiap baris pada tabel Prerequisites (langkah 9): Verifikasi checkbox seleksi baris tersebut sesuai kolom "Hasil untuk Hendra Wijaya"
10. Verifikasi angka pada button Select All = 1
11. Verifikasi counter = 1

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Langkah 3 dan 9 diulang per baris tabel Prerequisites (7 iterasi masing-masing; parameter tiap iterasi ada di tabel, tanpa langkah bersyarat); jumlah langkah dengan ekspansi 24.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC sumber): logout lalu login sebagai Hendra Wijaya (langkah 6) dan membuka Detail pada akun itu (langkah 7).
- Asersi universal pada langkah 3 dan 9 didahului baris pembanding: kolom "checked" pada tabel membuktikan Select All memilih baris, dan kolom "disabled dan tidak checked" diperiksa terhadap baris yang sama pada tabel yang sudah termuat.
- Pembagian TC lintas spec: TC-GS-ROLE-41, 42, 43 ada di spec 019; spec ini dijalankan pada kondisi Pre-setup 7 baris (baris Wawan Setiawan dan Nina Kartika dibuat di TC-GS-ROLE-94, di luar spec ini).
- Temuan untuk QA:
  - TC-GS-ROLE-49 Expected a ("tidak pernah checked") tidak menyebut apakah checkbox Ahmad Fauzi dan Budi Santoso disabled; spec hanya memverifikasi tidak checked setelah Select All. TC-GS-ROLE-41 menetapkan keduanya disabled.
  - Kombinasi aktor Manage user and role Read dan C/R/D tanpa Update pada checkbox seleksi Detail tidak punya TC sumber; tidak ditambahkan (usulan TC baru bila diperlukan).
