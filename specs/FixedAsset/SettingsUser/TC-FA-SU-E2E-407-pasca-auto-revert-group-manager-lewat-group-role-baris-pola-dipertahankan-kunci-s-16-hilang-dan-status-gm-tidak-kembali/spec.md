---
id: TC-FA-SU-E2E-407-pasca-auto-revert-group-manager-lewat-group-role-baris-pola-dipertahankan-kunci-s-16-hilang-dan-status-gm-tidak-kembali
title: "Pasca Auto-Revert Group Manager lewat Sub-tab Group Role: Baris Pola Dipertahankan, Label Role Tetap, Kunci S-16 Hilang, dan Status GM Tidak Kembali"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-SU-1100
coverage:
  web: automated
---

# Pasca Auto-Revert Group Manager lewat Sub-tab Group Role: Baris Pola Dipertahankan, Label Role Tetap, Kunci S-16 Hilang, dan Status GM Tidak Kembali

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun kedua (ganti akun eksplisit di langkah 27): Manage user & role Group (Update) Sinta Dewi (Pre-setup #6; Group Role Manage user & role pada Finance & Accounting, Read dan Update), kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`; email tidak tertulis di Pre-setup TC (disediakan tim FE).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan varian Group Manager (Pre-setup #48).
- Pengguna target: Putri Anggraeni, Group Manager Finance & Accounting (turunan: Accounts Payable) dengan baris pola Group Manager pada kedua node, ditambah penugasan non-pola Group Role Manage user & role pada Finance & Accounting (Read dan Update), Transaction Role Disposal × Staff pada IT Infrastructure, dan Damaged × Monitoring & Report pada Branch Surabaya (Pre-setup #48).
- Data uji: baris Manage files × Accounts Payable (node turunan, bukan node penugasan Group Manager), centang Delete dihapus (langkah 6) lalu dicentang kembali (langkah 20); aktor langkah 32: Sinta Dewi menghapus centang Update pada Finance & Accounting.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan Putri Anggraeni ke Pre-setup #48; pembacaan label Role Putri di User List dan jumlah entri `Auto-Revert` Tab Changelog Putri sebelum aksi sebagai baseline (bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: status Group Manager dan baris Manage files × Accounts Payable serta Manage files × Finance & Accounting milik Putri Anggraeni; dipulihkan ke Pre-setup #48 lewat seed API pada langkah 36 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1100: Pasca Auto-Revert Group Manager lewat Sub-tab Group Role: baris pola dipertahankan sebagai baris biasa, label Role tetap menghitungnya, kunci S-16 hilang, dan status GM tidak kembali walau baris dikembalikan ke nilai pola

1. Ketik Search `Putri Anggraeni`, tekan Enter
2. Catat label Role Putri Anggraeni di User List dan jumlah entri `Auto-Revert` Tab Changelog Putri Anggraeni sebagai baseline
3. Klik Name `Putri Anggraeni`
4. Klik Tab Role lalu Sub-tab Group Role
5. Klik `[Assign Group]` pada baris Manage files
6. Hapus centang Delete pada Accounts Payable
7. Klik `[Save]`
8. Klik `[Remove]` pada dialog `Remove Group Manager`
9. Tunggu aksi selesai (toast sukses tampil dan banner Group Manager hilang)
10. Verifikasi banner Group Manager hilang di Sub-tab Group Role
11. Verifikasi seluruh baris pola Group Role (enam role katalog selain Manage user & role pada Accounts Payable dan Finance & Accounting) tetap tampil sebagai baris biasa tanpa penanda
12. Verifikasi baris Manage files × Accounts Payable tampil dengan Delete tidak dicentang
13. Klik Sub-tab Transaction Role
14. Verifikasi banner Group Manager hilang di Sub-tab Transaction Role
15. Verifikasi baris Transaction Role Asset Admin dan Approver tetap tampil sebagai baris biasa tanpa penanda
16. Buka Settings > User lewat sidebar lalu ketik Search `Putri Anggraeni`, tekan Enter
17. Verifikasi label Role Putri Anggraeni di User List tetap menghitung seluruh baris yang dipertahankan (jumlah tidak berkurang dibanding baseline)
18. Verifikasi label Role Putri Anggraeni tanpa badge Group Manager
19. Klik Name `Putri Anggraeni`, klik Tab Role lalu Sub-tab Group Role, dan klik `[Assign Group]` pada baris Manage files
20. Centang kembali Delete pada Accounts Payable
21. Klik `[Save]`
22. Verifikasi toast "Success, group role has been updated."
23. Verifikasi dialog Auto-Revert tidak tampil
24. Verifikasi banner Group Manager tidak muncul kembali di Sub-tab Group Role
25. Buka Tab Changelog Putri Anggraeni, lalu muat ulang sampai entri tampil
26. Verifikasi jumlah entri `Auto-Revert` Putri Anggraeni bertambah tepat satu dibanding baseline (hanya dari pelepasan langkah 8, tidak ada entri baru dari penyimpanan langkah 21)
27. Ganti akun: logout lalu login sebagai Sinta Dewi (`Spectra.env.FA_MURGR_UPD_PASSWORD`)
28. Ketik Search `Putri Anggraeni`, tekan Enter, klik Name `Putri Anggraeni`, lalu klik Tab Role dan Sub-tab Group Role
29. Klik `[Assign Group]` pada baris Manage files
30. Verifikasi checkbox CRUD baris Finance & Accounting Enabled saat kursor diarahkan ke checkbox (tidak terkunci S-16)
31. Verifikasi ikon hapus baris Finance & Accounting Enabled saat kursor diarahkan ke ikon (tidak terkunci S-16)
32. Hapus centang Update pada Finance & Accounting
33. Klik `[Save]`
34. Verifikasi toast "Success, group role has been updated."
35. Verifikasi dialog Auto-Revert tidak tampil
36. Pulihkan Putri Anggraeni ke Pre-setup #48 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 9, 13, 16, 19, 25, 27 dan 36. Langkah 3 sampai 8 adalah aksi pelepasan TC-FA-SU-1100 langkah 2 ("seperti TC-FA-SU-1082") dijalankan di spec ini sendiri tanpa asersi dialog (S-04), sehingga spec tidak bergantung pada hasil spec lain; asersi dialog Auto-Revert ada di spec 392. Search `Putri Anggraeni` pada langkah 1, 16 dan 28 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #48 (S-06, S-09). Langkah 27 adalah ganti akun eksplisit (S-07).
- Spec ini 36 langkah. Alasan melewati sekitar 35 langkah: satu TC (TC-FA-SU-1100) dengan empat tahap berurutan pada state yang sama (pelepasan, label Role, penyimpanan ulang, aksi Sinta Dewi); tiap Expected bermajemuk wajib satu `Verifikasi` per klausa (S-01) dan tahap berikutnya bergantung pada baris yang dipertahankan tahap sebelumnya, sehingga pemecahan menyalin ulang pelepasan berat (S-04) tanpa makna sendiri.
- Anchor 8b butir 2: toast "Success, group role has been updated." (langkah 22, 34) menjadi anchor bagi dialog Auto-Revert tidak tampil (langkah 23, 35) dan banner tidak muncul kembali (langkah 24); banner hilang dan baris pola tetap tampil (langkah 10, 11) menjadi anchor bagi banner tidak muncul kembali. Absence entri `Auto-Revert` baru pada langkah 26 ditulis sebagai selisih tepat satu terhadap baseline langkah 2, sehingga entri `Auto-Revert` dari pelepasan langkah 8 menjadi anchor positifnya.
- Post Condition TC-FA-SU-1100 ("hanya entri `Edit` baris yang tercatat setelah entri `Auto-Revert` awal") tidak punya langkah observasi di Expected dan tidak diasersi selain hitungan `Auto-Revert` pada langkah 26.
- Temuan untuk QA:
  - Pertanyaan terbuka: TC-FA-SU-1100 dan TC-FA-SU-1101 mengasumsikan Sinta Dewi (Manage user & role Group, Finance & Accounting) dapat mengedit baris yang dipertahankan karena kunci S-16 hilang (`FARP-LOGIC-04j`: tidak lagi dilindungi `03b`); spec mengasersi checkbox, ikon hapus, dan penyimpanan Sinta Dewi (langkah 30 sampai 35) apa adanya dari TC. Mohon dikonfirmasi dengan implementasi apakah scope Group Role Sinta Dewi (Read dan Update pada Finance & Accounting) memang mengizinkan edit baris Manage files × Finance & Accounting yang dipertahankan.
  - Email Sinta Dewi tidak tertulis di Pre-setup TC dan `suite.md`; spec merujuk nama env `FA_MURGR_UPD_PASSWORD` yang sudah terdaftar. Mohon email disediakan tim FE.
  - TC-FA-SU-1100 Expected a menyebut "enam role katalog selain Manage user & role" tanpa nama role dan "tanpa penanda" tanpa menjelaskan bentuk penanda di UI; spec mengasersi baris pola tetap tampil dan tidak ada penanda secara umum (langkah 11, 15).
  - TC-FA-SU-1100 Expected b menyebut label Role "tetap menghitung seluruh baris" tanpa angka; spec membandingkan label dengan baseline (langkah 2 dan 17) dan tidak mengasersi angka (angka turunan seperti 48 dan 25 di Pre-setup #43, PRD Open Item 3 belum diputuskan PM).
  - TC-FA-SU-1100 Expected d menyebut "hover checkbox dan ikon hapus" tanpa teks tooltip kunci S-16; spec mengasersi elemen Enabled saat kursor diarahkan, tanpa teks tooltip.
  - Copy dialog Auto-Revert D-05 (`Their individual role permissions will remain as edited.`) adalah copy usulan (PM, `settings-role-permission` Open Item #7d); spec ini tidak mengasersi isi dialog (aksi pelepasan hanya precondition).
  - Toast "Success, group role has been updated." pada langkah 22 dan 34 ditulis di TC (Expected c dan d) sebagai teks persis. "Status GM tidak kembali" (`FASU-LOGIC-04e`) tidak punya indikator tersendiri di UI selain banner yang tidak muncul kembali dan jumlah entri `Auto-Revert` yang tidak bertambah; spec mengasersi keduanya.
