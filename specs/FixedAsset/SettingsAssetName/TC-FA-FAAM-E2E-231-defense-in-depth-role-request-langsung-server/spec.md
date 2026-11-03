---
id: TC-FA-FAAM-E2E-231-defense-in-depth-role-request-langsung-server
title: "Defense-in-Depth: Request Langsung Create-Edit-Delete-Bulk-Baca-Import Tanpa Hak Ditolak Server"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-611
  - TC-FA-FAAM-612
  - TC-FA-FAAM-613
  - TC-FA-FAAM-614
  - TC-FA-FAAM-615
  - TC-FA-FAAM-616
coverage:
  web: automated
---

# Defense-in-Depth: Request Langsung Create-Edit-Delete-Bulk-Baca-Import Tanpa Hak Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Hook suite: login akun default, sesi API aktor, seed API per TC, dan pemulihan state global mengikuti `suite.md`.
- Akun aktor UI (pengamat state): Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1; `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Sesi API aktor yang mengirim request langsung ke server (login API password, token tidak dihitung sebagai sesi web; disediakan tim BE/FE): Read Only `readOnly_automated_{namaCompany}@qwertysystem.net` (No. 2; `Spectra.env.FA_RO_PASSWORD`), Create-Only `createOnly_automated_{namaCompany}@qwertysystem.net` (No. 4; `Spectra.env.FA_CO_PASSWORD`), Update-Only `updateOnly_automated_{namaCompany}@qwertysystem.net` (No. 5; `Spectra.env.FA_UO_PASSWORD`), Tanpa Role Ini `noAssetMasterRole_automated_{namaCompany}@qwertysystem.net` (No. 8; `Spectra.env.FA_NR_PASSWORD`). Klien HTTP untuk request langsung disediakan tim BE/FE; endpoint tidak disebut TC dan tidak dikarang spec.
- Env var: `FA_TC_PASSWORD`, `FA_RO_PASSWORD`, `FA_CO_PASSWORD`, `FA_UO_PASSWORD`, `FA_NR_PASSWORD`.
- Data Dinamis, di-seed lewat API di hook `before`, nama bersuffix `{runId}-231`, Total Asset 0 (salinan fixture):
  - `Edit Direct Item 612 {runId}-231` (Code `EDI612`; salinan fixture 13d).
  - `Warehouse Pallet 613 {runId}-231` (Code `PLT-WH613`; salinan fixture 13).
  - `Bulk Direct A 614 {runId}-231` dan `Bulk Direct B 614 {runId}-231` (salinan fixture 13c).
  - Nama pada request: `Direct Create Item 611 {runId}-231` (TC-FA-FAAM-611) dan `Direct Import Item 616 {runId}-231` (TC-FA-FAAM-616); keduanya tidak boleh ada setelah request ditolak.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus seed milik spec ini lewat API.
- State global yang diubah: tidak ada. Suite berjalan serial (`parallel: false`).
- Precondition: sesi API berperan sebagaimana ditulis per TC; pengamat UI Total Control berada di Fixed Asset > Settings > Asset Master > Asset Name.

## Test Steps

### TC-FA-FAAM-611: Request Create langsung oleh Read Only ditolak server

1. Kirim request langsung ke server: POST Create Asset Name `Direct Create Item 611 {runId}-231` memakai sesi API Read Only
2. Verifikasi server menolak dengan 403 Forbidden
3. Muat ulang List dan ketik Search `Direct Create Item 611 {runId}-231`, tekan Enter
4. Verifikasi empty state `No results found`, sehingga `Direct Create Item 611 {runId}-231` tidak tercipta

### TC-FA-FAAM-612: Request Edit langsung oleh Create-Only ditolak server

5. Ganti isi kotak search dengan `Edit Direct Item 612 {runId}-231`, tekan Enter
6. Verifikasi Code baris `Edit Direct Item 612 {runId}-231` adalah `EDI612`
7. Kirim request langsung ke server: PATCH Edit Asset Name `Edit Direct Item 612 {runId}-231` dengan Code `EDI612-X` memakai sesi API Create-Only
8. Verifikasi server menolak dengan 403 Forbidden
9. Muat ulang List dan ketik Search `Edit Direct Item 612 {runId}-231`, tekan Enter
10. Verifikasi Code baris `Edit Direct Item 612 {runId}-231` tetap `EDI612`

### TC-FA-FAAM-613: Request Delete langsung oleh Update-Only ditolak server

11. Ganti isi kotak search dengan `Warehouse Pallet 613 {runId}-231`, tekan Enter
12. Verifikasi baris `Warehouse Pallet 613 {runId}-231` ada
13. Kirim request langsung ke server: DELETE Asset Name `Warehouse Pallet 613 {runId}-231` memakai sesi API Update-Only
14. Verifikasi server menolak dengan 403 Forbidden
15. Muat ulang List dan ketik Search `Warehouse Pallet 613 {runId}-231`, tekan Enter
16. Verifikasi baris `Warehouse Pallet 613 {runId}-231` masih ada

### TC-FA-FAAM-614: Request Bulk Delete langsung oleh Update-Only ditolak server

17. Ganti isi kotak search dengan `Bulk Direct`, tekan Enter
18. Verifikasi baris `Bulk Direct A 614 {runId}-231` dan `Bulk Direct B 614 {runId}-231` ada
19. Kirim request langsung ke server: Bulk Delete `Bulk Direct A 614 {runId}-231` dan `Bulk Direct B 614 {runId}-231` memakai sesi API Update-Only
20. Verifikasi server menolak dengan 403 Forbidden
21. Muat ulang List dan ketik Search `Bulk Direct`, tekan Enter
22. Verifikasi kedua Asset Name tetap ada (jumlah baris tidak berubah)

### TC-FA-FAAM-615: Request baca langsung oleh pemegang tanpa Role ini ditolak

23. Kirim request list Asset Name langsung memakai sesi API Tanpa Role Ini
24. Verifikasi server menolak dengan 403 Forbidden

### TC-FA-FAAM-616: Create lewat jalur Import tanpa Global Role Import Data ditolak

25. Panggil jalur Create Import langsung dengan Asset Name `Direct Import Item 616 {runId}-231` memakai sesi API Create-Only tanpa Global Role Import Data
26. Verifikasi server menolak
27. Muat ulang List dan ketik Search `Direct Import Item 616 {runId}-231`, tekan Enter
28. Verifikasi empty state `No results found`, sehingga tidak ada Asset Name dibuat

## Notes

- Langkah penghubung tanpa `Verifikasi`: langkah 3, 5, 9, 11, 15, 17, 21, 27 (muat ulang List dan Search untuk menemukan baris target atau mengamati state data).
- K-1: TC-FA-FAAM-611 sampai 616 adalah TC kelas a dengan Expected respons API; tetap berada di spec FE+BE walau tumpang tindih dengan `tc-settings-asset-name-backend.md`, karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Spec ini hanya mengasersi status respons dan state data (bagian 8b butir 1). Klausa "Changelog tidak memuat entri baru (tanpa entri log)" pada TC-FA-FAAM-611 sampai 614 diasersi di spec 247 (kelas g) dengan request yang sama sebagai pemicu.
- Langkah 4 dan 28 adalah asersi absence dengan anchor empty state `No results found` hasil Search (bagian 8b butir 2); langkah 10, 16, 22 mengasersi state tidak berubah dengan anchor langkah 6, 12, 18 (keadaan sebelum request).
- Pelaku yang mengirim request adalah sesi API (bukan konteks UI kedua); tidak ada langkah ganti akun UI.
- Temuan untuk QA:
  - TC-FA-FAAM-612 memakai `Dell Latitude` dan TC-FA-FAAM-613 memakai `Warehouse Pallet` (Pre-setup bersama) pada request yang ditolak; spec memakai salinan milik spec (S-06).
  - TC-FA-FAAM-612 tidak menyebut isi PATCH; spec memakai Code `EDI612-X`. TC-FA-FAAM-614 tidak menyebut nama dua Asset Name; spec memakai `Bulk Direct A/B 614`.
  - TC-FA-FAAM-615 dan 616 tidak punya state data yang diamati selain status respons (TC-FA-FAAM-616 menyebut "tidak ada Asset Name dibuat" tanpa nama; spec menamainya).
