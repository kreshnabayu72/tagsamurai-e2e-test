---
id: TC-FA-SU-E2E-408-pasca-auto-revert-group-manager-lewat-transaction-role-baris-pola-dipertahankan-kunci-s-16-hilang-dan-remove-d-07a-biasa
title: "Pasca Auto-Revert Group Manager lewat Sub-tab Transaction Role: Baris Pola Dipertahankan, Kunci S-16 Hilang, dan Remove Memakai Dialog D-07a Biasa"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1101
coverage:
  web: automated
---

# Pasca Auto-Revert Group Manager lewat Sub-tab Transaction Role: Baris Pola Dipertahankan, Kunci S-16 Hilang, dan Remove Memakai Dialog D-07a Biasa

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun kedua (ganti akun eksplisit di langkah 11 dan kembali ke Ahmad Dahlan di langkah 17): Manage user & role Group (Update) Sinta Dewi (Pre-setup #6; Group Role Manage user & role pada Finance & Accounting, Read dan Update), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`; email tidak tertulis di Pre-setup TC (disediakan tim FE).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan varian Group Manager (Pre-setup #48).
- Pengguna target: Putri Anggraeni, Group Manager Finance & Accounting (turunan: Accounts Payable) dengan baris pola Group Manager pada kedua node, ditambah penugasan non-pola Group Role Manage user & role pada Finance & Accounting (Read dan Update), Transaction Role Disposal × Staff pada IT Infrastructure, dan Damaged × Monitoring & Report pada Branch Surabaya (Pre-setup #48).
- Data uji: penugasan pemicu Disposal × Monitoring & Report pada Finance & Accounting (Group Finance & Accounting, Transaction Disposal, Role Monitoring & Report; menggantikan Disposal × Asset Admin); baris diuji: Transfer × Approver.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan Putri Anggraeni ke Pre-setup #48; pembacaan jumlah entri Tab Changelog Putri Anggraeni lewat kemampuan baca BE sebagai baseline sebelum aksi Cancel (bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: status Group Manager dan seluruh baris Transaction Role Putri Anggraeni; dipulihkan ke Pre-setup #48 lewat seed API pada langkah 32 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1101: Pasca Auto-Revert Group Manager lewat Sub-tab Transaction Role: baris pola Transaction Role dipertahankan sebagai penugasan biasa, kunci S-16 hilang, dan Remove memakai dialog Remove Transaction Role biasa

1. Ketik Search `Putri Anggraeni`, tekan Enter, lalu klik Name `Putri Anggraeni`
2. Klik Tab Role lalu Sub-tab Transaction Role
3. Klik `[+ Assign]`
4. Pilih Group Finance & Accounting, Transaction Disposal, Role Monitoring & Report
5. Klik `[Submit]`
6. Klik `[Remove]` pada dialog `Remove Group Manager`
7. Tunggu aksi selesai (toast sukses tampil dan banner Group Manager hilang)
8. Verifikasi banner Group Manager hilang di Sub-tab Transaction Role
9. Verifikasi baris pola Asset Admin dan Approver per Jenis Transaksi tetap tampil sebagai baris biasa tanpa penanda (selain Disposal × Asset Admin pada Finance & Accounting yang digantikan aksi pemicu)
10. Verifikasi baris Disposal × Monitoring & Report pada Finance & Accounting tersimpan
11. Ganti akun: logout lalu login sebagai Sinta Dewi (`Spectra.env.FA_MURGR_UPD_PASSWORD`), lalu buka Fixed Asset > Settings > User
12. Ketik Search `Putri Anggraeni`, tekan Enter, klik Name `Putri Anggraeni`, lalu klik Tab Role dan Sub-tab Transaction Role
13. Klik ⋯ pada baris Transfer × Approver, lalu arahkan kursor ke row action `Remove`
14. Verifikasi row action `Remove` baris Transfer × Approver Enabled saat kursor diarahkan (tidak terkunci S-16)
15. Tutup menu dengan Esc, lalu arahkan kursor ke checkbox baris Transfer × Approver
16. Verifikasi checkbox baris Transfer × Approver Enabled saat kursor diarahkan ke checkbox (tidak terkunci S-16)
17. Ganti akun: logout lalu login sebagai Ahmad Dahlan (`Spectra.env.FA_DU_PASSWORD`), lalu buka Fixed Asset > Settings > User
18. Ketik Search `Putri Anggraeni`, tekan Enter, klik Name `Putri Anggraeni`, lalu klik Tab Role dan Sub-tab Transaction Role
19. Baca jumlah entri Tab Changelog Putri Anggraeni lewat kemampuan baca BE sebagai baseline
20. Klik ⋯ pada baris Transfer × Approver lalu klik `Remove`
21. Verifikasi dialog Title `Remove Transaction Role` (D-07a) tampil
22. Verifikasi Body bullet `• Putri Anggraeni`
23. Verifikasi kalimat `This user will lose the selected transaction role.`
24. Verifikasi penutup `Are you sure you want to remove it?`
25. Verifikasi dialog Auto-Revert `Remove Group Manager` tidak tampil
26. Klik `[Cancel]`
27. Verifikasi dialog tertutup
28. Verifikasi baris Transfer × Approver tetap ada tanpa perubahan
29. Verifikasi tidak ada toast
30. Baca jumlah entri Tab Changelog Putri Anggraeni lewat kemampuan baca BE
31. Verifikasi jumlah entri Tab Changelog Putri Anggraeni sama dengan baseline langkah 19
32. Pulihkan Putri Anggraeni ke Pre-setup #48 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 7, 12, 15, 18, 19, 30 dan 32. Langkah 3 sampai 6 adalah aksi pemicu TC-FA-SU-1101 langkah 2 ("seperti TC-FA-SU-1092") dijalankan di spec ini sendiri tanpa asersi dialog (S-04), sehingga spec tidak bergantung pada hasil spec lain; asersi dialog turun tangga Auto-Revert ada di spec 395. Search `Putri Anggraeni` pada langkah 1, 12 dan 18 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Langkah 11 dan 17 adalah ganti akun eksplisit (S-07) yang masing-masing diikuti pembukaan Fixed Asset > Settings > User; baseline log dibaca pada langkah 19 setelah kembali ke Ahmad Dahlan supaya entri pelepasan langkah 6 tidak terhitung (S-12). Pemulihan lewat seed API memulihkan Pre-setup #48 (S-06, S-09).
- Anchor 8b butir 2: dialog `Remove Transaction Role` tampil (langkah 21) menjadi anchor bagi dialog Auto-Revert tidak tampil (langkah 25) dan tidak ada toast (langkah 29); baris Transfer × Approver tetap ada (langkah 28) dan jumlah entri sama dengan baseline (langkah 31) menyatakan `[Cancel]` tanpa perubahan dan tanpa entri log (Expected c). Banner hilang (langkah 8) diasersi langsung; toast sukses pada langkah 7 hanya keterangan penanda aksi pemicu selesai dan tidak diverifikasi (lihat Temuan untuk QA).
- Post Condition TC-FA-SU-1101 (status GM tetap terlepas dan seluruh baris pola tersimpan) diamati lewat langkah 8 sampai 10.
- Temuan untuk QA:
  - Pertanyaan terbuka: TC-FA-SU-1100 dan TC-FA-SU-1101 mengasumsikan Sinta Dewi (Manage user & role Group, Finance & Accounting) dapat mengedit atau menghapus baris yang dipertahankan karena kunci S-16 hilang (`FARP-LOGIC-04j`: tidak lagi dilindungi `03b`); spec mengasersi row action `Remove` dan checkbox Enabled apa adanya dari TC (langkah 14 sampai 16). Mohon dikonfirmasi dengan implementasi.
  - Email Sinta Dewi tidak tertulis di Pre-setup TC dan `suite.md`; spec merujuk nama env `FA_MURGR_UPD_PASSWORD` yang sudah terdaftar. Mohon email disediakan tim FE.
  - TC-FA-SU-1101 Expected a menyebut baris pola "tampil sebagai baris biasa tanpa penanda" tanpa menjelaskan bentuk penanda; spec mengasersi baris pola tetap tampil tanpa penanda secara umum (langkah 9). Jumlah baris pasca penggantian tangga (Disposal × Asset Admin ke Monitoring & Report) tidak diasersi karena hitungan baris tepat bergantung fixture Pre-setup #48.
  - TC-FA-SU-1101 Expected b ("hover row action `Remove` dan checkbox") tidak menyebut teks tooltip kunci S-16; spec mengasersi elemen Enabled saat kursor diarahkan, tanpa teks tooltip.
  - TC-FA-SU-1101 Expected c menyebut "tanpa entri log" tanpa surface; spec membaca Tab Changelog target lewat kemampuan baca BE (langkah 19 dan 30).
  - Toast sukses pada langkah 7 tidak diverifikasi sebagai asersi: TC-FA-SU-1101 tidak mengasersi toast pelepasan Group Manager, sehingga langkah 7 hanya menunggu aksi selesai dan asersi banner hilang pada langkah 8 tidak bergantung pada toast.
