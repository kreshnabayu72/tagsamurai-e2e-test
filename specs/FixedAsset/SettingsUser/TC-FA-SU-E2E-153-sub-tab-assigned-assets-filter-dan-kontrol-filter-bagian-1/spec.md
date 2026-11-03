---
id: TC-FA-SU-E2E-153-sub-tab-assigned-assets-filter-dan-kontrol-filter-bagian-1
title: "Sub-tab Assigned Assets: Filter dan Kontrol Filter (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-451
  - TC-FA-SU-452
coverage:
  web: automated
---

# Sub-tab Assigned Assets: Filter dan Kontrol Filter (Bagian 1)

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
- Tabel parameter "Field Filter" (dipakai langkah 15 sampai 22):

| Field | Opsi dropdown (DISTINCT data tabel) | Pilihan | Baris tersisa |
|---|---|---|---|
| `Name` | `AC Split Ruang Kerja`, `Lemari Arsip`, `Meja Kerja Kepala Divisi`, `Printer Multifungsi`, `Server Rack Mini` | `AC Split Ruang Kerja` | `AC Split Ruang Kerja` (1 baris) |
| `Brand` | `Canon`, `Daikin`, `HP`, `Lion`, `Modera` | `Canon` | `Printer Multifungsi` (1 baris) |
| `Model / Type` | `1PK`, `2 Pintu`, `Executive`, `PIXMA G3010`, `ProLiant DL20` | `1PK` | `AC Split Ruang Kerja` (1 baris) |
| `PIC` | `Ahmad D`, `Citra L`, `Eka W` | `Ahmad D` | `AC Split Ruang Kerja`, `Meja Kerja Kepala Divisi` (2 baris) |

## Test Steps

### TC-FA-SU-451: Screening Filter Panel Sub-tab Assigned Assets: field, label, placeholder, dan tombol

1. Klik nama `Budi Santoso` di User List
2. Klik tab Responsibilities, lalu klik Sub-tab Assigned Assets
3. Klik icon Filter
4. Verifikasi panel Filter terbuka di bawah Table Tools
5. Verifikasi ikon Filter menjadi gelap
6. Hover icon Filter
7. Verifikasi tooltip `Filter` tampil
8. Verifikasi field berurutan Name | Brand | Model / Type | PIC
9. Verifikasi field Name berupa multi-select searchable dengan placeholder `All assets`
10. Verifikasi field Brand berupa multi-select searchable dengan placeholder `All brands`
11. Verifikasi field Model / Type berupa multi-select searchable dengan placeholder `All models/types`
12. Verifikasi field PIC berupa multi-select searchable dengan placeholder `All PICs`
13. Verifikasi footer panel menampilkan `[Clear Field]` di kiri dan `[Apply]` di kanan
14. Verifikasi ikon Filter tanpa badge titik selama belum ada filter ter-Apply

### TC-FA-SU-452: Filter kelas fk: Name, Brand, Model / Type, PIC

15. Untuk setiap baris tabel parameter "Field Filter" (langkah 15 sampai 22): buka dropdown pada field itu
16. Verifikasi opsi dropdown sama dengan DISTINCT data tabel sesuai kolom Opsi pada tabel parameter
17. Centang opsi pada kolom Pilihan
18. Klik `[Apply]`
19. Verifikasi tabel menyisakan baris sesuai kolom Baris tersisa pada tabel parameter
20. Verifikasi chip opsi terpilih tampil di dalam field itu
21. Klik `[Clear Field]` pada field itu
22. Klik `[Apply]`
23. Klik icon Filter untuk menutup panel

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pembukaan Detail dan sub-tab (langkah 1 dan 2) serta langkah yang mengosongkan Search, Filter, atau popup di antara blok TC supaya blok berikutnya tidak mengandalkan state blok sebelumnya (S-09).
- Langkah 15 sampai 22 diulang untuk empat baris tabel parameter "Field Filter" (ekspansi 32 langkah dari 8 langkah nominal, bagian 8b butir 7). `[Clear Field]` lalu `[Apply]` di akhir tiap iterasi mengikuti TC-FA-SU-452 langkah 5, 8, dan 11 supaya tiap field diuji terpisah.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (47 langkah, 23 langkah nominal). Seluruhnya satu kelas (fungsional/screening sub-tab Assigned Assets, satu akun, data Pre-setup sama, tanpa mengubah data Pre-setup), dan tiap blok TC berdiri sendiri: kegagalan satu blok tidak menghilangkan makna blok lain. Satu pembukaan Detail dipakai bersama seluruh blok.
- Pembagian TC lintas spec: TC-FA-SU-453 sampai 455 ada di spec 154 dan 169.
- Temuan untuk QA (S-15):
  - TC-FA-SU-452 memuat nilai PIC dengan format singkat (`Ahmad D`) pada opsi dropdown sedangkan Search PIC (TC-FA-SU-445) memakai nama belakang penuh (`Wulandari`); spec mengikuti masing-masing TC.
  - TC-FA-SU-451 Expected b tidak menyebut urutan label dan input di dalam field; spec mengasersi tipe kontrol dan placeholder tiap field sesuai Expected.
