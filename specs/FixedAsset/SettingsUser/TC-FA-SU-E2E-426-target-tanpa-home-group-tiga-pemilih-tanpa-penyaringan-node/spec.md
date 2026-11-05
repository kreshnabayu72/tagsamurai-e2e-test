---
id: TC-FA-SU-E2E-426-target-tanpa-home-group-tiga-pemilih-tanpa-penyaringan-node
title: "Target Tanpa Home Group: Pemilih Group Role, Modal Assign Transaction Role, dan Popup Assign Group Transaction Role Tanpa Penyaringan Node"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1119
coverage:
  web: automated
---

# Target Tanpa Home Group: Pemilih Group Role, Modal Assign Transaction Role, dan Popup Assign Group Transaction Role Tanpa Penyaringan Node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan Transaction Role (Pre-setup #39). Target tanpa Home Group memakai seed `FaUserNoHG` (Pre-setup #50), diterapkan per target: hanya Home Group Gita Permata dan Mira Anggraini yang dikosongkan lewat seed API di hook `before`; pengguna lain tidak diubah. Seed `FaUserNoHG` wajib disediakan tim FE/BE sebelum eksekusi.
- Pengguna target: Gita Permata (Group Role baris Manage files; Home Group dikosongkan) dan Mira Anggraini (Disposal × Staff pada Finance & Accounting; Pre-setup #39; Home Group dikosongkan). Gita Permata juga akun aktor Pre-setup #20; di spec ini hanya menjadi pengguna target dan sesi aktor tetap Total Control Lina Marlina.
- Data uji: node Finance & Accounting, Accounts Payable, IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa, dan Jakarta Selatan Distribution Center pada tiga pemilih: popup Select Group (Gita Permata, baris Manage files), modal Assign Transaction Role tombol Group (Mira Anggraini), dan popup Assign Group Transaction Role baris Disposal × Staff (Mira Anggraini).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): seed `FaUserNoHG` (Pre-setup #50) per target di hook `before`; pemulihan Home Group Gita Permata dan Mira Anggraini ke Finance & Accounting (Home Group awal menurut Pre-setup #51) di hook `after`. Selektor node pohon, status Disabled, dan tooltip disediakan tim FE.
- State global yang diubah: Home Group Gita Permata dan Mira Anggraini (dikosongkan di hook `before`); dipulihkan lewat seed API di hook `after`. Tidak ada data yang disimpan oleh langkah; popup dan modal dibuang lewat `[Cancel]` dan `[Leave]`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script (kunci baru: node Accounts Payable, Region Jawa, Jakarta Selatan Distribution Center, dan seed #50 per target).

## Test Steps

### TC-FA-SU-1119: Target tanpa Home Group: pemilih Group Role, modal Assign Transaction Role, dan popup Assign Group Transaction Role tanpa penyaringan node

1. Ketik Search `Gita Permata`, tekan Enter, lalu klik Name `Gita Permata`
2. Klik Tab Role lalu Sub-tab Group Role
3. Catat badge setiap baris Sub-tab Group Role Gita Permata sebagai baseline
4. Klik `[Assign Group]` pada baris Manage files, lalu klik `[+ Assign Group]`
5. Verifikasi pada popup Select Group Finance & Accounting, Accounts Payable, IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa, dan Jakarta Selatan Distribution Center tidak Disabled dan dapat dicentang
6. Arahkan kursor ke IT Infrastructure
7. Verifikasi tidak ada tooltip node di luar Home Group pada IT Infrastructure
8. Arahkan kursor ke Region Jawa
9. Verifikasi tidak ada tooltip node di luar Home Group pada Region Jawa
10. Klik `[Cancel]` pada popup Select Group, lalu klik `[Cancel]` pada popup Assign Group Role
11. Verifikasi Sub-tab Group Role Gita Permata memuat badge setiap baris yang sama dengan baseline langkah 3 (tidak ada perubahan tersimpan)
12. Buka Settings > User lewat sidebar, ketik Search `Mira Anggraini`, tekan Enter, lalu klik Name `Mira Anggraini`
13. Klik Tab Role lalu Sub-tab Transaction Role
14. Catat jumlah baris Sub-tab Transaction Role Mira Anggraini dan badge grup tiap baris sebagai baseline
15. Klik `[+ Assign]`, lalu klik tombol Group
16. Verifikasi pada modal Assign Transaction Role Finance & Accounting, Accounts Payable, IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa, dan Jakarta Selatan Distribution Center tidak Disabled dan dapat dicentang
17. Arahkan kursor ke IT Infrastructure
18. Verifikasi tidak ada tooltip node di luar Home Group pada IT Infrastructure
19. Arahkan kursor ke Region Jawa
20. Verifikasi tidak ada tooltip node di luar Home Group pada Region Jawa
21. Klik `[✕]` pada modal
22. Verifikasi dialog `Unsaved Changes`
23. Klik `[Leave]`
24. Klik `[Assign Group]` pada baris Disposal × Staff
25. Verifikasi pada popup Assign Group Transaction Role Finance & Accounting, Accounts Payable, IT Infrastructure, Branch Surabaya, General Affairs, Logistics Warehouse, Region Jawa, dan Jakarta Selatan Distribution Center tidak Disabled dan dapat dicentang
26. Arahkan kursor ke IT Infrastructure
27. Verifikasi tidak ada tooltip node di luar Home Group pada IT Infrastructure
28. Arahkan kursor ke Region Jawa
29. Verifikasi tidak ada tooltip node di luar Home Group pada Region Jawa
30. Klik `[Cancel]`
31. Verifikasi Sub-tab Transaction Role Mira Anggraini memuat jumlah baris dan badge tiap baris yang sama dengan baseline langkah 14 (tidak ada perubahan tersimpan)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 10, 12, 13, 14, dan 30. Search pada langkah 1 dan 12 menemukan baris target (R-16, R-23). Langkah 12 membuka layar secara eksplisit sesudah pindah dari Detail Gita Permata ke Detail Mira Anggraini (S-14). Baseline langkah 3 dan 14 dipakai Expected c (langkah 11 dan 31).
- Expected a (delapan node tidak Disabled dan dapat dicentang) ditulis satu `Verifikasi` per pemilih (langkah 5, 16, 25) dengan delapan node disebut utuh. Expected b (tidak ada tooltip) ditulis satu `Verifikasi` per node yang di-hover (IT Infrastructure dan Region Jawa) pada tiap pemilih (langkah 7, 9, 18, 20, 27, 29); hover mendahului tiap asersi (bagian 8b butir 5) dan `Verifikasi` node tidak Disabled dan dapat dicentang pada langkah 5, 16, dan 25 menjadi anchor positif bahwa node tampil (bagian 8b butir 2).
- Penutupan modal pada langkah 21 sampai 23 mengikuti S-08; popup ditutup lewat `[Cancel]` (langkah 10, 30).
- Pre-setup #50 diterapkan hanya pada Gita Permata dan Mira Anggraini (bukan seluruh 25 pengguna): kebutuhan TC-FA-SU-1119 hanya dua target itu, dan Home Group keduanya dipulihkan di hook `after`. TC-FA-SU-1119 tidak ada di spec lain.
- Temuan untuk QA:
  - Pre-setup #50 (`FaUserNoHG`) didefinisikan global (Home Group seluruh 25 pengguna dikosongkan); spec memakai penerapan per target (hanya Gita Permata dan Mira Anggraini) untuk menghindari state global berat. Mohon konfirmasi bila #50 harus diterapkan penuh.
  - Seed `FaUserNoHG` (Pre-setup #50) wajib disediakan tim FE/BE; kunci fixture baru dicatat untuk fixture `fixtures/fixed-asset-settings-user.json`.
  - TC-FA-SU-1119 langkah 4 menutup modal lewat `[Leave]` walau TC tidak menyebut pilihan node pada modal; spec menuliskan `[✕]`, dialog `Unsaved Changes`, lalu `[Leave]` (S-08). Bila modal tanpa pilihan tidak dirty sehingga dialog tidak tampil, langkah 21 sampai 23 perlu disesuaikan oleh QA.
  - TC-FA-SU-1119 Expected c ("tidak ada perubahan tersimpan") tidak menyebut cara observasi; spec membandingkan badge Sub-tab Group Role Gita Permata dan baris Sub-tab Transaction Role Mira Anggraini terhadap baseline.
  - TC-FA-SU-1119 langkah 2 meminta `[Cancel]` pada popup Assign Group Role tanpa pilihan node; spec mengikuti TC dan tidak menambahkan dialog.
  - Post Condition TC-FA-SU-1119 ("Tidak ada perubahan data") hanya diasersi lewat Expected c.
