---
id: TC-FA-FAAM-E2E-248-defense-in-depth-request-langsung-aturan-server
title: "Defense-in-Depth: Request Langsung Category Internal, Non-TAG Bersama Tipe TAG, Delete In-Use, dan Category Tidak Ada Ditolak Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-628
  - TC-FA-FAAM-629
  - TC-FA-FAAM-630
  - TC-FA-FAAM-631
  - TC-FA-FAAM-632
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Category Internal, Non-TAG Bersama Tipe TAG, Delete In-Use, dan Category Tidak Ada Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor UI (pengamat state): Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Pengirim request langsung memakai sesi API Total Control yang sama (login API password; disediakan tim BE/FE). Klien HTTP untuk request langsung disediakan tim BE/FE; endpoint tidak disebut TC dan tidak dikarang spec. Password tidak ditulis di spec atau fixture.
- Env var: `FA_TC_PASSWORD`.
- Data Pre-setup (hanya dibaca): No. 22 (Category internal `Electronics` dan `IT Equipment`).
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-248`:
  - `Direct InUse Item 630 {runId}-248` (Total Asset 1; in-use).
  - `Bulk Used X 631 {runId}-248` (Total Asset 3) dan `Bulk Used Y 631 {runId}-248` (Total Asset 1); salinan fixture 14o.
  - Category `Deleted Category 632 {runId}-248` yang dibuat lalu dihapus lewat API di hook `before`.
  - Nama pada request Create: `Direct Category Item 628 {runId}-248`, `Direct Tag Item 629 {runId}-248`, `Direct Deleted Cat Item 632 {runId}-248` (tidak boleh ada setelah request ditolak).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition TC-FA-FAAM-628 sampai 632: login sebagai Total Control; pengamat UI berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-628: Request langsung dengan Category internal ditolak

1. Kirim request langsung ke server: POST Create Asset Name `Direct Category Item 628 {runId}-248` dengan Category internal `Electronics`
2. Verifikasi server menolak dengan `422` (error validasi pada Category)
3. Muat ulang List dan ketik Search `Direct Category Item 628 {runId}-248`, tekan Enter
4. Verifikasi empty state `No results found`, sehingga tidak ada mutasi

### TC-FA-FAAM-629: Request langsung dengan Non-TAG bersama tipe TAG ditolak

5. Kirim request langsung ke server: POST Create Asset Name `Direct Tag Item 629 {runId}-248` dengan TAG Type `Non-TAG` dan `QR`
6. Verifikasi server menolak dengan error validasi (422)
7. Ganti isi kotak search dengan `Direct Tag Item 629 {runId}-248`, tekan Enter
8. Verifikasi empty state `No results found`, sehingga tidak ada mutasi

### TC-FA-FAAM-632: Request langsung dengan Category yang tidak ada ditolak

9. Kirim request langsung ke server: POST Create Asset Name `Direct Deleted Cat Item 632 {runId}-248` dengan Category `Deleted Category 632 {runId}-248` yang sudah dihapus
10. Verifikasi server menolak dengan `422` (error validasi per field Category)

### TC-FA-FAAM-630: Request Delete langsung pada Asset Name in-use ditolak

11. Ganti isi kotak search dengan `Direct InUse Item 630 {runId}-248`, tekan Enter
12. Verifikasi baris `Direct InUse Item 630 {runId}-248` ada
13. Kirim request langsung ke server: DELETE Asset Name `Direct InUse Item 630 {runId}-248`
14. Verifikasi server menolak (409)
15. Muat ulang List dan ketik Search `Direct InUse Item 630 {runId}-248`, tekan Enter
16. Verifikasi baris `Direct InUse Item 630 {runId}-248` masih ada (tanpa mutasi)

### TC-FA-FAAM-631: Request Bulk Delete langsung semua in-use dikembalikan skipped tanpa mutasi

17. Ganti isi kotak search dengan `Bulk Used`, tekan Enter
18. Verifikasi baris `Bulk Used X 631 {runId}-248` dan `Bulk Used Y 631 {runId}-248` ada
19. Kirim request langsung ke server: Bulk Delete `Bulk Used X 631 {runId}-248` dan `Bulk Used Y 631 {runId}-248`
20. Verifikasi respons 200 dengan deleted 0 dan skipped 2
21. Verifikasi respons memuat rincian skipped untuk kedua Asset Name
22. Muat ulang List dan ketik Search `Bulk Used`, tekan Enter
23. Verifikasi kedua Asset Name masih ada (tanpa mutasi)

## Notes

- K-1: TC-FA-FAAM-628 sampai 632 adalah TC kelas a dengan Expected respons API; tetap berada di spec FE+BE walau tumpang tindih dengan `tc-settings-asset-name-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Spec ini hanya mengasersi status respons dan state data (bagian 8b butir 1). Pelaku pengirim request adalah sesi API (bukan konteks UI kedua).
- Langkah penghubung tanpa `Verifikasi`: langkah 3, 7, 11, 15, 17, 22 (muat ulang List atau Search). Langkah 4 dan 8 adalah asersi absence dengan anchor empty state `No results found`; langkah 16 dan 23 dengan anchor langkah 12 dan 18 (keadaan sebelum request).
- Urutan TC: TC-FA-FAAM-628, 629, 632 (tidak ada data yang diubah), lalu TC-FA-FAAM-630 dan 631 (menyasar data in-use); tidak ada aksi yang menghapus data karena seluruh request ditolak.
- Pembagian TC lintas spec: absence entri log atas Bulk Delete langsung semua in-use ada di spec 251 (TC-FA-FAAM-844).
- Temuan untuk QA:
  - TC-FA-FAAM-630 memakai `Dell Latitude` dan TC-FA-FAAM-631 memakai `Bulk Used X` dan `Bulk Used Y` (Pre-setup bersama); spec memakai salinan milik spec (S-06) karena request langsung yang ditolak tetap memakai data milik spec.
  - TC-FA-FAAM-632 tidak menyebut cara membentuk "Category yang sudah dihapus"; spec membentuknya lewat seed API.
