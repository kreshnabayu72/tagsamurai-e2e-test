---
id: TC-FA-SU-E2E-410-preview-scope-di-popup-assign-group-transaction-role
title: "Preview Scope di Popup Assign Group Transaction Role: Hanya untuk Grup yang Baru Dicentang, Read-only, dan Cancel Membuangnya tanpa Dialog"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1103
coverage:
  web: automated
---

# Preview Scope di Popup Assign Group Transaction Role: Hanya untuk Grup yang Baru Dicentang, Read-only, dan Cancel Membuangnya tanpa Dialog

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21: Region Jawa dengan anak Jakarta Selatan Distribution Center; IT Infrastructure; Finance & Accounting) dan Transaction Role (Pre-setup #39).
- Pengguna target: Mira Anggraini (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting; 2 baris; Pre-setup #39). Spec ini mengubah data Mira Anggraini. Mira Anggraini ber-Home Group Finance & Accounting (Pre-setup #43/#48), sehingga Region Jawa dan IT Infrastructure di luar constraint dan Disabled di pemilih Group (tooltip S-45); sesuai Catatan TC (Home Group constraint FI-32), target tanpa Home Group memakai seed `FaUserNoHG` (Pre-setup #50), diterapkan per target: hanya Home Group Mira Anggraini yang dikosongkan lewat seed API di hook `before`; penugasan lain tidak berubah. Seed `FaUserNoHG` wajib disediakan tim FE/BE sebelum eksekusi.
- Data uji: baris Disposal × Staff (Finance & Accounting); grup baru Region Jawa; IT Infrastructure dicentang lalu dibuang lewat `[Cancel]`.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk mengosongkan Home Group Mira Anggraini (Pre-setup #50 per target) di hook `before` dan memulihkan Mira Anggraini ke Pre-setup #39 serta Home Group Finance & Accounting (Pre-setup #43) (Region Jawa dicabut dari baris Disposal × Staff); pembacaan jumlah entri Tab Changelog Mira Anggraini lewat kemampuan baca BE sebagai baseline sebelum aksi (bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit. Selektor preview scope disediakan tim FE (lihat Temuan untuk QA).
- State global yang diubah: grup pada baris Disposal × Staff Mira Anggraini (Region Jawa ditambahkan) dan Tab Changelog Mira Anggraini; dipulihkan ke Pre-setup #39 dan #43 (Home Group Finance & Accounting, dikosongkan di hook `before`) lewat seed API pada langkah 29 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1103: Preview scope di popup Assign Group Transaction Role: hanya untuk grup yang baru dicentang, read-only, dan Cancel membuangnya tanpa dialog

1. Ketik Search `Mira Anggraini`, tekan Enter, lalu klik Name `Mira Anggraini`
2. Klik Tab Role lalu Sub-tab Transaction Role
3. Baca jumlah entri Tab Changelog Mira Anggraini lewat kemampuan baca BE sebagai baseline
4. Klik `[Assign Group]` pada baris Disposal × Staff
5. Verifikasi Finance & Accounting yang sudah ter-assign tercentang di popup
6. Verifikasi preview scope tidak memuat node apa pun sebelum ada centang baru
7. Verifikasi Finance & Accounting tidak masuk preview scope
8. Centang Region Jawa
9. Verifikasi preview scope mendaftar Region Jawa dan Jakarta Selatan Distribution Center sebelum `[Save]`
10. Verifikasi preview scope read-only (tanpa checkbox atau tombol)
11. Verifikasi preview scope tidak mengubah centang (Finance & Accounting dan Region Jawa tetap tercentang)
12. Hapus centang Region Jawa, lalu centang IT Infrastructure
13. Verifikasi preview scope hanya memuat IT Infrastructure
14. Klik `[Cancel]`
15. Verifikasi popup tertutup
16. Verifikasi baris Disposal × Staff menampilkan badge Finance & Accounting saja (tanpa perubahan tersimpan)
17. Verifikasi tidak ada dialog
18. Klik `[Assign Group]` pada baris Disposal × Staff
19. Centang Region Jawa
20. Klik `[Save]`
21. Verifikasi tidak ada dialog D-06 maupun D-07
22. Verifikasi toast "Success, Staff has been assigned." tampil
23. Verifikasi baris Disposal × Staff menampilkan badge Finance & Accounting dan Region Jawa
24. Verifikasi Jakarta Selatan Distribution Center tidak menjadi badge
25. Klik Tab Changelog
26. Verifikasi jumlah entri Tab Changelog Mira Anggraini bertambah tepat satu dari baseline langkah 3 (kemampuan baca BE)
27. Verifikasi entri teratas bertipe `Assign` dengan Field `Disposal — Region Jawa — Staff`
28. Verifikasi tidak ada entri untuk Jakarta Selatan Distribution Center di antara entri baru
29. Pulihkan Mira Anggraini ke Pre-setup #39 dan Home Group Mira Anggraini ke Pre-setup #43 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 25 dan 29. Search `Mira Anggraini` pada langkah 1 menemukan baris target (R-16, R-23). Baseline langkah 3 dibaca sekali sebelum popup dibuka dan berlaku untuk seluruh spec: `[Cancel]` pada langkah 14 tidak menyimpan apa pun sehingga selisih pada langkah 26 hanya berasal dari `[Save]` langkah 20 (S-12). Pemulihan lewat seed API memulihkan Pre-setup #39 dan #43 (S-06, S-09).
- Langkah 5 (Finance & Accounting tercentang) dan langkah 15 serta 16 (popup tertutup, baris Sub-tab tampil dengan badge) adalah anchor positif bagi asersi tidak ada preview (langkah 6, 7) dan tidak ada dialog (langkah 17) (bagian 8b butir 2). Langkah 22 (toast) adalah anchor bagi absence dialog langkah 21.
- Langkah 18 membuka popup yang sama sekali lagi sesuai TC langkah 5.
- Entri baru Tab Changelog dibaca pada baris teratas urutan default `Date` terbaru setelah selisih jumlah dari baseline dibuktikan (langkah 26); langkah 28 beranchor entri langkah 27 (S-14).
- Temuan untuk QA:
  - TC-FA-SU-1103 Precondition tidak menyebut Pre-setup #50 sedangkan Mira Anggraini ber-Home Group, sehingga Region Jawa dan IT Infrastructure akan Disabled (S-45) dan penugasan ditolak 422 V-09; spec mengikuti Catatan TC (Home Group constraint FI-32) dan memakai seed `FaUserNoHG` (Pre-setup #50) per target, bukan seluruh 25 pengguna. Mohon dikonfirmasi bila #50 harus diterapkan penuh atau Precondition TC diperbarui.
  - Preview scope: PRD tidak menetapkan copy atau format preview. Spec mengasersi preview sebagai daftar node (longgar). "Preview tidak memuat node sebelum ada centang baru" (TC-FA-SU-1103 Expected a) adalah penafsiran TC, bukan ketentuan PRD. Selektor preview scope perlu dikonfirmasi tim FE.
  - TC-FA-SU-1103 Expected b menyebut preview "tidak mengubah centang" tanpa menyebut elemen yang diperiksa; spec mengasersi centang Finance & Accounting dan Region Jawa tetap tercentang.
  - TC-FA-SU-1103 Expected c menyebut `[Cancel]` "tanpa perubahan tersimpan" tanpa surface; spec mengasersi badge baris Disposal × Staff (langkah 16) dan selisih entri Tab Changelog (langkah 26).
  - Post Condition TC (entri log pada Tab System Log aktor dan Activity Log) tidak punya langkah observasi di TC sehingga tidak diasersi; hanya Tab Changelog target yang diasersi (Expected e).
