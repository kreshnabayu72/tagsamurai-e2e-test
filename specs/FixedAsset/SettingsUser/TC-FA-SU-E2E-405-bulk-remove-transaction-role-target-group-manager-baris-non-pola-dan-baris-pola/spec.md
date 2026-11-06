---
id: TC-FA-SU-E2E-405-bulk-remove-transaction-role-target-group-manager-baris-non-pola-dan-baris-pola
title: "Bulk Remove Transaction Role Target Group Manager: Baris Non-Pola dan Baris Pola"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1091
coverage:
  web: automated
---

# Bulk Remove Transaction Role Target Group Manager: Baris Non-Pola dan Baris Pola

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Putri Anggraeni (Pre-setup #48 `FaUserGM`): Group Manager Finance & Accounting (turunan Accounts Payable) dengan baris pola Group Manager pada kedua node, ditambah penugasan non-pola Group Role Manage user & role pada Finance & Accounting (Read dan Update), Transaction Role Disposal x Staff pada IT Infrastructure, dan Damaged x Monitoring & Report pada Branch Surabaya. Email akun ini tidak tertulis di Pre-setup TC; target hanya dibuka lewat Search nama.
- Data uji: seleksi non-pola (2 baris): Disposal x Staff (IT Infrastructure) dan Damaged x Monitoring & Report (Branch Surabaya); seleksi pola (2 baris): Disposal x Asset Admin dan Transfer x Approver.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan Putri Anggraeni ke Pre-setup #48 (di hook `before`, pada langkah penghubung akhir, dan di hook `after`); pembacaan jumlah entri Tab Changelog target sebelum aksi sebagai baseline (bagian 8b butir 10).
- State global yang diubah: status Group Manager dan seluruh baris pola serta penugasan Putri Anggraeni; dipulihkan ke Pre-setup #48 lewat seed API pada langkah 38 dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1091: Bulk Remove pada target Group Manager: baris non-pola memakai dialog Bulk Remove biasa, seleksi baris pola memicu satu dialog D-05c dan Cancel mempertahankan seleksi

1. Catat jumlah entri Tab Changelog Putri Anggraeni sebagai baseline
2. Ketik Search `Putri Anggraeni`, tekan Enter, lalu klik Name `Putri Anggraeni`
3. Klik Tab Role lalu Sub-tab Transaction Role
4. Verifikasi banner Group Manager tampil di Sub-tab Transaction Role
5. Centang baris Disposal x Staff (IT Infrastructure) dan Damaged x Monitoring & Report (Branch Surabaya)
6. Klik `[Bulk Remove]`
7. Verifikasi dialog tampil dengan Title `Remove Transaction Roles`, Body bullet `• Putri Anggraeni`, kalimat `This user will lose the selected transaction roles.` dan `Are you sure you want to remove them?`
8. Verifikasi dialog Auto-Revert dengan Title `Remove Group Manager` tidak tampil
9. Klik `[Cancel]`
10. Verifikasi dialog tertutup dan kedua baris tetap ada
11. Verifikasi seleksi kedua baris dipertahankan
12. Hapus seleksi
13. Centang baris Disposal x Asset Admin dan Transfer x Approver
14. Verifikasi counter `2 Transaction Roles selected`
15. Klik `[Bulk Remove]`
16. Verifikasi satu dialog D-05c varian Role Transaksi tampil dengan Title `Remove Group Manager`, Body bullet `• Putri Anggraeni`, kalimat `This change will remove Group Manager status for this group.`, `Their other role assignments will remain as they are.` dan `Are you sure you want to remove it?`, serta tombol `[Cancel]` (Text, Contrast) dan `[Remove]`
17. Verifikasi dialog `Remove Transaction Roles` (D-07) tidak tampil
18. Klik `[Cancel]`
19. Verifikasi tidak ada toast
20. Verifikasi dialog tertutup
21. Verifikasi seleksi kedua baris pola dan baris tersebut dipertahankan
22. Klik Tab Changelog
23. Verifikasi jumlah entri Tab Changelog Putri Anggraeni sama dengan baseline
24. Klik Tab Role lalu Sub-tab Transaction Role
25. Centang baris Disposal x Asset Admin dan Transfer x Approver
26. Klik `[Bulk Remove]`
27. Verifikasi dialog dengan Title `Remove Group Manager` tampil
28. Klik `[Remove]` pada dialog
29. Verifikasi toast gabungan sukses Remove Transaction Role disertai klausa auto-revert Group Manager tampil
30. Verifikasi hanya satu toast yang tampil, bukan toast terpisah
31. Verifikasi banner Group Manager hilang di Sub-tab Transaction Role
32. Verifikasi baris non-pola Disposal x Staff (IT Infrastructure) dan Damaged x Monitoring & Report (Branch Surabaya) tetap ada
33. Verifikasi kedua baris yang diseleksi (Disposal x Asset Admin dan Transfer x Approver) terhapus oleh aksi aktor sendiri
34. Verifikasi seluruh baris pola Group Manager Transaction Role lain (Asset Admin dan Approver pada seluruh Jenis Transaksi untuk Accounts Payable dan Finance & Accounting) tetap tersimpan sebagai baris biasa
35. Klik Sub-tab Group Role
36. Verifikasi baris non-pola Manage user & role pada Finance & Accounting tetap ada
37. Verifikasi seluruh baris pola Group Manager Group Role (Group Role katalog selain Manage user & role pada Finance & Accounting dan Accounts Payable) tetap tersimpan sebagai baris biasa
38. Pulihkan Putri Anggraeni ke Pre-setup #48 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan mengikuti TC: Bulk Remove non-pola (langkah 5 sampai 12), Bulk Remove pola dengan `[Cancel]` (langkah 13 sampai 23), lalu konfirmasi `[Remove]` yang mengubah state (S-09, S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 12 (dari TC: hapus seleksi), 22, 24, 25, 34 dan 37. Search `Putri Anggraeni` pada langkah 2 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Langkah 22 sampai 25 memindah Tab untuk membaca log, sehingga seleksi dibentuk ulang pada langkah 25 sebelum `[Bulk Remove]` lagi (TC: "klik `[Bulk Remove]` lagi"). Baseline log mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #48 (S-06, S-09).
- Anchor 8b butir 2: banner Group Manager tampil (langkah 4, tidak tertulis di Expected TC) menjadi anchor bagi banner hilang (langkah 31); baris non-pola tetap ada (langkah 32, 36) berdampingan dengan baris pola yang tetap tersimpan (langkah 34, 37) dan kedua baris seleksi terhapus oleh aksi aktor (langkah 33), tidak lagi diasersi sebagai absence; dialog D-05c tampil (langkah 16) menjadi anchor bagi asersi dialog D-07 tidak tampil (langkah 17) dan tidak ada toast (langkah 19); dialog D-07 tampil (langkah 7) menjadi anchor bagi dialog Auto-Revert tidak tampil (langkah 8).
- Alasan di atas sekitar 35 langkah (38): satu TC dengan tiga eksekusi `[Bulk Remove]` berurutan sesuai langkah 3 sampai 5 TC, tanpa kelas harness; pemecahan menyisakan eksekusi yang tidak bermakna sendiri. Tambahan langkah berasal dari Expected bermajemuk (S-01), pembacaan Tab Changelog satu surface (langkah 22 dan 23) dan pembentukan ulang seleksi (langkah 24 dan 25).
- Klausa "dalam transaksi atomik yang sama" (Expected d) tidak teramati terpisah lewat UI; keadaan akhir lengkap diasersi pada langkah 31 sampai 37.
- Pembagian TC lintas spec: TC-FA-SU-1090 (Remove satu baris pola target Group Manager) ada di spec 394. Post Condition b TC-FA-SU-1091 (entri `Auto-Revert` di tiga surface log dan notifikasi) tidak punya langkah observasi di TC ini dan diasersi pada spec 394 untuk aksi yang sama (TC-FA-SU-1090 Expected e).
- Temuan untuk QA:
  - Copy dialog D-05c varian Role Transaksi dan tombol `[Remove]` bertanda "copy usulan, perlu persetujuan PM" (TC-FA-SU-1091 butir b dan d; `D-05` `settings-role-permission` Open Item #7d). Spec memakai teks apa adanya; PRD DO-12 menyebut tombol `[Revoke]` pada dialog D-10 (jalur Edit Home Group) sedangkan DO-02 memakai `[Remove]` untuk D-05; mohon dikonfirmasi label D-05c.
  - Toast gabungan (butir d, T-06b dengan T-17/T-18 klausa auto-revert Group Manager) tidak ditulis literal di TC maupun PRD; spec mengasersi toast gabungan secara longgar tanpa teks persis.
  - Teks banner Group Manager untuk Putri Anggraeni tidak tertulis di TC; spec hanya mengasersi banner tampil atau hilang. Spec 386 (TC-FA-SU-1074) masih menyatakan banner Group Manager tidak tampil di Sub-tab Transaction Role, sedangkan TC-FA-SU-1091 mengasersi banner hilang di sub-tab itu.
  - TC-FA-SU-1091 ACC menyebut `#20` (id Client `FaUserMain`, bukan nomor akun); aktor diambil dari langkah "Login sebagai Ahmad Dahlan (Default User)". Mohon dikonfirmasi.
  - Post Condition b (entri `Auto-Revert` di tiga surface log, notifikasi in-app view-only ke Putri Anggraeni) tidak punya langkah observasi di TC dan tidak diasersi; Putri Anggraeni tidak punya nama env password di `suite.md`. Expected c "tanpa entri log" tidak menyebut surface; spec membaca Tab Changelog target (langkah 22 dan 23).
  - Kondisi Expected b "seleksi dipertahankan" sesudah `[Cancel]` tidak menyebut apakah seleksi bertahan sesudah berpindah Tab; spec membentuk ulang seleksi (langkah 25).
