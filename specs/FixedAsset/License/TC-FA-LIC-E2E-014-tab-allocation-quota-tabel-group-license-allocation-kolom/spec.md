---
id: TC-FA-LIC-E2E-014-tab-allocation-quota-tabel-group-license-allocation-kolom
title: "Tab Allocation Quota: Tabel Group License Allocation, Kolom, Nilai, Group Name, dan Empty State"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-52
  - TC-FA-LIC-53
  - TC-FA-LIC-54
  - TC-FA-LIC-55
  - TC-FA-LIC-59
  - TC-FA-LIC-62
  - TC-FA-LIC-327
coverage:
  web: automated
---

# Tab Allocation Quota: Tabel Group License Allocation, Kolom, Nilai, Group Name, dan Empty State

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #12: delapan grup (Produksi, Cabang Medan, Cabang Surabaya, Kantor Pusat, Divisi Logistik, Divisi IT, Divisi Keuangan, Gudang A) dengan alokasi, Used, Reserved, dan pemakaian addon sesuai Example Data PRD §4.1.3; jumlah kolom addon lintas delapan grup sama dengan Used License Summary (Audit 60, Tracking 48, Maintenance 12, Repair Ticketing 12, IT Inventory 120; Maps belum dialokasikan). Nilai dibaca dari `Fixture.fixedAssetLicense.*`; berkas fixture belum ada, disediakan tim FE.
- State yang diubah spec dan dipulihkan: satu grup dengan nama 120 karakter (termasuk suffix `+{runId}-014`) dibuat di bawah Kantor Pusat lewat fixture BE (TC-FA-LIC-62, langkah 30) dan dihapus pada langkah 34; hook `after` menghapusnya bila langkah gagal. Fixture BE pembuat dan penghapus grup disediakan tim FE/BE.
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-52: Kolom, nilai, dan urutan default

1. Klik Tab `Allocation Quota`
2. Verifikasi kolom Section 2 pada node `All Groups`: `Group Name (sortable) | Group Code (sortable) | Allocated Quota | Allocated to Subgroups | Used by This Group | Reserved by This Group | Remaining Quota | + Audit | + Tracking | + Maintenance Routine | + Repair Ticketing | + Maps | + IT Inventory | Column Visibility (⋯)` (kolom data dari Group Name sampai + IT Inventory sortable)
3. Verifikasi urutan default: Produksi (Used 1450), Cabang Medan (880), Cabang Surabaya (780), Kantor Pusat (700)
4. Verifikasi Produksi: Group Code GRP-PRD, Allocated Quota 1500, Allocated to Subgroups 0, Used 1450, Reserved 5, Remaining 45, + Audit 20, + Tracking 20, + Maintenance Routine 4, + Repair Ticketing 4, + Maps `—`, + IT Inventory 40
5. Verifikasi Cabang Surabaya: Allocated Quota 800, Used 780, Reserved 10, Remaining 10

### TC-FA-LIC-327: Group Name berupa link

6. Arahkan kursor ke teks `Produksi`
7. Verifikasi warna teks berubah menjadi biru (primary Fixed Asset)
8. Verifikasi teks `Produksi` tanpa garis bawah
9. Klik teks `Produksi`
10. Verifikasi klik tidak membuka halaman lain, hanya memilih node di Sidebar

### TC-FA-LIC-53: Used dan Reserved hanya aset langsung di grup

11. Klik node `Kantor Pusat`; catat `Used by This Group`
12. Klik node `Divisi Logistik`; catat `Used by This Group`
13. Verifikasi Kantor Pusat `Used by This Group` = 700 (tidak menjumlah child)
14. Verifikasi Divisi Logistik `Used by This Group` = 350
15. Verifikasi aset Gudang A (100) tidak dihitung ke Divisi Logistik

### TC-FA-LIC-54: Kolom addon per grup

16. Klik node `All Groups`; catat kolom addon keempat grup level 1
17. Klik node `Kantor Pusat`; catat kolom addon ketiga grup anak
18. Klik node `Divisi Logistik`; catat kolom addon grup `Gudang A`
19. Verifikasi jumlah kolom lintas delapan grup: `+ Audit` = 60, `+ Tracking` = 48, `+ Maintenance Routine` = 12, `+ Repair Ticketing` = 12, `+ IT Inventory` = 120 (sama dengan Used di License Summary)
20. Verifikasi kolom `+ Maps` bernilai `—` di semua grup

### TC-FA-LIC-55: Group Name memilih node di Sidebar dan Sidebar auto-expand

21. Klik tombol Expand/Collapse All untuk menutup seluruh node Sidebar
22. Klik node `All Groups`
23. Klik teks `Kantor Pusat` di Section 2
24. Verifikasi node `Kantor Pusat` terpilih di Sidebar dan kedua section berganti ke Kantor Pusat
25. Verifikasi Sidebar auto-expand sampai node `Kantor Pusat` tampil

### TC-FA-LIC-59: Search tanpa hasil

26. Klik node `All Groups`
27. Ketik Search `zzzz`, tekan Enter
28. Verifikasi Section 2: ilustrasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`
29. Klik `(←)` pada kotak Search

### TC-FA-LIC-62: Nama grup panjang tampil utuh

30. Buat grup dengan nama 120 karakter di bawah Kantor Pusat lewat fixture BE, lalu muat ulang halaman License
31. Klik Tab `Allocation Quota`
32. Klik node `Kantor Pusat`
33. Verifikasi kolom Group Name pada Section 2 menampilkan nama grup 120 karakter utuh (hug content), tidak dipotong `..`
34. Hapus grup dengan nama 120 karakter lewat fixture BE

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-52, 53, 54, 55, 59, 62, 327). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC-327 sesudah TC-52 (halaman yang sama), TC-62 (membuat grup) di akhir (S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 1 (klik Tab), langkah 21 (menutup seluruh node untuk precondition TC-55), langkah 22 (kembali ke node `All Groups`), langkah 26 (kembali ke node `All Groups`), langkah 29 (menutup input Search), langkah 31 (membuka Tab sesudah muat ulang), langkah 34 (pemulihan). Langkah 16 sampai 18 menggabungkan klik node dan pencatatan nilai kolom yang menjadi langkah TC-54.
- Langkah 15 mengasersi klausa TC-53 butir b bagian kedua ("aset Gudang A (100) tidak dihitung ke Divisi Logistik") sebagai Verifikasi sendiri.
- Temuan untuk QA:
  - TC-54 meminta "jumlahkan tiap kolom addon di delapan grup" tanpa menyebut nilai per grup anak; nilai anak (Kantor Pusat, Divisi Logistik) tidak ada di TC, sehingga asersi memakai jumlah lintas delapan grup saja.
  - TC-55 Precondition "Sidebar dalam keadaan collapse semua node" tidak menyebut cara mencapainya; langkah 21 memakai tombol Expand/Collapse All dan mengasumsikan klik menutup seluruh node walau sebagian node terbuka akibat langkah sebelumnya.
  - TC-62 Precondition menyebut grup 120 karakter "Pre-setup #12" padahal Pre-setup #12 tidak memuat grup itu; grup dibuat lewat fixture BE.
