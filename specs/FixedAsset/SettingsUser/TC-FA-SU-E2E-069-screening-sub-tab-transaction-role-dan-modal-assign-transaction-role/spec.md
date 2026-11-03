---
id: TC-FA-SU-E2E-069-screening-sub-tab-transaction-role-dan-modal-assign-transaction-role
title: "Screening Sub-tab Transaction Role dan Modal Assign Transaction Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-228
  - TC-FA-SU-229
  - TC-FA-SU-230
  - TC-FA-SU-231
  - TC-FA-SU-232
coverage:
  web: automated
---

# Screening Sub-tab Transaction Role dan Modal Assign Transaction Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting; 2 baris); Yuda Pratama (7 baris contoh PRD: Borrowing & Assignment × Approver pada IT Infrastructure, Damaged × Monitoring & Report pada Branch Surabaya, Disposal × Staff pada Logistics Warehouse, Missing × Approver pada Branch Surabaya, General Affairs, dan Logistics Warehouse, Transfer × Asset Admin pada Finance & Accounting dan IT Infrastructure, Transfer × Monitoring & Report pada Branch Surabaya, Disposal × Approver pada All Groups); Hana Kusuma (tanpa Transaction Role; Pre-setup #20).
- Data uji: Group Finance & Accounting dan Transaction Disposal dipilih pada TC-FA-SU-232.
- State global yang diubah: tidak ada data yang disimpan; isian modal dibuang lewat `[Leave]`.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-228: Screening Sub-tab Transaction Role: toolbar, kolom, aksi baris, dan ikon

1. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role
2. Verifikasi TableTools berisi Search, Filter, tombol `[+ Assign]`, dan ikon Changelog
3. Verifikasi Bulk Actions Bar dengan `[Bulk Remove]` tidak tampil selama belum ada baris terpilih
4. Centang satu baris
5. Verifikasi Bulk Actions Bar dengan `[Bulk Remove]` tampil
6. Verifikasi tabel berkolom checkbox | Transaction | Role | Group | Actions
7. Verifikasi kolom Role tidak dapat di-sort
8. Verifikasi aksi baris `[Assign Group]` dengan ikon sama dengan `[Assign Group]` Sub-tab Group Role
9. Buka menu `⋯` pada baris itu
10. Verifikasi menu `⋯` berisi `Remove` (ikon `DeleteBin6Line`, severity danger)
11. Verifikasi ukuran halaman tabel 10 baris per halaman
12. Verifikasi tidak ada matriks CRUD maupun banner
13. Tutup menu `⋯` dan hapus centang baris

### TC-FA-SU-229: Group Summary Badge pada Sub-tab Transaction Role: 1, 2, lebih dari 2 grup, dan All Groups

14. Buka Detail Yuda Pratama > Tab Role > Sub-tab Transaction Role
15. Verifikasi baris Borrowing & Assignment × Approver menampilkan 1 badge
16. Verifikasi baris Transfer × Asset Admin menampilkan 2 badge (Finance & Accounting, IT Infrastructure)
17. Verifikasi baris Missing × Approver menampilkan 2 badge dan chip `+1 more`
18. Klik chip `+1 more`
19. Verifikasi popover memuat seluruh grup baris Missing × Approver
20. Verifikasi baris Disposal × Approver pada seluruh grup menampilkan badge tunggal `All Groups`
21. Verifikasi kolom Group tidak pernah kosong pada setiap baris
22. Tutup popover

### TC-FA-SU-230: Empty state Sub-tab Transaction Role tanpa penugasan

23. Buka Detail Hana Kusuma > Tab Role > Sub-tab Transaction Role
24. Verifikasi ilustrasi dengan Title `No transaction role yet` dan Description `Transaction roles assigned to this user will appear here.`
25. Verifikasi tombol `[+ Assign]` tetap tampil

### TC-FA-SU-231: Screening modal Assign Transaction Role: header, field, placeholder, dan footer

26. Buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role lalu klik `[+ Assign]`
27. Verifikasi header `Assign Transaction Role` dengan close `[✕]`
28. Verifikasi field `Group *` berupa TreeSelect multi-select dengan tombol `Select Group`
29. Verifikasi field `Transaction *` berupa Select dengan placeholder `Select transaction type...`
30. Verifikasi field `Role *` berupa Select dengan placeholder `Select role...`
31. Verifikasi checkbox `Stay on this form after submitting` rata kanan dan tidak tercentang
32. Verifikasi footer `[Clear Field]` (Text, Primary) dan `[Submit]` (Success)
33. Verifikasi tidak ada tombol `[Cancel]`
34. Verifikasi field Transaction dan Role Disabled sejak awal

### TC-FA-SU-232: Transaction terkunci sampai Group dipilih dan Role terkunci sampai Transaction dipilih

35. Verifikasi sebelum ada Group terpilih field Transaction Disabled
36. Verifikasi sebelum Transaction dipilih field Role Disabled
37. Klik tombol Group, centang Finance & Accounting, klik `[Select]`
38. Verifikasi field Transaction Enabled
39. Pilih Transaction Disposal
40. Verifikasi field Role Enabled
41. Klik `[✕]` pada modal
42. Verifikasi dialog `Unsaved Changes`
43. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 13, 22 dan 41 sampai 43. Penutupan modal dirty mengikuti S-08.
- Modal Assign Transaction Role dibuka sekali pada TC-FA-SU-231 dan dipakai TC-FA-SU-232 tanpa dibuka ulang (halaman yang sama dipakai berulang, bagian 3 prinsip 13); keadaan awal modal tidak berubah antar kedua TC.
- Jumlah langkah 43, di atas smell 35 langkah; semua blok satu kelas harness (screening baca tanpa menyimpan data) dan berdiri sendiri, kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-SU-228 butir d ("terpaginasi 10 baris per halaman") tidak dapat diamati pada Mira Anggraini yang hanya memiliki 2 baris Transaction Role; spec mengasersi ukuran halaman default 10 baris per halaman.
  - TC-FA-SU-228 langkah 3 ("buka menu ⋯ baris itu") tidak disertai Expected untuk menu selain isi `Remove`; spec mengasersi sesuai teks Expected.
  - TC-FA-SU-229 butir b menyebut popover `+1 more` "membuka popover seluruh grup" tanpa menyebut isinya; spec mengasersi bahwa popover memuat seluruh grup baris itu (Branch Surabaya, General Affairs, Logistics Warehouse).
