---
id: TC-FA-SU-E2E-152-sub-tab-assigned-assets-sort
title: "Sub-tab Assigned Assets: Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-448
  - TC-FA-SU-449
  - TC-FA-SU-450
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Sort

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md` (flag Guided Tooltip User List `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (hanya dibaca, tidak diubah): Client `FaUserMain` (#20) dan Responsibilities (#24): Detail Budi Santoso dengan Sub-tab Assigned Assets 5 baris (satu halaman). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE). Pre-setup #24 hanya menyebut "5 baris"; nilai kolom di bawah diturunkan dari Expected TC (Asset ID dan Transaction ID hanya tertulis sebagian):

| Name | Asset ID | Transaction ID | Brand | Model / Type | PIC |
|---|---|---|---|---|---|
| `AC Split Ruang Kerja` | tidak tertulis | tidak tertulis | `Daikin` | `1PK` | `Ahmad D` |
| `Lemari Arsip` | tidak tertulis | tidak tertulis | `Lion` | `2 Pintu` | `Citra L` |
| `Meja Kerja Kepala Divisi` | tidak tertulis | `ASG-20260505` | `Modera` | `Executive` | `Ahmad D` |
| `Printer Multifungsi` | tidak tertulis | tidak tertulis | `Canon` | `PIXMA G3010` | `Citra L` |
| `Server Rack Mini` | `AST-02113` | tidak tertulis | `HP` | `ProLiant DL20` | `Eka W` (Eka Wulandari) |
- Data Dinamis: tidak ada.
- State global: tidak ada yang diubah; spec hanya membaca Pre-setup. Suite berjalan serial (`parallel: false`).
- Tabel parameter "Kolom Sort" (dipakai langkah 3 sampai 8); urutan baris ditulis berdasarkan kolom Name, dan klik ketiga mengembalikan urutan default Name ascending (`AC Split Ruang Kerja`, `Lemari Arsip`, `Meja Kerja Kepala Divisi`, `Printer Multifungsi`, `Server Rack Mini`):

| Kolom | Klik 1 ascending (↑) | Klik 2 descending (↓) |
|---|---|---|
| `Name` | `AC Split Ruang Kerja`, `Lemari Arsip`, `Meja Kerja Kepala Divisi`, `Printer Multifungsi`, `Server Rack Mini` | `Server Rack Mini`, `Printer Multifungsi`, `Meja Kerja Kepala Divisi`, `Lemari Arsip`, `AC Split Ruang Kerja` |
| `Asset ID` | `Meja Kerja Kepala Divisi`, `AC Split Ruang Kerja`, `Printer Multifungsi`, `Lemari Arsip`, `Server Rack Mini` | `Server Rack Mini`, `Lemari Arsip`, `Printer Multifungsi`, `AC Split Ruang Kerja`, `Meja Kerja Kepala Divisi` |
| `Transaction ID` | `Meja Kerja Kepala Divisi`, `AC Split Ruang Kerja`, `Printer Multifungsi`, `Lemari Arsip`, `Server Rack Mini` | `Server Rack Mini`, `Lemari Arsip`, `Printer Multifungsi`, `AC Split Ruang Kerja`, `Meja Kerja Kepala Divisi` |
| `Brand` | `Printer Multifungsi`, `AC Split Ruang Kerja`, `Server Rack Mini`, `Lemari Arsip`, `Meja Kerja Kepala Divisi` | `Meja Kerja Kepala Divisi`, `Lemari Arsip`, `Server Rack Mini`, `AC Split Ruang Kerja`, `Printer Multifungsi` |
| `Model / Type` | `AC Split Ruang Kerja`, `Lemari Arsip`, `Meja Kerja Kepala Divisi`, `Printer Multifungsi`, `Server Rack Mini` | `Server Rack Mini`, `Printer Multifungsi`, `Meja Kerja Kepala Divisi`, `Lemari Arsip`, `AC Split Ruang Kerja` |
| `PIC` | `AC Split Ruang Kerja`, `Meja Kerja Kepala Divisi`, `Lemari Arsip`, `Printer Multifungsi`, `Server Rack Mini` | `Server Rack Mini`, `Lemari Arsip`, `Printer Multifungsi`, `AC Split Ruang Kerja`, `Meja Kerja Kepala Divisi` |

## Test Steps

### TC-FA-SU-448: Sort kelas teks: Name, Asset ID, Transaction ID, Brand, Model / Type

1. Ketik Search `Budi Santoso`, tekan Enter, lalu klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
3. Untuk setiap baris tabel parameter "Kolom Sort" (langkah 3 sampai 8): klik header kolom itu satu kali
4. Verifikasi urutan baris ascending (↑) sesuai kolom Klik 1 ascending pada tabel parameter
5. Klik header kolom itu kedua kali
6. Verifikasi urutan baris descending (↓) sesuai kolom Klik 2 descending pada tabel parameter
7. Klik header kolom itu ketiga kali
8. Verifikasi urutan baris netral kembali ke default Name ascending

### TC-FA-SU-449: Sort kelas user: PIC

9. Klik header PIC satu kali
10. Verifikasi urutan baris ascending (↑): `AC Split Ruang Kerja`, `Meja Kerja Kepala Divisi`, `Lemari Arsip`, `Printer Multifungsi`, `Server Rack Mini`
11. Klik header PIC kedua kali
12. Verifikasi urutan baris descending (↓): `Server Rack Mini`, `Lemari Arsip`, `Printer Multifungsi`, `AC Split Ruang Kerja`, `Meja Kerja Kepala Divisi`
13. Klik header PIC ketiga kali
14. Verifikasi urutan baris netral kembali ke default Name ascending: `AC Split Ruang Kerja`, `Lemari Arsip`, `Meja Kerja Kepala Divisi`, `Printer Multifungsi`, `Server Rack Mini`

### TC-FA-SU-450: Guard kolom non-sortable: Photo

15. Hover header Photo
16. Verifikasi header Photo tidak memiliki icon sort
17. Klik header Photo
18. Verifikasi urutan baris tidak berubah dan tetap default Name ascending

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): Search nama `Budi Santoso` serta pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Langkah 3 sampai 8 diulang untuk lima baris tabel parameter "Kolom Sort" (ekspansi 30 langkah dari 6 langkah nominal, bagian 8b butir 7); Verifikasi tetap satu per klausa (ascending, descending, netral) untuk tiap kolom. Klik ketiga mengembalikan urutan default sehingga tidak perlu pembersih di antara kolom.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (42 langkah, 18 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Assigned Assets, satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Temuan untuk QA (S-15):
  - TC-FA-SU-448 dan 449: Expected menulis urutan dengan nama baris Name, bukan nilai kolom yang diurutkan, sehingga nilai Asset ID, Transaction ID, dan PIC per baris tidak terbaca di Pre-setup; spec mengasersi urutan baris sesuai Expected.
  - Urutan sesama nilai PIC (`Ahmad D` dua baris, `Citra L` dua baris) pada klik 1 dan klik 2 mengikuti Expected TC (tie-break sama pada kedua arah); TC tidak menyebut aturan tie-break.
