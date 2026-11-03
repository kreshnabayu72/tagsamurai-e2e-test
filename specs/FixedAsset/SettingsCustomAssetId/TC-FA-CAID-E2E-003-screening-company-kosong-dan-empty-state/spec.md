---
id: TC-FA-CAID-E2E-003-screening-company-kosong-dan-empty-state
title: "Company Kosong: Nilai Default Form dan Empty State Modal"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-6
  - TC-FA-CAID-158
  - TC-FA-CAID-228
coverage:
  web: automated
---

# Company Kosong: Nilai Default Form dan Empty State Modal

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka hook `beforeEach` suite.
- Akun aktor pertama (TC-FA-CAID-6 dan TC-FA-CAID-158): Total Control `Company Kosong` (Pre-setup No 12), email disediakan tim FE/BE (Pre-setup TC), password `Spectra.env.FA_KOSONG_TC_PASSWORD`. Akun kedua (TC-FA-CAID-228, ganti akun eksplisit): Total Control `Company Kosong Changelog` (Pre-setup No 37), email dan env var password disediakan tim FE/BE (Pre-setup No 37 tidak menyebut nama env; lihat Temuan untuk QA). Hook `after` spec ini mengembalikan sesi ke akun default suite (Total Control Company Alpha). Password tidak ditulis di spec atau fixture.
- Hook suite (`suite.md`): flag Guided Tooltip disetel seen untuk akun UI yang dipakai suite, termasuk akun Company Kosong dan Company Kosong Changelog.
- Data Pre-setup No 12: `Company Kosong` tanpa konfigurasi tersimpan, tanpa aset, tanpa Asset Name, dan tanpa Account. Keadaan itu dikembalikan tim FE/BE sebelum tiap run (seed company khusus, `suite.md`). Data Pre-setup No 37: `Company Kosong Changelog`, Company khusus yang dibuat baru pada setiap run oleh fixture (disediakan tim FE/BE) sehingga audit trail Custom Asset ID dijamin kosong; tanpa konfigurasi tersimpan, tanpa aset, dan tidak dipakai TC lain. Nilai default dibaca dari `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Spec hanya membaca: tidak membuat data, tidak menekan `[Save]` atau Master Switch, tidak mengubah state global. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-6: Konfigurasi belum pernah disimpan: nilai default dan tombol Save aktif

1. Verifikasi switch `Enable Custom Asset ID` pada posisi ON
2. Verifikasi Separator bernilai `/ (Slash)`
3. Verifikasi urutan segmen: `Initial Company`, `Group Code`, `Category Code`, `Asset Name Code`, `Division Code`, `Account Code`, `Purchase Date (MMYY)`, `Asset Increment`
4. Verifikasi status centang segmen: `Initial Company`, `Division Code`, dan `Account Code` tidak tercentang; `Group Code`, `Category Code`, `Asset Name Code`, `Purchase Date (MMYY)`, dan `Asset Increment` tercentang; checkbox `Asset Increment` terkunci
5. Verifikasi tombol `[Save]` berstatus aktif walau form belum disentuh
6. Verifikasi Live Preview menampilkan `JKT/LAP/T490/0926/1`

### TC-FA-CAID-158: Empty state tab Code List tanpa master data ber-Code

7. Klik tautan `[View Code List]`
8. Klik tab `Asset Name Codes`
9. Verifikasi tab `Asset Name Codes` menampilkan Illustration dengan Title `No codes available` dan Description `Define codes in master settings to use them in Custom Asset ID.`
10. Klik tab `Account Codes`
11. Verifikasi tab `Account Codes` menampilkan Illustration dengan Title `No codes available` dan Description `Define codes in master settings to use them in Custom Asset ID.`
12. Tutup modal `Code List Reference` dengan `✕`

### TC-FA-CAID-228: Empty state Changelog saat belum ada entri

13. Ganti akun: logout akun Total Control Company Kosong, login sebagai Total Control Company Kosong Changelog (Pre-setup No 37), lalu buka Fixed Asset > Settings > Asset Master > Custom Asset ID
14. Klik tombol `[Changelog]` pada header kartu
15. Verifikasi tabel Changelog menampilkan Illustration dengan Title `No changelog yet` dan Description `Activities and changes will appear here.`
16. Tutup modal `Changelog: Custom Asset ID` dengan `✕`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular. Langkah buka tab pada TC-FA-CAID-6 dan TC-FA-CAID-158 dipenuhi hook `beforeEach` suite; TC-FA-CAID-228 memakai akun dan Company lain sehingga halaman dibuka pada langkah 13.
- Pecahan Expected TC-FA-CAID-6: a menjadi langkah 1 sampai 4, b menjadi langkah 5, c menjadi langkah 6. Daftar urutan segmen dan daftar status centang masing-masing disebut utuh dalam satu butir Expected TC (langkah 3 dan 4).
- TC-FA-CAID-158 menyebut anggota `Asset Name Codes` dan `Account Codes`; keduanya ditulis sebagai dua blok langkah (langkah 8 dan 9, 10 dan 11) dengan teks Expected yang sama. Empty state satu butir Expected (ilustrasi, judul, deskripsi) ditulis satu `Verifikasi` (S-01).
- Langkah penghubung (tanpa `Verifikasi`): langkah 12 dan 16 (menutup modal agar langkah berikutnya mengamati surface yang benar), langkah 13 (ganti akun ke Company Kosong Changelog dan membuka halaman), dan langkah 14 (membuka modal Changelog sebagai pemicu).
- Tab `Asset Name Codes` dan `Account Codes` pada TC-FA-CAID-158 adalah empty state genuin, jadi tidak ada asersi absence yang butuh anchor lain; modal terbuka dibuktikan oleh tab yang dapat diklik pada langkah 8 dan 10.
- Temuan untuk QA:
  - Pre-setup No 37 (`Company Kosong Changelog`) menyebut email dan env var password "disediakan tim FE/BE" tanpa nama env; nama env dan pendaftarannya (`suite.md`, `spectra.config.ts`, `.env.example`) ditentukan tim FE (S-13). Mekanisme fixture yang membuat Company ini baru per run juga disediakan tim FE/BE dan tidak tertulis di TC, PRD, atau LLD.
  - Post Condition TC-FA-CAID-6, 158, dan 228 kosong; tidak ada yang diasersi.
