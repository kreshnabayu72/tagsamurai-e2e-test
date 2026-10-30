---
id: TC-GS-ROLE-E2E-069-resilience-export-gagal-download-tabel-dan-changelog
title: "Resilience Export: Kegagalan Download Tabel Total Control dan Modal Changelog"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-ROLE-179
  - TC-GS-ROLE-205
coverage:
  web: automated
---

# Resilience Export: Kegagalan Download Tabel Total Control dan Modal Changelog

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata; kelas harness fault injection, prinsip 13b konvensi).
- Akun aktor: Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission > Total Control.
- Data Pre-setup (tetap di environment, hanya dibaca): Tab Total Control memuat Ahmad Fauzi, Budi Santoso (Default User), dan Dewi Lestari.
- Seeding precondition TC (lewat API oleh akun Ahmad Fauzi di hook `before`, dipakai sebagai precondition TC, tidak diasersi; kemampuan dari `openapi.yaml`: POST/DELETE `/v2/iam/products/{product}/roles/access-level`): Fikri Ramadhan (Pre-setup #18) di-assign Total Control lalu di-Remove Total Control, supaya Changelog Tab Total Control tidak kosong (asumsi seeding lewat API mencatat entri Changelog sama seperti aksi UI). Hook `after` mengembalikan Fikri Ramadhan ke kondisi kandidat Pre-setup #18 (Active, Access Global Settings dicentang, tanpa access level, tanpa baris role) lewat API.
- Kebutuhan intercept (`Spectra.intercept()`), dipasang dan dilepas lewat langkah eksplisit, respons dipaksa HTTP 500 tanpa meneruskan request ke server:
  - export tabel Tab Total Control (`Download as CSV`): endpoint `POST /v2/iam/products/{product}/roles/access-level/export` (`openapi.yaml`, `low-level-design.md`) (TC-GS-ROLE-179);
  - export Modal Changelog Tab Total Control (`Download CSV`): endpoint export Changelog tidak tercantum di `openapi.yaml` maupun `low-level-design.md`, sehingga endpoint-nya ditentukan tim FE (TC-GS-ROLE-205).
- Kemampuan teknis: mengamati bahwa tidak ada berkas terunduh (event download browser).
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): semua intercept dilepas; Modal Changelog ditutup. Spec tidak mengubah data Role selain seeding di atas.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-179: Download gagal pada Tab Total Control

1. Pasang intercept pada respons export Tab Total Control: jawab 500
2. Klik icon Download di Table Tools
3. Klik `Download as CSV`
4. Verifikasi toast error `Error, failed to download Role-Permission-Total-Control.`
5. Verifikasi tidak ada berkas terunduh
6. Lepas intercept respons export Tab Total Control

### TC-GS-ROLE-205: Download Modal Changelog gagal

7. Klik icon Changelog di Table Tools
8. Pasang intercept pada respons export Changelog Tab Total Control: jawab 500
9. Klik Download di modal, lalu klik `Download CSV`
10. Verifikasi toast error `Error, failed to download Changelog-Role-Permission-Total-Control.`
11. Verifikasi tidak ada berkas terunduh
12. Lepas intercept respons export Changelog Tab Total Control
13. Tutup Modal Changelog lewat `[✕]`

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE (intercept parsial dan state backend nyata; kelas harness fault injection).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber (179, 205) dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 dan 12 (melepas intercept segera setelah pemicu, S-09) dan langkah 13 (menutup Modal Changelog). Precondition "User berada di Global Settings > Role & Permission > Total Control" dipenuhi hook `beforeEach`.
- Pembagian TC lintas spec: isi berkas Download Tab Total Control dan Tab Read Only (TC-GS-ROLE-174 sampai 178) dan Download Modal Changelog yang berhasil (TC-GS-ROLE-204) ada di spec lain; Download lebih dari 5.000 baris (TC-GS-ROLE-180) ada di spec volume data.
- Temuan untuk QA:
  - TC-GS-ROLE-179 dan 205 tidak menyebut endpoint yang di-intercept maupun cara memaksa respons 5xx; endpoint export tabel diambil dari `openapi.yaml` dan `low-level-design.md`, endpoint export Changelog tidak ada di keduanya dan disediakan tim FE (tidak mengarang endpoint).
  - TC-GS-ROLE-205 tidak memuat Expected tentang toast yang hilang atau tombol `[Try Again]`; spec hanya mengasersi toast error dan tidak adanya berkas terunduh.
  - TC-GS-ROLE-205 precondition tidak menyebut Changelog harus berisi entri; spec men-seed satu pasang entri Assign dan Remove agar Download tidak berada pada kondisi riwayat kosong.
  - Teks toast gagal download mengikuti TC dengan pola `Error, failed to download [File Name].` (NC-13 di `tc-role.md` berstatus Dikonfirmasi).
