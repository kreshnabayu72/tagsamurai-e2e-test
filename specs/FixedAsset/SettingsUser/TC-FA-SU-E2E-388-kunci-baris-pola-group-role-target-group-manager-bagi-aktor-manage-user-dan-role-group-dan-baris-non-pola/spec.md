---
id: TC-FA-SU-E2E-388-kunci-baris-pola-group-role-target-group-manager-bagi-aktor-manage-user-dan-role-group-dan-baris-non-pola
title: "Kunci Baris Pola Group Role Target Group Manager bagi Aktor Manage User & Role Group dan Baris Manage User & Role Non-pola"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1085
coverage:
  web: automated
---

# Kunci Baris Pola Group Role Target Group Manager bagi Aktor Manage User & Role Group dan Baris Manage User & Role Non-pola

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Manage user & role Group (Update) Sinta Dewi (Pre-setup #6, Group Role Manage user & role pada Finance & Accounting, Read dan Update); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE; kredensial `Spectra.env.FA_MURGR_UPD_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan varian Group Manager `FaUserGM` (Pre-setup #48).
- Pengguna target: Putri Anggraeni (Pre-setup #48): Group Manager Finance & Accounting (turunan: Accounts Payable) dengan baris pola Group Manager pada kedua node, ditambah Group Role Manage user & role pada Finance & Accounting (Read dan Update).
- Data uji: spec mengubah Pre-setup #48 (Putri Anggraeni, Group Role Manage user & role × Finance & Accounting: Update dihapus lalu dicentang kembali oleh langkah 25 sampai 27); efeknya pada Last Updated dan Modified By Putri serta entri Changelog dan System Log tidak dipulihkan. Hook `before` memastikan fixture Pre-setup #48 sesuai kondisi awal dan hook `after` memulihkannya lewat seed API (kemampuan disediakan tim BE/FE, sesuai Catatan TC: fixture yang diubah disediakan ulang lewat seed API). Pre-setup #48 tidak dapat dimiliki spec karena kunci tier dan baris pola hanya ada pada fixture itu.
- Kemampuan teknis: seed API untuk memulihkan Pre-setup #48 (di atas).
- State global yang diubah: tidak ada selain Pre-setup #48 di atas; suite berjalan serial (`parallel: false`).
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1085: Aktor Manage user & role Group: baris pola Group Manager di node GM dan turunan terkunci (S-16), node subtree Disabled di pemilih grup, sedangkan baris Manage user & role tetap dapat diedit

1. Ketik Search `Putri Anggraeni`, tekan Enter, lalu klik Name `Putri Anggraeni`
2. Klik Tab Role lalu Sub-tab Group Role
3. Klik `[Assign Group]` pada baris Manage files
4. Arahkan kursor ke checkbox C/R/U/D pada baris Finance & Accounting
5. Verifikasi checkbox C/R/U/D baris Finance & Accounting Disabled dengan tooltip "You don't have permission to edit."
6. Arahkan kursor ke ikon hapus pada baris Finance & Accounting
7. Verifikasi ikon hapus baris Finance & Accounting Disabled dengan tooltip "You don't have permission to edit."
8. Arahkan kursor ke checkbox C/R/U/D pada baris Accounts Payable
9. Verifikasi checkbox C/R/U/D baris Accounts Payable Disabled dengan tooltip "You don't have permission to edit."
10. Arahkan kursor ke ikon hapus pada baris Accounts Payable
11. Verifikasi ikon hapus baris Accounts Payable Disabled dengan tooltip "You don't have permission to edit."
12. Klik `[+ Assign Group]`
13. Arahkan kursor ke node Finance & Accounting
14. Verifikasi node Finance & Accounting di popup Select Group Disabled dengan tooltip "You don't have permission to edit."
15. Arahkan kursor ke node Accounts Payable
16. Verifikasi node Accounts Payable di popup Select Group Disabled dengan tooltip "You don't have permission to edit."
17. Klik `[✕]` untuk menutup popup Select Group, lalu klik `[✕]` untuk menutup popup Assign Group Role Manage files
18. Klik `[Assign Group]` pada baris Manage user & role
19. Verifikasi checkbox Update pada baris Finance & Accounting Enabled
20. Hapus centang Update pada baris Finance & Accounting
21. Klik `[Save]`
22. Verifikasi dialog Auto-Revert tidak tampil
23. Klik `[Assign Group]` pada baris Manage user & role
24. Verifikasi centang Update pada baris Finance & Accounting tidak tercentang (perubahan tersimpan)
25. Centang kembali Update pada baris Finance & Accounting
26. Klik `[Save]`
27. Tunggu aksi selesai (popup tertutup dan tabel Group Role tampil kembali)
28. Verifikasi banner `This user is a Group Manager for: Finance & Accounting.` masih tampil (status Group Manager tidak berubah)
29. Verifikasi baris pola Manage files tetap memuat grup `Accounts Payable` dan `Finance & Accounting` (baris pola tidak berubah)
30. Verifikasi `[Assign Group]` Enabled pada seluruh baris
31. Verifikasi `[Detail]` Enabled pada seluruh baris
32. Klik Sub-tab Global Role
33. Verifikasi Global Role Putri Anggraeni Disabled (S-39)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 17, 23, 25, 26, 27. Search pada langkah 1 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Langkah 17 menutup popup tanpa perubahan (tidak ada dialog `Unsaved Changes`). Langkah 23 membuka ulang popup untuk mengamati hasil simpan. Langkah 25 sampai 27 memulihkan Update Manage user & role × Finance & Accounting ke nilai awal Pre-setup #48 (S-09); hook `after` memulihkan fixture lewat seed API sebagai cadangan.
- Langkah 22 (dialog Auto-Revert tidak tampil) diletakkan segera setelah `[Save]` pada langkah 21; pemicunya menjadi anchor, dan hasil tersimpan dibuktikan pada langkah 24 (8b butir 11).
- Perubahan urutan: Expected butir d memuat `[Assign Group]` dan `[Detail]` Enabled serta Global Role Disabled; langkah 30 sampai 33 diamati sesudah pemulihan (langkah 25 sampai 27) karena Enabled tidak bergantung pada nilai Update dan state sudah dipulihkan.
- Temuan untuk QA:
  - TC-FA-SU-1085 Pre-setup #6 menyebut Sinta Dewi tetapi suite.md dan Pre-setup TC tidak memuat email akunnya; spec menandainya "disediakan tim FE".
  - TC-FA-SU-1085 langkah 6 menyebut "serta banner" tetapi Expected tidak memuat butir banner; spec mengasersi banner Group Manager hanya sebagai bukti status Group Manager tidak berubah (Expected butir c).
  - TC-FA-SU-1085 Expected butir c ("`[Save]` tersimpan") tidak menyebut toast atau perilaku popup sesudah `[Save]`; spec mengasersi hasil tersimpan lewat membuka ulang popup (langkah 23 dan 24) dan mengandaikan popup tertutup sesudah `[Save]`.
  - TC-FA-SU-1085 Expected butir d ("Global Role Putri Disabled (S-39) dan tidak terkait kunci pola") tidak punya cara observasi bahwa kunci tidak terkait pola; spec hanya mengasersi Global Role Disabled (langkah 33).
  - TC-FA-SU-1085 langkah 4 menyebut popup pemilih grup hanya sebagai "popup" ke-2; spec memakai nama popup Select Group sesuai Expected butir b.
