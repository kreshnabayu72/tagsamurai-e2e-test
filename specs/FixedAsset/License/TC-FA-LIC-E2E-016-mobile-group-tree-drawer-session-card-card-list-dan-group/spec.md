---
id: TC-FA-LIC-E2E-016-mobile-group-tree-drawer-session-card-card-list-dan-group
title: "Mobile: Group Tree Drawer, Session Card, Card List, dan Group Quota Summary Scroll Horizontal"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-80
  - TC-FA-LIC-81
  - TC-FA-LIC-82
  - TC-FA-LIC-522
coverage:
  web: automated
---

# Mobile: Group Tree Drawer, Session Card, Card List, dan Group Quota Summary Scroll Horizontal

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; General Settings `dd/MM/yy`, `HH:mm`; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License (Tab All License) dibuka hook `beforeEach` suite pada viewport desktop. Hook `after` mengembalikan sesi ke akun default suite dan memulihkan viewport desktop.
- Data Pre-setup: kuota dan hierarki #12 (Kantor Pusat), riwayat #13, sesi aktif #14 (Budi Santoso: `Chrome on Windows`, Login Time 29/09/26 06:40, Last Activity 29/09/26 07:05); hanya dibaca, tidak diubah. Nilai dibaca dari `Fixture.fixedAssetLicense.*`; berkas fixture belum ada, disediakan tim FE.
- State sisi klien yang diubah spec: ukuran viewport diubah ke mobile pada langkah 1 dan dipulihkan ke desktop pada langkah 22; hook `after` memulihkannya bila spec gagal di tengah. Kemampuan mengubah dan memulihkan viewport disediakan tim FE.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-82: Tabel riwayat dan T-FALIC-03 menjadi Card List; Tabs Bar scrollable

1. Ubah viewport ke ukuran mobile
2. Verifikasi Tabs Bar dan Sub-Tab switcher berupa bar horizontal scrollable
3. Verifikasi kartu Subscription History berjudul Subscription ID dengan atribut kolom default Visible
4. Verifikasi tabel License Summary scroll horizontal dengan kolom `License` pinned kiri
5. Klik Tab `Allocation Quota`
6. Verifikasi kartu grup memiliki tombol ikon `[Edit]`

### TC-FA-LIC-80: Sidebar Group Tree menjadi drawer

7. Verifikasi Sidebar Group Tree tidak tampil permanen
8. Verifikasi tombol `Groups` tampil
9. Klik tombol `Groups`
10. Verifikasi klik membuka drawer samping berisi pohon grup
11. Pilih node `Kantor Pusat`
12. Verifikasi konten berganti ke Kantor Pusat
13. Ketuk ikon `[Edit]` di samping nilai `Total` pada Group Quota Summary Kantor Pusat
14. Verifikasi modal Edit Allocation muncul sebagai bottom sheet
15. Tutup modal Edit Allocation dengan `[×]`

### TC-FA-LIC-522: Group Quota Summary scroll horizontal dengan kolom License pinned kiri

16. Gulir Group Quota Summary Kantor Pusat ke kanan
17. Verifikasi Group Quota Summary Kantor Pusat dapat digulir horizontal
18. Verifikasi kolom `License` (baris `Total`, `Allocated to Subgroups`, `Used by This Group`, `Reserved by This Group`, `Remaining`) tetap pinned di kiri saat digulir

### TC-FA-LIC-81: Active Sessions menjadi Session Card

19. Klik Tab `Concurrent User`
20. Verifikasi kartu Budi Santoso: avatar dan `Budi Santoso`, email, `Chrome on Windows`, `Login Time: 29/09/26 06:40`, `Last Activity: 29/09/26 07:05`
21. Verifikasi tombol `[Force Logout]` lebar penuh dengan severity danger
22. Pulihkan viewport ke ukuran desktop

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-80, 81, 82, 522). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC-82 (Tab All License) di awal, TC-80 dan TC-522 berurutan di Tab Allocation Quota, TC-81 terakhir, sehingga tab tidak dibuka berulang (S-10). Langkah 2 TC-522 ("Ketuk node `Kantor Pusat` lewat tombol `Groups`") dipenuhi oleh langkah 9 dan 11.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 1 (mengubah viewport sesuai Precondition), langkah 15 (menutup modal Edit Allocation), langkah 22 (memulihkan viewport), serta klik tab pada langkah 5 dan 19. Modal Edit Allocation ditutup tanpa perubahan sehingga dialog `Unsaved Changes` tidak muncul (form tidak dirty).
- Temuan untuk QA:
  - TC-82 Expected d menyebut tabel License Summary scroll horizontal tanpa menyebut tab; spec mengasersinya di Tab `All License` sebelum membuka Tab `Allocation Quota`.
