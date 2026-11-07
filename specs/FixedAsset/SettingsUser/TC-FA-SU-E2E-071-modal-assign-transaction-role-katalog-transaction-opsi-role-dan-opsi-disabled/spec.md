---
id: TC-FA-SU-E2E-071-modal-assign-transaction-role-katalog-transaction-opsi-role-dan-opsi-disabled
title: "Modal Assign Transaction Role: Katalog Transaction, Opsi Role, dan Opsi Disabled"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-236
  - TC-FA-SU-237
  - TC-FA-SU-238
coverage:
  web: automated
---

# Modal Assign Transaction Role: Katalog Transaction, Opsi Role, dan Opsi Disabled

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan Transaction Role (Pre-setup #39); tenant `FaUserTR` (Pre-setup #44, varian `FaUserMain`) untuk blok terakhir TC-FA-SU-238. Perpindahan tenant ke `FaUserTR` dengan akun aktor yang sama adalah kemampuan "disediakan tim FE" (TC tidak menyebut caranya, lihat Temuan untuk QA).
- Pengguna target: Mira Anggraini (Disposal × Staff dan Borrowing & Assignment × Approver pada Finance & Accounting); Nanda Pratama pada `FaUserTR` (Disposal × Monitoring & Report, Transfer × Asset Admin, Transfer × Monitoring & Report, dan Transfer × Approver, seluruhnya pada Finance & Accounting).
- Data uji (tabel "Opsi Role per Jenis Transaksi", dipakai TC-FA-SU-237):

| Jenis Transaksi | Opsi Role |
|---|---|
| Borrowing & Assignment | Asset Admin, Monitoring & Report, Approver |
| Transfer | Asset Admin, Monitoring & Report, Approver |
| Damaged | Asset Admin, Monitoring & Report, Approver |
| Missing | Asset Admin, Monitoring & Report, Approver |
| Disposal | Asset Admin, Staff, Monitoring & Report, Approver |
| Audit | Asset Admin, Staff, Monitoring & Report, Approver |
| Repair Ticketing | Asset Admin, Staff, Monitoring & Report, Approver |
| Tracking | Asset Admin, Staff, Monitoring & Report, Approver |
| Maintenance Routine | Asset Admin, Staff, Monitoring & Report, Approver |

- Group: Finance & Accounting (TC-FA-SU-236 dan 238 bagian Nanda), IT Infrastructure (TC-FA-SU-237 dan 238 bagian Mira).
- State global yang diubah: tidak ada data yang disimpan; isian modal dibuang lewat `[Leave]`.
- Target tanpa Home Group (Pre-setup #50, `FaUserNoHG`; Catatan TC: TC penugasan Tab Role Section 3d, 3e, 4c, 8, dan 9 yang memilih node bebas dijalankan pada varian tanpa Home Group, FI-32), diterapkan per target: Home Group Mira Anggraini (Finance & Accounting pada Pre-setup #43) dikosongkan lewat seed API di hook `before` supaya node IT Infrastructure (langkah 5 dan 8) tidak Disabled oleh gate Home Group constraint; Home Group Mira Anggraini dipulihkan ke Finance & Accounting di hook `after`. Seed per target disediakan tim FE/BE.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-236: Opsi Transaction memuat katalog sembilan Jenis Transaksi

1. Ketik Search `Mira Anggraini`, tekan Enter, lalu buka Detail Mira Anggraini > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, lalu pilih Group Finance & Accounting
2. Buka dropdown Transaction
3. Verifikasi dropdown Transaction memuat Borrowing & Assignment, Transfer, Disposal, Damaged, Missing, Audit, Repair Ticketing, Tracking, dan Maintenance Routine
4. Verifikasi seluruh sembilan jenis tersedia tanpa bergantung lisensi Addon

### TC-FA-SU-237: Opsi Role menyesuaikan Jenis Transaksi: Staff hanya pada jenis yang menyediakannya

5. Klik `[Clear Field]` lalu pilih Group IT Infrastructure
6. Untuk setiap baris tabel "Opsi Role per Jenis Transaksi" (langkah 6 sampai 7): pilih Transaction sesuai kolom Jenis Transaksi lalu buka dropdown Role
7. Verifikasi dropdown Role memuat opsi sesuai kolom Opsi Role (Staff hanya pada jenis yang menyediakannya)

### TC-FA-SU-238: Opsi Role yang kombinasinya sudah ada Disabled dengan tooltip dan dropdown tidak dapat dipilih bila tak tersisa opsi

8. Klik `[Clear Field]` lalu pilih Group IT Infrastructure
9. Pilih Transaction Disposal lalu hover opsi Staff pada dropdown Role
10. Verifikasi opsi Staff Disabled
11. Verifikasi tooltip "This role is already assigned. Use Assign Group on its row to add groups."
12. Pilih Transaction Borrowing & Assignment lalu buka dropdown Role
13. Verifikasi opsi Approver Disabled
14. Klik `[✕]` pada modal
15. Verifikasi dialog `Unsaved Changes`
16. Klik `[Leave]`
17. Pindah ke tenant `FaUserTR` dengan akun aktor yang sama
18. Ketik Search `Nanda Pratama`, tekan Enter, lalu buka Detail Nanda Pratama > Tab Role > Sub-tab Transaction Role, klik `[+ Assign]`, pilih Group Finance & Accounting, lalu pilih Transaction Transfer
19. Verifikasi tidak ada opsi Role Enabled sehingga dropdown Role tidak dapat dipilih
20. Klik `[✕]` pada modal
21. Verifikasi dialog `Unsaved Changes`
22. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan TC sumber dipertahankan.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 5, 8, 14 sampai 17 dan 20 sampai 22. `[Clear Field]` memulihkan isian modal antar TC (S-09); penutupan modal dirty mengikuti S-08.
- Langkah 6 sampai 7 diulang untuk sembilan baris tabel "Opsi Role per Jenis Transaksi" (bagian 8b butir 7); jumlah langkah bernomor 22, dan dengan ekspansi iterasi (sembilan kali dua langkah) menjadi 38 langkah.
- Modal Assign Transaction Role dibuka sekali di awal untuk TC-FA-SU-236 sampai 238 bagian Mira Anggraini dan dipakai tanpa dibuka ulang (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Jumlah langkah dengan ekspansi 38, di atas smell 35 langkah; semua blok satu topik (opsi pada modal Assign Transaction Role), satu kelas harness, dan baca tanpa menyimpan data.
- Pre-setup #50 diterapkan hanya pada Mira Anggraini (bukan seluruh 25 pengguna): pemilih Group Role dan Role Transaksi men-Disabled node di luar Home Group constraint target (FI-32, tooltip S-45) dan permintaan langsung di luar constraint ditolak `422`, sedangkan TC ini memilih IT Infrastructure (langkah 5 dan 8); Home Group Mira Anggraini dipulihkan di hook `after`. Mohon dikonfirmasi bila #50 harus diterapkan penuh.
- Langkah penghubung Search (S-03): Search nama pengguna target pada langkah 1 dan 18 digabung ke langkah pembuka Detail atau pembacaan baris, untuk menemukan baris target di User List yang memuat 25 pengguna pada 3 halaman (R-16, bagian 8b butir 13); langkah berikutnya mengganti isi kotak search yang masih berisi nama sebelumnya (bagian 8b butir 9).
- Temuan untuk QA:
  - TC-FA-SU-238 langkah 5 pindah ke tenant `FaUserTR` tanpa menyebut akun atau cara berpindah; spec menulisnya sebagai kemampuan "disediakan tim FE".
  - TC-FA-SU-236 butir b ("tanpa bergantung lisensi Addon") tidak menyebut tenant tanpa lisensi Addon pada langkah; TC-FA-SU-279 mengujinya pada tenant tanpa Addon, sedangkan spec ini hanya mengasersi kesembilan jenis tampil.
  - TC-FA-SU-238 butir a menyebut baris Disposal × Staff untuk Mira pada Group IT Infrastructure padahal penugasan Mira ada pada Finance & Accounting; spec mengasersi opsi Staff Disabled sesuai teks TC.
