---
id: TC-FA-SU-E2E-002-sidebar-group-tree-screening-tombol-open-collapse-dan-pencarian-node
title: "Sidebar Group Tree: Screening, Tombol Open/Collapse, dan Pencarian Node"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-4
  - TC-FA-SU-5
  - TC-FA-SU-6
coverage:
  web: automated
---

# Sidebar Group Tree: Screening, Tombol Open/Collapse, dan Pencarian Node

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan pohon grup (#21): All Groups > Finance & Accounting (anak: Accounts Payable), IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa (anak: Jakarta Selatan Distribution Center). Nilai dibaca dari `Fixture.faSettingsUser.preSetup` (fixture belum ada, disediakan tim FE).
- Data Dinamis: tidak ada.
- Kemampuan teknis: penghapusan state persisten panel Sidebar Group Tree (Open atau Collapsed) milik akun aktor di hook `before` sehingga panel berada pada kunjungan pertama (precondition TC-FA-SU-5 Expected a), dan pemulihannya di hook `after`; kemampuan ini disediakan tim FE (mekanisme penyimpanan state tidak disebut TC).
- State global: state panel Sidebar Group Tree akun aktor; dipulihkan langkah 20 dan hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-4: Screening Sidebar Group Tree: header, node, dan urutan

1. Verifikasi panel Right Panel Collapsible lebar `w-64` tampil di kanan halaman dengan Title `Groups`
2. Verifikasi header tanpa tombol close ✕
3. Verifikasi header tanpa garis pembatas di bawahnya
4. Verifikasi baris kedua memuat TreeSearchInput (prefix icon search, suffix clear) sejajar tombol icon-only Expand/Collapse All
5. Verifikasi pohon `All Groups` > Finance & Accounting (anak: Accounts Payable), IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse
6. Verifikasi tidak ada tombol aksi Group pada panel
7. Verifikasi tidak ada menu ⋯ per node pada tree halaman ini

### TC-FA-SU-5: Tombol Open/Collapse Sidebar Group Tree: tooltip dan state persisten

8. Verifikasi panel Open dengan tombol mengambang ▶ di tepi kiri panel
9. Hover tombol mengambang di tepi panel
10. Verifikasi tooltip tombol saat Open `Collapse Group Tree`
11. Klik tombol mengambang di tepi panel
12. Verifikasi panel collapse dan tombol pindah ke tepi kanan layar dengan ikon ◀
13. Verifikasi tabel melebar penuh
14. Hover tombol dalam state Collapsed
15. Verifikasi tooltip tombol saat Collapsed `Open Group Tree`
16. Tekan F5
17. Verifikasi panel tetap Collapsed setelah F5
18. Pindah ke menu lain pada sidebar navigasi lalu kembali ke Settings > User
19. Verifikasi panel tetap Collapsed setelah kunjungan ulang
20. Klik tombol ◀ untuk memulihkan panel ke state Open

### TC-FA-SU-6: Sidebar Group Tree: pencarian node saat Enter, Expand/Collapse All

21. Ketik `Finance` di TreeSearchInput tanpa menekan Enter
22. Verifikasi tree belum difilter (node `Branch Surabaya` masih tampil)
23. Tekan Enter
24. Verifikasi node Finance & Accounting tampil beserta parent-nya (`All Groups`)
25. Verifikasi node yang tidak cocok disembunyikan (node `Branch Surabaya` tidak tampil)
26. Kosongkan input TreeSearchInput lalu tekan Enter
27. Verifikasi tree kembali ke kondisi tanpa filter (node `Branch Surabaya` tampil)
28. Klik tombol Expand/Collapse All
29. Verifikasi seluruh node terbuka
30. Klik tombol Expand/Collapse All sekali lagi
31. Verifikasi seluruh node tertutup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 18 ("menu lain" dipilih penulis skrip; tujuan hanya sarana pindah halaman), langkah 20 (memulihkan panel ke Open sebelum TC-FA-SU-6, S-09). Langkah 22 dan 25 memakai node `Branch Surabaya` sebagai pembanding agar asersi absence tidak lolos pada tree yang belum termuat (bagian 8b butir 2, S-03).
- Langkah 1 TC-FA-SU-5 ("Buka Settings > User") dipenuhi hook `beforeEach` suite.
- Temuan untuk QA:
  - TC-FA-SU-5 langkah 5 ("Pindah ke menu lain") tidak menyebut menu tujuan; spec memakai menu lain mana pun pada sidebar navigasi.
  - TC-FA-SU-5 Expected a ("Kunjungan pertama") membutuhkan state panel yang belum pernah disimpan, tetapi Precondition TC tidak menyebutnya; spec menuliskannya sebagai kemampuan "disediakan tim FE".
  - TC-FA-SU-4 menyebut pohon tanpa `Region Jawa` pada Expected c padahal Pre-setup #21 memuat `Region Jawa` dengan anak `Jakarta Selatan Distribution Center`; spec mengasersi persis seperti Expected TC (enam node di bawah `All Groups`).
  - TC-FA-SU-6 Expected d dan TC-FA-SU-4 Expected c: Expected TC-FA-SU-4 menampilkan seluruh node (terbuka) pada kondisi awal, sedangkan Expected TC-FA-SU-6 d menyebut klik pertama Expand/Collapse All "membuka seluruh node"; keadaan awal pohon (terbuka atau tertutup) tidak konsisten antar TC. Spec mengikuti TC-FA-SU-6 (klik pertama membuka, klik kedua menutup).
