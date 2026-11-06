---
id: TC-FA-SU-E2E-409-preview-scope-di-modal-assign-transaction-role
title: "Preview Scope di Modal Assign Transaction Role: Tampil Setelah Group Dipilih, Memuat Node Terpilih beserta Descendant, Read-only, dan Bukan Baris Tabel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1102
coverage:
  web: automated
---

# Preview Scope di Modal Assign Transaction Role: Tampil Setelah Group Dipilih, Memuat Node Terpilih beserta Descendant, Read-only, dan Bukan Baris Tabel

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21: Finance & Accounting dengan anak Accounts Payable; Region Jawa dengan anak Jakarta Selatan Distribution Center) dan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting; 2 baris; Pre-setup #39). Spec ini mengubah data Mira Anggraini. Mira Anggraini ber-Home Group Finance & Accounting (Pre-setup #43/#48), sehingga Region Jawa di luar constraint dan Disabled di pemilih Group (tooltip S-45); sesuai Catatan TC (Home Group constraint FI-32), target tanpa Home Group memakai seed `FaUserNoHG` (Pre-setup #50), diterapkan per target: hanya Home Group Mira Anggraini yang dikosongkan lewat seed API di hook `before`; penugasan lain tidak berubah. Seed `FaUserNoHG` wajib disediakan tim FE/BE sebelum eksekusi.
- Data uji: Group Finance & Accounting lalu Finance & Accounting dan Region Jawa; Transaction Damaged × Role Asset Admin.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk mengosongkan Home Group Mira Anggraini (Pre-setup #50 per target) di hook `before` dan memulihkan Mira Anggraini ke Pre-setup #39 serta Home Group Finance & Accounting (Pre-setup #43) (baris Damaged × Asset Admin dihapus); pembacaan jumlah entri Tab Changelog Mira Anggraini lewat kemampuan baca BE sebagai baseline sebelum aksi `[Submit]` (bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit. Selektor preview scope disediakan tim FE (lihat Temuan untuk QA).
- State global yang diubah: seluruh baris Transaction Role Mira Anggraini (baris Damaged × Asset Admin ditambahkan) dan Tab Changelog Mira Anggraini; dipulihkan ke Pre-setup #39 dan #43 (Home Group Finance & Accounting, dikosongkan di hook `before`) lewat seed API pada langkah 24 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1102: Preview scope di Modal Assign Transaction Role: tampil setelah Group dipilih, memuat node terpilih beserta seluruh descendant, read-only, dan tidak menjadi baris tabel

1. Ketik Search `Mira Anggraini`, tekan Enter, lalu klik Name `Mira Anggraini`
2. Klik Tab Role lalu Sub-tab Transaction Role
3. Baca jumlah entri Tab Changelog Mira Anggraini lewat kemampuan baca BE sebagai baseline
4. Klik `[+ Assign]`
5. Verifikasi modal `Assign Transaction Role` tampil
6. Verifikasi tidak ada preview scope sebelum Group dipilih
7. Klik tombol Group, centang Finance & Accounting, klik `[Select]`
8. Verifikasi preview scope tampil sebelum `[Submit]`
9. Verifikasi preview scope mendaftar Finance & Accounting dan Accounts Payable (node terpilih dan seluruh descendant)
10. Verifikasi preview scope read-only (tanpa checkbox atau tombol)
11. Verifikasi preview scope tidak mengubah pilihan Group (tombol Group berlabel `1 Group selected`)
12. Klik tombol Group lagi, tambah centang Region Jawa (Finance & Accounting tetap tercentang), klik `[Select]`
13. Verifikasi preview scope mendaftar Finance & Accounting, Accounts Payable, Region Jawa, dan Jakarta Selatan Distribution Center
14. Verifikasi label tombol Group `2 Groups selected` tidak berubah oleh preview
15. Pilih Transaction Damaged dan Role Asset Admin
16. Klik `[Submit]`
17. Verifikasi muncul satu baris Damaged × Asset Admin
18. Verifikasi baris Damaged × Asset Admin menampilkan dua badge (Finance & Accounting dan Region Jawa)
19. Verifikasi Accounts Payable dan Jakarta Selatan Distribution Center tidak menjadi badge maupun baris tabel
20. Klik Tab Changelog
21. Verifikasi jumlah entri Tab Changelog Mira Anggraini bertambah tepat dua dari baseline langkah 3 (kemampuan baca BE)
22. Verifikasi dua entri teratas bertipe `Assign` dengan Field `Damaged — Finance & Accounting — Asset Admin` dan `Damaged — Region Jawa — Asset Admin`
23. Verifikasi tidak ada entri untuk Accounts Payable maupun Jakarta Selatan Distribution Center di antara entri baru
24. Pulihkan Mira Anggraini ke Pre-setup #39 dan Home Group Mira Anggraini ke Pre-setup #43 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 20 dan 24. Search `Mira Anggraini` pada langkah 1 menemukan baris target (R-16, R-23). Baseline langkah 3 dibaca sebelum aksi pemicu `[Submit]` (S-12). Pemulihan lewat seed API memulihkan Pre-setup #39 dan #43 (S-06, S-09).
- Langkah 5 (`Assign Transaction Role` tampil) adalah anchor positif bagi asersi tidak ada preview scope pada langkah 6 (bagian 8b butir 2); asersi itu bukan klausa Expected TC tambahan.
- Entri baru Tab Changelog dibaca pada dua baris teratas urutan default `Date` terbaru setelah selisih jumlah dari baseline dibuktikan (langkah 21); kedua entri jatuh dalam menit yang sama, sehingga spec mengasersi himpunan dua baris teratas tanpa mengandalkan urutan di antaranya (S-14). Langkah 23 beranchor dua entri langkah 22.
- Asersi tombol Group `1 Group selected` (langkah 11) memakai label tombol Group dari TC-FA-SU-234 sebagai cara mengamati bahwa pilihan Group tidak berubah oleh preview.
- Jumlah entri langkah 21 membuktikan satu entri per node terpilih, bukan satu per descendant.
- Temuan untuk QA:
  - TC-FA-SU-1102 Precondition tidak menyebut Pre-setup #50 sedangkan Mira Anggraini ber-Home Group, sehingga Region Jawa akan Disabled (S-45) dan penugasan ditolak 422 V-09; spec mengikuti Catatan TC (Home Group constraint FI-32) dan memakai seed `FaUserNoHG` (Pre-setup #50) per target, bukan seluruh 25 pengguna. Mohon dikonfirmasi bila #50 harus diterapkan penuh atau Precondition TC diperbarui.
  - Preview scope: PRD tidak menetapkan copy atau format preview. Spec mengasersi preview sebagai daftar node (longgar) dan tidak mengasersi teks judul atau urutan node; selektor preview scope perlu dikonfirmasi tim FE.
  - TC-FA-SU-1102 Expected b menyebut "read-only (tanpa checkbox atau tombol)" tanpa menyebut elemen yang diperiksa; spec mengasersi tidak ada checkbox maupun tombol di dalam area preview.
  - TC-FA-SU-1102 langkah 5 tidak menyebut toast hasil `[Submit]`; spec tidak mengasersi toast. Post Condition TC (entri log pada Tab System Log aktor dan Activity Log) tidak punya langkah observasi di TC sehingga tidak diasersi; hanya Tab Changelog target yang diasersi (Expected e).
  - Mira Anggraini hanya dipulihkan oleh seed API; spec bergantung pada kemampuan seed API tim FE/BE untuk Pre-setup #39.
