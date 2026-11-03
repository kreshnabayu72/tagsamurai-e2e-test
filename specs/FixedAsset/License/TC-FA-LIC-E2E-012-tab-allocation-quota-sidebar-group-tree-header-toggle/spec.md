---
id: TC-FA-LIC-E2E-012-tab-allocation-quota-sidebar-group-tree-header-toggle
title: "Tab Allocation Quota: Sidebar Group Tree, Header, Pencarian, Pemilihan Node, dan Toggle Collapse"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-47
  - TC-FA-LIC-48
  - TC-FA-LIC-56
  - TC-FA-LIC-57
  - TC-FA-LIC-539
coverage:
  web: automated
---

# Tab Allocation Quota: Sidebar Group Tree, Header, Pencarian, Pemilihan Node, dan Toggle Collapse

## Prerequisites

- Mode: FE+BE
- Akun aktor: Total Control Pre-setup #1 `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (client PT Sejahtera, plan Professional (Paid), `License allocation per group` ON; kredensial `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman Fixed Asset > License dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup #12: hierarki Produksi, Kantor Pusat (Divisi Logistik (Gudang A), Divisi IT, Divisi Keuangan), Cabang Surabaya, Cabang Medan; hanya dibaca, tidak diubah. Nilai dibaca dari `Fixture.fixedAssetLicense.*`; berkas fixture belum ada, disediakan tim FE.
- State sisi klien yang diubah spec: status collapsed Sidebar Group Tree (TC-FA-LIC-48) dikembalikan ke terbuka pada langkah 36; preferensi tersimpan dipulihkan oleh hook `after` (kemampuan menghapus preferensi di browser disediakan tim FE). Keadaan awal Sidebar Group Tree pada kunjungan pertama: seluruh node tertutup (sesuai Precondition TC-FA-LIC-55).
- Hook dan kemampuan suite (flag Guided Tooltip seen, sesi API aktor, fixture BE, pemulihan preferensi di browser): dinyatakan sekali di suite.md.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-FA-LIC-47: Header Sidebar tanpa tombol aksi, pencarian saat Enter, Expand/Collapse All

1. Klik Tab `Allocation Quota`
2. Verifikasi header Sidebar: judul `Groups`, TreeSearchInput, dan tombol Expand/Collapse All
3. Verifikasi tidak ada tombol aksi `+ Group` pada header Sidebar
4. Ketik `Logistik` di TreeSearchInput tanpa menekan Enter
5. Verifikasi pohon tidak berubah sebelum Enter
6. Tekan Enter
7. Verifikasi pohon menampilkan node yang cocok `Divisi Logistik` beserta induknya
8. Kosongkan input TreeSearchInput, lalu tekan Enter
9. Verifikasi pohon kembali utuh
10. Klik tombol Expand/Collapse All
11. Verifikasi seluruh node pohon terbuka

### TC-FA-LIC-539: Node Sidebar hanya untuk memilih

12. Arahkan kursor ke node `Kantor Pusat`
13. Arahkan kursor ke node yang sedang terpilih (`All Groups`)
14. Verifikasi tidak ada tombol aksi titik tiga `⋯` pada baris node `All Groups`, `Produksi`, `Kantor Pusat`, `Divisi Logistik`, dan `Gudang A`, termasuk saat hover dan pada node terpilih
15. Verifikasi tidak ada indikator fungsi (titik berwarna) pada baris node yang sama
16. Klik node `Divisi Logistik`
17. Verifikasi klik node hanya memilih node: Section 1 dan Section 2 berganti tanpa menu atau popover aksi

### TC-FA-LIC-56: Klik node mengganti kedua section sekaligus

18. Klik node `Kantor Pusat`
19. Verifikasi Section 1 dan Section 2 berganti sekaligus ke `Kantor Pusat`
20. Klik node `Divisi Logistik`
21. Verifikasi Section 1 dan Section 2 berganti sekaligus ke `Divisi Logistik`
22. Klik node `All Groups`
23. Verifikasi Section 1 dan Section 2 berganti sekaligus ke `All Groups`
24. Verifikasi hanya satu node aktif pada satu waktu dan selalu ada satu node aktif

### TC-FA-LIC-57: Node leaf menampilkan empty state No subgroup yet

25. Klik node `Gudang A`
26. Verifikasi Section 1 `Group Quota` menampilkan Group Quota Summary Gudang A
27. Verifikasi Section 2 `Child Groups Quota`: ilustrasi empty state dengan Title `No subgroup yet` dan Description `This group does not have any subgroups.`

### TC-FA-LIC-48: Toggle collapse dengan tooltip dan state tersimpan

28. Arahkan kursor ke tombol toggle di tepi panel Sidebar
29. Verifikasi tooltip `Collapse Group Tree`
30. Klik tombol toggle untuk collapse
31. Verifikasi konten kiri melebar penuh saat Sidebar collapse
32. Arahkan kursor ke tombol toggle
33. Verifikasi tooltip `Open Group Tree`
34. Buka halaman lain (menu Dashboard), lalu kembali ke License > Allocation Quota
35. Verifikasi state collapsed Sidebar dipertahankan setelah kembali ke halaman
36. Klik tombol toggle untuk membuka Sidebar kembali

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md` (TC-FA-LIC-47, 48, 56, 57, 539). Tidak ada TC hanya-BE di spec ini.
- Urutan TC diubah dari urutan nomor: TC-48 (menyimpan state collapsed) di akhir, dan TC-539 sesudah TC-47 karena langkah 10 membuka seluruh node sehingga langkah "klik Expand All" TC-539 terpenuhi (S-10).
- Spec di atas 35 langkah (36 langkah): seluruh blok satu topik (Sidebar Group Tree pada dataset #12 yang sama) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 1 (klik Tab `Allocation Quota`, langkah TC-47), langkah 36 (membuka kembali Sidebar). Langkah 12, 13, 16 memetakan langkah TC-539; langkah 34 memetakan langkah 4 TC-48.
- Temuan untuk QA:
  - TC-47 Expected e ("Expand/Collapse All membuka atau menutup seluruh node") tidak menyebut arah toggle pada keadaan awal; spec mengasumsikan keadaan awal tertutup (Precondition TC-55) sehingga klik pertama membuka seluruh node dan asersi menutup seluruh node tidak ditulis.
  - TC-48 butir c menyebut state collapsed dipertahankan setelah kembali ke halaman tanpa menyebut mekanisme penyimpanan; spec mengasersi hanya perilaku UI.
