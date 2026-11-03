---
id: TC-FA-LBL-E2E-065-filter-labels-list-independen-kolom-clear-field-dan-opsi-baru
title: "Filter Labels List: Independen dari Visibilitas Kolom, Clear Field, dan Opsi Modified By Baru"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LBL-237
  - TC-FA-LBL-238
  - TC-FA-LBL-240
coverage:
  web: automated
---

# Filter Labels List: Independen dari Visibilitas Kolom, Clear Field, dan Opsi Modified By Baru

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, pengguna Sarah Johnson), `Fixture.assetLabeling.totalControl` (email pola `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture.
- Hook suite (`before`, `beforeEach`, `after` di `suite.md`) berlaku; spec ini tidak menulis ulang isinya.
- Fixture `fixtures/asset-labeling.json` (fixture baru; isi identitas data ditetapkan tim FE).
- Data Pre-setup #12 (katalog Company Alpha, 9 label; hanya dibaca, tidak diubah; Total Asset berasal dari Pre-setup #13):

  | Label | Modified By |
  |---|---|
  | `High Priority` | `Sarah J` |
  | `Finance Department` | `David K` |
  | `Audit Ready` | `Sarah J` |
  | `Executive Asset` | `Michael W` |
  | `Maintenance Due` | `David K` |
  | `Seasonal Event` | `Michael W` |
  | `Night Shift` | `Sarah J` |
  | `Warehouse Priority` | `Sarah J` |
  | `Field Kit` | `David K` |

- Akun pelaku kedua: Full-CRUD (Pre-setup #7), `Fixture.assetLabeling.fullCrud` (email pola `fullCrud_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_FULLCRUD_PASSWORD`; hanya dipakai lewat sesi API (login API password, token tidak dihitung sebagai sesi web).
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor (akun Total Control dan Full-CRUD) untuk membuat dan mengubah label, serta fixture BE untuk menghapus label.
- Data Dinamis (sufiks `{runId}-065`, `{runId}` hanya digit): label `Modified By Probe 240 {runId}-065` dibuat pada langkah 22, Color default, tanpa aset; dihapus di hook `after` lewat fixture BE (tidak berasumsi seeding berhasil). Setelah dihapus, opsi pengguna Full-CRUD hilang dari dropdown Modified By sehingga spec lain yang mengasersi tiga opsi tidak terpengaruh.
- State global yang diubah: kolom `Modified By` Labels List disembunyikan lalu ditampilkan kembali (langkah 5 dan 12); hook `after` suite menghapus preferensi kolom di browser sebagai cadangan.

## Test Steps

### TC-FA-LBL-237: Filter independen dari visibilitas kolom

1. Klik icon Filter di Table Tools
2. Pilih `Modified By` = `Sarah J`
3. Klik `[Apply]`
4. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
5. Hapus centang kolom `Modified By`
6. Klik `[Save]`
7. Verifikasi filter ter-Apply tetap berlaku: tabel hanya memuat empat baris `Audit Ready`, `High Priority`, `Night Shift`, `Warehouse Priority` walau kolom `Modified By` disembunyikan
8. Klik icon Filter di Table Tools
9. Verifikasi field `Modified By` tetap tersedia di Filter Panel
10. Bersihkan saringan: klik `[Clear Field]`, klik `[Apply]`, lalu klik area di luar panel
11. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
12. Centang kolom `Modified By`
13. Klik `[Save]`

### TC-FA-LBL-238: Clear Field di Filter Panel mengosongkan kriteria

14. Klik icon Filter di Table Tools
15. Isi `Total Asset` Min dengan 2
16. Pilih `Modified By` = `Sarah J`
17. Klik `[Apply]`
18. Klik `[Clear Field]`
19. Klik `[Apply]`
20. Verifikasi seluruh field panel kosong
21. Verifikasi 9 label tampil kembali

### TC-FA-LBL-240: Opsi Modified By bertambah saat pengguna baru memodifikasi label

22. Lewat sesi API akun Total Control, buat label `Modified By Probe 240 {runId}-065` hingga label tersimpan
23. Lewat sesi API akun Full-CRUD, ubah warna label `Modified By Probe 240 {runId}-065` hingga perubahan tersimpan
24. Tekan F5 pada sesi UI Total Control
25. Klik icon Filter di Table Tools
26. Buka dropdown `Modified By`
27. Verifikasi opsi bertambah menjadi empat: `David K`, `Michael W`, `Sarah J`, dan pengguna Full-CRUD (`Fixture.assetLabeling.fullCrud.modifiedByDisplay`) sebagai Modified By label `Modified By Probe 240 {runId}-065`
28. Verifikasi opsi `Michael W` tetap ada

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`, section 4a.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 10 membersihkan Filter dan panel; langkah 11 sampai 13 memulihkan kolom `Modified By` sebelum TC berikutnya mengandalkan lima kolom (S-09); langkah 22 menyiapkan label milik spec dan langkah 24 memuat ulang sesi UI aktor utama agar membaca data terbaru (pengganti "Login sbg Role: Total Control, buka tab Labels" karena sesi UI Total Control sudah aktif).
- Pelaku kedua (Full-CRUD) memakai sesi API (bagian 3 P-2, keputusan 2026-10-30): bukan konteks kedua, sehingga tidak memakai butir `P-2`.
- Label target TC-FA-LBL-240 adalah label milik spec (S-06), bukan `Seasonal Event` Pre-setup #12: mengubah label Pre-setup mengubah Modified By dan Last Updated yang diasersi spec lain. Opsi `Michael W` tetap ada karena `Executive Asset` tetap tercatat atas `Michael W`.
- Temuan untuk QA:
  - TC-FA-LBL-240 Expected menulis "pengguna Full-CRUD sebagai Modified By `Seasonal Event`" (kalimat tidak lengkap; `Seasonal Event` adalah nama label, bukan nilai Modified By), dan nama tampilan pengguna Full-CRUD (Pre-setup #7) tidak tertulis; spec memakai `Fixture.assetLabeling.fullCrud.modifiedByDisplay` (format `[First Name] [Last Initial]`) yang ditetapkan tim FE.
  - TC-FA-LBL-240 mengandaikan opsi Modified By sebelum aksi berjumlah tiga; spec tidak mengasersi keadaan sebelum aksi karena TC tidak memberi langkah observasinya.
