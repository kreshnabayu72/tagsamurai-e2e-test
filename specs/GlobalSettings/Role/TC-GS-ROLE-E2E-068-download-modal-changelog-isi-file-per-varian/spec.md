---
id: TC-GS-ROLE-E2E-068-download-modal-changelog-isi-file-per-varian
title: "Download Modal Changelog: Berkas CSV dan XLSX per Varian"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-204
coverage:
  web: automated
---

# Download Modal Changelog: Berkas CSV dan XLSX per Varian

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control, Ahmad Fauzi (`Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Hook `beforeEach`: kembali ke layar Global Settings > Role & Permission > Total Control.
- Seeding precondition TC (lewat API oleh akun Ahmad Fauzi di hook `before`, dipakai sebagai precondition TC, tidak diasersi; kemampuan dari `openapi.yaml`: POST/DELETE `/v2/iam/products/{product}/roles/access-level`, POST/DELETE `/v2/iam/products/{product}/roles/capabilities/users`; asumsi seeding lewat API mencatat entri Changelog sama seperti aksi UI):
  - Fikri Ramadhan (Pre-setup #18): Assign Total Control lalu Remove Total Control, lalu Assign Read Only lalu Remove Read Only, sehingga Changelog Tab Total Control dan Tab Read Only tidak kosong.
  - Citra Dewanti (Pre-setup #18): Assign Role Manage TAG lalu Remove baris Manage TAG, sehingga Changelog Tab System dan Detail "Manage TAG" tidak kosong.
- Pemulihan di hook `after` (tetap jalan walau spec gagal di tengah): Fikri Ramadhan dan Citra Dewanti dikembalikan ke kondisi kandidat Pre-setup #18 (Active, Access Global Settings dicentang, tanpa access level, tanpa baris role) lewat API; berkas unduhan dihapus; Modal Changelog ditutup. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis (kelas binary buffer, prinsip 13f): menangkap berkas unduhan browser ke direktori bersih dan membaca nama serta ekstensi berkas CSV dan XLSX; mengamati toast.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ROLE-204: Download Modal Changelog per varian

1. Klik icon Changelog di Table Tools
2. Klik Download di modal, lalu klik `Download CSV`
3. Verifikasi tidak ada toast sukses
4. Verifikasi file `Changelog-Role-Permission-Total-Control.csv` terunduh
5. Klik Download di modal, lalu klik `Download XLSX`
6. Verifikasi tidak ada toast sukses
7. Verifikasi file `Changelog-Role-Permission-Total-Control.xlsx` terunduh
8. Tutup Modal Changelog lewat `[✕]`
9. Klik Tab `Read Only`
10. Klik icon Changelog di Table Tools
11. Klik Download di modal, lalu klik `Download CSV`
12. Verifikasi tidak ada toast sukses
13. Verifikasi file `Changelog-Role-Permission-Read-Only.csv` terunduh
14. Tutup Modal Changelog lewat `[✕]`
15. Klik Tab `System`
16. Klik icon Changelog di Table Tools
17. Klik Download di modal, lalu klik `Download CSV`
18. Verifikasi tidak ada toast sukses
19. Verifikasi file `Changelog-Role-Permission-System.csv` terunduh
20. Tutup Modal Changelog lewat `[✕]`
21. Klik Role Name `Manage TAG`
22. Klik icon Changelog di Table Tools
23. Klik Download di modal, lalu klik `Download CSV`
24. Verifikasi tidak ada toast sukses
25. Verifikasi file `Changelog-Role-Permission-Manage-TAG.csv` terunduh
26. Tutup Modal Changelog lewat `[✕]`

## Notes

- Sumber TC: `global-settings/role/TestCases/tc-role.md`. Mode: FE+BE.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan unduhan diubah dari TC sumber (Langkah Uji 1 empat CSV, Langkah Uji 2 XLSX): XLSX Tab Total Control diunduh langsung sesudah CSV Tab Total Control (langkah 5 sampai 7) supaya modal yang sama tidak dibuka dua kali.
- Asersi "tidak ada toast sukses" (Expected f) diletakkan segera sesudah pemicu unduhan dan sebelum asersi berkas (bagian 8b butir 11); pemicu unduhan menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas, dan diulang pada tiap unduhan.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 8, 14, 20, dan 26 (menutup Modal Changelog), langkah 9 dan 15 (pindah tab), langkah 21 (membuka Detail "Manage TAG" lewat Role Name di Tab System).
- Isi berkas export dipisah dari spec kegagalan export (kelas binary buffer, prinsip 13f); kegagalan download Changelog (TC-GS-ROLE-205) ada di spec 069.
- Tidak ada TC lain yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-ROLE-204 Expected a sampai e hanya menyebut nama berkas dan tidak menyebut isi berkas (kolom, jumlah baris, format tanggal); spec hanya mengasersi nama dan ekstensi berkas yang terunduh serta tidak adanya toast sukses, sehingga isi berkas tidak diasersi.
  - Item menu unduh Modal Changelog ditulis `Download CSV` dan `Download XLSX` pada TC-GS-ROLE-204 dan 205, sedangkan menu Download tabel memakai `Download as CSV` dan `Download as XLSX` (TC-GS-ROLE-174 dan 179); spec memakai teks TC masing-masing.
