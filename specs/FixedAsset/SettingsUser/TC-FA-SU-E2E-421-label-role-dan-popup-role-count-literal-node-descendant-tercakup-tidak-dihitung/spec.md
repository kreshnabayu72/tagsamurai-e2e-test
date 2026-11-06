---
id: TC-FA-SU-E2E-421-label-role-dan-popup-role-count-literal-node-descendant-tercakup-tidak-dihitung
title: "Label Role dan Popup Role Count Literal: Node Descendant yang Tercakup Tidak Dihitung"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1113
coverage:
  web: automated
---

# Label Role dan Popup Role Count Literal: Node Descendant yang Tercakup Tidak Dihitung

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1, `totalControl_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite. Hook suite dinyatakan di `suite.md`.
- Data Pre-setup: Client `FaUserMain` (#20), pohon grup (#21: Region Jawa dengan anak Jakarta Selatan Distribution Center), dan varian `FaUserOV` (#49). Target: Rina Susanti dalam varian `FaUserOV`, tanpa Global Role dan Group Role, dengan 5 penugasan Transaction Role: Disposal × Asset Admin (Region Jawa), Disposal × Approver (Region Jawa), Disposal × Monitoring & Report (Jakarta Selatan Distribution Center), Damaged × Staff (Finance & Accounting), Transfer × Monitoring & Report (Jakarta Selatan Distribution Center); label Role awal `5 roles`. Varian `FaUserOV` wajib disediakan tim FE/BE lewat seed API sebelum eksekusi (belum ada di environment).
- Rina Susanti juga akun aktor Read Only (Pre-setup #5, `Spectra.env.FA_MURG_RO_PASSWORD`) pada suite lain; di spec ini ia hanya target aksi dan tidak dipakai sebagai sesi aktor.
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Rina Susanti (Logistics Warehouse pada Pre-setup #43/#49) dikosongkan lewat seed API di hook `before` supaya Region Jawa (langkah 13) tidak Disabled oleh gate Home Group constraint dan Assign Damaged × Asset Admin pada Region Jawa tidak ditolak `422` (V-09); seed pemulihan Pre-setup #49 pada langkah 24 memulihkan penugasan Transaction Role, dan Home Group Rina Susanti dipulihkan ke Logistics Warehouse di hook `after`. Seed per target disediakan tim FE/BE.
- Data uji: penugasan baru Damaged × Asset Admin pada Group Region Jawa (mencakup Jakarta Selatan Distribution Center), Transaction `Damaged`, Role `Asset Admin`.
- Nilai nama pengguna, grup, dan penugasan dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed API untuk menyediakan Rina Susanti varian `FaUserOV` (#49) dan memulihkannya dengan menghapus penugasan Damaged × Asset Admin.
- State global dan pemulihan: Transaction Role, Last Updated, Modified By, dan Tab Changelog Rina Susanti berubah oleh langkah 14. Dipulihkan ke Pre-setup #49 lewat seed API pada langkah 24 dan di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-1113: Label kolom Role dan Popup Role Count menghitung baris penugasan tersimpan secara literal: node descendant yang hanya tercakup tidak dihitung

1. Ketik Search `Rina`, tekan Enter
2. Verifikasi label kolom Role Rina Susanti `5 roles`
3. Klik label `5 roles` pada Rina Susanti
4. Verifikasi header popup `Active Roles (5)` sama dengan label kolom Role
5. Verifikasi seksi Transaction Role tampil di popup
6. Verifikasi seksi Global Role dan Group Role tidak tampil di popup
7. Verifikasi bullet seksi Transaction Role urut Role lalu Transaction: `Asset Admin — Disposal — 1 group`, `Approver — Disposal — 1 group`, `Monitoring & Report — Disposal — 1 group`, `Monitoring & Report — Transfer — 1 group`, `Staff — Damaged — 1 group`
8. Verifikasi Region Jawa dihitung satu group walau mencakup Jakarta Selatan Distribution Center (bullet `Asset Admin — Disposal — 1 group` dan `Approver — Disposal — 1 group`)
9. Tutup popup lewat `[✕]`
10. Klik Name `Rina Susanti`
11. Klik Tab Role lalu Sub-tab Transaction Role
12. Klik `[+ Assign]`
13. Pilih Group Region Jawa, Transaction Damaged, Role Asset Admin
14. Klik `[Submit]`
15. Tunggu aksi selesai (modal Assign Transaction Role tertutup dan baris Damaged × Asset Admin tampil di Sub-tab Transaction Role)
16. Kembali ke User List lewat Breadcrumb
17. Ganti isi kotak search dengan `Rina`, tekan Enter
18. Verifikasi label kolom Role Rina Susanti `6 roles` (bertambah satu dari `5 roles`)
19. Klik label `6 roles` pada Rina Susanti
20. Verifikasi header popup `Active Roles (6)` sama dengan label kolom Role
21. Verifikasi bullet baru `Asset Admin — Damaged — 1 group` tampil di seksi Transaction Role
22. Verifikasi hitungan `6` sama dengan jumlah penugasan tersimpan secara literal (5 awal ditambah 1 baru) dan tidak bertambah oleh node Jakarta Selatan Distribution Center yang hanya tercakup Region Jawa
23. Tutup popup lewat `[✕]`
24. Pulihkan Rina Susanti ke Pre-setup #49 lewat seed API (hapus penugasan Damaged × Asset Admin)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, S-03): langkah 1 dan 17 (Search untuk menemukan baris target, R-16; langkah 10 memakai Search langkah 1 yang masih aktif, R-23), langkah 9 dan 23 (menutup popup), langkah 15 (tunggu aksi selesai karena langkah berikutnya berpindah surface, 8b butir 8), langkah 16 (kembali ke User List), dan langkah 24 (pemulihan, S-09).
- Langkah 6 adalah asersi absence; anchornya langkah 5 (seksi Transaction Role tampil pada popup yang sama, 8b butir 2).
- Expected d TC ("hitungan mengikuti penugasan literal tersimpan") diasersi pada langkah 22 sebagai kesimpulan atas langkah 18, 20, dan 21; ketiganya tetap punya `Verifikasi` sendiri.
- Pre-setup #50 diterapkan hanya pada Rina Susanti (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih Region Jawa di luar Home Group Logistics Warehouse. Penugasan Transaction Role tetap sesuai Pre-setup #49. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Temuan untuk QA:
  - Seed varian `FaUserOV` (Pre-setup #49) wajib disediakan untuk spec ini; tanpa seed itu langkah 2 sampai 8 tidak dapat dijalankan.
  - TC-FA-SU-1113 langkah 4 ("Kembali ke User List") tidak menyebut caranya; spec memakai Breadcrumb dan kotak Search diisi ulang (8b butir 9). Selektor Breadcrumb perlu dikonfirmasi tim FE.
  - Pre-setup TC tidak mencatat email Rina Susanti dalam varian `FaUserOV`; spec mengikuti TC dengan Search `Rina` dan mengidentifikasi baris lewat Name `Rina Susanti` (R-06). Bila ada pengguna lain yang namanya memuat `Rina`, Search perlu dipersempit; email disediakan tim FE.
  - Rina Susanti juga akun aktor Read Only (#5) pada suite ini; spec memakainya hanya sebagai target dan tidak mencampur sesi aktor.
  - Expected b menyebut `Region Jawa dihitung satu group`; bullet Region Jawa pada Pre-setup #49 adalah `Asset Admin — Disposal` dan `Approver — Disposal`, sehingga spec mengasersinya pada kedua bullet itu (langkah 8).
